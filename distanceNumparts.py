from brian2 import *
from scipy import signal
import pprint
import pickle

def appl_menps_square(num_menps, relative_epsilon_shell, epsilon, coercivity, h_amp, pulse_width, menp_diam, core_diam,
                      rx, ry, remanence, saturation_m, ymod_shell, coupling1, coupling2, lambda111, piezod,
                      duty_cy, time_step, sigma_ext):

    appl_MENPs_square_values = {}

    n44 = (3*lambda111)/(saturation_m**2)
    alpha_consts = (0.67 * coupling1 * coupling2 * ymod_shell * piezod * n44)/(epsilon * (relative_epsilon_shell - 1))
    elect_mem_dist = sqrt((rx**2)+(ry**2))
    area = (pi/4) * ((menp_diam**2)-(core_diam**2))

    hmag = h_amp * signal.square(2 * pi * ((duty_cy * time_step) / pulse_width), duty_cy)

    delhmag_delt = hmag * 2 * pi * (duty_cy / pulse_width)

    magn = (2 / pi) * saturation_m * arctan((hmag / coercivity) * tan((pi / 2) * (remanence / saturation_m)))

    delmagn_delhmag = ((2 / pi) * saturation_m * tan((pi / 2) * (remanence / saturation_m)) * (1 / coercivity) *
                     1 / (1 + (((hmag * tan((pi / 2) * (remanence / saturation_m))) / coercivity) ** 2)))

    delmagn_delt = ((2 / pi) * saturation_m * tan((pi / 2) * (remanence / saturation_m)) * (1 / coercivity) *
                    delhmag_delt / (1 + (((hmag * tan((pi / 2) * (remanence / saturation_m))) / coercivity) ** 2)))

    magnetostriction = 0.33 * n44 * magn ** 2

    delmagnetostriction_delhmag = 0.67 * magn * delmagn_delhmag

    del2magn_deltdelhmag = (((-4 / pi) * saturation_m * ((tan((pi / 2) * (remanence / saturation_m))) ** 3) * (
                1 / (coercivity ** 3))
                          * hmag * delhmag_delt) / ((
                                     1 + (((hmag * tan((pi / 2) * (remanence / saturation_m))) / coercivity) ** 2))**2))

    delalpha_delt = alpha_consts * (delmagn_delt * delmagn_delhmag + magn * del2magn_deltdelhmag) * (1/delmagn_delhmag)

    alpha = absolute(alpha_consts * delmagnetostriction_delhmag)

    alpha_mixed = alpha * (10/(4*pi))

    polarizationI_MENPs = (area*num_menps*epsilon*relative_epsilon_shell*(delalpha_delt*hmag + alpha*delhmag_delt))

    applMembrane_voltage = polarizationI_MENPs / (4 * pi * elect_mem_dist * sigma_ext)

    appl_MENPs_square_values['MENPs Current'] = polarizationI_MENPs
    appl_MENPs_square_values['MENPs Voltage at Neuron'] = applMembrane_voltage
    appl_MENPs_square_values['MENPs Magnetization'] = magn
    appl_MENPs_square_values['MENPs Field'] = hmag
    appl_MENPs_square_values['MENPs Magnetostriction'] = magnetostriction
    appl_MENPs_square_values['MENPs Magnetostriction Change'] = delmagnetostriction_delhmag
    appl_MENPs_square_values['MENPs Alpha'] = alpha_mixed
    return appl_MENPs_square_values


def nonlinear_menps (myelinated_axon, g_node, sigma_ext, epsilon0):
    defaultclock.dt = 0.01 * ms

    pw = 25 * ms
    distance_vs_numparts_values = {}
    m_dist_initial = 20*nmeter

    voltage_monitor = StateMonitor(myelinated_axon, 'v', record=True)
    net = Network(myelinated_axon, voltage_monitor)
    net.store()
    menps = 1.45e4

    for j in range(0, 10):
        m_dist = m_dist_initial + j * 20 * nmeter
        delta_vm = 0
        n = 0
        while delta_vm <= 119.99:
            net.restore()
            net.run(2 * pw)
            vm_initial = -90
            menps = menps + n * 1e2

            v_jminus1_menps_values = appl_menps_square(num_menps=menps, relative_epsilon_shell=200,
                                                       epsilon=epsilon0*farad/meter, coercivity=25465*amp/meter,
                                                       h_amp=63662*amp/meter, pulse_width=pw, menp_diam=20*nmeter,
                                                       core_diam=15*nmeter, rx=m_dist, ry=500*nmeter,
                                                       remanence=520*amp/meter, saturation_m=1587*amp/meter,
                                                       ymod_shell=67*Gjoule/meter**3, coupling1=1, coupling2=1,
                                                       lambda111=120e-6, piezod=191*pcoulomb/(kilogram*meter/second**2),
                                                       duty_cy=0.5, time_step=defaultclock.dt, sigma_ext=sigma_ext)

            v_jminus1 = v_jminus1_menps_values['MENPs Voltage at Neuron']

            v_j_menps_values = appl_menps_square(num_menps=menps, relative_epsilon_shell=200,
                                                 epsilon=epsilon0*farad/meter, coercivity=25465*amp/meter,
                                                 h_amp=63662*amp/meter, pulse_width=pw, menp_diam=20*nmeter,
                                                 core_diam=15*nmeter, rx=m_dist, ry=0, remanence=520*amp/meter,
                                                 saturation_m=1587*amp/meter, ymod_shell=67*Gjoule/meter**3,
                                                 coupling1=1, coupling2=1, lambda111=120e-6,
                                                 piezod=191*pcoulomb/(kilogram*meter/second**2),
                                                 duty_cy=0.5, time_step=defaultclock.dt, sigma_ext=sigma_ext)

            v_j = v_j_menps_values['MENPs Voltage at Neuron']

            v_jplus1_menps_values = appl_menps_square(num_menps=menps, relative_epsilon_shell=200,
                                                      epsilon=epsilon0 * farad / meter, coercivity=25465 * amp / meter,
                                                      h_amp=63662 * amp / meter, pulse_width=pw, menp_diam=20 * nmeter,
                                                      core_diam=15 * nmeter, rx=m_dist, ry=500 * nmeter,
                                                      remanence=520 * amp / meter, saturation_m=1587 * amp / meter,
                                                      ymod_shell=67 * Gjoule / meter ** 3, coupling1=1, coupling2=1,
                                                      lambda111=120e-6,
                                                      piezod=191 * pcoulomb / (kilogram * meter / second ** 2),
                                                      duty_cy=0.5, time_step=defaultclock.dt, sigma_ext=sigma_ext)

            v_jplus1 = v_jplus1_menps_values['MENPs Voltage at Neuron']

            myelinated_axon[2].i_appl = g_node * (v_jminus1 - 2 * v_j + v_jplus1)

            net.run(2 * pw, report='text')
            myelinated_axon[2].i_appl = 0
            net.run(2 * pw)
            n += 1
            v_mont = voltage_monitor.v[2] / mV
            vm_peak = max(v_mont)
            delta_vm = vm_peak - vm_initial
            print(vm_peak)
            print(delta_vm)
            print(menps)

        error = (vm_peak - 30) / 30
        m_dist_save = m_dist / nmeter
        if error > 0:
            menps_ideal = menps - error * menps
        else:
            menps_ideal = menps + error * menps
        distance_vs_numparts_values[m_dist_save] = [menps, menps_ideal]

        pprint.pprint(distance_vs_numparts_values, width=1)
    with open('distance_numparts.pkl', 'wb') as fp:
        pickle.dump(distance_vs_numparts_values, fp)
        print('data saved to file')

