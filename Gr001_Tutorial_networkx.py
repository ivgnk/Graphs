'''
https://networkx.org/documentation/stable/tutorial.html
https://networkx.org/documentation/stable/tutorial.html#drawing-graphs
'''

import matplotlib.pyplot as plt
import networkx as nx
import pprint

def thetest_nodes_and_edges():
    '''
    https://networkx.org/documentation/stable/tutorial.html#creating-a-graph
    https://networkx.org/documentation/stable/tutorial.html#nodes
    https://networkx.org/documentation/stable/tutorial.html#edges
    '''
    G = nx.Graph()  # Create an empty graph with no nodes and no edges
    G.add_node(1)   # add one node
    G.add_node(2)   # add one node
    G.add_nodes_from([3, 4])
    G.add_nodes_from([
        (5, {"color": "red"}),
        (6, {"color": "green"}),
    ])
    G.add_nodes_from([7, 8])
    # H = nx.path_graph(10)
    # G.add_nodes_from(H)
    G.add_edge(1, 2)
    G.add_edges_from([(1, 4), (1, 3)])
    e = (4, 5)
    # e = [4, 5]
    G.add_edge(*e)
    G.add_edges_from([(5, 6)])
    G.add_node("spam")
    G.add_nodes_from("spam")
    G.add_edge(3, 'm')
    print(f'{G.number_of_nodes()=}')
    print(f'{G.number_of_edges()=}')

    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()

def thetest_edge_order():
    DG = nx.DiGraph()
    DG.add_edge(2, 1)  # adds the nodes in order 2, 1
    DG.add_edge(1, 3)
    DG.add_edge(2, 4)
    DG.add_edge(1, 2)
    assert list(DG.successors(2)) != [1, 4], 'ошибка 1'
    assert list(DG.edges) == [(2, 1), (2, 4), (1, 3), (1, 2)], 'ошибка 2'

def thetest_petersen_graph():
    G = nx.petersen_graph()
    subax1 = plt.subplot(121)
    nx.draw(G, with_labels=True, font_weight='bold')
    subax2 = plt.subplot(122)
    nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
    plt.show()

if __name__ == "__main__":
    # thetest_petersen_graph()
    # thetest_nodes_and_edges()
    thetest_edge_order()