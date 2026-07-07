"""Entry point for uvx execution."""
from garza_tools_discovery.server import mcp

def main():
    mcp.run(transport="stdio")
