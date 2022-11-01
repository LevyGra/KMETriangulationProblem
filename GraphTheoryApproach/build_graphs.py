from Classes import Graph
from collections import Counter
from itertools import product
from pickle import dump

# Functions to programatically generate divisors
def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n /= i
            yield i
        else:
            i += 1
    if n > 1:
        yield n

def prod(iterable):
    result = 1
    for i in iterable:
        result *= i
    return result


def get_divisors(n):
    pf = prime_factors(n)
    pf_with_multiplicity = Counter(pf)
    powers = [
        [factor ** i for i in range(count + 1)]
        for factor, count in pf_with_multiplicity.items()
    ]
    for prime_power_combo in product(*powers):
        yield int(prod(prime_power_combo))
        

# Start building graphs
n_list = [2, 4]

for n in n_list:
    for k in get_divisors(n):
        print(f"Building graph for {n} verticies in {k} rows.")
        graph = Graph(n, k)
        graph.build()
        graph.print_graph()
        filename = f"GeneratedGraphs/graph_{n}_{k}.pkl"
        dump(graph, open(filename, "wb"))
        print("Dumped graph to", filename)