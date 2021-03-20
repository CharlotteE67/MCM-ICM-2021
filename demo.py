import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

influence = pd.read_csv("influence_data.csv")
target_genre = 'R&B;'
target_id = 31067

graph = dict()
for i in range(len(influence)):
    if influence['influencer_main_genre'][i] == target_genre and influence['follower_main_genre'][i] == target_genre:
        if influence['influencer_id'][i] not in graph.keys():
            graph[int(influence['influencer_id'][i])] = []
        graph[int(influence['influencer_id'][i])].append(influence['follower_name'][i])

if target_id not in graph.keys():
    print("Not Found!")
else:
    print(graph[target_id])