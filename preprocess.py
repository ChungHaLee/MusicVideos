# import pandas as pd
#
#
# melon = pd.read_csv('./melon4.csv')
# print(melon[melon['artist'].str.contains('&')])
# print('--------------------------------------------------------------------------------')
# print(melon[melon['title'].str.contains('&')])
# print('--------------------------------------------------------------------------------')
# print(melon[melon['title'].str.contains('?')])
# print('--------------------------------------------------------------------------------')
# print(melon[melon['title'].str.contains('!')])
# print('--------------------------------------------------------------------------------')
# print(melon[melon['title'].str.contains('#')])


# def melondata(filename):
#     meloncsv = pd.read_csv('./%s'%filename)
#     for i in range(len(meloncsv)):
#         # if meloncsv.genre[i].split(',')[0] == '발라드':
#         #     meloncsv.genre[i] = '발라드'
#
#         if (meloncsv.genre[i].split(',')[0] == '인디음악') or (meloncsv.genre[i].split(',')[0] == '국내드라마'):
#             if meloncsv.genre[i].split(',')[1]  == '댄스':
#                 meloncsv.genre[i] = '댄스'
#             elif meloncsv.genre[i].split(',')[1] == '랩/힙합':
#                 meloncsv.genre[i] = '랩/힙합'
#             elif meloncsv.genre[i].split(',')[1] == 'R&B/Soul':
#                 meloncsv.genre[i] = 'R&B/Soul'
#             elif meloncsv.genre[i].split(',')[1] == '록/메탈':
#                 meloncsv.genre[i] = '록/메탈'
#             elif meloncsv.genre[i].split(',')[1] == '포크/블루스':
#                 meloncsv.genre[i] = '포크/블루스'
#         else:
#             if meloncsv.genre[i].split(',')[0] == '댄스':
#                 meloncsv.genre[i] = '댄스'
#             elif meloncsv.genre[i].split(',')[0] == '랩/힙합':
#                 meloncsv.genre[i] = '랩/힙합'
#             elif meloncsv.genre[i].split(',')[0] == 'R&B/Soul':
#                 meloncsv.genre[i] = 'R&B/Soul'
#             elif meloncsv.genre[i].split(',')[0] == '록/메탈':
#                 meloncsv.genre[i] = '록/메탈'
#             elif meloncsv.genre[i].split(',')[0] == '포크/블루스':
#                 meloncsv.genre[i] = '포크/블루스'
#
#     meloncsv.to_csv('%s_final.'%filename)
#     #
#     #
#     # rhythmblues = meloncsv.genre == 'R&B/Soul'
#     # rhythmbluescsv = meloncsv[rhythmblues][['artist', 'title']]
#     #
#     #
#     #
#     # balladcsv.to_csv('ballad.csv')
#     #
#     # dancecsv.to_csv('dance.csv')
#     #
#     # raphiphopcsv.to_csv('raphiphop.csv')
#
#
#
#
#
# melondata('melon1.csv')
# melondata('melon2.csv')
# # melondata('melon3.csv')
# # melondata('melon4.csv')
