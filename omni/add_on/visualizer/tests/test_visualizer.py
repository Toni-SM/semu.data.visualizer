# NOTE:
#   omni.kit.test - std python's unittest module with additional wrapping to add suport for async/await tests
#   For most things refer to unittest docs: https://docs.python.org/3/library/unittest.html
import omni.kit.test

# Import extension python module we are testing with absolute import path, as if we are external user (other extension)
from omni.add_on.visualizer import _visualizer

import time
import numpy as np

# Having a test class dervived from omni.kit.test.AsyncTestCase declared on the root of module will make it auto-discoverable by omni.kit.test
class TestVisualizer(omni.kit.test.AsyncTestCaseFailOnLogError):
    # Before running each test
    async def setUp(self):
        pass

    # After running each test
    async def tearDown(self):
        pass

    # Actual test, notice it is "async" function, so "await" can be used if needed
    async def test_visualizer(self):
        # image
        print("test_visualizer - image")
        _visualizer.imshow("window", np.zeros((100,100,3), dtype=np.uint8))

        # plot (new figure)
        print("test_visualizer - plot (new figure)")
        x = np.linspace(0, 5, 10)
        y = np.cos(2*np.pi*x) * np.exp(-x)

        _visualizer.plot(x, y, 'ro--')
        _visualizer.bar(x, y)

        # plot (redraw)
        print("test_visualizer - plot (redraw)")
        figure = _visualizer.figure()

        for i in range(3):
            time.sleep(0.1)

            d = np.random.rand(4,50)
            figure.scatter(d[0,:], d[1,:], s=(d[2,:]*30)**2, c=d[3,:], alpha=0.5)

        # plot 3d
        print("test_visualizer - plot 3d")
        states = np.random.random((3,3))
        _visualizer.plot3d(states[:,0], states[:,1], states[:,2], 'o--', c='orange', aspect="equal")

        # native
        print("test_visualizer - native")
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
