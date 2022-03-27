import omni.ext

try:
    from .. import _visualizer
except:
    print(">>>> [DEVELOPMENT] import visualizer")
    from .. import visualizer as _visualizer


class Extension(omni.ext.IExt):
    def on_startup(self, ext_id):
        self._interface = _visualizer.acquire_visualizer_interface(ext_id)

    def on_shutdown(self):
        _visualizer.release_visualizer_interface(self._interface)
