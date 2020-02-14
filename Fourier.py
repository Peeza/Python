import numpy as np                                                                                
import matplotlib.pyplot as plt
from math import pi
from pylab import scatter,xlabel,ylabel,xlim,ylim,show
import statistics

#Variables
N = 2000   
f1 = 40
f2 = 80
fs = 4000


#Question 1

# time
t = np.linspace(0.0,0.5,N)  

#time-domain function for amplitude
a1 = (np.sin(f1*(2*pi)*t)) + (0.5 * np.sin(f2*(2*pi)*t)) 

#plotting time vs. amplitude
plt.plot(t,a1)  
xlabel("Time [s]")
ylabel("Amplitude")
plt.show()                                                                                         #showing part 1 plot on screen


#Question 2

a_2 = np.fft.rfft(a1)

#fast fourier transform function for amplitude
a2 = np.abs(a_2) * 1/N  
T = 1/4000

#frequency
f = np.linspace(0, N, len(a2)) 

#plotting frequency vs. amplitude
plt.bar(f, a2) 
xlim(0,100)
ylim(0,1.0)
xlabel("Frequency [Hz]")
ylabel("Amplitude")
plt.show() #plot 2


#Question 3

print("Lengths: time =", len(t), " time-domain function =", len(a1), " FFT =", len(a2))
print("Sample rate =", T, " Frequency =", 1/T)
print("Lengths: f =", N, " abs(f) =", len(a2))
print("Lengths: f(N/2) =", N/2, " abs(fft(N/2)) =", N/2, "\n\n")

#filtering f = 40 Hz out of bar graph
for i in range(0,26): 
    print(i)
    if (a2[i] > 0.3):
        a_2[i] = ((a_2[i-1] + a_2[i+1])/2)
    print(f[i], a_2[i], a2[i])

a3 = np.abs(a_2)*1/N

#plotting filtered frequency vs. amplitude
plt.bar(f, a3) 
xlim(0,100)
ylim(0,1.0)
xlabel("Frequency [Hz]")
ylabel("Amplitude")
plt.show()  #plot 3


#Question 4

#filtered time variable
t2 = np.linspace(0,0.5,1001)
#amplitude of inverse fast fourier transform
a4 = np.fft.ifft(a_2) 

#Plot
plt.plot(t2,a4)               
xlabel("Time [s]")
ylabel("Amplitude (after FFt filtering)")
xlim(0,0.5)
ylim(-0.5,0.5)
plt.show()



