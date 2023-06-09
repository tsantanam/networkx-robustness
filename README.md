# networkx-robustness

[![DOI](https://zenodo.org/badge/631239682.svg)](https://zenodo.org/badge/latestdoi/631239682) [![PyPI Version](https://img.shields.io/pypi/v/networkx-robustness.svg)](https://pypi.python.org/pypi/networkx-robustness)

A package for simulating network attacks and calculating robustness measures on NetworkX graphs. The current supported attacks include random attacks and targeted attacks on nodes with the highest degree centrality, betweenness centrality, closeness centrality, and eigenvector centrality. Attack functions return the initial fraction of nodes in the giant component, a list of the fraction of nodes in the giant component after each node removal, and a list of the average path length in the giant component after each node removal.

The package also contains functions for calculating the Molloy-Reed criterion and the critical threshold for a network.

## Citation

If you use this package, please cite the package as:

Tejas Santanam. (2023). tsantanam/networkx-robustness: v0.0.7 (v0.0.7). Zenodo. https://doi.org/10.5281/zenodo.7855211

## Installation

The package can be installed using the pip package manager and requires Python 3.7 or greater. There is a package dependency with NetworkX.

```bash
pip install networkx-robustness
```

## Example

An example of importing and using the package is shown below

```python
import networkx as nx
from networkx_robustness import networkx_robustness

#Random NetworkX graph with 100 nodes
G = nx.gnp_random_graph(100, 0.5)

#Simulate a random attack on 20 nodes
initial, frac, apl = networkx_robustness.simulate_random_attack(G, attack_fraction=0.2)
```

## Documentation

### Simulating random attacks

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

### Simulating degree centrality targeted attacks

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

### Simulating betweenness centrality targeted attacks

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

### Simulating closeness centrality targeted attacks

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

### Simulating eigenvector centrality targeted attacks

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

### Calculating the Molloy-Reed Criterion

```python
molloy_reed = molloy_reed(G=None)
    """
    Compute the Molloy-Reed criterion for a network
    :param G: networkx graph
    :return: Molloy-Reed criterion
    """
```

### Calculating the critical threshold

```python
critical_threshold = critical_threshold(G=None)
    """
    Compute the critical threshold for a network
    :param G: networkx graph
    :return: critical threshold
    """
```
