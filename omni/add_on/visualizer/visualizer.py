import os
import sys

import omni
import omni.ui as ui

try:
    import numpy as np
except ImportError:
    print("numpy not found. Attempting to install...")
    omni.kit.pipapi.install("numpy")
    import numpy as np
try:
    import matplotlib
except ImportError:
    print("matplotlib not found. Attempting to install...")
    omni.kit.pipapi.install("matplotlib")
    import matplotlib
try:
    import cv2
except ImportError:
    print("opencv-python not found. Attempting to install...")
    omni.kit.pipapi.install("opencv-python")
    import cv2

from matplotlib.figure import Figure
from matplotlib.backend_bases import FigureManagerBase
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib._pylab_helpers import Gcf


def acquire_visualizer_interface(ext_id: str = "") -> dict:
    """Acquire the visualizer interface

    :param ext_id: The extension id
    :type ext_id: str

    :returns: The interface
    :rtype: dict
    """
    # add current path to sys.path to import the backend
    path = os.path.dirname(__file__)
    if path not in sys.path:
        sys.path.append(path)

    matplotlib_backend = matplotlib.get_backend()
    interface = {"matplotlib_backend": matplotlib_backend if type(matplotlib_backend) is str else "Agg",
                 "opencv_imshow": cv2.imshow,
                 "opencv_waitKey": cv2.waitKey}
    
    if os.path.basename(__file__).startswith("_visualizer"):
        matplotlib.use("module://_visualizer")
    else:
        print(">>>> [DEVELOPMENT] module://visualizer")
        matplotlib.use("module://visualizer")
    
    cv2.imshow = imshow
    cv2.waitKey = waitKey

    return interface

def release_visualizer_interface(interface: dict) -> None:
    """Release the visualizer interface

    :param interface: The interface to release
    :type interface: dict
    """
    # restore default matplotlib backend
    try:
        matplotlib.use(interface.get("matplotlib_backend", "Agg"))
    except Exception as e:
        pass
    matplotlib.rcdefaults()

    # restore default opencv imshow
    try:
        cv2.imshow = interface.get("opencv_imshow", None)
        cv2.waitKey = interface.get("opencv_waitKey", None)
    except Exception as e:
        pass

    # remove current path from sys.path
    path = os.path.dirname(__file__)
    if path in sys.path:
        sys.path.remove(path)


# opencv backend

def imshow(winname: str, mat: np.ndarray) -> None:
    """Show the image

    :param winname: The window name
    :type winname: str
    :param mat: The image
    :type mat: np.ndarray
    """
    print(">>>> [DEVELOPMENT] imshow")

def waitKey(delay: int = 0) -> int:
    """Wait for a key press on the canvas

    :param delay: The delay in milliseconds
    :type delay: int

    :returns: The key code
    :rtype: int
    """
    return -1


# matplotlib backend

def draw_if_interactive():
    """
    For image backends - is not required.
    For GUI backends - this should be overridden if drawing should be done in
    interactive python mode.
    """
    print(">>>> [DEVELOPMENT] draw_if_interactive")

def show(*, block: bool = None) -> None:
    """Show all figures and enter the main loop

    For image backends - is not required.
    For GUI backends - show() is usually the last line of a pyplot script and
    tells the backend that it is time to draw.  In interactive mode, this should do nothing

    :param block: If not None, the call will block until the figure is closed
    :type block: bool
    """
    for manager in Gcf.get_all_fig_managers():
        manager.show(block=block)

def new_figure_manager(num: int, *args, FigureClass: type = Figure, **kwargs) -> 'FigureManagerOmniUi':
    """Create a new figure manager instance
    
    :param num: The figure number
    :type num: int
    :param args: The arguments to be passed to the Figure constructor
    :type args: tuple
    :param FigureClass: The class to use for creating the figure
    :type FigureClass: type
    :param kwargs: The keyword arguments to be passed to the Figure constructor
    :type kwargs: dict

    :returns: The figure manager instance
    :rtype: FigureManagerOmniUi
    """
    return new_figure_manager_given_figure(num, FigureClass(*args, **kwargs))

def new_figure_manager_given_figure(num: int, figure: 'Figure') -> 'FigureManagerOmniUi':
    """Create a new figure manager instance for the given figure.

    :param num: The figure number
    :type num: int
    :param figure: The figure
    :type figure: Figure

    :returns: The figure manager instance
    :rtype: FigureManagerOmniUi
    """
    canvas = FigureCanvasAgg(figure)
    manager = FigureManagerOmniUi(canvas, num)
    return manager


class FigureManagerOmniUi(FigureManagerBase):
    def __init__(self, canvas: 'FigureCanvasBase', num: int) -> None:
        """Figure manager for the Omni UI backend

        :param canvas: The canvas
        :type canvas: FigureCanvasBase
        :param num: The figure number
        :type num: int
        """
        super().__init__(canvas, num)

        self._window_title = "Figure {}".format(num) if type(num) is int else num
        self._byte_provider = None
        self._window = None 

    def destroy(self) -> None:
        """Destroy the figure window"""
        try:
            self._byte_provider = None
            self._window = None
        except:
            pass

    def set_window_title(self, title: str) -> None:
        """Set the window title

        :param title: The title
        :type title: str
        """
        self._window_title = title
        try:
            self._window.title = title
        except:
            pass

    def get_window_title(self) -> str:
        """Get the window title

        :returns: The window title
        :rtype: str
        """
        return self._window_title

    def resize(self, w: int, h: int) -> None:
        """Resize the window

        :param w: The width
        :type w: int
        :param h: The height
        :type h: int
        """
        print("[WARNING] resize() is not implemented")

    def show(self, *, block: bool = None) -> None:
        """Show the figure window

        :param block: If not None, the call will block until the figure is closed
        :type block: bool
        """
        # draw canvas and get figure
        self.canvas.draw()
        image = np.asarray(self.canvas.buffer_rgba())
        height, width = image.shape[:2]

        # enable the window visibility
        if self._window is not None and not self._window.visible:
            self._window.visible = True

        # create the byte provider    
        if self._byte_provider is None:
            self._byte_provider = ui.ByteImageProvider()
            self._byte_provider.set_bytes_data(image.flatten().tolist(), [width, height])
            # create the window
            if self._window is None:
                self._window = ui.Window(self._window_title,
                                         width=self.canvas.figure.get_figwidth() * self.canvas.figure.get_dpi(), 
                                         height=self.canvas.figure.get_figheight() * self.canvas.figure.get_dpi(),
                                         visible=True)
                with self._window.frame:
                    with ui.VStack():
                        ui.ImageWithProvider(self._byte_provider)
        # update the byte provider
        else:
            self._byte_provider.set_bytes_data(image.flatten().tolist(), [width, height])


# provide the standard names that backend.__init__ is expecting
FigureCanvas = FigureCanvasAgg
FigureManager = FigureManagerOmniUi
