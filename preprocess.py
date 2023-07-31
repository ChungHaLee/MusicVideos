import pandas as pd



def melondata():
    meloncsv = pd.read_csv('./melon1.csv')
    # for i in range(len(meloncsv)):


        # FIRST TAG OF THE MUSIC
        # genretag = meloncsv['genre'][i].split(',')[0]

    ballad = meloncsv.genre == '발라드'
    balladcsv = meloncsv[ballad][['artist', 'title']]

    dance = meloncsv.genre == '댄스'
    dancecsv = meloncsv[dance][['artist', 'title']]


    raphiphop = meloncsv.genre == '랩/힙합'
    raphiphopcsv = meloncsv[raphiphop][['artist', 'title']]


    balladcsv.to_csv('ballad.csv')

    dancecsv.to_csv('dance.csv')

    raphiphopcsv.to_csv('raphiphop.csv')





melondata()

