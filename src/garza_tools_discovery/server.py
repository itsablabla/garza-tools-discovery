"""garza-tools-discovery: MCP discovery layer for all connected MCP servers."""

from fastmcp import FastMCP

mcp = FastMCP("garza-tools-discovery")

TOOL_GROUPS = {
    "list_tavily_tools": [
        {"name": "tavily_search_tavilyl", "description": "Search the web using Tavily AI-powered search"},
        {"name": "tavily_extract_tavilyl", "description": "Extract structured content from one or more URLs"},
        {"name": "tavily_crawl_tavilyl", "description": "Crawl a website and return all discovered content"},
        {"name": "tavily_map_tavilyl", "description": "Map a website's link structure and sitemap"},
        {"name": "tavily_research_tavilyl", "description": "Conduct deep multi-step research on a topic"},
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
    fn = mcp.tool(description=f"Get tools for {name}")(fn)

if __name__ == "__main__":
    mcp.run(transport="stdio")
