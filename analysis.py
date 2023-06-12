import os
import pandas as pd
import numpy as np
import librosa


mv_list = os.listdir('result')

feature_list = ['mfcc', 'chroma_stft', 'chroma_cqt', 'chroma_cens', 'melspectrogram', 'rms', 'spectral_centroid', 'spectral_bandwidth', 'spectral_flatness',
                 'spectral_rolloff', 'poly_features', 'tonnetz', 'zero_crossing_rate', 'tempogram', 'fourier_tempogram']



def analyze(title):
    data = os.listdir('result/%s'%(title))

    df = pd.DataFrame()
    
    
    for i in range(len(data)):
        y, sr = librosa.load('result/%s/%s_%d.mp3'%(title, title, i))

        # FEATURE EXTRACTION STARTS FROM HERE
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
        chroma_cqt = librosa.feature.chroma_cqt(y=y, sr=sr)
        chroma_cens = librosa.feature.chroma_cens(y=y, sr=sr)
        melspectrogram = librosa.feature.melspectrogram(y=y, sr=sr)
        rms = librosa.feature.rms(y=y)
        spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
        spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)
        spectral_flatness = librosa.feature.spectral_flatness(y=y)
        spectral_rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
        poly_features = librosa.feature.poly_features(y=y, sr=sr)
        tonnetz = librosa.feature.tonnetz(y=y, sr=sr)
        zero_crossing_rate = librosa.feature.zero_crossing_rate(y=y)

        tempogram = librosa.feature.tempogram(y=y, sr=sr)
        fourier_tempogram = librosa.feature.fourier_tempogram(y=y, sr=sr)

        df = df.append(pd.DataFrame([[mfcc, chroma_stft, chroma_cqt, chroma_cens, melspectrogram, 
                 rms, spectral_centroid, spectral_bandwidth, spectral_flatness,
                 spectral_rolloff, poly_features, tonnetz, zero_crossing_rate, tempogram, fourier_tempogram]]), 
                 ignore_index=True)
        
    df.columns = ['mfcc', 'chroma_stft', 'chroma_cqt', 'chroma_cens', 'melspectrogram',
                'rms', 'spectral_centroid', 'spectral_bandwidth', 'spectral_flatness',
                'spectral_rolloff', 'poly_features', 'tonnetz', 'zero_crossing_rate', 
                'tempogram', 'fourier_tempogram']
    
    df.to_excel('%s.xlsx'%(title))
    return df

        
        
        


def result():
    analyze(mv_list[13])

result()