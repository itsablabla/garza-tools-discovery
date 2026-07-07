"""garza-tools-discovery: MCP discovery layer for all 28 connected MCP servers."""

from fastmcp import FastMCP

mcp = FastMCP("garza-tools-discovery")

TOOL_GROUPS = {
    "list_beeperbox_tools": [
        {"name": "list_accounts", "description": "List all connected messaging accounts"},
        {"name": "get_chat", "description": "Get metadata for a specific chat"},
        {"name": "read_chat", "description": "Read messages from a chat"},
        {"name": "archive_chat", "description": "Archive or unarchive a chat"},
        {"name": "list_inbox", "description": "List recently active chats"},
        {"name": "list_unread", "description": "List chats with unread messages"},
        {"name": "send_message", "description": "Send a text message to a chat"},
        {"name": "search_messages", "description": "Full-text search across all messages"},
        {"name": "react_to_message", "description": "Add an emoji reaction"},
        {"name": "poll_messages", "description": "Poll for new messages"},
        {"name": "note_to_self", "description": "Send message to note-to-self chat"},
        {"name": "download_asset", "description": "Download an attachment by URL"},
    ],
    "list_brightdata_tools": [
        {"name": "brightdata_web_scraping", "description": "Web scraping via Bright Data"},
    ],
    "list_browserbase_tools": [
        {"name": "browserbase_automation", "description": "Cloud browser automation via Browserbase"},
    ],
    "list_cloudflare_tools": [
        {"name": "cf_api_request", "description": "Cloudflare API requests"},
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
    "list_context7_tools": [
        {"name": "query_docs_context7", "description": "Query documentation for a library"},
        {"name": "resolve_library_id_context7", "description": "Resolve a package to a Context7 ID"},
    ],
    "list_e2b_tools": [
        {"name": "run_code", "description": "Execute Python in E2B sandbox"},
    ],
    "list_exa_tools": [
        {"name": "exa_web_search", "description": "AI-powered web search via Exa"},
        {"name": "exa_get_contents", "description": "Extract content from URLs via Exa"},
    ],
    "list_firecrawl_tools": [
        {"name": "firecrawl_scrape_firecl", "description": "Scrape a single URL"},
        {"name": "firecrawl_crawl_firecl", "description": "Crawl an entire website"},
        {"name": "firecrawl_search_firecl", "description": "Search the web and scrape results"},
        {"name": "firecrawl_map_firecl", "description": "Map website URL structure"},
        {"name": "firecrawl_extract_firecl", "description": "Extract structured data from URLs"},
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
    "list_hyperbrowser_tools": [
        {"name": "browser_use_agent", "description": "AI web browsing agent via Hyperbrowser"},
        {"name": "crawl_webpages", "description": "Crawl and extract webpages"},
        {"name": "create_profile", "description": "Create a browser profile"},
        {"name": "delete_profile", "description": "Delete a browser profile"},
    ],
    "list_lark_base_tools": [
        {"name": "lark_base_search_records", "description": "Search Lark Base records"},
        {"name": "lark_base_create_record", "description": "Create a Lark Base record"},
        {"name": "lark_base_list_tables", "description": "List Lark Base tables"},
    ],
    "list_lark_calendar_tools": [
        {"name": "lark_calendar_list_events", "description": "List calendar events"},
        {"name": "lark_calendar_create_event", "description": "Create a calendar event"},
    ],
    "list_lark_contacts_tools": [
        {"name": "lark_contact_list_users", "description": "List users in contacts"},
    ],
    "list_lark_docs_tools": [
        {"name": "lark_docx_create", "description": "Create a Lark document"},
        {"name": "lark_docx_get_content", "description": "Get document content"},
    ],
    "list_lark_drive_tools": [
        {"name": "lark_drive_list_files", "description": "List files in Drive"},
    ],
    "list_lark_im_tools": [
        {"name": "lark_send_message", "description": "Send a Lark message"},
        {"name": "lark_list_chats", "description": "List Lark chats"},
    ],
    "list_lark_mail_admin_tools": [
        {"name": "lark_mail_list_groups", "description": "List mail groups"},
    ],
    "list_lark_mail_user_tools": [
        {"name": "lark_mail_list_messages", "description": "List email messages"},
        {"name": "lark_mail_send", "description": "Send an email"},
    ],
    "list_lark_sheets_tools": [
        {"name": "lark_sheets_read", "description": "Read spreadsheet data"},
    ],
    "list_lark_tasks_tools": [
        {"name": "lark_task_create", "description": "Create a task"},
        {"name": "lark_task_list", "description": "List tasks"},
    ],
    "list_lark_wiki_tools": [
        {"name": "lark_wiki_search", "description": "Search wiki pages"},
    ],
    "list_mem_tools": [
        {"name": "read_at_mem_ai", "description": "Read a note from Mem"},
        {"name": "create_note_mem_ai", "description": "Create a note in Mem"},
        {"name": "search_mem_ai", "description": "Search across Mem notes"},
        {"name": "list_notes_mem_ai", "description": "List recent Mem notes"},
    ],
    "list_onepassword_tools": [
        {"name": "item_get", "description": "Get a 1Password item"},
        {"name": "item_list", "description": "List 1Password items"},
        {"name": "item_lookup", "description": "Look up item by UUID"},
        {"name": "note_create", "description": "Create a secure note"},
        {"name": "password_create", "description": "Create a password"},
        {"name": "password_generate", "description": "Generate a random password"},
        {"name": "password_read", "description": "Read a stored password"},
        {"name": "vault_list", "description": "List 1Password vaults"},
        {"name": "password_update", "description": "Update a password"},
    ],
    "list_playwright_tools": [
        {"name": "playwright_browser_automation", "description": "Browser automation via Playwright"},
    ],
    "list_tavily_tools": [
        {"name": "tavily_search_tavilyl", "description": "Search the web via Tavily"},
        {"name": "tavily_extract_tavilyl", "description": "Extract content from URLs"},
        {"name": "tavily_crawl_tavilyl", "description": "Crawl a website"},
        {"name": "tavily_map_tavilyl", "description": "Map website link structure"},
        {"name": "tavily_research_tavilyl", "description": "Deep research on a topic"},
    ],
    "list_tfy_admin_tools": [
        {"name": "tfy_list_servers", "description": "List all MCP servers"},
        {"name": "tfy_register", "description": "Register a new MCP server"},
        {"name": "tfy_delete", "description": "Delete an MCP server"},
    ],
    "list_voicenotes_tools": [
        {"name": "search_notes_voicefx", "description": "Search voice notes"},
        {"name": "list_notes_voicefx", "description": "List voice notes"},
        {"name": "get_note_voicefx", "description": "Get full voice note"},
        {"name": "create_note_voicefx", "description": "Create a voice note"},
    ],
}

for name, tools in TOOL_GROUPS.items():
    fn = (lambda t: lambda: t)(tools)
    fn.__name__ = name
    fn.__doc__ = f"Get the complete list of {name.replace('_',' ')} available on garza-tools."
    mcp.tool()(fn)

if __name__ == "__main__":
    mcp.run(transport="stdio")
