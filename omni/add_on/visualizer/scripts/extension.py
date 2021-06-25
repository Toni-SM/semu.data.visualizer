import omni.ext
try:
    from .. import _data_visualizer
except:
    print(">>>> [DEVELOPMENT] import data_visualizer")
    from .. import data_visualizer as _data_visualizer

__all__ = ["_visualizer"]
_visualizer = _data_visualizer.Visualizer()

EXTENSION_NAME = "Data Visualizer"


class Extension(omni.ext.IExt):
    def on_startup(self):
        pass

    def on_shutdown(self):
        pass
