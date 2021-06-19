import omni.ext
from .. import _visualizer as visualizer

__all__ = ["_visualizer"]
_visualizer = visualizer.Visualizer()

EXTENSION_NAME = "Data Visualizer"


class Extension(omni.ext.IExt):
    def on_startup(self):
        pass

    def on_shutdown(self):
        pass
