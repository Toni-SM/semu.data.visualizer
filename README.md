## Data visualizer for NVIDIA Omniverse apps

This extension allows to switch [Matplotlib](https://matplotlib.org/) and [OpenCV](https://docs.opencv.org/) backend to display graphics and images inside NVIDIA Omniverse apps without modifying the code logic

**Target applications:** Any NVIDIA Omniverse app

**Supported OS:** Windows and Linux 

**Table of Contents:**

- [Extension setup](#setup)
- [Extension usage](#usage)

<hr>

<a name="setup"></a>
### Extension setup

1. Add the extension using the [Extension Manager](https://docs.omniverse.nvidia.com/prod_extensions/prod_extensions/ext_extension-manager.html) or by following the steps described in [Extension Search Paths](https://docs.omniverse.nvidia.com/py/kit/docs/guide/extensions.html#extension-search-paths)

    * Git url (git+https) as extension search path: 
    
        ```
        git+https://github.com/Toni-SM/omni.add_on.visualizer.git?branch=main&dir=exts
        ```

    * Compressed (.zip) file for import

        [omni.add_on.visualizer.zip](https://github.com/Toni-SM/omni.add_on.visualizer/releases)

2. Enable the extension using the [Extension Manager](https://docs.omniverse.nvidia.com/prod_extensions/prod_extensions/ext_extension-manager.html) or by following the steps described in [Extension Enabling/Disabling](https://docs.omniverse.nvidia.com/py/kit/docs/guide/extensions.html#extension-enabling-disabling)

<hr>

<a name="usage"></a>
### Extension usage

**Enabling the extension** switches the Matplotlib and OpenCV backends **to display graphics and images in the Omniverse app**

To **revert the changes** (display the graphics and images in a separate application window using the frameworks of the libraries according to the operating system) it is only necessary to disable the extension