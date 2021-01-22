import omni.ui as ui

import numpy as np
from matplotlib.figure import Figure as Matplotlib_Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as Matplotlib_FigureCanvasAgg


class Figure():
    def __init__(self, num=None, figsize=(6.4, 4.8), dpi=100.0, **kwargs):
        """
        Figure

        Based on matplotlib.figure.Figure
        https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.figure.Figure.html?highlight=figure#matplotlib.figure.Figure

        Parameters
        ----------
        num : int or str, optional
            Unique identifier for the figure.
            If the parameter is not given, a new identifier is created based on the current system time
        figsize : tuple
            Width and height of the window in inches
        dpi: float
            Resolution of the figure in pixels-per-inch (called dpi to keep compatibility with matplotlib)
        """
        # window name
        if num == None:
            import datetime
            num = str(datetime.datetime.today().time())
            name = "Figure " + num
        if type(num) == int:
            name = "Figure " + str(num)
        elif type(num) == str:
            name = num
        else:
            raise Exception("Invalid identifier type for the figure: ")
        
        # create window
        self._window = ui.Window(name,
                                 width=int(figsize[0]*dpi), 
                                 height=int(figsize[1]*dpi), 
                                 visible=True)

        self._num = num
        self._dpi = dpi
        self._figsize = figsize
        self._byte_provider = None
    
    def is_instance(self, num):
        """
        Identify if the current figure has the specified identifier

        Parameters
        ----------
        num : int or str, optional
            Unique identifier for the figure

        Returns
        -------
        bool
            True if the current figure has the specified identifier  
        """
        if num == None:
            return False
        return self._num == num
        
    def imshow(self, winname, mat):
        """
        Displays an image in the specified window

        Based on opencv.imshow
        https://docs.opencv.org/master/d7/dfc/group__highgui.html#ga453d42fe4cb60e5723281a89973ee563

        Parameters
        ----------
        winname : str
            Name of the window
        mat : numpy.ndarray (dtype: uint8)
            Image to be shown
        """
        height, width = mat.shape[:2]
        
        # enabled visibility
        if not self._window.visible:
            self._window.visible = True
        
        # update if exist
        if self._byte_provider:
            self._byte_provider.set_data(mat.flatten().tolist(), [width, height])
            return
        
        # create provider
        self._byte_provider = ui.ByteImageProvider()
        self._byte_provider.set_data(mat.flatten().tolist(), [width, height])
        
        # create image viewer
        with self._window.frame:
            with ui.VStack():
                ui.ImageWithProvider(self._byte_provider)
        
    def _render(self, *args, plot_method="plot", **kwargs):
        """
        Render a matplotlib.pyplot method

        Parameters
        ----------
        plot_method : str
            Name of the matplotib.pyplot method
        args: tuple
            Positional arguments of the method to be called
        kwargs: dict
            Key-value arguments of the method to be called
        """
        # create canvas
        fig = Matplotlib_Figure(figsize=self._figsize, dpi=self._dpi)
        canvas = Matplotlib_FigureCanvasAgg(fig)
        
        # plotting
        ax = fig.gca()
        exec("ax.{}(*args, **kwargs)".format(plot_method))

        # convert renderer buffer to numpy
        canvas.draw()
        img = np.asarray(canvas.buffer_rgba())
        
        # show rendered image
        self.imshow(None, img)

    # matplotib pyplot methods
    # https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.html
    def acorr(self, *args, **kwargs): self._render(*args, plot_method="acorr", **kwargs)
    def angle_spectrum(self, *args, **kwargs): self._render(*args, plot_method="angle_spectrum", **kwargs)
    def bar(self, *args, **kwargs): self._render(*args, plot_method="bar", **kwargs)
    def barbs(self, *args, **kwargs): self._render(*args, plot_method="barbs", **kwargs)
    def barh(self, *args, **kwargs): self._render(*args, plot_method="barh", **kwargs)
    def boxplot(self, *args, **kwargs): self._render(*args, plot_method="boxplot", **kwargs)
    def broken_barh(self, *args, **kwargs): self._render(*args, plot_method="broken_barh", **kwargs)
    def cohere(self, *args, **kwargs): self._render(*args, plot_method="cohere", **kwargs)
    def contour(self, *args, **kwargs): self._render(*args, plot_method="contour", **kwargs)
    def contourf(self, *args, **kwargs): self._render(*args, plot_method="contourf", **kwargs)
    def csd(self, *args, **kwargs): self._render(*args, plot_method="csd", **kwargs)
    def errorbar(self, *args, **kwargs): self._render(*args, plot_method="errorbar", **kwargs)
    def eventplot(self, *args, **kwargs): self._render(*args, plot_method="eventplot", **kwargs)
    def fill(self, *args, **kwargs): self._render(*args, plot_method="fill", **kwargs)
    def fill_between(self, *args, **kwargs): self._render(*args, plot_method="fill_between", **kwargs)
    def fill_betweenx(self, *args, **kwargs): self._render(*args, plot_method="fill_betweenx", **kwargs)
    def hist(self, *args, **kwargs): self._render(*args, plot_method="hist", **kwargs)
    def hist2d(self, *args, **kwargs): self._render(*args, plot_method="hist2d", **kwargs)
    def hlines(self, *args, **kwargs): self._render(*args, plot_method="hlines", **kwargs)
    def loglog(self, *args, **kwargs): self._render(*args, plot_method="loglog", **kwargs)
    def magnitude_spectrum(self, *args, **kwargs): self._render(*args, plot_method="magnitude_spectrum", **kwargs)
    def matshow(self, *args, **kwargs): self._render(*args, plot_method="matshow", **kwargs)
    def pcolor(self, *args, **kwargs): self._render(*args, plot_method="pcolor", **kwargs)
    def pcolormesh(self, *args, **kwargs): self._render(*args, plot_method="pcolormesh", **kwargs)
    def phase_spectrum(self, *args, **kwargs): self._render(*args, plot_method="phase_spectrum", **kwargs)
    def pie(self, *args, **kwargs): self._render(*args, plot_method="pie", **kwargs)
    def plot(self, *args, **kwargs): self._render(*args, plot_method="plot", **kwargs)
    def plot_date(self, *args, **kwargs): self._render(*args, plot_method="plot_date", **kwargs)
    def polar(self, *args, **kwargs): self._render(*args, plot_method="polar", **kwargs)
    def psd(self, *args, **kwargs): self._render(*args, plot_method="psd", **kwargs)
    def quiver(self, *args, **kwargs): self._render(*args, plot_method="quiver", **kwargs)
    def scatter(self, *args, **kwargs): self._render(*args, plot_method="scatter", **kwargs)
    def semilogx(self, *args, **kwargs): self._render(*args, plot_method="semilogx", **kwargs)
    def semilogy(self, *args, **kwargs): self._render(*args, plot_method="semilogy", **kwargs)
    def specgram(self, *args, **kwargs): self._render(*args, plot_method="specgram", **kwargs)
    def spy(self, *args, **kwargs): self._render(*args, plot_method="spy", **kwargs)
    def stackplot(self, *args, **kwargs): self._render(*args, plot_method="stackplot", **kwargs)
    def stem(self, *args, **kwargs): self._render(*args, plot_method="stem", **kwargs)
    def step(self, *args, **kwargs): self._render(*args, plot_method="step", **kwargs)
    def streamplot(self, *args, **kwargs): self._render(*args, plot_method="streamplot", **kwargs)
    def tricontour(self, *args, **kwargs): self._render(*args, plot_method="tricontour", **kwargs)
    def tricontourf(self, *args, **kwargs): self._render(*args, plot_method="tricontourf", **kwargs)
    def tripcolor(self, *args, **kwargs): self._render(*args, plot_method="tripcolor", **kwargs)
    def triplot(self, *args, **kwargs): self._render(*args, plot_method="triplot", **kwargs)
    def violinplot(self, *args, **kwargs): self._render(*args, plot_method="violinplot", **kwargs)
    def vlines(self, *args, **kwargs): self._render(*args, plot_method="vlines", **kwargs)


class Visualization():
    def __init__(self):
        """
        Data visualization for NVIDIA Omniverse

        Matplotlib and OpenCV like data visualizer
        """
        # TODO: release figures after close them
        self._figures = []

    def figure(self, num=None, figsize=(6.4, 4.8), dpi=100.0, **kwargs):
        """
        Create a new figure or return an existing one

        Parameters
        ----------
        num : int or str, optional
            Unique identifier for the figure.
            If the parameter is not given, a new identifier is created based on the current system time
        figsize : tuple
            Width and height of the window in inches
        dpi: float
            Resolution of the figure in pixels-per-inch (called dpi to keep compatibility with matplotlib)
        
        Returns
        -------
        Figure
            Instance of the created or existing figure
        """
        for fig in self._figures:
            if fig.is_instance(num):
                return fig
        fig = Figure(num, figsize, dpi, **kwargs)
        self._figures.append(fig)
        return fig

    def imshow(self, winname, mat):
        """
        Displays an image in the specified window

        Parameters
        ----------
        winname : str
            Name of the window
        mat : numpy.ndarray
            Image to be shown
        """
        self.figure(winname).imshow(winname, mat)

    # matplotib pyplot methods
    def acorr(self, *args, **kwargs): self.figure(None).acorr(*args, **kwargs)
    def angle_spectrum(self, *args, **kwargs): self.figure(None).angle_spectrum(*args, **kwargs)
    def bar(self, *args, **kwargs): self.figure(None).bar(*args, **kwargs)
    def barbs(self, *args, **kwargs): self.figure(None).barbs(*args, **kwargs)
    def barh(self, *args, **kwargs): self.figure(None).barh(*args, **kwargs)
    def boxplot(self, *args, **kwargs): self.figure(None).boxplot(*args, **kwargs)
    def broken_barh(self, *args, **kwargs): self.figure(None).broken_barh(*args, **kwargs)
    def cohere(self, *args, **kwargs): self.figure(None).cohere(*args, **kwargs)
    def contour(self, *args, **kwargs): self.figure(None).contour(*args, **kwargs)
    def contourf(self, *args, **kwargs): self.figure(None).contourf(*args, **kwargs)
    def csd(self, *args, **kwargs): self.figure(None).csd(*args, **kwargs)
    def errorbar(self, *args, **kwargs): self.figure(None).errorbar(*args, **kwargs)
    def eventplot(self, *args, **kwargs): self.figure(None).eventplot(*args, **kwargs)
    def fill(self, *args, **kwargs): self.figure(None).fill(*args, **kwargs)
    def fill_between(self, *args, **kwargs): self.figure(None).fill_between(*args, **kwargs)
    def fill_betweenx(self, *args, **kwargs): self.figure(None).fill_betweenx(*args, **kwargs)
    def hist(self, *args, **kwargs): self.figure(None).hist(*args, **kwargs)
    def hist2d(self, *args, **kwargs): self.figure(None).hist2d(*args, **kwargs)
    def hlines(self, *args, **kwargs): self.figure(None).hlines(*args, **kwargs)
    def loglog(self, *args, **kwargs): self.figure(None).loglog(*args, **kwargs)
    def magnitude_spectrum(self, *args, **kwargs): self.figure(None).magnitude_spectrum(*args, **kwargs)
    def matshow(self, *args, **kwargs): self.figure(None).matshow(*args, **kwargs)
    def pcolor(self, *args, **kwargs): self.figure(None).pcolor(*args, **kwargs)
    def pcolormesh(self, *args, **kwargs): self.figure(None).pcolormesh(*args, **kwargs)
    def phase_spectrum(self, *args, **kwargs): self.figure(None).phase_spectrum(*args, **kwargs)
    def pie(self, *args, **kwargs): self.figure(None).pie(*args, **kwargs)
    def plot(self, *args, **kwargs): self.figure(None).plot(*args, **kwargs)
    def plot_date(self, *args, **kwargs): self.figure(None).plot_date(*args, **kwargs)
    def polar(self, *args, **kwargs): self.figure(None).polar(*args, **kwargs)
    def psd(self, *args, **kwargs): self.figure(None).psd(*args, **kwargs)
    def quiver(self, *args, **kwargs): self.figure(None).quiver(*args, **kwargs)
    def scatter(self, *args, **kwargs): self.figure(None).scatter(*args, **kwargs)
    def semilogx(self, *args, **kwargs): self.figure(None).semilogx(*args, **kwargs)
    def semilogy(self, *args, **kwargs): self.figure(None).semilogy(*args, **kwargs)
    def specgram(self, *args, **kwargs): self.figure(None).specgram(*args, **kwargs)
    def spy(self, *args, **kwargs): self.figure(None).spy(*args, **kwargs)
    def stackplot(self, *args, **kwargs): self.figure(None).stackplot(*args, **kwargs)
    def stem(self, *args, **kwargs): self.figure(None).stem(*args, **kwargs)
    def step(self, *args, **kwargs): self.figure(None).step(*args, **kwargs)
    def streamplot(self, *args, **kwargs): self.figure(None).streamplot(*args, **kwargs)
    def tricontour(self, *args, **kwargs): self.figure(None).tricontour(*args, **kwargs)
    def tricontourf(self, *args, **kwargs): self.figure(None).tricontourf(*args, **kwargs)
    def tripcolor(self, *args, **kwargs): self.figure(None).tripcolor(*args, **kwargs)
    def triplot(self, *args, **kwargs): self.figure(None).triplot(*args, **kwargs)
    def violinplot(self, *args, **kwargs): self.figure(None).violinplot(*args, **kwargs)
    def vlines(self, *args, **kwargs): self.figure(None).vlines(*args, **kwargs)
    

_visualization = Visualization()
