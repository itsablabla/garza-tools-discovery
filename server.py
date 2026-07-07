"""
garza-tools-discovery MCP Server

Discovery layer for the garza-tools virtual MCP server.
Exposes one discovery tool per backing MCP server group.
"""
from fastmcp import FastMCP
mcp = FastMCP(name="garza-tools-discovery",instructions="Discovery layer for garza-tools. Query a discovery tool to get available tools.")
TAVILY=[{"name":"tavily_search_tavilyl","description":"Web search via Tavily"},{"name":"tavily_extract_tavilyl","description":"Extract content from URLs"},{"name":"tavily_crawl_tavilyl","description":"Crawl a website"},{"name":"tavily_map_tavilyl","description":"Map URL structure"},{"name":"tavily_research_tavilyl","description":"Deep multi-step research"}]
HINDSIGHT=[{"name":"retain_hindsp7","description":"Save a memory"},{"name":"sync_retain_hindsp7","description":"Sync save memory"},{"name":"recall_hindsp7","description":"Retrieve memories"},{"name":"reflect_hindsp7","description":"Generate insights"},{"name":"list_banks_hindsp7","description":"List memory banks"},{"name":"create_bank_hindsp7","description":"Create memory bank"},{"name":"get_bank_hindsp7","description":"Get bank details"},{"name":"get_bank_stats_hindsp7","description":"Bank statistics"},{"name":"update_bank_hindsp7","description":"Update bank settings"},{"name":"delete_bank_hindsp7","description":"Delete bank"},{"name":"clear_memories_hindsp7","description":"Clear memories"},{"name":"list_mental_models_hindsp7","description":"List mental models"},{"name":"get_mental_model_hindsp7","description":"Get mental model"},{"name":"create_mental_model_hindsp7","description":"Create mental model"},{"name":"update_mental_model_hindsp7","description":"Update mental model"},{"name":"delete_mental_model_hindsp7","description":"Delete mental model"},{"name":"refresh_mental_model_hindsp7","description":"Refresh mental model"},{"name":"list_directives_hindsp7","description":"List directives"},{"name":"create_directive_hindsp7","description":"Create directive"},{"name":"delete_directive_hindsp7","description":"Delete directive"},{"name":"list_memories_hindsp7","description":"List memories"},{"name":"get_memory_hindsp7","description":"Get memory"},{"name":"delete_memory_hindsp7","description":"Delete memory"},{"name":"list_documents_hindsp7","description":"List documents"},{"name":"get_document_hindsp7","description":"Get document"},{"name":"delete_document_hindsp7","description":"Delete document"},{"name":"list_operations_hindsp7","description":"List operations"},{"name":"get_operation_hindsp7","description":"Get operation"},{"name":"cancel_operation_hindsp7","description":"Cancel operation"},{"name":"list_tags_hindsp7","description":"List tags"}]
VOICENOTES=[{"name":"search_notes_voicefx","description":"Search voice notes"},{"name":"list_notes_voicefx","description":"List voice notes"},{"name":"get_note_voicefx","description":"Get voice note"},{"name":"create_note_voicefx","description":"Create voice note"}]
COMPOSIO=[{"name":"COMPOSIO_MANAGE_CONNECTIONS_compohq","description":"Manage OAuth connections"},{"name":"COMPOSIO_MULTI_EXECUTE_TOOL_compohq","description":"Execute actions across services"},{"name":"COMPOSIO_REMOTE_BASH_TOOL_compohq","description":"Remote bash execution"},{"name":"COMPOSIO_REMOTE_WORKBENCH_compohq","description":"Remote workbench"},{"name":"COMPOSIO_SEARCH_TOOLS_compohq","description":"Search integrations"},{"name":"COMPOSIO_WAIT_FOR_CONNECTIONS_compohq","description":"Wait for OAuth"},{"name":"COMPOSIO_GET_TOOL_SCHEMAS_compohq","description":"Get tool schemas"}]
BROWSERBASE=[{"name":"browserbase_automation","description":"Cloud browser automation"}]
HYPERBROWSER=[{"name":"browser_use_agent","description":"AI web browsing agent"},{"name":"claude_computer_use_agent","description":"Claude computer use"},{"name":"crawl_webpages","description":"Crawl webpages"},{"name":"create_profile","description":"Create browser profile"},{"name":"delete_profile","description":"Delete browser profile"}]
BRIGHTDATA=[{"name":"brightdata_scraping","description":"Web scraping"}]
EXA=[{"name":"exa_web_search","description":"AI web search"},{"name":"exa_get_contents","description":"Extract URL content"}]
PLAYWRIGHT=[{"name":"browser_click","description":"Click element"},{"name":"browser_close","description":"Close browser"},{"name":"browser_console_messages","description":"Console messages"},{"name":"browser_drag","description":"Drag element"},{"name":"browser_drop","description":"Drop element"},{"name":"browser_evaluate","description":"Execute JavaScript"},{"name":"browser_fill","description":"Fill input"},{"name":"browser_hover","description":"Hover element"},{"name":"browser_navigate","description":"Navigate URL"},{"name":"browser_screenshot","description":"Take screenshot"},{"name":"browser_select","description":"Select option"}]
FIRECRAWL=[{"name":"firecrawl_scrape_firecl","description":"Scrape URL"},{"name":"firecrawl_crawl_firecl","description":"Crawl website"},{"name":"firecrawl_search_firecl","description":"Web search"},{"name":"firecrawl_map_firecl","description":"Map URLs"},{"name":"firecrawl_extract_firecl","description":"Extract data"}]
MEM=[{"name":"read_at_mem_ai","description":"Read note"},{"name":"create_note_mem_ai","description":"Create note"},{"name":"search_mem_ai","description":"Search notes"},{"name":"list_notes_mem_ai","description":"List notes"}]
E2B=[{"name":"run_code","description":"Execute Python"}]
BEEPERBOX=[{"name":"list_accounts","description":"List accounts"},{"name":"get_chat","description":"Get chat"},{"name":"read_chat","description":"Read chat"},{"name":"archive_chat","description":"Archive chat"},{"name":"list_inbox","description":"List inbox"},{"name":"list_unread","description":"List unread"},{"name":"send_message","description":"Send message"},{"name":"search_messages","description":"Search messages"},{"name":"react_to_message","description":"React to message"},{"name":"poll_messages","description":"Poll messages"},{"name":"note_to_self","description":"Note to self"},{"name":"download_asset","description":"Download asset"}]
CONTEXT7=[{"name":"query_docs_context7","description":"Query docs"},{"name":"resolve_library_id_context7","description":"Resolve library ID"}]
CLOUDFLARE=[{"name":"cf_api_request","description":"Cloudflare API"}]
ONEPASSWORD=[{"name":"item_get","description":"Get item"},{"name":"item_list","description":"List items"},{"name":"item_lookup","description":"Lookup item"},{"name":"note_create","description":"Create note"},{"name":"password_create","description":"Create password"},{"name":"password_generate","description":"Generate password"},{"name":"password_read","description":"Read password"},{"name":"vault_list","description":"List vaults"},{"name":"password_update","description":"Update password"}]
TFY_ADMIN=[{"name":"tfy_list_servers","description":"List MCP servers"},{"name":"tfy_register","description":"Register MCP server"},{"name":"tfy_delete","description":"Delete MCP server"}]
LARK_IM=[{"name":"lark_send_message","description":"Send message"},{"name":"lark_list_chats","description":"List chats"}]
LARK_BASE=[{"name":"lark_base_search_records","description":"Search records"},{"name":"lark_base_create_record","description":"Create record"},{"name":"lark_base_list_tables","description":"List tables"}]
LARK_CAL=[{"name":"lark_calendar_list_events","description":"List events"},{"name":"lark_calendar_create_event","description":"Create event"}]
LARK_DOCS=[{"name":"lark_docx_create","description":"Create doc"},{"name":"lark_docx_get_content","description":"Get content"}]
LARK_DRIVE=[{"name":"lark_drive_list_files","description":"List files"}]
LARK_SHEETS=[{"name":"lark_sheets_read","description":"Read spreadsheet"}]
LARK_WIKI=[{"name":"lark_wiki_search","description":"Search wiki"}]
LARK_TASKS=[{"name":"lark_task_create","description":"Create task"},{"name":"lark_task_list","description":"List tasks"}]
LARK_CONTACTS=[{"name":"lark_contact_list_users","description":"List users"}]
LARK_MAIL_ADMIN=[{"name":"lark_mail_list_groups","description":"List groups"}]
LARK_MAIL_USER=[{"name":"lark_mail_list_messages","description":"List messages"},{"name":"lark_mail_send","description":"Send email"}]
ALL={r"tavily":TAVILY,r"hindsight":HINDSIGHT,r"voicenotes":VOICENOTES,r"composio":COMPOSIO,r"browserbase":BROWSERBASE,r"hyperbrowser":HYPERBROWSER,r"brightdata":BRIGHTDATA,r"exa":EXA,r"playwright":PLAYWRIGHT,r"firecrawl":FIRECRAWL,r"mem":MEM,r"e2b":E2B,r"beeperbox":BEEPERBOX,r"context7":CONTEXT7,r"cloudflare":CLOUDFLARE,r"onepassword":ONEPASSWORD,r"tfy-admin":TFY_ADMIN,r"lark-im":LARK_IM,r"lark-base":LARK_BASE,r"lark-cal":LARK_CAL,r"lark-docs":LARK_DOCS,r"lark-drive":LARK_DRIVE,r"lark-sheets":LARK_SHEETS,r"lark-wiki":LARK_WIKI,r"lark-tasks":LARK_TASKS,r"lark-contacts":LARK_CONTACTS,r"lark-mail-admin":LARK_MAIL_ADMIN,r"lark-mail-user":LARK_MAIL_USER}
@mcp.tool(description="List all tool groups by server")
def list_all_groups():
    return [{"name":k,"tools":len(v)} for k,v in ALL.items()]
for name,tools in ALL.items():
    @mcp.tool(description=f"Get tools for {name}")
    def make_fn(t=tools): return t
    locals()[f"list_{name}_tools"] = make_fn
if __name__=="__main__":
    import sys
    t=sys.argv[1] if len(sys.argv)>1 else "streamable-http"
    mcp.run(transport="stdio" if t=="stdio" else "streamable-http",host="0.0.0.0",port=8000 if t!="stdio" else None)
