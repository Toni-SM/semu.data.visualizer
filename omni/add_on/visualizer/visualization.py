import omni.ui as ui


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
        self._byte_provider = None
        
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
        
    def is_instance(self, num):
        if num == None:
            return False
        return self._num == num

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


_visualization = Visualization()
