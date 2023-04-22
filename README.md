# networkx_robustness

A package for simulating network attacks on NetworkX graphs. The current supported attacks include random attacks and targeted attacks on nodes with the highest degree centrality, betweenness centrality, closeness centrality, and eigenvector centrality. Attack functions return the initial fraction of nodes in the giant component, a list of the fraction of nodes in the giant component after each node removal, and a list of the average path length in the giant component after each node removal.

## Installation

The package can be installed using the pip package manager and requires Python 3.7 or greater.

```bash
pip install networkx_robustness
```

## Simulating random attacks

```python
initial, frac, apl = simulate_random_attack(G=None, attack_fraction=0.1, weight=None)
    """
    Simulate random attack on a network
    :param G: networkx graph
    :param attack_fraction: fraction of nodes to be attacked (default: 0.1)
    :param weight: weight of edges (default: None)
    :return: initial (float), frac (list), apl (list)
    """
```

## Simulating degree centrality targeted attacks

```python
initial, frac, apl = simulate_degree_attack(G=None, attack_fraction=0.1, weight=None)
    """
    Simulate degree attack on a network
    :param G: networkx graph
    :param attack_fraction: fraction of nodes to be attacked (default: 0.1)
    :param weight: weight of edges (default: None)
    :return: initial (float), frac (list), apl (list)
    """
```

## Simulating betweenness centrality targeted attacks

```python
initial, frac, apl = simulate_betweenness_attack(G=None, attack_fraction=0.1, weight=None, normalized=True, k=None, seed=None, endpoints=False)
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
```

## Simulating closeness centrality targeted attacks

```python
initial, frac, apl = simulate_closeness_attack(G=None, attack_fraction=0.1, weight=None, u=None, wf_improved=True)
    """
    Simulate closeness attack on a network
    :param G: networkx graph
    :param attack_fraction: fraction of nodes to be attacked (default: 0.1)
    :param weight: weight of edges (default: None)
    :param u: node for which closeness is to be computed (default: None)
    :param wf_improved: use of the improved algorithm to scale by the fraction of nodes reachable (default: True)
    :return: initial (float), frac (list), apl (list)
    """
```

## Simulating eigenvector centrality targeted attacks

```python
initial, frac, apl = simulate_eigenvector_attack(G=None, attack_fraction=0.1, weight=None, tol=1e-06, max_iter=100, nstart=None)
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
```
