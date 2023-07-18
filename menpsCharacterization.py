import numpy as np
import magnetoelectricModels

# consts
epsilon0 = (8.85e-12) #* farad / meter

t = np.arange(0, 50.1e-3, 1e-4)
# duty_cy = 0.5
# freq = 100

# Sine Wave
# menps_nonlinear_sine = magnetoelectricModels.appl_menps_sine(num_menps=1, relative_epsilon_shell=200, epsilon=epsilon0,
#                                                              coercivity=25464, h_amp=7957.7, hdc=79577,
#                                                              menp_diam=20e-9, core_diam=15e-9, rx=2e-8, ry=0,
#                                                              remanence=520, saturation_m=1587, ymod_shell=67e9,
#                                                              coupling1=1, coupling2=1, lambda111=120e-6, piezod=191e-12,
#                                                              frequency=freq, time_step=t, sigma_ext=0.2)

# magnetoelectricModels.plot_nonlinear_model(t, h_menps=menps_nonlinear_sine['MENPs Field'],
#                                            m_menps=menps_nonlinear_sine['MENPs Magnetization'],
#                                            magnetostrict_menps=menps_nonlinear_sine['MENPs Magnetostriction'],
#                                            alpha_menps=menps_nonlinear_sine['MENPs Alpha'], duty_cy_freq=freq)


# menps_nonlinear_sq = magnetoelectricModels.appl_menps_square(num_menps=1, relative_epsilon_shell=200, epsilon=epsilon0,
#                                                              coercivity=25464, h_amp=63662, pulse_width=25e-3,
#                                                              menp_diam=20e-9, core_diam=15e-9, rx=2e-8, ry=0,
#                                                              remanence=520, saturation_m=1587, ymod_shell=67e9,
#                                                              coupling1=1, coupling2=1, lambda111=120e-6, piezod=191e-12,
#                                                              duty_cy=duty_cy, time_step=t, sigma_ext=0.2)
#
# magnetoelectricModels.plot_nonlinear_model_waveforms(t, duty_cy,
#                                                      polarization_curr_menps=menps_nonlinear_sq['MENPs Current'],
#                                                      appl_mem_voltage=menps_nonlinear_sq['MENPs Voltage at Neuron'])


# menps_lin_sq = magnetoelectricModels.appl_menps_linearSq(num_menps=1, relative_epsilon=1e4, permitivity=epsilon0,
#                                                          scaled_me_coeff=500, h_amp=800, pulse_width=25e-3,
#                                                          menp_diam=20e-9, rx=2e-8, ry=0, duty_cy=duty_cy, time_step=t,
#                                                          sigma_ext=0.2)
#
# magnetoelectricModels.plot_linear_model(t, duty_cy=duty_cy, polarization_curr_menps=menps_lin_sq['MENPs Current'],
#                                         appl_mem_voltage=menps_lin_sq['MENPs Voltage at Neuron'])

