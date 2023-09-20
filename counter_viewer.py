import sys
import pylink
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from functools import partial
from collections import deque

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i, jlink, memory_address, xs, ys, interval):
    read = jlink.memory_read32(memory_address, 1)

    ys.append(float(read[0]))
    xs.append(float(i * (interval/1000)))

    xslist = list(xs)
    yslist = list(ys)

    ax1.clear()
    ax1.plot(xslist, yslist)

def counter_viewer(device, address, intervalMs):
    """Polls the content of the counter variable at address address.
    Args:
      device (str): the target CPU
      address: the address of the uint32_t counter variable in hex
      interval: the polling interval in milliseconds

    Returns:
      Always returns ``0``.

    Raises:
      JLinkException: on error
    """
    jlink = pylink.JLink()
    jlink.open()
    jlink.set_tif(pylink.enums.JLinkInterfaces.SWD)
    jlink.connect(device, verbose=True)

    memory_address = int(address, 16)
    polling_interval = int(intervalMs, 10)

    xs = deque(maxlen=100)
    ys = deque(maxlen=100)

    ani = animation.FuncAnimation(fig, partial(animate, jlink=jlink, memory_address=memory_address, 
                                  xs=xs, ys=ys, interval=polling_interval), interval=polling_interval, cache_frame_data=False)
    plt.show()


if __name__ == '__main__':
    counter_viewer(sys.argv[1], sys.argv[2], sys.argv[3])
