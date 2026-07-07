"""
garza-tools-discovery MCP Server - Discovery layer for all 28 MCP server groups
"""
from fastmcp import FastMCP
mcp = FastMCP(name="garza-tools-discovery",instructions="Discovery layer for garza-tools. Query a discovery tool to get available tools for that group.")

T={}
T["tavily"]=[{"name":"tavily_search_tavilyl","description":"Web search via Tavily"},{"name":"tavily_extract_tavilyl","description":"Extract content from URLs"},{"name":"tavily_crawl_tavilyl","description":"Crawl a website"},{"name":"tavily_map_tavilyl","description":"Map URL structure"},{"name":"tavily_research_tavilyl","description":"Deep multi-step research"}]
T["hindsight"]=[{"name":"retain_hindsp7","description":"Save a memory"},{"name":"sync_retain_hindsp7","description":"Sync save memory"},{"name":"recall_hindsp7","description":"Retrieve memories"},{"name":"reflect_hindsp7","description":"Generate insights"},{"name":"list_banks_hindsp7","description":"List memory banks"},{"name":"create_bank_hindsp7","description":"Create memory bank"},{"name":"get_bank_hindsp7","description":"Get bank details"},{"name":"get_bank_stats_hindsp7","description":"Bank statistics"},{"name":"update_bank_hindsp7","description":"Update bank settings"},{"name":"delete_bank_hindsp7","description":"Delete bank"},{"name":"clear_memories_hindsp7","description":"Clear memories"},{"name":"list_mental_models_hindsp7","description":"List mental models"},{"name":"get_mental_model_hindsp7","description":"Get mental model"},{"name":"create_mental_model_hindsp7","description":"Create mental model"},{"name":"update_mental_model_hindsp7","description":"Update mental model"},{"name":"delete_mental_model_hindsp7","description":"Delete mental model"},{"name":"refresh_mental_model_hindsp7","description":"Refresh mental model"},{"name":"list_directives_hindsp7","description":"List directives"},{"name":"create_directive_hindsp7","description":"Create directive"},{"name":"delete_directive_hindsp7","description":"Delete directive"},{"name":"list_memories_hindsp7","description":"List memories"},{"name":"get_memory_hindsp7","description":"Get memory"},{"name":"delete_memory_hindsp7","description":"Delete memory"},{"name":"list_documents_hindsp7","description":"List documents"},{"name":"get_document_hindsp7","description":"Get document"},{"name":"delete_document_hindsp7","description":"Delete document"},{"name":"list_operations_hindsp7","description":"List operations"},{"name":"get_operation_hindsp7","description":"Get operation"},{"name":"cancel_operation_hindsp7","description":"Cancel operation"},{"name":"list_tags_hindsp7","description":"List tags"}]
T["voicenotes"]=[{"name":"search_notes_voicefx","description":"Search voice notes"},{"name":"list_notes_voicefx","description":"List voice notes"},{"name":"get_note_voicefx","description":"Get voice note"},{"name":"create_note_voicefx","description":"Create voice note"}]
T["composio"]=[{"name":"COMPOSIO_MANAGE_CONNECTIONS_compohq","description":"Manage OAuth connections"},{"name":"COMPOSIO_MULTI_EXECUTE_TOOL_compohq","description":"Multi-execute actions"},{"name":"COMPOSIO_REMOTE_BASH_TOOL_compohq","description":"Remote bash"},{"name":"COMPOSIO_REMOTE_WORKBENCH_compohq","description":"Remote workbench"},{"name":"COMPOSIO_SEARCH_TOOLS_compohq","description":"Search integrations"},{"name":"COMPOSIO_WAIT_FOR_CONNECTIONS_compohq","description":"Wait for OAuth"},{"name":"COMPOSIO_GET_TOOL_SCHEMAS_compohq","description":"Get tool schemas"}]
T["browserbase"]=[{"name":"browserbase_automation","description":"Cloud browser automation"}]
T["hyperbrowser"]=[{"name":"browser_use_agent","description":"AI web browsing agent"},{"name":"claude_computer_use_agent","description":"Claude computer use"},{"name":"crawl_webpages","description":"Crawl webpages"},{"name":"create_profile","description":"Create profile"},{"name":"delete_profile","description":"Delete profile"}]
T["brightdata"]=[{"name":"brightdata_scraping","description":"Web scraping"}]
T["exa"]=[{"name":"exa_web_search","description":"AI web search"},{"name":"exa_get_contents","description":"Extract URL content"}]
T["playwright"]=[{"name":"browser_click","description":"Click element"},{"name":"browser_close","description":"Close browser"},{"name":"browser_console_messages","description":"Console messages"},{"name":"browser_drag","description":"Drag element"},{"name":"browser_drop","description":"Drop element"},{"name":"browser_evaluate","description":"Execute JS"},{"name":"browser_fill","description":"Fill input"},{"name":"browser_hover","description":"Hover element"},{"name":"browser_navigate","description":"Navigate URL"},{"name":"browser_screenshot","description":"Take screenshot"},{"name":"browser_select","description":"Select option"}]
T["firecrawl"]=[{"name":"firecrawl_scrape_firecl","description":"Scrape URL"},{"name":"firecrawl_crawl_firecl","description":"Crawl website"},{"name":"firecrawl_search_firecl","description":"Web search"},{"name":"firecrawl_map_firecl","description":"Map URLs"},{"name":"firecrawl_extract_firecl","description":"Extract data"}]
T["mem"]=[{"name":"read_at_mem_ai","description":"Read note"},{"name":"create_note_mem_ai","description":"Create note"},{"name":"search_mem_ai","description":"Search notes"},{"name":"list_notes_mem_ai","description":"List notes"}]
T["e2b"]=[{"name":"run_code","description":"Execute Python in sandbox"}]
T["beeperbox"]=[{"name":"list_accounts","description":"List accounts"},{"name":"get_chat","description":"Get chat"},{"name":"read_chat","description":"Read chat"},{"name":"archive_chat","description":"Archive chat"},{"name":"list_inbox","description":"List inbox"},{"name":"list_unread","description":"List unread"},{"name":"send_message","description":"Send message"},{"name":"search_messages","description":"Search messages"},{"name":"react_to_message","description":"React to message"},{"name":"poll_messages","description":"Poll messages"},{"name":"note_to_self","description":"Note to self"},{"name":"download_asset","description":"Download asset"}]
T["context7"]=[{"name":"query_docs_context7","description":"Query docs"},{"name":"resolve_library_id_context7","description":"Resolve library ID"}]
T["cloudflare"]=[{"name":"cf_api_request","description":"Cloudflare API requests"}]
T["onepassword"]=[{"name":"item_get","description":"Get item"},{"name":"item_list","description":"List items"},{"name":"item_lookup","description":"Lookup item"},{"name":"note_create","description":"Create note"},{"name":"password_create","description":"Create password"},{"name":"password_generate","description":"Generate password"},{"name":"password_read","description":"Read password"},{"name":"vault_list","description":"List vaults"},{"name":"password_update","description":"Update password"}]
T["tfy-admin"]=[{"name":"tfy_list_servers","description":"List MCP servers"},{"name":"tfy_register","description":"Register MCP server"},{"name":"tfy_delete","description":"Delete MCP server"}]
T["lark-im"]=[{"name":"lark_send_message","description":"Send message"},{"name":"lark_list_chats","description":"List chats"}]
T["lark-base"]=[{"name":"lark_base_search_records","description":"Search records"},{"name":"lark_base_create_record","description":"Create record"},{"name":"lark_base_list_tables","description":"List tables"}]
T["lark-cal"]=[{"name":"lark_calendar_list_events","description":"List events"},{"name":"lark_calendar_create_event","description":"Create event"}]
T["lark-docs"]=[{"name":"lark_docx_create","description":"Create doc"},{"name":"lark_docx_get_content","description":"Get content"}]
T["lark-drive"]=[{"name":"lark_drive_list_files","description":"List files"}]
T["lark-sheets"]=[{"name":"lark_sheets_read","description":"Read spreadsheet"}]
T["lark-wiki"]=[{"name":"lark_wiki_search","description":"Search wiki"}]
T["lark-tasks"]=[{"name":"lark_task_create","description":"Create task"},{"name":"lark_task_list","description":"List tasks"}]
T["lark-contacts"]=[{"name":"lark_contact_list_users","description":"List users"}]
T["lark-mail-admin"]=[{"name":"lark_mail_list_groups","description":"List groups"}]
T["lark-mail-user"]=[{"name":"lark_mail_list_messages","description":"List messages"},{"name":"lark_mail_send","description":"Send email"}]
NAMES=list(T.keys())

@mcp.tool(description="List all available tool groups with counts")
def list_all_groups():
    return [{"name":k,"count":len(v)} for k,v in T.items()]

@mcp.tool(description="Get complete list of Tavily web search tools")
def list_tavily_tools():return T["tavily"]
@mcp.tool(description="Get complete list of Hindsight memory management tools")
def list_hindsight_tools():return T["hindsight"]
@mcp.tool(description="Get complete list of VoiceNotes tools")
def list_voicenotes_tools():return T["voicenotes"]
@mcp.tool(description="Get complete list of Composio integration tools")
def list_composio_tools():return T["composio"]
@mcp.tool(description="Get complete list of Browserbase cloud browser tools")
def list_browserbase_tools():return T["browserbase"]
@mcp.tool(description="Get complete list of Hyperbrowser web browsing tools")
def list_hyperbrowser_tools():return T["hyperbrowser"]
@mcp.tool(description="Get complete list of Bright Data web scraping tools")
def list_brightdata_tools():return T["brightdata"]
@mcp.tool(description="Get complete list of Exa AI search tools")
def list_exa_tools():return T["exa"]
@mcp.tool(description="Get complete list of Playwright browser automation tools")
def list_playwright_tools():return T["playwright"]
@mcp.tool(description="Get complete list of Firecrawl web scraping tools")
def list_firecrawl_tools():return T["firecrawl"]
@mcp.tool(description="Get complete list of Mem knowledge tools")
def list_mem_tools():return T["mem"]
@mcp.tool(description="Get complete list of E2B code execution tools")
def list_e2b_tools():return T["e2b"]
@mcp.tool(description="Get complete list of Beeperbox messaging tools")
def list_beeperbox_tools():return T["beeperbox"]
@mcp.tool(description="Get complete list of Context7 documentation tools")
def list_context7_tools():return T["context7"]
@mcp.tool(description="Get complete list of Cloudflare Gateway API tools")
def list_cloudflare_tools():return T["cloudflare"]
@mcp.tool(description="Get complete list of 1Password secrets management tools")
def list_onepassword_tools():return T["onepassword"]
@mcp.tool(description="Get complete list of TFY MCP Admin tools")
def list_tfy_admin_tools():return T["tfy-admin"]
@mcp.tool(description="Get complete list of Lark IM messaging tools")
def list_lark_im_tools():return T["lark-im"]
@mcp.tool(description="Get complete list of Lark Base database tools")
def list_lark_base_tools():return T["lark-base"]
@mcp.tool(description="Get complete list of Lark Calendar tools")
def list_lark_calendar_tools():return T["lark-cal"]
@mcp.tool(description="Get complete list of Lark Docs tools")
def list_lark_docs_tools():return T["lark-docs"]
@mcp.tool(description="Get complete list of Lark Drive tools")
def list_lark_drive_tools():return T["lark-drive"]
@mcp.tool(description="Get complete list of Lark Sheets tools")
def list_lark_sheets_tools():return T["lark-sheets"]
@mcp.tool(description="Get complete list of Lark Wiki tools")
def list_lark_wiki_tools():return T["lark-wiki"]
@mcp.tool(description="Get complete list of Lark Tasks tools")
def list_lark_tasks_tools():return T["lark-tasks"]
@mcp.tool(description="Get complete list of Lark Contacts tools")
def list_lark_contacts_tools():return T["lark-contacts"]
@mcp.tool(description="Get complete list of Lark Mail Admin tools")
def list_lark_mail_admin_tools():return T["lark-mail-admin"]
@mcp.tool(description="Get complete list of Lark Mail User tools")
def list_lark_mail_user_tools():return T["lark-mail-user"]

if __name__=="__main__":
    import sys
    t=sys.argv[1] if len(sys.argv)>1 else "streamable-http"
    mcp.run(transport="stdio" if t=="stdio" else "streamable-http",host="0.0.0.0",port=8000)
