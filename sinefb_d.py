import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as ply

feedback = np.linspace(-2.0, 2.0, 20)
feedback = np.append(feedback, [-1.0, 1.0, 0.0, 0.25, -0.25, 0.5, -0.5, -1.125, 1.125, 1.25, -1.25])

t_min = 0.0
t_max = 2 * np.pi
steps = 10000
# steps = 100000
time = np.linspace(t_min, t_max, steps)


def phasor(time, feedback_amt, steps=steps):
    phasor = np.linspace(time[0], time[1], steps)
    for t in np.arange(1, steps):
        phasor[t] = (phasor[t] + feedback_amt * np.sin(phasor[t - 1]))  # % (2 * np.pi)

    return phasor


def fit_to_polynomial(time, phasor, degree=8):
    poly = ply.Polynomial.fit(time, phasor, deg=degree)
    return poly


def plot_phasors(time=time, feedback=feedback):
    for fb in feedback:
        fig, ax = plt.subplots(2)
        phs = phasor([t_min, t_max], fb)
        # print(fb)
        # print(fit_to_polynomial(time, phs))
        fig.suptitle(f"Sine feedback for $a = {fb}$.")
        ax[0].scatter(time, phs, s=0.25)
        ax[1].scatter(time, np.sin(phs), s=0.25)
        ax[0].set_ylabel(r"$\phi(t)$")
        ax[1].set_ylabel(r"$\sin[\phi(t)]$")
        fig.tight_layout()
        plt.savefig(f"figs/phasor/phasor_{fb}.pdf")
        plt.close()


def plot_spectrum(time=time, feedback=feedback):
    for fb in feedback:
        phs = phasor(time, fb)
        phs_0 = []
        phs_1 = []
        for t in range(1, len(time)):
            phs_0.append(phs[t - 1])
            phs_1.append(phs[t])
        phs_0 = np.array(phs_0)
        phs_1 = np.array(phs_1)
        plt.scatter(phs_0, phs_1)
        plt.xlabel(r"$\phi(t)$")
        plt.ylabel(r"$\phi(t + dt)$")
        plt.savefig(f"figs/map/map_{fb}.pdf")
        plt.close()


plot_phasors()
plot_spectrum()
