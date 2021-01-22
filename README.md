
### Display an image in a window (OpenCV-like interface)

**```imshow(winname, mat)```**

Parameters:
- **winname**: name of the window
- **mat**: image to be shown

Example:

```
from omni.add_on.visualizer import _visualizer
from omni.isaac.synthetic_utils import SyntheticDataHelper

image = SyntheticDataHelper().get_rgb_numpy()

_visualizer.imshow("window", image)
```

### Generate and display a figure using matplotlib.pyplot API (Matplotlib-like interface)

This extension allows the **single-line and easy generation and visualization** of the plotting functions described by the [matplotlib.pyplot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot) API. 

Apart from the **most popular visualization functions** ([```plot```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot), [```scatter```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter), [```bar```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar), [```pie```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pie)), the following functions are supported: 

[```acorr```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.acorr), [```angle_spectrum```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.angle_spectrum), [```barbs```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.barbs), [```barh```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.barh), [```boxplot```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.boxplot), [```broken_barh```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.broken_barh), [```cohere```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.cohere), [```contour```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.contour), [```contourf```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.contourf), [```csd```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.csd), [```errorbar```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.errorbar), [```eventplot```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.eventplot), [```fill```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.fill), [```fill_between```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.fill_between), [```fill_betweenx```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.fill_betweenx), [```hist```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist), [```hist2d```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist2d), [```hlines```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hlines), [```loglog```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.loglog), [```magnitude_spectrum```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.magnitude_spectrum), [```matshow```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.matshow), [```pcolor```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pcolor), [```pcolormesh```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pcolormesh), [```phase_spectrum```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.phase_spectrum), [```plot_date```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot_date), [```polar```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.polar), [```psd```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.psd), [```quiver```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.quiver), [```semilogx```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.semilogx), [```semilogy```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.semilogy), [```specgram```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.specgram), [```spy```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.spy), [```stackplot```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.stackplot), [```stem```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.stem), [```step```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.step), [```streamplot```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.streamplot), [```tricontour```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.tricontour), [```tricontourf```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.tricontourf), [```tripcolor```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.tripcolor), [```triplot```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.triplot), [```violinplot```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.violinplot), [```vlines```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.vlines)

All supported functions **accept the same parameters** as their respective counterparts described in the Matplotlib API reference. However, the generated figures are not interactive

Example:

```
from omni.add_on.visualizer import _visualizer
import numpy as np

x = np.linspace(0, 5, 10)
y = np.cos(2*np.pi*x) * np.exp(-x)

_visualizer.plot(x, y, 'o-')
_visualizer.bar(x, y)
```
