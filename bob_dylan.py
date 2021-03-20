import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import pairwise_distances
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("new-artist-feature-5.csv")
# 每一行就是一个vecs里面的一个元素
artist_id = dict()
vecs = []
for i in range(len(df)):
    vec = []
    vec.append(df.at[i, "danceability-new"])
    vec.append(df.at[i, "energy-new"])
    vec.append(df.at[i, "valence-new"])
    vec.append(df.at[i, "tempo-new"])
    vec.append(df.at[i, "loudness-new"])
    vecs.append(vec)
    artist_id[df['artists_id'][i]] = i

# z-score 标准化，将数据放缩
std = StandardScaler()
vecs = std.fit_transform(vecs)
D = pairwise_distances(vecs, metric='euclidean')
# D[i][j]= D[j][i] 代表着第i行和第j行的欧拉距离
# D[i][i] 是第i行自己和自己之间的距离，为0或者一个很小的小数

influence = pd.read_csv("influence_data.csv")
target_name = 'Bob Dylan'

influ_id = []
for i in range(len(influence)):
    if influence['follower_name'][i] == target_name:
        print("name: ", influence['influencer_name'][i],
              "genre: ", influence['influencer_main_genre'][i],
              "active_start: ", influence['influencer_active_start'][i])
        influ_id.append(influence['influencer_id'][i])

similarities = []

for i in range(len(influ_id)):
    similarities.append([])
    for j in range(len(influ_id)):
        if j != i:
            similarities[i].append(D[artist_id[influ_id[i]]][artist_id[influ_id[j]]])
# sim_max = max(max(similarities))
# # sim_min = min(min(similarities))
# # bias = sim_max - sim_min
sim_max = 18.91153643501641
sim_min = 0.09032906116655692
bias = 18.82120737384985
for i in range(len(similarities)):
    for j in range(len(similarities[i])):
        similarities[i][j] = (similarities[i][j] - sim_min) / bias
for i in range(len(similarities)):
    print(similarities[i])
print(max(similarities))
print(min(similarities))