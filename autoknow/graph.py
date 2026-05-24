# autoknow/graph.py
import networkx as nx

def build_knowledge_graph(files: list) -> nx.DiGraph:
    """Build a knowledge graph from files."""
    graph = nx.DiGraph()
    for file in files:
        graph.add_node(file, type="file")
        # TODO: Add relationships (imports, function calls)
    return graph