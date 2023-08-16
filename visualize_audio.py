import numpy as np
import IPython.display
import librosa.display

import scipy.io.wavfile as wav
from matplotlib import cm
import matplotlib.pyplot as plt
from python_speech_features import mfcc
import librosa

plt.rcParams['figure.figsize'] = (18,5)


# mfcc
# y, sr = librosa.load("mp3_result/justinbieber_peaches/justinbieber_peaches_25.mp3")
# mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=12)
# print(mfccs.shape)
# librosa.display.specshow(mfccs, x_axis='time', y_axis='mel')
# plt.colorbar()
# plt.tight_layout()
# plt.title('mfcc')
# plt.show()






# zcr

# x, fs = librosa.load("wav_result/aespa_spicy/aespa_spicy_0.wav")

# # librosa.display.waveshow(x, sr=fs)
# # zero_crossings = librosa.zero_crossings(x, pad=False)
# zcrs = librosa.feature.zero_crossing_rate(x)

# # print('zcrs.shape', zcrs.shape)
# plt.plot(zcrs[0])
# plt.show()
# # print('sum of zero crossing', sum(zero_crossings))



# rms energy

# y, sr = librosa.load('mp3_result/monstax_lovekilla/monstax_lovekilla_80.mp3')
# rms = librosa.feature.rms(y=y)
# times = librosa.times_like(rms)
# plt.plot(times, rms[0])
# plt.show()



# spectral centroid
# y, sr = librosa.load('wav_result/aespa_spicy/aespa_spicy_95.wav')
# cent = librosa.feature.spectral_centroid(y=y, sr=sr)
# spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
# flatness = librosa.feature.spectral_flatness(y=y)

# times = librosa.times_like(cent)
# librosa.display.specshow(librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max), y_axis='linear', x_axis='time')
# plt.plot(times, cent.T, label='Spectral centroid', color='w')
# plt.legend()
# plt.show()



# spectral bandwidth
# y, sr = librosa.load('wav_result/aespa_spicy/aespa_spicy_.wav')
# S, phase = librosa.magphase(librosa.stft(y=y))
# spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
# times = librosa.times_like(spec_bw)
# centroid = librosa.feature.spectral_centroid(S=S)

# fig, ax = plt.subplots(nrows=2, sharex=True)

# ax[1].fill_between(times, np.maximum(0, centroid[0] - spec_bw[0]),
#                 np.minimum(centroid[0] + spec_bw[0], sr/2),
#                 alpha=0.5, label='Centroid +- bandwidth')
# ax[1].plot(times, centroid[0], label='Spectral centroid', color='w')
# ax[1].legend(loc='lower right')
# plt.show()



# spectral flatness
# y, sr = librosa.load('wav_result/aespa_spicy/aespa_spicy_0.wav')
# flatness = librosa.feature.spectral_flatness(y=y)
# # print(flatness)
# plt.plot(flatness[0])
# plt.show()



# chroma_stft

# y, sr = librosa.load('mp3_result/silksonic_leavethedooropen/silksonic_leavethedooropen_68.mp3')
# hop_length = 512
# chromagram = librosa.feature.chroma_stft(y, sr=sr, hop_length=hop_length)
# print(chromagram)
# plt.figure(figsize=(15, 5))
# librosa.display.specshow(chromagram, x_axis='time', y_axis='chroma', hop_length=hop_length, cmap='coolwarm')
# plt.show()



# tonnetz
# y, sr = librosa.load('mp3_result/silksonic_leavethedooropen/silksonic_leavethedooropen_68.mp3')
# tonnetz = librosa.feature.tonnetz(y=y, sr=sr)
# fig, ax = plt.subplots(nrows=2, sharex=True)
# img1 = librosa.display.specshow(tonnetz,
#                                 y_axis='tonnetz', x_axis='time', ax=ax[0])
# ax[0].set(title='Tonal Centroids (Tonnetz)')
# ax[0].label_outer()
# # img2 = librosa.display.specshow(librosa.feature.chroma_stft(y=y, sr=sr),
# #                                 y_axis='chroma', x_axis='time', ax=ax[1])
# # # ax[1].set(title='Chroma')
# fig.colorbar(img1, ax=[ax[0]])
# # fig.colorbar(img2, ax=[ax[1]])
# plt.show()



# tempo
x, sr = librosa.load('wav_result/aespa_spicy/aespa_spicy_0.wav')
tempo = librosa.beat.tempo(x, sr=sr)
print(tempo)


# # tempogram
# x, sr = librosa.load('wav_result/aespa_spicy/aespa_spicy_0.wav')
# hop_length = 200 # samples per frame
# onset_env = librosa.onset.onset_strength(x, sr=sr, hop_length=hop_length, n_fft=2048)
# frames = range(len(onset_env))
# t = librosa.frames_to_time(frames, sr=sr, hop_length=hop_length)
# S = librosa.stft(onset_env, hop_length=1, n_fft=512)
# fourier_tempogram = np.absolute(S)
# n0 = 0
# n1 = 100
# tmp = np.log1p(onset_env[n0:n1])
# r = librosa.autocorrelate(tmp)
# tempogram = librosa.feature.tempogram(onset_envelope=onset_env, sr=sr, hop_length=hop_length, win_length=400)
# librosa.display.specshow(tempogram, sr=sr, hop_length=hop_length, x_axis='time', y_axis='tempo')

# plt.show()