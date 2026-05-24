# autoknow/query.py
import os

def query_graph(query: str) -> list:
    """Query the knowledge graph for relevant code snippets."""
    # Simplified: Search for query in file contents
    results = []
    for root, _, filenames in os.walk("."):
        for filename in filenames:
            if filename.endswith((".py", ".js", ".go", ".rs", ".java", ".ts")):
                filepath = os.path.join(root, filename)
                with open(filepath, "r") as f:
                    for line_num, line in enumerate(f, 1):
                        if query.lower() in line.lower():
                            results.append({
                                "file": filepath,
                                "line": line_num,
                                "code": line.strip(),
                            })
    return results