import os
import extcolors
import pandas as pd




def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100
    v = mx*100
    return h, s, v



def colorpicker():
    file_path = './coverart'

    for filename in os.listdir(file_path):
        new_df = pd.DataFrame()
        if filename == '.DS_Store':
            pass
        else:
            print('title:', filename)
            palette = extcolors.extract_from_path('./coverart/%s'%filename)

            for i in range(len(palette[0])):
                rgb, count = palette[0][i]
                for _ in range(len(rgb)):
                    hsv = rgb_to_hsv(rgb[0], rgb[1], rgb[2])
                print('HSV:', hsv)
                hsv_series = pd.Series(hsv, name=i, index=['hue', 'saturation', 'value'])
                new_df = pd.concat([new_df, hsv_series], axis=1)
            excelname = filename.split('.')[0]
            new_df.to_excel('./colordata/%s.xlsx'%excelname)
        print('-------------------------------------------------------------------------------------')







                    


colorpicker()
