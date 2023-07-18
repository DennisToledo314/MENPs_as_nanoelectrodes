import matplotlib.pyplot as plt
from brian2 import *
import pickle

def graph_strength_duration (stren_dur_file):
    upperlimits = []
    lowerlimits = []
    data_to_be_graphed = pickle.load(open(stren_dur_file, "rb"))
    data_list = sorted(data_to_be_graphed.items())
    pulse_width, i_elect = zip(*data_list)
    i_elect, i_elect_ideal = zip(*i_elect)
    i_elect = -1 * np.asarray(i_elect)
    i_elect_ideal = -1 * np.asarray(i_elect_ideal)
    print(i_elect)
    print(i_elect_ideal)
    for i in np.arange(0, len(data_to_be_graphed), 1):
        if i_elect_ideal[i] > i_elect[i]:
            upperlimits.append(True)
            lowerlimits.append(False)
        else:
            upperlimits.append(False)
            lowerlimits.append(True)
    plt.errorbar(pulse_width, i_elect, yerr=abs(i_elect_ideal-i_elect), uplims=upperlimits, lolims=lowerlimits)
    plt.xlabel('Pulse Width (ms)')
    plt.ylabel('Magnitude of Threshold Current (mA)')
    plt.title('Strength vs. Duration')
    plt.grid()
    plt.show()

def graph_distance_numparts (dist_numparts_file):
    upperlimits = []
    lowerlimits = []
    data_to_be_graphed = pickle.load(open(dist_numparts_file, "rb"))
    data_list = sorted(data_to_be_graphed.items())
    m_dist, menps = zip(*data_list)
    menps, menps_ideal = zip(*menps)
    menps = np.asarray(menps)
    menps_ideal = np.asarray(menps_ideal)
    print(menps)
    print(menps_ideal)
    for i in np.arange(0, len(data_to_be_graphed), 1):
        if menps_ideal[i] > menps[i]:
            upperlimits.append(False)
            lowerlimits.append(True)
        else:
            upperlimits.append(True)
            lowerlimits.append(False)

    plt.figure(layout='tight')
    plt.errorbar(m_dist, menps/1e5, yerr=abs((menps_ideal/1e5)-(menps/1e5)), uplims=upperlimits, lolims=lowerlimits)
    plt.xlabel('Distance From Node to Point O (nm)')
    plt.ylabel('MENPs Required for Threshold (in hundreds of thousands)')
    plt.title('MENPs vs. Distance')
    plt.grid()
    plt.show()

def graph_layers (layers_file):
    data_to_be_graphed = pickle.load(open(layers_file, "rb"))
    data_list = sorted(data_to_be_graphed.items())
    number_of_layers, delta_vm = zip(*data_list)
    plt.plot(number_of_layers, delta_vm)
    plt.xlabel('Number of Layers (3500 MENPs per Layer)')
    plt.ylabel('Change in Membrane Voltage (mV)')
    plt.title('Membrane Voltage Change')
    plt.grid()
    plt.show()
