import os
import moviepy.editor as mp
import pandas as pd



mv_list = ['aespa_spicy']


def readtime(timepath):
    f = open(timepath, 'r')
    data = f.read().splitlines()
    return data
        


        
# aespa_spicy/0.mp4
def mvinput(mvpath, timepath):
    data = readtime(timepath)
    for i in range(len(data)):
        start = float(data[i].split('\t')[0])
        end = float(data[i].split('\t')[1])

        title = mvpath.split('/')[1].split('.')[0]
        clip = mp.VideoFileClip(mvpath).subclip(start, end)
        clip.audio.write_audiofile("wav_result/%s/%s_%s.wav"%(title, title, i))


def main():
    for i in range(len(mv_list)):
        title = mv_list[i]
        readtime('timestamp/result_%s_sec.txt'%(title))
        mvinput('mvs/%s.mp4'%(title), 'timestamp/result_%s_sec.txt'%(title))




main()