from __future__ import print_function
import matplotlib.widgets as widgets
import numpy as np
import matplotlib.pyplot as plt


class MyRectangleSelector(widgets.RectangleSelector):

    def release(self, event):
        super(MyRectangleSelector, self).release(event)
        self.to_draw.set_visible(True)
        self.canvas.draw()


def line_select_callback(eclick, erelease):
    'eclick and erelease are the press and release events'
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    print("(%3.2f, %3.2f) --> (%3.2f, %3.2f)" % (x1, y1, x2, y2))
    print(" The button you used were: %s %s" %
          (eclick.button, erelease.button))


def toggle_selector(event):
    print(' Key pressed.')
    if event.key in ['Q', 'q'] and toggle_selector.RS.active:
        print(' RectangleSelector deactivated.')
        toggle_selector.RS.set_active(False)
    if event.key in ['A', 'a'] and not toggle_selector.RS.active:
        print(' RectangleSelector activated.')
        toggle_selector.RS.set_active(True)


fig, current_ax = plt.subplots()                    # make a new plotingrange
N = 100000                                       # If N is large one can see
x = np.linspace(0.0, 10.0, N)                    # improvement by use blitting!

plt.plot(x, +np.sin(.2 * np.pi * x), lw=3.5, c='b', alpha=.7)  # plot something
plt.plot(x, +np.cos(.2 * np.pi * x), lw=3.5, c='r', alpha=.5)
plt.plot(x, -np.sin(.2 * np.pi * x), lw=3.5, c='g', alpha=.3)

print("\n      click  -->  release")

# drawtype is 'box' or 'line' or 'none'
toggle_selector.RS = MyRectangleSelector(current_ax, line_select_callback,
                                         drawtype='box', useblit=True,
                                         # don't use middle button
                                         button=[1, 3],
                                         minspanx=5, minspany=5,
                                         spancoords='pixels')
plt.connect('key_press_event', toggle_selector)
plt.show()
