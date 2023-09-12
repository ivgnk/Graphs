'''
https://networkx.org/documentation/stable/tutorial.html
https://networkx.org/documentation/stable/tutorial.html#drawing-graphs
'''

import matplotlib.pyplot as plt
import networkx as nx
import pprint

G = nx.petersen_graph()
subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
subax2 = plt.subplot(122)
nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')

plt.show()