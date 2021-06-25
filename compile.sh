export LIBRARY_PATH=/isaac-sim/kit/python/include

# delete old data
rm -r build
rm _data*.so
rm omni/add_on/visualizer/*.so
rm omni/add_on/visualizer/*.c

# compile code
/isaac-sim/kit/python/bin/python3 compile.py build_ext --inplace

# # move compiled file
mv _data_visualizer.cpython-37m-x86_64-linux-gnu.so omni/add_on/visualizer/

# delete temporal data
rm -r build
rm omni/add_on/visualizer/*.c
