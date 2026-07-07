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
        "Query one of the 28 tools to get the full list of available tools "
        "for that category. Then call those tools on the main garza-tools MCP server."
    ),
)

TAVILY_TOOLS=[{"name":"tavily_search_tavilyl","description":"Search the web using Tavily AI-powered search"},{"name":"tavily_extract_tavilyl","description":"Extract structured content from one or more URLs"},{"name":"tavily_crawl_tavilyl","description":"Crawl a website and return all discovered content"},{"name":"tavily_map_tavilyl","description":"Map a website's link structure and sitemap"},{"name":"tavily_research_tavilyl","description":"Conduct deep multi-step research on a topic"}]
HINDSIGHT_TOOLS=[{"name":"retain_hindsp7","description":"Save a memory or piece of information to a bank"},{"name":"sync_retain_hindsp7","description":"Synchronously save a memory (blocking)"},{"name":"recall_hindsp7","description":"Retrieve stored memories relevant to a query"},{"name":"reflect_hindsp7","description":"Generate reflective insights from stored memories"},{"name":"list_banks_hindsp7","description":"List all memory banks in the account"},{"name":"create_bank_hindsp7","description":"Create a new named memory bank"},{"name":"get_bank_hindsp7","description":"Get details of a specific memory bank"},{"name":"get_bank_stats_hindsp7","description":"Get statistics (size, count) for a memory bank"},{"name":"update_bank_hindsp7","description":"Update a memory bank's settings or metadata"},{"name":"delete_bank_hindsp7","description":"Delete a memory bank and all its contents"},{"name":"clear_memories_hindsp7","description":"Clear all memories from a bank without deleting the bank"},{"name":"list_mental_models_hindsp7","description":"List all mental models"},{"name":"get_mental_model_hindsp7","description":"Get a specific mental model by ID"},{"name":"create_mental_model_hindsp7","description":"Create a new mental model from memories"},{"name":"update_mental_model_hindsp7","description":"Update an existing mental model"},{"name":"delete_mental_model_hindsp7","description":"Delete a mental model"},{"name":"refresh_mental_model_hindsp7","description":"Regenerate a mental model from recent memories"},{"name":"list_directives_hindsp7","description":"List all behavioral directives"},{"name":"create_directive_hindsp7","description":"Create a new behavioral directive"},{"name":"delete_directive_hindsp7","description":"Delete a directive"},{"name":"list_memories_hindsp7","description":"List all stored memory entries"},{"name":"get_memory_hindsp7","description":"Get a specific memory entry by ID"},{"name":"delete_memory_hindsp7","description":"Delete a specific memory entry"},{"name":"list_documents_hindsp7","description":"List all documents stored in memory"},{"name":"get_document_hindsp7","description":"Get the content of a specific document"},{"name":"delete_document_hindsp7","description":"Delete a specific document"},{"name":"list_operations_hindsp7","description":"List all ongoing async operations"},{"name":"get_operation_hindsp7","description":"Get the status of a specific operation"},{"name":"cancel_operation_hindsp7","description":"Cancel an ongoing async operation"},{"name":"list_tags_hindsp7","description":"List all tags used across memory banks"}]
VOICENOTES_TOOLS=[{"name":"search_notes_voicefx","description":"Semantically search through voice notes"},{"name":"list_notes_voicefx","description":"List all voice notes with metadata"},{"name":"get_note_voicefx","description":"Get full content of a voice note"},{"name":"create_note_voicefx","description":"Create a new voice note"}]
COMPOSIO_TOOLS=[{"name":"COMPOSIO_MANAGE_CONNECTIONS_compohq","description":"Manage OAuth connections to external services"},{"name":"COMPOSIO_MULTI_EXECUTE_TOOL_compohq","description":"Execute multiple Composio actions across services"},{"name":"COMPOSIO_REMOTE_BASH_TOOL_compohq","description":"Execute bash in remote Composio workbench"},{"name":"COMPOSIO_REMOTE_WORKBENCH_compohq","description":"Full remote workbench environment"},{"name":"COMPOSIO_SEARCH_TOOLS_compohq","description":"Search for Composio actions and integrations"},{"name":"COMPOSIO_WAIT_FOR_CONNECTIONS_compohq","description":"Wait for OAuth connection flows"},{"name":"COMPOSIO_GET_TOOL_SCHEMAS_compohq","description":"Get input/output schemas for tools"}]
BROWSERBASE_TOOLS=[{"name":"browserbase_browser_automation","description":"Cloud browser automation via Browserbase"}]
HYPERBROWSER_TOOLS=[{"name":"browser_use_agent","description":"Run an AI agent to browse the web"},{"name":"claude_computer_use_agent","description":"Claude-powered computer use agent"},{"name":"crawl_webpages","description":"Crawl and extract webpages"},{"name":"create_profile","description":"Create a browser profile"},{"name":"delete_profile","description":"Delete a browser profile"}]
BRIGHTDATA_TOOLS=[{"name":"brightdata_web_scraping","description":"Web scraping via Bright Data"}]
EXA_TOOLS=[{"name":"exa_web_search","description":"AI-powered web search via Exa"},{"name":"exa_get_contents","description":"Extract content from URLs via Exa"}]
PLAYWRIGHT_TOOLS=[{"name":"browser_click","description":"Click an element on the page"},{"name":"browser_close","description":"Close the browser"},{"name":"browser_console_messages","description":"Get console messages"},{"name":"browser_drag","description":"Drag an element"},{"name":"browser_drop","description":"Drop a dragged element"},{"name":"browser_evaluate","description":"Execute JavaScript"},{"name":"browser_fill","description":"Fill an input field"},{"name":"browser_hover","description":"Hover over an element"},{"name":"browser_navigate","description":"Navigate to a URL"},{"name":"browser_screenshot","description":"Take a screenshot"},{"name":"browser_select","description":"Select an option"}]
FIRECRAWL_TOOLS=[{"name":"firecrawl_scrape_firecl","description":"Scrape a URL"},{"name":"firecrawl_crawl_firecl","description":"Crawl a website"},{"name":"firecrawl_search_firecl","description":"Search the web"},{"name":"firecrawl_map_firecl","description":"Map URL structure"},{"name":"firecrawl_extract_firecl","description":"Extract structured data"}]
MEM_TOOLS=[{"name":"read_at_mem_ai","description":"Read a note from Mem"},{"name":"create_note_mem_ai","description":"Create a note in Mem"},{"name":"search_mem_ai","description":"Search Mem notes"},{"name":"list_notes_mem_ai","description":"List recent notes"}]
E2B_TOOLS=[{"name":"run_code","description":"Execute Python in E2B sandbox"}]
BEEPERBOX_TOOLS=[{"name":"list_accounts","description":"List messaging accounts"},{"name":"get_chat","description":"Get chat metadata"},{"name":"read_chat","description":"Read messages from chat"},{"name":"archive_chat","description":"Archive/unarchive a chat"},{"name":"list_inbox","description":"List active chats"},{"name":"list_unread","description":"List chats with unread"},{"name":"send_message","description":"Send a message"},{"name":"search_messages","description":"Full-text message search"},{"name":"react_to_message","description":"React with emoji"},{"name":"poll_messages","description":"Poll for new messages"},{"name":"note_to_self","description":"Send to note-to-self"},{"name":"download_asset","description":"Download attachment"}]
CONTEXT7_TOOLS=[{"name":"query_docs_context7","description":"Query library documentation"},{"name":"resolve_library_id_context7","description":"Resolve package to library ID"}]
CLOUDFLARE_TOOLS=[{"name":"cf_api_request","description":"Cloudflare API requests"}]
ONEPASSWORD_TOOLS=[{"name":"item_get","description":"Get 1Password item"},{"name":"item_list","description":"List 1Password items"},{"name":"item_lookup","description":"Look up item by UUID"},{"name":"note_create","description":"Create secure note"},{"name":"password_create","description":"Create password"},{"name":"password_generate","description":"Generate random password"},{"name":"password_read","description":"Read stored password"},{"name":"vault_list","description":"List 1Password vaults"},{"name":"password_update","description":"Update password"}]
TFY_MCP_ADMIN_TOOLS=[{"name":"tfy_list_servers","description":"List all MCP servers"},{"name":"tfy_register","description":"Register new MCP server"},{"name":"tfy_delete","description":"Delete MCP server"}]
LARK_IM_TOOLS=[{"name":"lark_send_message","description":"Send Lark message"},{"name":"lark_list_chats","description":"List Lark chats"}]
LARK_BASE_TOOLS=[{"name":"lark_base_search_records","description":"Search Base records"},{"name":"lark_base_create_record","description":"Create Base record"},{"name":"lark_base_list_tables","description":"List Base tables"}]
LARK_CALENDAR_TOOLS=[{"name":"lark_calendar_list_events","description":"List calendar events"},{"name":"lark_calendar_create_event","description":"Create calendar event"}]
LARK_DOCS_TOOLS=[{"name":"lark_docx_create","description":"Create Lark document"},{"name":"lark_docx_get_content","description":"Get document content"}]
LARK_DRIVE_TOOLS=[{"name":"lark_drive_list_files","description":"List Drive files"}]
LARK_SHEETS_TOOLS=[{"name":"lark_sheets_read","description":"Read spreadsheet data"}]
LARK_WIKI_TOOLS=[{"name":"lark_wiki_search","description":"Search Wiki pages"}]
LARK_TASKS_TOOLS=[{"name":"lark_task_create","description":"Create task"},{"name":"lark_task_list","description":"List tasks"}]
LARK_CONTACTS_TOOLS=[{"name":"lark_contact_list_users","description":"List users"}]
LARK_MAIL_ADMIN_TOOLS=[{"name":"lark_mail_list_groups","description":"List mail groups"}]
LARK_MAIL_USER_TOOLS=[{"name":"lark_mail_list_messages","description":"List emails"},{"name":"lark_mail_send","description":"Send email"}]

@mcp.tool(description="Get web search and crawling tools via Tavily")
def list_tavily_tools():
    return TAVILY_TOOLS

@mcp.tool(description="Get memory management tools via Hindsight")
def list_hindsight_tools():
    return HINDSIGHT_TOOLS

@mcp.tool(description="Get voice notes tools")
def list_voicenotes_tools():
    return VOICENOTES_TOOLS

@mcp.tool(description="Get Composio integration tools")
def list_composio_tools():
    return COMPOSIO_TOOLS

@mcp.tool(description="Get cloud browser automation tools via Browserbase")
def list_browserbase_tools():
    return BROWSERBASE_TOOLS

@mcp.tool(description="Get web browsing tools via Hyperbrowser")
def list_hyperbrowser_tools():
    return HYPERBROWSER_TOOLS

@mcp.tool(description="Get web scraping tools via Bright Data")
def list_brightdata_tools():
    return BRIGHTDATA_TOOLS

@mcp.tool(description="Get AI web search tools via Exa")
def list_exa_tools():
    return EXA_TOOLS

@mcp.tool(description="Get browser testing tools via Playwright")
def list_playwright_tools():
    return PLAYWRIGHT_TOOLS

@mcp.tool(description="Get web scraping tools via Firecrawl")
def list_firecrawl_tools():
    return FIRECRAWL_TOOLS

@mcp.tool(description="Get knowledge management tools via Mem")
def list_mem_tools():
    return MEM_TOOLS

@mcp.tool(description="Get code execution tools via E2B")
def list_e2b_tools():
    return E2B_TOOLS

@mcp.tool(description="Get messaging tools via Beeperbox")
def list_beeperbox_tools():
    return BEEPERBOX_TOOLS

@mcp.tool(description="Get documentation lookup tools via Context7")
def list_context7_tools():
    return CONTEXT7_TOOLS

@mcp.tool(description="Get Cloudflare API tools")
def list_cloudflare_tools():
    return CLOUDFLARE_TOOLS

@mcp.tool(description="Get 1Password secrets management tools")
def list_onepassword_tools():
    return ONEPASSWORD_TOOLS

@mcp.tool(description="Get TrueFoundry MCP admin tools")
def list_tfy_admin_tools():
    return TFY_MCP_ADMIN_TOOLS

@mcp.tool(description="Get Lark IM tools")
def list_lark_im_tools():
    return LARK_IM_TOOLS

@mcp.tool(description="Get Lark Base tools")
def list_lark_base_tools():
    return LARK_BASE_TOOLS

@mcp.tool(description="Get Lark Calendar tools")
def list_lark_calendar_tools():
    return LARK_CALENDAR_TOOLS

@mcp.tool(description="Get Lark Docs tools")
def list_lark_docs_tools():
    return LARK_DOCS_TOOLS

@mcp.tool(description="Get Lark Drive tools")
def list_lark_drive_tools():
    return LARK_DRIVE_TOOLS

@mcp.tool(description="Get Lark Sheets tools")
def list_lark_sheets_tools():
    return LARK_SHEETS_TOOLS

@mcp.tool(description="Get Lark Wiki tools")
def list_lark_wiki_tools():
    return LARK_WIKI_TOOLS

@mcp.tool(description="Get Lark Tasks tools")
def list_lark_tasks_tools():
    return LARK_TASKS_TOOLS

@mcp.tool(description="Get Lark Contacts tools")
def list_lark_contacts_tools():
    return LARK_CONTACTS_TOOLS

@mcp.tool(description="Get Lark Mail Admin tools")
def list_lark_mail_admin_tools():
    return LARK_MAIL_ADMIN_TOOLS

@mcp.tool(description="Get Lark Mail User tools")
def list_lark_mail_user_tools():
    return LARK_MAIL_USER_TOOLS

if __name__=="__main__":
    import sys
    transport=sys.argv[1] if len(sys.argv)>1 else "streamable-http"
    if transport=="stdio":
        mcp.run(transport="stdio")
    else:
        mcp.run(transport="streamable-http",host="0.0.0.0",port=8000)
