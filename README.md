# Autonomous Code Knowledge Graph CLI

`autoknow` is a **fully autonomous, open-source CLI tool** that turns any codebase into a **queryable knowledge graph** for AI agents. Designed for **Claude Code, Codex, Cursor, Copilot, and Hermes Agent**, it reduces token usage and improves context awareness by pre-processing code into a structured format.

## Features
- **Autonomous Indexing**: Scans local directories and builds a knowledge graph.
- **Query Interface**: Search for functions, classes, and dependencies.
- **AI Agent Integration**: Optimized for CLI-based AI agents.
- **Zero Configuration**: Works out of the box with no setup.
- **Multi-Language Support**: Python, JavaScript, TypeScript, Go, Rust, Java.

## Installation
```bash
pip install autoknow
```

## Usage
### 1. Index a Codebase
```bash
autoknow index
```

### 2. Query the Knowledge Graph
```bash
autoknow query "authenticate"
```

## Example Output
```
./test_dir/test.py:1 - def authenticate_user(): pass
```

## Technical Architecture
- **Scanner**: Recursively scans directories for code files.
- **Graph Builder**: Constructs a knowledge graph using `networkx`.
- **Query Engine**: Searches for keywords in file contents.

## Roadmap
- Add **AST parsing** for deeper code analysis.
- Support **more languages** (C++, Swift, Kotlin).
- Integrate with **Claude Code and Hermes Agent** as a plugin.

## License
MIT