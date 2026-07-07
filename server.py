"""
garza-tools-discovery MCP Server

A lightweight discovery layer for the garza-tools virtual MCP server.
Instead of exposing all 46 tools at once, this server exposes 4 tools —
one per backing server group. Each tool returns the complete list of
tools available in that group, so an agent can plan which tools to
call on the main garza-tools server.

Usage with the main garza-tools:
  1. Call a discovery tool here → get the list of tools for that group
  2. Call the actual tools on the garza-tools MCP server
"""

from fastmcp import FastMCP

mcp = FastMCP(
    name="garza-tools-discovery",
    instructions=(
        "Discovery layer for garza-tools. "
        "Query one of the 9 tools to get the full list of available tools "
        "for that category. Then call those tools on the main garza-tools MCP server."
    ),
)

# ---------------------------------------------------------------------------
# Tool catalogs (mirrors garza-tools virtual MCP, grouped by backing server)
# ---------------------------------------------------------------------------

TAVILY_TOOLS = [
    {"name": "tavily_search_tavilyl",   "description": "Search the web using Tavily AI-powered search"},
    {"name": "tavily_extract_tavilyl",  "description": "Extract structured content from one or more URLs"},
    {"name": "tavily_crawl_tavilyl",    "description": "Crawl a website and return all discovered content"},
    {"name": "tavily_map_tavilyl",      "description": "Map a website's link structure and sitemap"},
    {"name": "tavily_research_tavilyl", "description": "Conduct deep multi-step research on a topic"},
]

HINDSIGHT_TOOLS = [
    {"name": "retain_hindsp7",               "description": "Save a memory or piece of information to a bank"},
    {"name": "sync_retain_hindsp7",          "description": "Synchronously save a memory (blocking)"},
    {"name": "recall_hindsp7",               "description": "Retrieve stored memories relevant to a query"},
    {"name": "reflect_hindsp7",              "description": "Generate reflective insights from stored memories"},
    {"name": "list_banks_hindsp7",           "description": "List all memory banks in the account"},
    {"name": "create_bank_hindsp7",          "description": "Create a new named memory bank"},
    {"name": "get_bank_hindsp7",             "description": "Get details of a specific memory bank"},
    {"name": "get_bank_stats_hindsp7",       "description": "Get statistics (size, count) for a memory bank"},
    {"name": "update_bank_hindsp7",          "description": "Update a memory bank's settings or metadata"},
    {"name": "delete_bank_hindsp7",          "description": "Delete a memory bank and all its contents"},
    {"name": "clear_memories_hindsp7",       "description": "Clear all memories from a bank without deleting the bank"},
    {"name": "list_mental_models_hindsp7",   "description": "List all mental models"},
    {"name": "get_mental_model_hindsp7",     "description": "Get a specific mental model by ID"},
    {"name": "create_mental_model_hindsp7",  "description": "Create a new mental model from memories"},
    {"name": "update_mental_model_hindsp7",  "description": "Update an existing mental model"},
    {"name": "delete_mental_model_hindsp7",  "description": "Delete a mental model"},
    {"name": "refresh_mental_model_hindsp7", "description": "Regenerate a mental model from recent memories"},
    {"name": "list_directives_hindsp7",      "description": "List all behavioral directives"},
    {"name": "create_directive_hindsp7",     "description": "Create a new behavioral directive"},
    {"name": "delete_directive_hindsp7",     "description": "Delete a directive"},
    {"name": "list_memories_hindsp7",        "description": "List all stored memory entries"},
    {"name": "get_memory_hindsp7",           "description": "Get a specific memory entry by ID"},
    {"name": "delete_memory_hindsp7",        "description": "Delete a specific memory entry"},
    {"name": "list_documents_hindsp7",       "description": "List all documents stored in memory"},
    {"name": "get_document_hindsp7",         "description": "Get the content of a specific document"},
    {"name": "delete_document_hindsp7",      "description": "Delete a specific document"},
    {"name": "list_operations_hindsp7",      "description": "List all ongoing async operations"},
    {"name": "get_operation_hindsp7",        "description": "Get the status of a specific operation"},
    {"name": "cancel_operation_hindsp7",     "description": "Cancel an ongoing async operation"},
    {"name": "list_tags_hindsp7",            "description": "List all tags used across memory banks"},
]

VOICENOTES_TOOLS = [
    {"name": "search_notes_voicefx", "description": "Semantically search through voice notes and transcriptions"},
    {"name": "list_notes_voicefx",   "description": "List all voice notes with metadata"},
    {"name": "get_note_voicefx",     "description": "Get the full content and transcript of a specific voice note"},
    {"name": "create_note_voicefx",  "description": "Create a new voice note entry"},
]

COMPOSIO_TOOLS = [
    {"name": "COMPOSIO_MANAGE_CONNECTIONS_compohq",  "description": "Manage OAuth connections to external services (Gmail, Slack, GitHub, etc.)"},
    {"name": "COMPOSIO_MULTI_EXECUTE_TOOL_compohq",  "description": "Execute multiple Composio actions across connected services in one call"},
    {"name": "COMPOSIO_REMOTE_BASH_TOOL_compohq",    "description": "Execute bash commands in a remote Composio workbench environment"},
    {"name": "COMPOSIO_REMOTE_WORKBENCH_compohq",    "description": "Interact with a full remote workbench (file system, terminal, browser)"},
    {"name": "COMPOSIO_SEARCH_TOOLS_compohq",        "description": "Search for available Composio actions and integrations by keyword"},
    {"name": "COMPOSIO_WAIT_FOR_CONNECTIONS_compohq","description": "Wait for pending OAuth connection flows to complete"},
    {"name": "COMPOSIO_GET_TOOL_SCHEMAS_compohq",    "description": "Get the input/output schemas for specific Composio tools"},
]

BROWSERBASE_TOOLS = [
    {"name": "browserbase_browser_automation", "description": "Cloud browser automation via Browserbase"},
]

HYPERBROWSER_TOOLS = [
    {"name": "hyperbrowser_web_browsing", "description": "Web browsing and automation via Hyperbrowser"},
]

BRIGHTDATA_TOOLS = [
    {"name": "brightdata_web_scraping", "description": "Web scraping and data collection via Bright Data"},
]

EXA_TOOLS = [
    {"name": "exa_web_search", "description": "AI-powered web search via Exa"},
    {"name": "exa_get_contents", "description": "Extract content from URLs via Exa"},
]

PLAYWRIGHT_TOOLS = [
    {"name": "playwright_browser_automation", "description": "Browser automation and web testing via Playwright"},
]

# ---------------------------------------------------------------------------
# Discovery tools
# ---------------------------------------------------------------------------

@mcp.tool(
    description=(
        "Get the complete list of web search and crawling tools available via the Tavily integration. "
        "Returns tool names and descriptions. Use these tool names on the garza-tools MCP server to execute them."
    )
)
def list_tavily_tools() -> list[dict]:
    """Returns all Tavily web search/crawl tools available on garza-tools."""
    return TAVILY_TOOLS


@mcp.tool(
    description=(
        "Get the complete list of memory and knowledge management tools available via the Hindsight integration. "
        "Covers memory banks, mental models, directives, documents, and async operations. "
        "Returns tool names and descriptions. Use these tool names on the garza-tools MCP server to execute them."
    )
)
def list_hindsight_tools() -> list[dict]:
    """Returns all Hindsight memory-management tools available on garza-tools."""
    return HINDSIGHT_TOOLS


@mcp.tool(
    description=(
        "Get the complete list of voice notes and audio transcription tools. "
        "Returns tool names and descriptions. Use these tool names on the garza-tools MCP server to execute them."
    )
)
def list_voicenotes_tools() -> list[dict]:
    """Returns all VoiceNotes tools available on garza-tools."""
    return VOICENOTES_TOOLS


@mcp.tool(
    description=(
        "Get the complete list of Composio integration tools for connecting to and executing actions on "
        "external services (GitHub, Gmail, Slack, Notion, Linear, and 250+ more). "
        "Returns tool names and descriptions. Use these tool names on the garza-tools MCP server to execute them."
    )
)
def list_composio_tools() -> list[dict]:
    """Returns all Composio integration tools available on garza-tools."""
    return COMPOSIO_TOOLS


@mcp.tool(
    description=(
        "Get the complete list of cloud browser automation tools available via Browserbase. "
        "Returns tool names and descriptions. Use these tool names on the garza-tools MCP server to execute them."
    )
)
def list_browserbase_tools() -> list[dict]:
    return BROWSERBASE_TOOLS


@mcp.tool(
    description=(
        "Get the complete list of web browsing and automation tools available via Hyperbrowser. "
        "Returns tool names and descriptions. Use these tool names on the garza-tools MCP server to execute them."
    )
)
def list_hyperbrowser_tools() -> list[dict]:
    return HYPERBROWSER_TOOLS


@mcp.tool(
    description=(
        "Get the complete list of web scraping and data collection tools available via Bright Data. "
        "Returns tool names and descriptions. Use these tool names on the garza-tools MCP server to execute them."
    )
)
def list_brightdata_tools() -> list[dict]:
    return BRIGHTDATA_TOOLS


@mcp.tool(
    description=(
        "Get the complete list of AI-powered web search tools available via Exa. "
        "Returns tool names and descriptions. Use these tool names on the garza-tools MCP server to execute them."
    )
)
def list_exa_tools() -> list[dict]:
    return EXA_TOOLS


@mcp.tool(
    description=(
        "Get the complete list of browser automation and web testing tools available via Playwright. "
        "Returns tool names and descriptions. Use these tool names on the garza-tools MCP server to execute them."
    )
)
def list_playwright_tools() -> list[dict]:
    return PLAYWRIGHT_TOOLS


if __name__ == "__main__":
    import sys
    transport = sys.argv[1] if len(sys.argv) > 1 else "streamable-http"
    if transport == "stdio":
        mcp.run(transport="stdio")
    else:
        mcp.run(transport="streamable-http", host="0.0.0.0", port=8000)
