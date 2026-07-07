# garza-tools-discovery

A lightweight MCP discovery layer for the [garza-tools](https://garza.truefoundry.cloud) virtual MCP server.

Instead of exposing all 46 tools at once, this server exposes **4 discovery tools** — one per backing server group. An agent can call a discovery tool to learn which tools are available in that category before calling the main server.

## Tools

| Tool | Backing Server | Tools Available |
|------|---------------|----------------|
| `list_tavily_tools` | Tavily | 5 web search/crawl tools |
| `list_hindsight_tools` | Hindsight | 30 memory management tools |
| `list_voicenotes_tools` | VoiceNotes | 4 voice note tools |
| `list_composio_tools` | Composio | 7 integration tools |

## Usage

```bash
uvx garza-tools-discovery
```

This runs the server in MCP stdio mode, suitable for use with TrueFoundry AI Gateway or any MCP-compatible agent.
