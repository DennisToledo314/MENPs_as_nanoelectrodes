from brian2 import *


def a_potential(myelinated_axon, na_potential, k_potential):
    defaultclock.dt = 0.01 * ms

    M = StateMonitor(myelinated_axon, 'v', record=True)

    run(50 * ms, report='text')
    myelinated_axon.i_appl[2] = 2000 * pA

    run(5 * ms)
    myelinated_axon.i_appl[2] = 0 * amp
    run(50 * ms, report='text')
    myelinated_axon.i_appl[2] = 2000 * pA

    run(5 * ms)
    myelinated_axon.i_appl[2] = 0 * amp
    run(50 * ms, report='text')
    myelinated_axon.i_appl[2] = 2000 * pA

    run(5 * ms, report='text')
    myelinated_axon.i_appl[2] = 0 * amp
    run(100 * ms, report='text')

    fig, ax = subplots(figsize=(15, 8.1), layout='tight')

    ax.plot(M.t / ms, M.v[3] / mV, label='Internode 2', color='magenta')
    ax.plot(M.t / ms, M.v[2] / mV, label='Node 2', color='blue')
    ax.plot(M.t / ms, M.v[1] / mV, label='Internode 1', color='orange')
    ax.plot(M.t / ms, M.v[0] / mV, label='Node 1', color='black')
    ax.hlines(na_potential / mV, M.t[0] / ms, M.t[-1] / ms, label='Sodium Reversal Potential', color='green')
    ax.hlines(k_potential / mV, M.t[0] / ms, M.t[-1] / ms, label='Potassium/Leak Reversal Potential', color='red')
    ax.grid()
    fig.legend(loc='center right')

    ax.set_title('Action Potential')
    ax.set_xlabel('Time (ms)')
    ax.set_ylabel('V (mV)')
    plt.show()
    return 0
