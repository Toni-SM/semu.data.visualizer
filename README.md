# omni.add_on.visualizer

Data visualizer for NVIDIA Omniverse (Matplotlib and OpenCV-like interfaces and native Omniverse plots)

> This extension (developed especially for headless containers and cloud deployments) allows the graphic representation of data using **Matplotlib and OpenCV-like interfaces** and **native Omniverse plots**

<br>

### Table of Contents

- [Add the extension to a NVIDIA Omniverse app and enable it](#extension)
- [Display an image in a window (OpenCV-like interface)](#visualizer-image)
- [Generate and display a figure using the matplotlib.pyplot API (Matplotlib-like interface)](#visualizer-pyplot)
- [Generate and display a 3D figure using the mplot3d Toolkit API (Matplotlib-like interface)](#visualizer-mplot3d)
- [Generate and display an Omniverse (native) figure](#visualizer-native)

<br>

<a name="extension"></a>
### Add the extension to a NVIDIA Omniverse app and enable it

1. Add the the extension by following the steps described in [Extension Search Paths](https://docs.omniverse.nvidia.com/py/kit/docs/guide/extensions.html#extension-search-paths)

2. Enable the extension by following the steps described in [Extension Enabling/Disabling](https://docs.omniverse.nvidia.com/py/kit/docs/guide/extensions.html#extension-enabling-disabling)

3. Import the extension into any python code and use it...

    ```python
    from omni.add_on.visualizer import _visualizer
    ```

<br>

<a name="visualizer-image"></a>
### Display an image in a window (OpenCV-like interface)

---
**```_visualizer.imshow(winname, mat) -> None```**

Displays an image in the specified window

Parameters:
- **winname** (str): name of the window
- **mat** (numpy.ndarray): image to be shown

---
Example:

```python
import omni
from omni.syntheticdata import sensors
from omni.add_on.visualizer import _visualizer

image = sensors.get_rgb(omni.kit.viewport.get_default_viewport_window())
_visualizer.imshow("window", image)
```

![imshow](https://user-images.githubusercontent.com/22400377/105614872-9174e200-5dcc-11eb-940c-198ec99688d2.png)

<br>

<a name="visualizer-pyplot"></a>
### Generate and display a figure using the matplotlib.pyplot API (Matplotlib-like interface)

This extension allows the **single-line and easy generation and visualization** of the plotting methods described by the [matplotlib.pyplot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot) API

Apart from the **most popular visualization methods** ([```plot```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot), [```scatter```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter), [```bar```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar), [```pie```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pie)), the following methods are supported: 

[```acorr```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.acorr), [```angle_spectrum```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.angle_spectrum), [```barbs```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.barbs), [```barh```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.barh), [```boxplot```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.boxplot), [```broken_barh```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.broken_barh), [```cohere```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.cohere), [```contour```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.contour), [```contourf```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.contourf), [```csd```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.csd), [```errorbar```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.errorbar), [```eventplot```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.eventplot), [```fill```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.fill), [```fill_between```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.fill_between), [```fill_betweenx```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.fill_betweenx), [```hist```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist), [```hist2d```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist2d), [```hlines```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hlines), [```loglog```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.loglog), [```magnitude_spectrum```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.magnitude_spectrum), [```matshow```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.matshow), [```pcolor```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pcolor), [```pcolormesh```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pcolormesh), [```phase_spectrum```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.phase_spectrum), [```plot_date```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot_date), [```polar```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.polar), [```psd```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.psd), [```quiver```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.quiver), [```semilogx```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.semilogx), [```semilogy```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.semilogy), [```specgram```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.specgram), [```spy```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.spy), [```stackplot```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.stackplot), [```stem```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.stem), [```step```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.step), [```streamplot```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.streamplot), [```tricontour```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.tricontour), [```tricontourf```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.tricontourf), [```tripcolor```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.tripcolor), [```triplot```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.triplot), [```violinplot```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.violinplot), [```vlines```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.vlines)

All these methods could be called directly from the main **```_visualizer```** object. In this case, the call will create a new figure each time. To create a figure and update its content use the **```_visualizer.figure```** method which returns a Figure object. Each plotting call, through this object, will update (redraw) the content of the figure

Parameters:

All supported methods **accept the same parameters** as their respective counterparts described in the Matplotlib API reference and don't return anything. However, the generated figures are not interactive

Additionality, they accept an experimental parameter (aspect="equal") designed to allow the same scaling from data to plot units

---
Example (create a new figure each time):

```python
from omni.add_on.visualizer import _visualizer
import numpy as np

x = np.linspace(0, 5, 10)
y = np.cos(2*np.pi*x) * np.exp(-x)

_visualizer.plot(x, y, 'ro--')
_visualizer.bar(x, y)
```

![pyplot](https://user-images.githubusercontent.com/22400377/105614874-92a60f00-5dcc-11eb-8224-1b10222f1d6e.png)

<br>

Example (redraw the content of the current figure):

```python
from omni.add_on.visualizer import _visualizer
import numpy as np
import time

figure = _visualizer.figure()

for i in range(3):
    time.sleep(1.0)
    d = np.random.rand(4,50)

    figure.scatter(d[0,:], d[1,:], s=(d[2,:]*30)**2, c=d[3,:], alpha=0.5)
```

![figure](https://user-images.githubusercontent.com/22400377/105614871-90dc4b80-5dcc-11eb-8eff-9dd79e1fcaf7.png)

<br>

<a name="visualizer-mplot3d"></a>
### Generate and display a 3D figure using the mplot3d Toolkit API (Matplotlib-like interface)

Also, this extension allows the **single-line and easy generation and visualization** of the 3D plotting methods described by the [Matplotlib mplot3d Toolkit](https://matplotlib.org/tutorials/toolkits/mplot3d) API

The following methods are supported: [```plot3d```](https://matplotlib.org/tutorials/toolkits/mplot3d#line-plots), [```scatter3d```](https://matplotlib.org/tutorials/toolkits/mplot3d#scatter-plots), [```plot_wireframe3d```](https://matplotlib.org/tutorials/toolkits/mplot3d#wireframe-plots), [```plot_surface3d```](https://matplotlib.org/tutorials/toolkits/mplot3d#surface-plots), [```plot_trisurf3d```](https://matplotlib.org/tutorials/toolkits/mplot3d#tri-surface-plots), [```contour3d```](https://matplotlib.org/tutorials/toolkits/mplot3d#contour-plots), [```contourf3d```](https://matplotlib.org/tutorials/toolkits/mplot3d#filled-contour-plots), [```add_collection3d```](https://matplotlib.org/tutorials/toolkits/mplot3d#polygon-plots), [```bar3d```](https://matplotlib.org/tutorials/toolkits/mplot3d#bar-plots), [```quiver3d```](https://matplotlib.org/tutorials/toolkits/mplot3d#quiver), [```text3d```](https://matplotlib.org/tutorials/toolkits/mplot3d#text)

All these methods could be called directly from the main **```_visualizer```** object. In this case, the call will create a new 3D figure each time. To create a 3D figure and update its content use the **```_visualizer.figure3d```** method which returns a Figure3D object. Each plotting call, through this object, will update (redraw) the content of the figure. **Note that the "-3d" suffix is added to the original API names**. This is needed to differentiate from the 2D matplotlib.pyplot names (however, it is possible to use the original name but only from an instance of Figure3D class returned by the **```_visualizer.figure3d```** method)

Parameters:

All supported methods **accept the same parameters** as their respective counterparts described in the Matplotlib API reference and don't return anything. However, the generated figures are not interactive

Additionality, they accept an experimental parameter (```aspect="equal"```) designed to allow the same scaling from data to plot units (*"mplot3d Axes 3D does not currently support any aspect but 'auto' which fills the axes with the data limits"* according to the [reference](https://matplotlib.org/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_aspect))

---
Example:

```python
from omni.add_on.visualizer import _visualizer
from omni.isaac.dynamic_control import _dynamic_control
import numpy as np

dci = _dynamic_control.acquire_dynamic_control_interface()
ar = dci.get_articulation("/environments/Kuka/iiwa14")

states = dci.get_articulation_body_states(ar, _dynamic_control.STATE_ALL)
states = np.array([s[0][0].tolist() for s in states])[:-2,:]

_visualizer.plot3d(states[:,0], states[:,1], states[:,2], 'o--', c='orange', aspect="equal")
```

![mplot3d](https://user-images.githubusercontent.com/22400377/106672085-cb559d80-65af-11eb-965c-e2baa1274b09.png)

<br>

<a name="visualizer-native"></a>
### Generate and display an Omniverse (native) figure

---
**```_visualizer.native_figure(num, figsize, ppu) -> NativeFigure```**

Create a native figure  

Parameters:
- **num** (int, float, srt or None): unique identifier for the figure. If the parameter is not given, a new identifier is created based on the current system time -  default: None
- **figsize** (tuple): width and height of the window in arbitrary units - default: (6.4, 4.8)
- **ppu** (float): pixels-per-unit conversion factor - default: 100.0

---
**```NativeFigure.add_plot(title, lines, colors, ylim, window_size, theme) -> NativePlot```**

Add a new native plot to the current native figure

Parameters:
- **title** (str): title of the frame - default: ""
- **lines** (int): number of line plots to handle in the current frame - default: 1
- **colors** (list): line plot color. The format of the colors follows the [matplotlib.colors](https://matplotlib.org/api/colors_api) reference. If the number of colors is different from the number of lines, a subset of predefined colors will be selected - default: []
- **ylim (tuple or None)**: limits of the Y axis - default: None
- **window_size** (int or None): amount of data to be shown in the frame (the data is represented using a double-ended queue). If this parameter is less or equal than zero or None the data will be represented as an accumulative list - default: 250
- **theme** (str): set the background color of the frame according to the selected mode: "light" or "dark" - default: "light"

---
**```NativePlot.add_data(data) -> None```**

Add a new data to the current native plot and show it

Parameters:
- **data** (int, float or numeric iterable object: list, tuple, numpy.ndarray, etc.): Data to be added. The numeric iterable object must to have the same length of the number of lines plot defined. If the data is a single number (int, float) only the first line will be updated

---
**```NativePlot.set_data(data) -> None```**

Set a new completed subset of data (for each line plot) to the current native plot and show them

Parameters:
- **data** (collection of numeric iterable objects: list, tuple, collections.queue, numpy.ndarray, etc.): Data to be added. Each subset of data will overwrite previous ones. The numeric iterable object must to have the same length of the number of lines plot defined. Each subset of data must to implement the .append(...) method (numpy.ndarray type will be converted to list automatically)

---
Example:

```python
from omni.add_on.visualizer import _visualizer
import numpy as np
import time

title1 = "[Plot 1] lines: 1, window_size: 20, theme: light (default)"
title2 = "[Plot 2] lines: 3, window_size: None, theme: dark, colors: [pink, lime, skyblue]"

native_figure = _visualizer.native_figure()
plot1 = native_figure.add_plot(title1, lines=1, window_size=20)
plot2 = native_figure.add_plot(title2, lines=3, window_size=None, colors=['pink', 'lime', 'skyblue'], theme='dark')

for i in range(40):
    time.sleep(0.1)
    d = np.random.rand(3)

    plot1.add_data([d[0]])
    plot2.add_data(d)
```

![native_figure](https://user-images.githubusercontent.com/22400377/105614868-9043b500-5dcc-11eb-8956-d2216d45d126.png)
