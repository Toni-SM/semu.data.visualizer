import omni.ext

try:
    from . import _backend
except:
    print(">>>> [DEVELOPMENT] import backend")
    from . import backend as _backend


class Extension(omni.ext.IExt):
    def on_startup(self, ext_id):
        self._interface = _backend.acquire_visualizer_interface(ext_id)

    def on_shutdown(self):
        _backend.release_visualizer_interface(self._interface)
