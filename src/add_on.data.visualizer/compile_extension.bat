
SET OV_PYTHON_INTERPRETER=%USERPROFILE%\AppData\Local\ov\pkg\code-2022.1.0\kit\python\python.exe

@REM delete old files
CALL clean_extension

@REM compile code
%OV_PYTHON_INTERPRETER% compile_extension.py build_ext --inplace --compiler=mingw32 -DMS_WIN64

@REM move compiled files
MOVE *.pyd add_on\\data\\visualizer

@REM delete temporal data
RMDIR /S /Q build
DEL /F /Q add_on\\data\\visualizer\\*.c
