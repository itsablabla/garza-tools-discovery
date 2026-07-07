"""Entry point for uvx/pipx execution — runs in stdio mode."""
from garza_tools_discovery.server import mcp

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
