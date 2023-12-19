import networkx as nx
import matplotlib.pyplot as plt

# Créer le graphique vide
G = nx.Graph()

# Ajouter les nœuds de 0 à 41 et les relier pour former un cercle
num_nodes_circle = 42
for i in range(num_nodes_circle):
    G.add_node(i)
    G.add_edge(i, (i + 1) % num_nodes_circle)

# Ajouter les nœuds 42 à 45 et les relier entre eux
nodes_between_0_and_72 = [42, 43, 44, 45, 46]
for i in range(len(nodes_between_0_and_72) - 1):
    G.add_edge(nodes_between_0_and_72[i], nodes_between_0_and_72[i + 1])

# Connecter le nœud 0 à 42 et le nœud 45 à 72
central_node = 72
G.add_edge(0, nodes_between_0_and_72[0])
G.add_edge(nodes_between_0_and_72[-1], central_node)

# Ajoute les noeuds 47 à 51 et les relier entre eux
nodes_between_72_21 = [47, 48, 49, 50, 51]
for i in range(len(nodes_between_72_21)- 1):
    G.add_edge(nodes_between_72_21[i], nodes_between_72_21[i +1])

# Connecte le noeud 47 à 72 et le noeud 51 à 21
G.add_edge(central_node, nodes_between_72_21[0])
G.add_edge(nodes_between_72_21[-1], 21)

# Ajoute les noeuds 52 à 56 et les relier entre eux
nodes_between_7_72 = [52, 53, 54, 55, 56]
for i in range(len(nodes_between_7_72)-1):
    G.add_edge(nodes_between_7_72[i], nodes_between_7_72[i +1])

# Connecte le noeud 52 à 7 et 56 à 72
G.add_edge(7,nodes_between_7_72[0])
G.add_edge(nodes_between_7_72[-1], central_node)

# Ajoute les noeuds 57 à 61 et les relier entre eux
nodes_between_72_28 = [57, 58, 59, 60, 61]
for i in range(len(nodes_between_72_28)-1):
    G.add_edge(nodes_between_72_28[i], nodes_between_72_28[i +1])
    
# Connecte le noeud 57 à 72 et le noeud 61 à 28
G.add_edge(central_node, nodes_between_72_28[0])
G.add_edge(nodes_between_72_28[-1], 28)

# Ajoute les noeuds 62 à 66 et les relier entre eux
nodes_between_72_14 = [62, 63, 64, 65, 66]
for i in range(len(nodes_between_72_14)-1):
    G.add_edge(nodes_between_72_14[i], nodes_between_72_14[i +1])

# Connecte le noeud 62 à 35 et 66 à 72
G.add_edge(14 ,nodes_between_72_14[0])
G.add_edge(nodes_between_72_14[-1], central_node)

# Ajoute les noeuds 67 à 71 et les relier entre eux
nodes_between_72_35 = [67, 68, 69, 70, 71]
for i in range(len(nodes_between_72_35)-1):
    G.add_edge(nodes_between_72_35[i], nodes_between_72_35[i +1])

# Connecte le noeud 67 à 72 et le noeud 71 à 14
G.add_edge(central_node, nodes_between_72_35[0])
G.add_edge(nodes_between_72_35[-1], 35)

# Dessiner le cercle avec le nœud central positionné au centre

# nx.draw_spectral(G, with_labels=True, node_size=200)
# plt.show()
