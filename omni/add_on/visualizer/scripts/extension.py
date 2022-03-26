import omni.ext
try:
    from .. import _visualizer as __visualizer
except:
    print(">>>> [DEVELOPMENT] import visualizer")
    from .. import visualizer as __visualizer

__all__ = ["_visualizer"]
_visualizer = __visualizer.Visualizer()


class Extension(omni.ext.IExt):
    def on_startup(self, ext_id):
        pass

    def on_shutdown(self):
        pass
