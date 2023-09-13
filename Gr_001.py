'''
Matplotlib: визуализация графов на Python
https://qaa-engineer.ru/matplotlib-vizualizacziya-grafov-na-python/

NetworkX
https://networkx.github.io/

https://networkx.org/documentation/stable/
Объекты NetworkX
https://networkx.github.io/documentation/stable/reference/classes/index.html
'''

import matplotlib.pyplot as plt
import networkx as nx
import pprint

edges = [(1, 2), (2, 3), (3, 4), (4, 1), (2, 4)]  # 4 вершины, 5 ребер
# Эта функция создаст граф со связями между вершинами, указанными в списке ребер.
G = nx.from_edgelist(edges)
print(f'{G=}')
print(G)
pprint.pprint(dir(G))
pprint.pprint(G._node)
# pprint.pprint(G.edge_subgraph)
fig1 = plt.figure(1)
axes1 = fig1.subplots(1, 1)
nx.draw(G, node_size=300, node_color='blue')
G = nx.Graph() # Undirected graph
plt.show()

# fig2 = plt.figure(1)
# edges_with_weights = [(1, 2, 0.5), (2, 3, 0.8), (3, 4, 0.3), (4, 1, 0.2), (2, 4, 1.0)]
# G.add_weighted_edges_from(edges_with_weights)
#
# # nx.draw(G)
# nx.draw(G, node_size=500, node_color='red')
# plt.show()

if __name__ == "__main__":
    #thetest_ulp()
    pass
