import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

x0 = 0


def h(t, y, w, a):
    return 1 / np.cos(w * t + a * y)


# def h(t, y, w, a):
#    return 1 / np.cos(w * t * a * y)


def xp(t, y, w, a):
    return w / (h(t, y, w, a) - a)


y0 = 0.0
# a = 0.25
w = 1.0
# ms = 0.0001
ms = 0.001


def solve_shit(t0=0.0, t1=2 * np.pi, max_step=ms, y0=y0, a=0, w=w):
    return sp.integrate.solve_ivp(xp, (t0, t1), [y0], args=(w, a), max_step = max_step)


feedback = np.linspace(-0.9, 0.9, 20)
feedback = np.append(feedback, [0.0])

# feedback = np.linspace(-1.0, 0.999, 10)

# plt.plot(solution.t, solution.y[0])
for fb in feedback:
    solution = solve_shit(w=w, a=fb)
    t = solution.t
    x = solution.y[0]
    dx = xp(t, x, w=w, a=fb)
    fig, ax = plt.subplots(1, layout="constrained")
    # ax[0].plot(t, x)
    ax.plot(x, dx)

    # ax[0].set_box_aspect(0.5)
    ax.set_box_aspect(1)
    # ax[0].set_xlabel(r"$t$")
    # ax[0].set_ylabel(r"$x(t)$")
    ax.set_xlabel(r"$x(t)$")
    ax.set_ylabel(r"$x'(t)$")
    ax.set_title(r"$\frac{d x(t)}{dt} = \frac{\omega}{\sec(\omega t + a x(t)) - a}$")

    plt.suptitle(f"$a = {fb}$")
    plt.savefig(f"figs/phase_portrait/pp_{fb}.pdf")
    plt.close()
