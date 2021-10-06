import omni.ext
try:
    from .. import _data_visualizer
except:
    print(">>>> [DEVELOPMENT] import data_visualizer")
    from .. import data_visualizer as _data_visualizer

__all__ = ["Extension", "_visualizer"]

_visualizer = _data_visualizer.Visualizer()


class Extension(omni.ext.IExt):
    def on_startup(self):
        pass

    def on_shutdown(self):
        pass
