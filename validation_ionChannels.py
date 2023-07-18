from brian2 import *


def validate_activation_inactivation(myelinated_axon):
    defaultclock.dt = 0.01 * ms

    myelinated_axon.v = np.linspace(-100, 100, len(myelinated_axon)) * mV

    plt.plot(myelinated_axon.v / mV, myelinated_axon.m_inf[:], label=r'$m_\infty$')
    plt.plot(myelinated_axon.v / mV, myelinated_axon.h_inf[:], label=r'$h_\infty$')
    plt.plot(myelinated_axon.v / mV, myelinated_axon.mp_inf[:], label=r'$mp_\infty$')
    plt.plot(myelinated_axon.v / mV, myelinated_axon.s_inf[:], label=r'$s_\infty$')

    plt.title('Steady-State Activation/Inactivation')
    plt.xlabel('V (mV)')
    plt.ylabel(r'$x_\infty$ (unitless)')
    plt.legend()
    plt.grid()
    plt.show()

    return 0


def validate_timeConsts(myelinated_axon, simple):
    defaultclock.dt = 0.01 * ms

    if simple:
        myelinated_axon.v = np.linspace(-100, 100, len(myelinated_axon)) * mV

        plt.plot(myelinated_axon.v / mV, myelinated_axon.tau_m[:] / ms, label=r'$\tau_m$')
        plt.plot(myelinated_axon.v / mV, myelinated_axon.tau_h[:] / ms, label=r'$\tau_h$')
        plt.plot(myelinated_axon.v / mV, myelinated_axon.tau_mp[:] / ms, label=r'$\tau_{mp}$', color='green')
        plt.plot(myelinated_axon.v / mV, myelinated_axon.tau_s[:] / ms, label=r'$\tau_s$', color='red')

        plt.title('Channel Time Constants')
        plt.xlabel('V (mV)')
        plt.ylabel(r'$\tau_x$ (ms)')
        plt.legend()
        plt.grid()
        plt.show()

    else:
        fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(15, 8.1))
        myelinated_axon.v = np.linspace(-100, 100, len(myelinated_axon)) * mV

        ax1.plot(myelinated_axon.v / mV, myelinated_axon.tau_s[:] / ms, label=r'$\tau_s$', color='red')
        ax1.set_title('Channel Time Constants')
        ax1.set_xlabel('V (mV)')
        ax1.set_ylabel(r'$\tau_x$ (ms)')
        ax1.legend()
        ax1.grid()

        ax2.plot(myelinated_axon.v / mV, myelinated_axon.tau_m[:] / ms, label=r'$\tau_m$')
        ax2.plot(myelinated_axon.v / mV, myelinated_axon.tau_h[:] / ms, label=r'$\tau_h$')
        ax2.set_title('Channel Time Constants')
        ax2.set_xlabel('V (mV)')
        ax2.set_ylabel(r'$\tau_x$ (ms)')
        ax2.legend()
        ax2.grid()

        ax3.plot(myelinated_axon.v / mV, myelinated_axon.tau_mp[:] / ms, label=r'$\tau_{mp}$', color='green')
        ax3.set_title('Channel Time Constants')
        ax3.set_xlabel('V (mV)')
        ax3.set_ylabel(r'$\tau_x$ (ms)')
        ax3.legend()
        ax3.grid()

        fig.tight_layout()
        plt.show()

    return 0
