## Data visualizer for NVIDIA Omniverse apps

This extension allows to switch [Matplotlib](https://matplotlib.org/) and [OpenCV](https://docs.opencv.org/) backend to display graphics and images inside NVIDIA Omniverse apps without modifying the code logic

<br>

**Target applications:** Any NVIDIA Omniverse app

**Supported OS:** Windows and Linux 

**Table of Contents:**

- [Extension setup](#setup)
- [Extension usage](#usage)

<br>

![showcase](https://user-images.githubusercontent.com/22400377/160294178-9b463c7c-bcef-4748-94c1-ecc3467c1e62.png)

<hr>

<a name="setup"></a>
### Extension setup

1. Add the extension using the [Extension Manager](https://docs.omniverse.nvidia.com/prod_extensions/prod_extensions/ext_extension-manager.html) or by following the steps in [Extension Search Paths](https://docs.omniverse.nvidia.com/py/kit/docs/guide/extensions.html#extension-search-paths)

    * Git url (git+https) as extension search path
    
        ```
        git+https://github.com/Toni-SM/add_on.data.visualizer.git?branch=main&dir=exts
        ```

    * Compressed (.zip) file for import

        [add_on.data.visualizer.zip](https://github.com/Toni-SM/add_on.data.visualizer/releases)

2. Enable the extension using the [Extension Manager](https://docs.omniverse.nvidia.com/prod_extensions/prod_extensions/ext_extension-manager.html) or by following the steps in [Extension Enabling/Disabling](https://docs.omniverse.nvidia.com/py/kit/docs/guide/extensions.html#extension-enabling-disabling)

<hr>

<a name="usage"></a>
### Extension usage

**Enabling the extension** switches the Matplotlib and OpenCV backends **to display graphics and images in the Omniverse app**

Disabling the extension reverts the changes: graphics and images will be displayed in their respective windows by default, outside the Omniverse app

> **Note:** The current implementation does not support interaction with the displayed graphics or images
