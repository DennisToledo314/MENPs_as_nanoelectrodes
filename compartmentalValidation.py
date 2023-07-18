from brian2 import *

# internode dimensions
internode_diam = 2 * um
internode_length = 199 * um

# node dimensions
node_diam = 1.4 * um
node_length = 1 * um

# potentials
leak_potential = -90 * mV
rest_potential = -90 * mV
Na_potential = 50 * mV
K_potential = -90 * mV

# node electrical properties
g_Na_f = 3 * siemens / cm ** 2
g_Na_p = 0.01 * siemens / cm ** 2
g_K = 0.08 * siemens / cm ** 2
g_L_node = 0.007 * siemens / cm ** 2

# internode electrical properties
g_L_inter = 8e-5 * siemens / cm ** 2
inter_C = 1.6 * uF / cm ** 2

# membrane electrical properties
membrane_C = 2 * uF / cm ** 2
axial_rho = 70 * ohm * cm

eqs = '''
gNaf: siemens/meter**2
gNap: siemens/meter**2
gK : siemens/meter**2
gL : siemens/meter**2

Im = -1*(IK+INaf+INap+IL) : amp/meter**2
INaf = gNaf*(m**3)*h*(v-ENa) : amp/meter**2
INap = gNap*(mp**3)*(v-ENa) : amp/meter**2
IK = gK*s*(v-EK) : amp/meter**2
IL = gL*(v-EL) : amp/meter**2
Iappl : amp (point current)

dm/dt = (alpha_m * (1-m) - beta_m * m) : 1
dh/dt = (alpha_h * (1-h) - beta_h * h) : 1
dmp/dt = (alpha_mp * (1-mp) - beta_mp * mp) : 1
ds/dt = (alpha_s * (1-s) - beta_s * s) : 1

alpha_m = (1.85*(1/ms)*10.3*mV*3.82)/(mV*exprel(-1*(v+21.4*mV)/(10.3*mV))) : Hz
beta_m = (0.076*(1/ms)*9.16*mV*3.82)/(mV*exprel((v+25.7*mV)/(9.16*mV))) : Hz

alpha_h = (0.034*(1/ms)*11*mV*6.11)/(mV*exprel((v+112*mV)/(11*mV))) : Hz
beta_h = (2.3*6.11/ms)/(1+exp(-(v+28.8*mV)/(13.6*mV))) : Hz

alpha_mp = (0.03*(1/ms)*10.2*mV*3.82)/(mV*exprel(-1*(v+23*mV)/(10.2*mV))) : Hz
beta_mp = (0.00019*(1/ms)*10*mV*3.82)/(mV*exprel((v+38*mV)/(10*mV))) : Hz

alpha_s = (0.0138*(1/ms)*9.4*mV*1.12)/(mV*exprel(-1*(v+14*mV)/(9.4*mV))) : Hz
beta_s = (0.000138*(1/ms)*1*mV*1.12)/(mV*exprel((v+56*mV)/(1*mV))) : Hz
'''

const_potentials = {'EL': leak_potential,
                    'ER': rest_potential,
                    'ENa': Na_potential,
                    'EK': K_potential}

axon_morpho = Cylinder(diameter=node_diam, length=node_length)
axon_morpho2 = Cylinder(diameter=internode_diam, length=internode_length)


myelinated_axon = SpatialNeuron(morphology=axon_morpho, model=eqs, Cm=membrane_C, Ri=axial_rho,
                                method='exponential_euler', namespace=const_potentials)

myelinated_axon2 = SpatialNeuron(morphology=axon_morpho2, model=eqs, Cm=membrane_C, Ri=axial_rho,
                                method='exponential_euler', namespace=const_potentials)

myelinated_axon2.v = 'ER'

myelinated_axon2.main.gNaf = 0
myelinated_axon2.main.gNap = 0
myelinated_axon2.main.gK = 0
myelinated_axon2.main.gL = g_L_inter
myelinated_axon2.main.Cm = inter_C

myelinated_axon.v = 'ER'

myelinated_axon.main.gNaf = g_Na_f
myelinated_axon.main.gNap = g_Na_p
myelinated_axon.main.gK = g_K
myelinated_axon.main.gL = g_L_node

defaultclock.dt = 0.01*ms

M = StateMonitor(myelinated_axon, 'v', record=True)
P = StateMonitor(myelinated_axon2, 'v', record=True)

run(50*ms, report='text')
myelinated_axon.Iappl[0] = 2000*pA
myelinated_axon2.Iappl[0] = 2000*pA

run(5*ms)
myelinated_axon.Iappl[0] = 0*amp
myelinated_axon2.Iappl[0] = 0*amp
run(50*ms, report='text')
myelinated_axon.Iappl[0] = 2000*pA
myelinated_axon2.Iappl[0] = 2000*pA

run(5*ms)
myelinated_axon.Iappl[0] = 0*amp
myelinated_axon2.Iappl[0] = 0*amp
run(50*ms, report='text')
myelinated_axon.Iappl[0] = 2000*pA
myelinated_axon2.Iappl[0] = 2000*pA

run(5*ms, report='text')
myelinated_axon.Iappl[0] = 0*amp
myelinated_axon2.Iappl[0] = 0*amp
run(100*ms, report='text')

fig, ax = subplots(figsize=(7.5, 4.05), layout='tight')
ax.plot(M.t/ms, M.v[0]/mV, color='blue', label='Node Equations')
ax.plot(M.t/ms, P.v[0]/mV, color='orange', label='Internode Equations')
ax.grid()
fig.legend()

ax.set_title('Action Potential')
ax.set_xlabel('Time (ms)')
ax.set_ylabel('V (mV)')
plt.show()
