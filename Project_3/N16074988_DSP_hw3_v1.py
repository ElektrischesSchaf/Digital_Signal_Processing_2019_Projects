import wave
import numpy as np
from scipy import signal
from scipy.signal import lfilter, butter
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavf

# Read the imput and output wav files
signal_wave = wave.open('singing16k16bit-clean.wav', 'r')
signal_wave_2=wave.open('singingWithPhoneRing16k16bit-noisy.wav', 'r')
filtered_singing=wave.open('filtered_singing.wav', 'w')

# assign sample frequency explicitly
sample_frequency = 16000

# check attributes of the source wav file
print('input channels= ' , signal_wave.getnchannels(), '\n' )
print('input width= ',signal_wave.getsampwidth(), '\n')
print('input getnframes= ', signal_wave.getnframes(),'\n')
print('input frame rate= ', signal_wave.getframerate(), '\n')

# transfer wav file to numpy array
data = np.fromstring(signal_wave.readframes(sample_frequency), dtype=np.int16)
data_2=np.fromstring(signal_wave_2.readframes(sample_frequency), dtype=np.int16)
sig = signal_wave.readframes(-1)
sig2=signal_wave_2.readframes(-1)
sig = np.fromstring(sig, 'Int16')
sig2=np.fromstring(sig2,'Int16')
sig = sig[:]
sig2 = sig2[:]

print('\nlen of sig: ', len(sig), ' len of sig2: ', len(sig2), '\n')
#sig = sig[25000:32000]
mutual_length=min(len(sig), len(sig2))
sig=sig[:mutual_length]
sig2=sig2[:mutual_length]

# Filtering with lfilter
'''
n = 15  # the larger n is, the smoother curve will be
b = [1.0 / n] * n
a = 1
sig3 = lfilter(b, a, sig2)
'''

# Band pass
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

# Band stop
def butter_bandstop_filter(data, lowcut, highcut, fs, order):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    i, u = butter(order, [low, high], btype='bandstop')
    y = lfilter(i, u, data)
    return y

# using band stop filter to eliminate the noise frequency band
sig3=butter_bandstop_filter(sig2, 5000, 6500, sample_frequency, order=5)
sig3=butter_bandstop_filter(sig3, 1000, 2000, sample_frequency, order=5)
sig3=sig3.astype(np.int16) # very important!!

# Testing
#sig3=butter_bandpass_filter(sig2, 0, 5000, sample_frequency, order=5)

# another way to export wav file
# wavf.write('filtered_singing-2.wav', sample_frequency, sig3) 

print('\nlen of sig3: ', len(sig3), '\n')

# Export the filtered audio file
filtered_singing.setnchannels(1)
filtered_singing.setsampwidth(2)
filtered_singing.setframerate(sample_frequency)
filtered_singing.setnframes( signal_wave_2.getnframes() )
filtered_singing.writeframes( sig3.tostring() )
filtered_singing.close()


my_plot_width=20
my_plot_height=15

# plot spectrogram for the signal

fig=plt.figure(1, figsize=(my_plot_width, my_plot_height))

c = plt.subplot(211)
Pxx, freqs, bins, im = c.specgram(sig, NFFT=1024, Fs=16000, noverlap=900)
c.set_title('Clean Signal', fontsize=15)
c.set_xlabel('Time (Seconds)')
c.set_ylabel('Frequency (Hz)')

c=plt.subplot(212)
Pxx, freqs, bins, im = c.specgram(sig2, NFFT=1024, Fs=16000, noverlap=900)
c.set_title('Noisy Signal', fontsize=15)
c.set_xlabel('Time (Seconds)')
c.set_ylabel('Frequency (Hz)')

'''
c=plt.subplot(313)
Pxx, freqs, bins, im = c.specgram(sig3, NFFT=1024, Fs=16000, noverlap=900)
c.set_title('Filtered Signal', fontsize=15)
c.set_xlabel('Time (Seconds)')
c.set_ylabel('Frequency (Hz)')
'''
fig.tight_layout()
#plt.show()
plt.savefig('Clean_audio_vs_noisy.png')


fig=plt.figure(1, figsize=(my_plot_width, my_plot_width*2) )

c = plt.subplot(211)
Pxx, freqs, bins, im = c.specgram(sig, NFFT=1024, Fs=16000, noverlap=900)
c.set_title('Clean Signal', fontsize=15)
c.set_xlabel('Time (Seconds)')
c.set_ylabel('Frequency (Hz)')

c=plt.subplot(212)
Pxx, freqs, bins, im = c.specgram(sig3, NFFT=1024, Fs=16000, noverlap=900)
c.set_title('Filtered Signal', fontsize=15)
c.set_xlabel('Time (Seconds)')
c.set_ylabel('Frequency (Hz)')

'''
c=plt.subplot(313)
Pxx, freqs, bins, im = c.specgram(sig3, NFFT=1024, Fs=16000, noverlap=900)
c.set_title('Filtered Signal', fontsize=15)
c.set_xlabel('Time (Seconds)')
c.set_ylabel('Frequency (Hz)')
'''
fig.tight_layout()
#plt.show()
plt.savefig('Clean_audio_vs_filtered.png')