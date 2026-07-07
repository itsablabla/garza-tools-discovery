"""garza-tools-discovery: MCP discovery layer for all connected MCP servers."""

from fastmcp import FastMCP

mcp = FastMCP("garza-tools-discovery")

TOOL_GROUPS = {
    "list_tavily_tools": [
        {"name": "tavily_search_tavilyl", "description": "Search the web using Tavily AI-powered search"},
        {"name": "tavily_extract_tavilyl", "description": "Extract structured content from URLs"},
        {"name": "tavily_crawl_tavilyl", "description": "Crawl a website and return content"},
        {"name": "tavily_map_tavilyl", "description": "Map website link structure"},
        {"name": "tavily_research_tavilyl", "description": "Deep multi-step research on a topic"},
    ],
    "list_hindsight_tools": [
        {"name": "retain_hindsp7", "description": "Save a memory to a bank"},
        {"name": "sync_retain_hindsp7", "description": "Synchronously save a memory"},
        {"name": "recall_hindsp7", "description": "Retrieve stored memories"},
        {"name": "reflect_hindsp7", "description": "Generate reflective insights"},
        {"name": "list_banks_hindsp7", "description": "List all memory banks"},
        {"name": "create_bank_hindsp7", "description": "Create a named memory bank"},
        {"name": "get_bank_hindsp7", "description": "Get bank details"},
        {"name": "get_bank_stats_hindsp7", "description": "Get bank statistics"},
        {"name": "update_bank_hindsp7", "description": "Update bank settings"},
        {"name": "delete_bank_hindsp7", "description": "Delete a bank"},
        {"name": "clear_memories_hindsp7", "description": "Clear all memories from bank"},
        {"name": "list_mental_models_hindsp7", "description": "List mental models"},
        {"name": "get_mental_model_hindsp7", "description": "Get a mental model"},
        {"name": "create_mental_model_hindsp7", "description": "Create a mental model"},
        {"name": "update_mental_model_hindsp7", "description": "Update a mental model"},
        {"name": "delete_mental_model_hindsp7", "description": "Delete a mental model"},
        {"name": "refresh_mental_model_hindsp7", "description": "Regenerate a mental model"},
        {"name": "list_directives_hindsp7", "description": "List behavioral directives"},
        {"name": "create_directive_hindsp7", "description": "Create a directive"},
        {"name": "delete_directive_hindsp7", "description": "Delete a directive"},
        {"name": "list_memories_hindsp7", "description": "List all stored memories"},
        {"name": "get_memory_hindsp7", "description": "Get a specific memory"},
        {"name": "delete_memory_hindsp7", "description": "Delete a memory"},
        {"name": "list_documents_hindsp7", "description": "List documents"},
        {"name": "get_document_hindsp7", "description": "Get document content"},
        {"name": "delete_document_hindsp7", "description": "Delete a document"},
        {"name": "list_operations_hindsp7", "description": "List async operations"},
        {"name": "get_operation_hindsp7", "description": "Get operation status"},
        {"name": "cancel_operation_hindsp7", "description": "Cancel an operation"},
        {"name": "list_tags_hindsp7", "description": "List tags across banks"},
    ],
    "list_voicenotes_tools": [
        {"name": "search_notes_voicefx", "description": "Semantically search voice notes"},
        {"name": "list_notes_voicefx", "description": "List voice notes with metadata"},
        {"name": "get_note_voicefx", "description": "Get full voice note content"},
        {"name": "create_note_voicefx", "description": "Create a voice note"},
    ],
    "list_composio_tools": [
        {"name": "COMPOSIO_MANAGE_CONNECTIONS_compohq", "description": "Manage OAuth connections"},
        {"name": "COMPOSIO_MULTI_EXECUTE_TOOL_compohq", "description": "Execute actions across services"},
        {"name": "COMPOSIO_REMOTE_BASH_TOOL_compohq", "description": "Remote bash execution"},
        {"name": "COMPOSIO_REMOTE_WORKBENCH_compohq", "description": "Remote workbench"},
        {"name": "COMPOSIO_SEARCH_TOOLS_compohq", "description": "Search for integrations"},
        {"name": "COMPOSIO_WAIT_FOR_CONNECTIONS_compohq", "description": "Wait for OAuth flows"},
        {"name": "COMPOSIO_GET_TOOL_SCHEMAS_compohq", "description": "Get tool schemas"},
    ],
    "list_browserbase_tools": [
        {"name": "browserbase_automation", "description": "Cloud browser automation via Browserbase"},
    ],
    "list_hyperbrowser_tools": [
        {"name": "browser_use_agent", "description": "AI web browsing agent via Hyperbrowser"},
        {"name": "crawl_webpages", "description": "Crawl and extract webpages"},
        {"name": "create_profile", "description": "Create a browser profile"},
        {"name": "delete_profile", "description": "Delete a browser profile"},
    ],
    "list_brightdata_tools": [
        {"name": "brightdata_web_scraping", "description": "Web scraping via Bright Data"},
    ],
    "list_exa_tools": [
        {"name": "exa_web_search", "description": "AI-powered web search via Exa"},
        {"name": "exa_get_contents", "description": "Extract content from URLs via Exa"},
    ],
    "list_playwright_tools": [
        {"name": "playwright_browser_automation", "description": "Browser automation via Playwright"},
    ],
}

for name, tools in TOOL_GROUPS.items():
    fn = (lambda t: lambda: t)(tools)
    fn.__name__ = name
    fn.__doc__ = f"Get the complete list of {name.replace('_',' ')} available on garza-tools."
    mcp.tool()(fn)

if __name__ == "__main__":
    mcp.run(transport="stdio")
