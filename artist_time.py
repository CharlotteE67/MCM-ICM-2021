import numpy as np
import pandas as pd

music = pd.read_csv("full_music_data.csv")

print(min(music['year']))
print(max(music['year']))
artist_id = dict()
for i in range(len(music)):
    raw = music['artists_id'][i]
    result = raw.split('[')[1].split(']')[0]
    ids = result.split(', ')
    for j in range(len(ids)):
        if int(ids[j]) not in artist_id:
            artist_id[ids[j]] = []
            for k in range(10):
                artist_id[ids[j]].append(0)
        artist_id[ids[j]][int((int(music['year'][i]) - 1920 - 1) / 10)] += 1
# for i in artist_id.keys():
#     print(sum(artist_id[i]))