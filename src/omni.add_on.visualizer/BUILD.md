## Building form source

### Linux

```bash
cd src/omni.add_on.visualizer
bash compile_extension.bash
```

### Windows (Microsoft Visual C++ (MSVC))

We don't do that here!

### Windows (MinGW64)

#### Build extension

```batch
cd src\omni.add_on.visualizer
compile_extension.bat
```

#### Troubleshooting

* **Cannot find -lvcruntime140: No such file or directory**

    ```
    cannot find -lvcruntime140: No such file or directory
    ```

    Find and copy `vcruntime140.dll` to `...mingw64\lib\`

* **Error: enumerator value for '__pyx_check_sizeof_voidp' is not an integer constant**

    ```
    error: enumerator value for '__pyx_check_sizeof_voidp' is not an integer constant
    ```

    Add -DMS_WIN64 to the build command (Cython issue [#2670](https://github.com/cython/cython/issues/2670#issuecomment-432212671))

* **ValueError: Unknown MS Compiler version XXXX**

    ```
    ValueError: Unknown MS Compiler version XXXX
    ```

    Apply this [path](https://bugs.python.org/file40608/patch.diff) or just return `return ['vcruntime140']` in `...distutils\cygwinccompiler.py`
    
## Removing old compiled files

Get a fresh clone of the repository and follow the next steps

```bash
# remove compiled files _visualizer.cpython-37m-x86_64-linux-gnu.so
git filter-repo --invert-paths --path exts/omni.add_on.visualizer/omni/add_on/visualizer/_visualizer.cpython-37m-x86_64-linux-gnu.so
git filter-repo --invert-paths --path exts/omni.add_on.visualizer/omni/add_on/visualizer/_visualizer.cp37-win_amd64.pyd

# add origin
git remote add origin git@github.com:Toni-SM/omni.add_on.visualizer.git

# push changes
git push origin --force --all
git push origin --force --tags
```

## Packaging the extension

```bash
cd src/omni.add_on.visualizer
bash package_extension.bash
```