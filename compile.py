from distutils.core import setup
from distutils.extension import Extension

from Cython.Distutils import build_ext


ext_modules = [
    Extension("_data_visualizer",
              ["omni/add_on/visualizer/data_visualizer.py"],
              library_dirs=['/isaac-sim/kit/python/include']),
]

setup(
    name = 'omni.add_on.visualizer',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
