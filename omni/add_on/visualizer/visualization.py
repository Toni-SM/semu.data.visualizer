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


class Visualization():
    def __init__(self):
        """
        Data visualization for NVIDIA Omniverse

        Matplotlib and OpenCV like data visualizer
        """
        # TODO: release figures after close them
        self._figures = [] 
        pass

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
        """
        for fig in self._figures:
            if fig.is_instance(num):
                return fig
        fig = Figure(num, figsize, dpi)
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
    # https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.html
    def acorr(self, *args, plot_method="acorr", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def angle_spectrum(self, *args, plot_method="angle_spectrum", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def bar(self, *args, plot_method="bar", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def barbs(self, *args, plot_method="barbs", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def barh(self, *args, plot_method="barh", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def boxplot(self, *args, plot_method="boxplot", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def broken_barh(self, *args, plot_method="broken_barh", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def cohere(self, *args, plot_method="cohere", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def contour(self, *args, plot_method="contour", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def contourf(self, *args, plot_method="contourf", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def csd(self, *args, plot_method="csd", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def errorbar(self, *args, plot_method="errorbar", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def eventplot(self, *args, plot_method="eventplot", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def fill(self, *args, plot_method="fill", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def fill_between(self, *args, plot_method="fill_between", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def fill_betweenx(self, *args, plot_method="fill_betweenx", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def hist(self, *args, plot_method="hist", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def hist2d(self, *args, plot_method="hist2d", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def hlines(self, *args, plot_method="hlines", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def loglog(self, *args, plot_method="loglog", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def magnitude_spectrum(self, *args, plot_method="magnitude_spectrum", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def matshow(self, *args, plot_method="matshow", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def pcolor(self, *args, plot_method="pcolor", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def pcolormesh(self, *args, plot_method="pcolormesh", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def phase_spectrum(self, *args, plot_method="phase_spectrum", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def pie(self, *args, plot_method="pie", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def plot(self, *args, plot_method="plot", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def plot_date(self, *args, plot_method="plot_date", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def polar(self, *args, plot_method="polar", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def psd(self, *args, plot_method="psd", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def quiver(self, *args, plot_method="quiver", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def scatter(self, *args, plot_method="scatter", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def semilogx(self, *args, plot_method="semilogx", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def semilogy(self, *args, plot_method="semilogy", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def specgram(self, *args, plot_method="specgram", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def spy(self, *args, plot_method="spy", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def stackplot(self, *args, plot_method="stackplot", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def stem(self, *args, plot_method="stem", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def step(self, *args, plot_method="step", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def streamplot(self, *args, plot_method="streamplot", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def tricontour(self, *args, plot_method="tricontour", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def tricontourf(self, *args, plot_method="tricontourf", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def tripcolor(self, *args, plot_method="tripcolor", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def triplot(self, *args, plot_method="triplot", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def violinplot(self, *args, plot_method="violinplot", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    def vlines(self, *args, plot_method="vlines", **kwargs): self.figure(None)._render(*args, plot_method=plot_method, **kwargs)
    

_visualization = Visualization()
