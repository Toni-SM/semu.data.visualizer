import os
from distutils.core import setup
from distutils.extension import Extension

from Cython.Distutils import build_ext


# OV python (kit\python\include)
python_library_dir = os.path.join("..", "..", "kit", "python", "include")
if not os.path.exists(python_library_dir):
    python_library_dir = os.path.join("app", os.path.join("..", "..", "app", "kit", "python", "include"))

ext_modules = [
    Extension("_data_visualizer",
              [os.path.join("omni", "add_on", "visualizer", "data_visualizer.py")],
              library_dirs=[python_library_dir]),
]

setup(
    name = 'omni.add_on.visualizer',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
