import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

#read data
influence = pd.read_csv("influence_data.csv")
# print(influence['influencer_id'])
artist = dict()
#construct graph
G = nx.DiGraph()
for i in range(len(influence)):
    artist[int(influence['influencer_id'][i])] = influence['influencer_name'][i]
    artist[int(influence['follower_id'][i])] = influence['follower_name'][i]
    G.add_node(int(influence['influencer_id'][i]), name=influence['influencer_name'][i],
               main_genre=influence['influencer_main_genre'][i], active_start=influence['influencer_active_start'][i])
    G.add_node(int(influence['follower_id'][i]), name=influence['follower_name'][i],
               main_genre=influence['follower_main_genre'][i], active_start=influence['follower_active_start'][i])
    G.add_edge(int(influence['influencer_id'][i]), int(influence['follower_id'][i]))

print(G.edges)

# G.add_node(1)
# G.add_edges_from([(1, 2), (1, 3)])
# G.add_node(1)
# G.add_edge(1, 2)
# G.add_node("spam")
# G.add_nodes_from("spam")
# nx.draw(G)
# plt.show()