import numpy as np
import matplotlib.pyplot as plt


# Varoab;es
gri_a_m = ['+', '+', '-', '-', '+', '-', '+', '-', 'dummy', '+']
gri_a_s = ['+', '+', '+', '+', '+', '-', '-', '+']
gri_b_m = ['+', '-', '-', '+', '+', '+', '+', '+', 'dummy', '-']
gri_b_s = ['+', '-', '+', '-', '+', '+', '-', '-'] 

pci = [[gri_a_m, gri_a_s], [gri_b_m, gri_b_s]]

id_list = [7430, 8390, 9930]


def gen_master_window(phase_code=['+', '+', '+', '+', '+', '+', '+', '+', '+', '+']):
    
    freq = 100e3
    tau = 0
    phase = 1
    master_window = np.array([])
    master_window_e = np.array([])
    timespace = np.array([])

    for i, pc in zip(range(0, 10), phase_code):
        
        t = np.linspace(tau, tau+1000, 10001)
        
        if pc == '+':
            phase = 1
            
        else:
            phase = -1
        
        
        if i == 8:
            normalized_e = np.zeros(shape=(10001, ))
            s = np.zeros(shape=(10001, ))
        
        else:
            envelope = (t-tau)**2*np.exp(-2*(t-tau)/65)
            normalized_e = phase * (envelope - np.min(envelope))/(np.max(envelope)-np.min(envelope))
            s = normalized_e *np.sin(2*np.pi*freq*t*1e-6)
        
        timespace = np.append(timespace[:-1], t)
        master_window = np.append(master_window[:-1], s)
        master_window_e = np.append(master_window_e[:-1], normalized_e)
        
        print("tau :", tau)
        print("length of time space :", len(timespace), timespace[-1], timespace[-2])
        print("length of master_window :", len(master_window))
        print("length of master_window_e :", len(master_window_e))
        
        tau += 1000
        
    return timespace, master_window, master_window_e
        

def gen_slave_window(phase_code=['+', '+', '+', '+', '+', '+', '+', '+']):
    
    freq = 100e3
    tau = 0
    phase = 1
    slave_window = np.array([])
    slave_window_e = np.array([])
    timespace = np.array([])

    for i, pc in zip(range(0, 8), phase_code):
        
        t = np.linspace(tau, tau+1000, 10001)
        
        if pc == '+':
            phase = 1
            
        else:
            phase = -1
 
        envelope = (t-tau)**2*np.exp(-2*(t-tau)/65)
        normalized_e = phase * (envelope - np.min(envelope))/(np.max(envelope)-np.min(envelope))
        s = normalized_e *np.sin(2*np.pi*freq*t*1e-6)
        
        timespace = np.append(timespace[:-1], t)
        slave_window = np.append(slave_window[:-1], s)
        slave_window_e = np.append(slave_window_e[:-1], normalized_e)
        
        #print("tau :", tau)
        #print("length of time space :", len(timespace))
        #print("length of slave_window :", len(slave_window))
        #print("length of slave_window_e :", len(slave_window_e))
        
        tau += 1000
        
    return timespace, slave_window, slave_window_e


def merge_signal_by_id(id=0, amp_ratio=0):
    
    if id==7430:
        id_chain = '7430 China North Sea chain'
        sending_station = ['master_Rongcheng', 'slave_Xuancheng', 'slave_Helong']
        emission_delays = [10000, 13459.7, 30852.32]
        
        if amp_ratio == 0:
            amp_ratio = [0.7, 0.3, 0.2]
    
    elif id==8390:
        id_chain = '8390 China East Sea chain'
        sending_station = ['master_Xuancheng', 'slave_Raoping', 'slave_Rongcheng']
        emission_delays = [10000, 13795.52, 31459.70]
        
        if amp_ratio == 0:
            amp_ratio = [0.7, 0.3, 0.2]
    
    elif id==9930:
        id_chain = '9930 East Asia chain'
        sending_station = ['master_Pohang', 'slave_Kwangju', 'slave_Ussuriisk', 'slave_Incheon']
        emission_delays = [10000, 11946.97, 54162.44, 81352]
        
        if amp_ratio == 0:
            amp_ratio = [0.7, 0.2, 0.15, 0.3]
    
    else:
        print("id error occured")
        return
    
    # variables
    start_time = 0
    standard_time = 0
    timespace = np.array([])
    signal = np.array([])
    signal_e = np.array([])
    
    #print("timspace_s size : ", len(timespace_s))
    #print("slave_window size : ", len(slave_window))
    #print("salve_window_e size : ", len(slave_window_e))
    
    for gri_m, gri_s in pci:
        
        # Generate Reference signal
        timespace_m, master_window, master_window_e = gen_master_window(gri_m)
        timespace_s, slave_window, slave_window_e = gen_slave_window(gri_s)
        
        for station, ed, amp in zip(sending_station, emission_delays, amp_ratio):
            
            # status check
            status, site = station.split('_')
            print("status, site :", status, site)
            
            if status=='master':
                #print("master process")
                
                timespace_m += standard_time
                
                amp_master_window = amp * master_window
                amp_master_window_e = amp * master_window_e
                
                timespace = np.append(timespace, timespace_m)
                signal = np.append(signal, amp_master_window)
                signal_e = np.append(signal_e, amp_master_window_e)
                
                start_time = ed
                print("length of timespace :", len(timespace), "|| length of signal :", len(signal), "|| length of signal_e :", len(signal_e))
                print("master process over; next_start_time :", start_time)
                print()
            
            elif status=='slave':
                
                end_time = standard_time + ed
                print("slave process; end time :", end_time)
                
                time_interval = end_time-start_time
                
                temp = np.linspace(start_time, end_time, int(10*(time_interval))+1)
                temp_signal = np.zeros(shape=(int(10*time_interval)+1, ))
                print("shape of temp :", temp.shape, "shape of temp_signal :", temp_signal.shape)
                
                timespace = np.append(timespace, temp[1:])
                signal = np.append(signal, temp_signal[1:])
                signal_e = np.append(signal_e, temp_signal[1:])
                
                print("length of timespace :", len(timespace), "|| length of signal :", len(signal), "|| length of signal_e :", len(signal_e))
                
                start_time = end_time
                print(start_time)            
                temp = start_time + timespace_s
                
                amp_slave_window = amp * slave_window
                amp_slave_window_e = amp * slave_window_e
                
                timespace = np.append(timespace, temp)
                signal = np.append(signal, amp_slave_window)
                signal_e = np.append(signal_e, amp_slave_window_e)
                
                start_time = timespace[-1]
                print("length of timespace :", len(timespace), "|| length of signal :", len(signal), "|| length of signal_e :", len(signal_e))
                print("slave process over; start_time :", start_time)
                print()
        
        end_time = standard_time + id*10
        time_interval = end_time - start_time
        temp = np.linspace(start_time, end_time, int(10*time_interval+1))
        temp_signal = np.zeros(shape=(int(10*time_interval+1), ))
        
        timespace = np.append(timespace, temp[1:])
        signal = np.append(signal, temp_signal[1:])
        signal_e = np.append(signal_e, temp_signal[1:])
        
        standard_time = end_time + 1
        
    return timespace, signal, signal_e, id_chain




"""
fig, axes = plt.subplots(3, 1, figsize=(23, 20))

plt.suptitle("Reference Signal of Loran Chain\nWith Phase Code", fontsize=23, weight='bold', ha='center', va='bottom')

axes_num = 0


for id_ in id_list:
    temp_time, temp_signal, temp_signal_e, id_chain = merge_signal_by_id(id_)
    
    # Line plot : signal data, enveloped signal
    axes[axes_num].plot(temp_time, temp_signal, 'k', label='Loran-c signal')
    axes[axes_num].plot(temp_time, temp_signal_e, 'orangered', label='Enveloped signal')
    
    # Line for checking end-point
    axes[axes_num].vlines(id_*10*2, -1, 1, color='green', linestyles='--')
    
    # Text for checking end-point
    axes[axes_num].text(id_*10*2+1000, -0.2, 'end\nof\nsignal\nwindow\n\n'+str(id_)+'chain', color='green', weight='bold')
    
    # Plot settings : xlim, xlabel, ylabel, legend
    axes[axes_num].set_xlim(-4000, 210000)
    axes[axes_num].set_title('Reference signal : '+ id_chain, fontsize=17)
    axes[axes_num].set_xlabel('time(μs)', fontsize=13)
    axes[axes_num].set_ylabel('Normalized Amplitude', fontsize=13)
    axes[axes_num].legend(loc='upper right')
    
    axes_num += 1

plt.subplots_adjust(hspace=0.3)

plt.show()
"""