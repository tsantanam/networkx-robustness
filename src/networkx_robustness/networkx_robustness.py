import networkx as nx
import random

def simulate_random_attack(G=None, attack_fraction=0.1, weight=None):
    """
    Simulate random attack on a network
    :param G: networkx graph
    :param attack_fraction: fraction of nodes to be attacked (default: 0.1)
    :param weight: weight of edges (default: None)
    :return: initial (float), frac (list), apl (list)
    """
    # copy the graph to avoid changing the original graph
    G = G.copy()
    # get the  number of nodes
    G_nodes = G.number_of_nodes()
    # get the largest connected component of G
    if G.is_directed():
        Gc = G.to_undirected().subgraph(sorted(nx.connected_components(G.to_undirected()), key=len, reverse=True)[0])
    else:
        Gc = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
    # get the number of nodes in the largest connected component
    Gc_nodes = Gc.number_of_nodes()
    # get the initial fraction of nodes in the largest connected component
    initial = Gc_nodes / G_nodes
    # initialize lists
    frac = []
    apl = []
    # simulate random attack
    for i in range(0, int(G_nodes * attack_fraction)):
        G.remove_node(random.choice(list(G.nodes())))
        # get the largest connected component of G
        if G.is_directed():
            Gc = G.to_undirected().subgraph(sorted(nx.connected_components(G.to_undirected()), key=len, reverse=True)[0])
        else:
            Gc = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
        # get the number of nodes in the largest connected component
        Gc_nodes = Gc.number_of_nodes()
        # get the fraction of nodes in the largest connected component
        frac.append(Gc_nodes / G_nodes)
        # get the average path length of the largest connected component
        apl.append(nx.average_shortest_path_length(Gc, weight=weight))

    return initial, frac, apl

def simulate_degree_attack(G=None, attack_fraction=0.1, weight=None):
    """
    Simulate degree attack on a network
    :param G: networkx graph
    :param attack_fraction: fraction of nodes to be attacked (default: 0.1)
    :param weight: weight of edges (default: None)
    :return: initial (float), frac (list), apl (list)
    """
    # copy the graph to avoid changing the original graph
    G = G.copy()
    # get the  number of nodes
    G_nodes = G.number_of_nodes()
    # get the largest connected component of G
    if G.is_directed():
        Gc = G.to_undirected().subgraph(sorted(nx.connected_components(G.to_undirected()), key=len, reverse=True)[0])
    else:
        Gc = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
    # get the number of nodes in the largest connected component
    Gc_nodes = Gc.number_of_nodes()
    # get the initial fraction of nodes in the largest connected component
    initial = Gc_nodes / G_nodes
    # initialize lists
    frac = []
    apl = []
    #get the degree of each node
    degree = nx.degree_centrality(G)
    # sort the nodes by degree
    degree = sorted(degree, key=degree.get, reverse=True)
    # simulate degree attack
    for i in range(0, int(G_nodes * attack_fraction)):
        # remove the node with the highest degree
        G.remove_node(degree[i])
        # get the largest connected component of G
        if G.is_directed():
            Gc = G.to_undirected().subgraph(sorted(nx.connected_components(G.to_undirected()), key=len, reverse=True)[0])
        else:
            Gc = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
        # get the number of nodes in the largest connected component
        Gc_nodes = Gc.number_of_nodes()
        # get the fraction of nodes in the largest connected component
        frac.append(Gc_nodes / G_nodes)
        # get the average path length of the largest connected component
        apl.append(nx.average_shortest_path_length(Gc, weight=weight))

    return initial, frac, apl

def simulate_betweenness_attack(G=None, attack_fraction=0.1, weight=None, normalized=True, k=None, seed=None, endpoints=False):
    """
    Simulate betweenness attack on a network
    :param G: networkx graph
    :param attack_fraction: fraction of nodes to be attacked (default: 0.1)
    :param weight: weight of edges (default: None)
    :param normalized: if True, betweenness is normalized by 2/((n-1)(n-2)) for graphs, and 1/((n-1)(n-2)) for directed graphs where n is the number of nodes in G (default: True)
    :param k: use k node samples to estimate betweenness (default: None)
    :param seed: seed for random number generator (default: None)
    :param endpoints: If True include the endpoints in the shortest path counts (default: False)
    :return: initial (float), frac (list), apl (list)
    """
    # copy the graph to avoid changing the original graph
    G = G.copy()
    # get the  number of nodes
    G_nodes = G.number_of_nodes()
    # get the largest connected component of G
    if G.is_directed():
        Gc = G.to_undirected().subgraph(sorted(nx.connected_components(G.to_undirected()), key=len, reverse=True)[0])
    else:
        Gc = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
    # get the number of nodes in the largest connected component
    Gc_nodes = Gc.number_of_nodes()
    # get the initial fraction of nodes in the largest connected component
    initial = Gc_nodes / G_nodes
    # initialize lists
    frac = []
    apl = []
    # get the betweenness of each node
    betweenness = nx.betweenness_centrality(G, weight=weight, normalized=normalized, k=k, seed=seed, endpoints=endpoints)
    # sort the nodes by betweenness
    betweenness = sorted(betweenness, key=betweenness.get, reverse=True)
    # simulate betweenness attack
    for i in range(0, int(G_nodes * attack_fraction)):
        # remove the node with the highest betweenness
        G.remove_node(betweenness[i])
        # get the largest connected component of G
        if G.is_directed():
            Gc = G.to_undirected().subgraph(sorted(nx.connected_components(G.to_undirected()), key=len, reverse=True)[0])
        else:
            Gc = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
        # get the number of nodes in the largest connected component
        Gc_nodes = Gc.number_of_nodes()
        # get the fraction of nodes in the largest connected component
        frac.append(Gc_nodes / G_nodes)
        # get the average path length of the largest connected component
        apl.append(nx.average_shortest_path_length(Gc, weight=weight))

    return initial, frac, apl

def simulate_closeness_attack(G=None, attack_fraction=0.1, weight=None, u=None, wf_improved=True):
    """
    Simulate closeness attack on a network
    :param G: networkx graph
    :param attack_fraction: fraction of nodes to be attacked (default: 0.1)
    :param weight: weight of edges (default: None)
    :param u: node for which closeness is to be computed (default: None)
    :param wf_improved: use of the improved algorithm to scale by the fraction of nodes reachable (default: True)
    :return: initial (float), frac (list), apl (list)
    """
    # copy the graph to avoid changing the original graph
    G = G.copy()
    # get the  number of nodes
    G_nodes = G.number_of_nodes()
    # get the largest connected component of G
    if G.is_directed():
        Gc = G.to_undirected().subgraph(sorted(nx.connected_components(G.to_undirected()), key=len, reverse=True)[0])
    else:
        Gc = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
    # get the number of nodes in the largest connected component
    Gc_nodes = Gc.number_of_nodes()
    # get the initial fraction of nodes in the largest connected component
    initial = Gc_nodes / G_nodes
    # initialize lists
    frac = []
    apl = []
    # get the closeness of each node
    closeness = nx.closeness_centrality(G, distance=weight, u=u, wf_improved=wf_improved)
    # sort the nodes by closeness
    closeness = sorted(closeness, key=closeness.get, reverse=True)
    # simulate closeness attack
    for i in range(0, int(G_nodes * attack_fraction)):
        # remove the node with the highest closeness
        G.remove_node(closeness[i])
        # get the largest connected component of G
        if G.is_directed():
            Gc = G.to_undirected().subgraph(sorted(nx.connected_components(G.to_undirected()), key=len, reverse=True)[0])
        else:
            Gc = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
        # get the number of nodes in the largest connected component
        Gc_nodes = Gc.number_of_nodes()
        # get the fraction of nodes in the largest connected component
        frac.append(Gc_nodes / G_nodes)
        # get the average path length of the largest connected component
        apl.append(nx.average_shortest_path_length(Gc, weight=weight))

    return initial, frac, apl

def simulate_eigenvector_attack(G=None, attack_fraction=0.1, weight=None, tol=1e-06, max_iter=100, nstart=None):
    """
    Simulate eigenvector attack on a network
    :param G: networkx graph
    :param attack_fraction: fraction of nodes to be attacked (default: 0.1)
    :param weight: weight of edges (default: None)
    :param tol: tolerance for the power iteration method (default: 1e-06)
    :param max_iter: maximum number of iterations for the power iteration method (default: 100)
    :param nstart: initial vector for the power iteration method (default: None)
    :return: initial (float), frac (list), apl (list)
    """
    # copy the graph to avoid changing the original graph
    G = G.copy()
    # get the  number of nodes
    G_nodes = G.number_of_nodes()
    # get the largest connected component of G
    if G.is_directed():
        Gc = G.to_undirected().subgraph(sorted(nx.connected_components(G.to_undirected()), key=len, reverse=True)[0])
    else:
        Gc = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
    # get the number of nodes in the largest connected component
    Gc_nodes = Gc.number_of_nodes()
    # get the initial fraction of nodes in the largest connected component
    initial = Gc_nodes / G_nodes
    # initialize lists
    frac = []
    apl = []
    # get the eigenvector of each node
    eigenvector = nx.eigenvector_centrality(G, weight=weight, tol=tol, max_iter=max_iter, nstart=nstart)
    # sort the nodes by eigenvector
    eigenvector = sorted(eigenvector, key=eigenvector.get, reverse=True)
    # simulate eigenvector attack
    for i in range(0, int(G_nodes * attack_fraction)):
        # remove the node with the highest eigenvector
        G.remove_node(eigenvector[i])
        # get the largest connected component of G
        if G.is_directed():
            Gc = G.to_undirected().subgraph(sorted(nx.connected_components(G.to_undirected()), key=len, reverse=True)[0])
        else:
            Gc = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
        # get the number of nodes in the largest connected component
        Gc_nodes = Gc.number_of_nodes()
        # get the fraction of nodes in the largest connected component
        frac.append(Gc_nodes / G_nodes)
        # get the average path length of the largest connected component
        apl.append(nx.average_shortest_path_length(Gc, weight=weight))

    return initial, frac, apl

def molloy_reed(G=None):
    """
    Compute the Molloy-Reed criterion for a network
    :param G: networkx graph
    :return: Molloy-Reed criterion
    """
    # get the average squared degree
    avg_sq_degree = sum([d ** 2 for n, d in G.degree()]) / G.number_of_nodes()
    # get the average degree
    avg_degree = sum([d for n, d in G.degree()]) / G.number_of_nodes()
    # compute the Molloy-Reed criterion
    molloy_reed = avg_sq_degree/avg_degree

    return molloy_reed

def critical_threshold(G=None):
    """
    Compute the critical threshold for a network
    :param G: networkx graph
    :return: critical threshold
    """
    # get the average squared degree
    avg_sq_degree = sum([d ** 2 for n, d in G.degree()]) / G.number_of_nodes()
    # get the average degree
    avg_degree = sum([d for n, d in G.degree()]) / G.number_of_nodes()
    # compute the Molloy-Reed criterion
    molloy_reed = avg_sq_degree/avg_degree
    # compute the critical threshold
    critical_threshold = 1 - (1/(molloy_reed-1))
