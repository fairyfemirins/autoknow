# autoknow/cli.py
import click
from autoknow.scanner import scan_codebase
from autoknow.graph import build_knowledge_graph
from autoknow.query import query_graph

@click.group()
def cli():
    """Autonomous Code Knowledge Graph for AI Agents."""
    pass

@cli.command()
def index():
    """Scan the current directory and build a knowledge graph."""
    click.echo("Scanning codebase...")
    files = scan_codebase(".")
    graph = build_knowledge_graph(files)
    click.echo(f"Built knowledge graph with {len(graph.nodes)} nodes.")

@cli.command()
@click.argument("query")
def query(query: str):
    """Query the knowledge graph for relevant code snippets."""
    results = query_graph(query)
    for result in results:
        click.echo(f"{result['file']}:{result['line']} - {result['code']}")

def main():
    cli()