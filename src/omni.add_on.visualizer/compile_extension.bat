
@REM delete old files
CALL clean_extension

@REM compile code
..\..\app\kit\python\python.exe compile_extension.py build_ext --inplace --compiler=mingw32 -DMS_WIN64

@REM move compiled files
MOVE *.pyd omni\\add_on\\visualizer

@REM delete temporal data
RMDIR /S /Q build
DEL /F /Q omni\\add_on\\visualizer\\*.c
