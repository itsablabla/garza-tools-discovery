"""garza-tools-discovery: MCP discovery layer for all connected MCP servers."""

from fastmcp import FastMCP

mcp = FastMCP("garza-tools-discovery")

# ─────────────────────────────────────────────
# Search & Research
# ─────────────────────────────────────────────

@mcp.tool()
def list_tavily_tools() -> dict:
    """List all tools available in the Tavily MCP server (AI-optimised web search for RAG agents)."""
    return {
        "server": "tavily",
        "type": "mcp-server/remote",
        "description": "AI-optimised search for RAG agents",
        "tools": [
            "tavily_search",
            "tavily_extract",
            "tavily_crawl",
            "tavily_map",
        ],
    }


@mcp.tool()
def list_context7_tools() -> dict:
    """List all tools available in the Context7 MCP server (up-to-date library docs for LLMs)."""
    return {
        "server": "context7",
        "type": "mcp-server/remote",
        "description": "Up-to-date library docs for LLMs and AI code editors",
        "tools": [
            "resolve-library-id",
            "get-library-docs",
        ],
    }


@mcp.tool()
def list_firecrawl_tools() -> dict:
    """List all tools available in the Firecrawl MCP server (web scraping and crawling platform)."""
    return {
        "server": "firecrawl",
        "type": "mcp-server/remote",
        "description": "Firecrawl web scraping platform",
        "tools": [
            "firecrawl_scrape",
            "firecrawl_map",
            "firecrawl_crawl",
            "firecrawl_check_crawl_status",
            "firecrawl_cancel_crawl",
            "firecrawl_search",
            "firecrawl_extract",
            "firecrawl_deep_research",
            "firecrawl_generate_llmstxt",
        ],
    }


# ─────────────────────────────────────────────
# Memory & Notes
# ─────────────────────────────────────────────

@mcp.tool()
def list_hindsight_tools() -> dict:
    """List all tools available in the Hindsight MCP server (memory and recall for AI agents)."""
    return {
        "server": "hindsight",
        "type": "mcp-server/remote",
        "description": "Memory and recall for AI agents",
        "tools": [
            "hindsight_remember",
            "hindsight_recall",
            "hindsight_forget",
            "hindsight_list",
        ],
    }


@mcp.tool()
def list_voicenotes_tools() -> dict:
    """List all tools available in the VoiceNotes MCP server (voice note management)."""
    return {
        "server": "voicenotes",
        "type": "mcp-server/remote",
        "description": "Voice note management",
        "tools": [
            "list_recordings",
            "get_recording",
            "get_transcript",
            "create_note",
            "search_notes",
        ],
    }


@mcp.tool()
def list_mem_tools() -> dict:
    """List all tools available in the Mem MCP server (AI notebook for knowledge management)."""
    return {
        "server": "mem",
        "type": "mcp-server/remote",
        "description": "AI notebook for everything on your mind",
        "tools": [
            "search",
            "create_mem",
            "update_mem",
            "delete_mem",
            "list_mems",
        ],
    }


# ─────────────────────────────────────────────
# Code Execution & Integrations
# ─────────────────────────────────────────────

@mcp.tool()
def list_e2b_tools() -> dict:
    """List all tools available in the E2B MCP server (secure cloud code execution sandbox)."""
    return {
        "server": "e2b",
        "type": "mcp-server/stdio",
        "description": "E2B secure code execution sandbox",
        "tools": [
            "run_code",
            "create_sandbox",
            "kill_sandbox",
            "list_sandboxes",
            "upload_file",
            "download_file",
        ],
    }


@mcp.tool()
def list_composio_tools() -> dict:
    """List all tools available in the Composio MCP server (500+ connected app integrations)."""
    return {
        "server": "composio-mcp",
        "type": "mcp-server/remote",
        "description": "Composio - 500+ connected apps via MCP",
        "tools": [
            "composio_execute_action",
            "composio_get_actions",
            "composio_search_actions",
            "composio_get_connections",
            "composio_initiate_connection",
        ],
    }


@mcp.tool()
def list_onepassword_tools() -> dict:
    """List all tools available in the 1Password MCP server (vault access and credential management)."""
    return {
        "server": "onepassword-cake",
        "type": "mcp-server/stdio",
        "description": "1Password vault access, item management, and password generation",
        "tools": [
            "get_vault",
            "list_vaults",
            "get_item",
            "list_items",
            "create_item",
            "update_item",
            "delete_item",
            "generate_password",
        ],
    }


# ─────────────────────────────────────────────
# Messaging & Communications
# ─────────────────────────────────────────────

@mcp.tool()
def list_beeperbox_tools() -> dict:
    """List all tools available in the Beeperbox MCP server (multi-account messaging via Beeper)."""
    return {
        "server": "beeperbox",
        "type": "mcp-server/remote",
        "description": "Multi-account messaging hub (iMessage, WhatsApp, Telegram, etc.) via Beeper",
        "tools": [
            "list_accounts",
            "list_inbox",
            "list_unread",
            "get_chat",
            "read_chat",
            "search_messages",
            "send_message",
            "note_to_self",
            "react_to_message",
            "archive_chat",
            "poll_messages",
            "download_asset",
        ],
    }


# ─────────────────────────────────────────────
# Platform & Infrastructure
# ─────────────────────────────────────────────

@mcp.tool()
def list_tfy_mcp_admin_tools() -> dict:
    """List all tools available in the TrueFoundry MCP Admin server (manage MCP servers via agents)."""
    return {
        "server": "tfy-mcp-admin",
        "type": "mcp-server/remote",
        "description": "TrueFoundry MCP Admin - manage MCP servers via AI agents",
        "tools": [
            "list_mcp_servers",
            "get_mcp_server",
            "create_mcp_server",
            "update_mcp_server",
            "delete_mcp_server",
            "validate_manifest",
            "apply_manifest",
        ],
    }


@mcp.tool()
def list_cloudflare_gateway_tools() -> dict:
    """List all tools available in the Cloudflare AI Gateway MCP server (LLM gateway analytics)."""
    return {
        "server": "cloudflare-gateway",
        "type": "mcp-server/remote",
        "description": "Cloudflare AI Gateway - LLM gateway and analytics",
        "tools": [
            "list_gateways",
            "get_gateway",
            "list_logs",
            "get_log",
            "list_datasets",
            "get_dataset_entry",
        ],
    }


# ─────────────────────────────────────────────
# Lark Suite
# ─────────────────────────────────────────────


@mcp.tool()
def list_lark_im_tools() -> dict:
    """List all tools available in the lark-im MCP server (Lark IM - messaging, chats, threads, reactions, and feed cards)."""
    return {
        "server": "lark-im",
        "type": "mcp-server/stdio",
        "description": "Lark IM - messaging, chats, threads, reactions, and feed cards",
        "tool_count": 66,
        "tools": [
            "im.v1.batchMessage.delete",
            "im.v1.batchMessage.getProgress",
            "im.v1.batchMessage.readUser",
            "im.v1.chatAnnouncement.get",
            "im.v1.chatAnnouncement.patch",
            "im.v1.chat.create",
            "im.v1.chat.delete",
            "im.v1.chat.get",
            "im.v1.chat.link",
            "im.v1.chat.list",
            "im.v1.chatManagers.addManagers",
            "im.v1.chatManagers.deleteManagers",
            "im.v1.chatMembers.create",
            "im.v1.chatMembers.delete",
            "im.v1.chatMembers.get",
            "im.v1.chatMembers.isInChat",
            "im.v1.chatMembers.meJoin",
            "im.v1.chatMenuItem.patch",
            "im.v1.chatMenuTree.create",
            "im.v1.chatMenuTree.delete",
            "im.v1.chatMenuTree.get",
            "im.v1.chatMenuTree.sort",
            "im.v1.chatModeration.get",
            "im.v1.chatModeration.update",
            "im.v1.chat.search",
            "im.v1.chatTab.create",
            "im.v1.chatTab.deleteTabs",
            "im.v1.chatTab.listTabs",
            "im.v1.chatTab.sortTabs",
            "im.v1.chatTab.updateTabs",
            "im.v1.chatTopNotice.deleteTopNotice",
            "im.v1.chatTopNotice.putTopNotice",
            "im.v1.chat.update",
            "im.v1.message.create",
            "im.v1.message.delete",
            "im.v1.message.forward",
            "im.v1.message.get",
            "im.v1.message.list",
            "im.v1.message.mergeForward",
            "im.v1.message.patch",
            "im.v1.message.pushFollowUp",
            "im.v1.messageReaction.create",
            "im.v1.messageReaction.delete",
            "im.v1.messageReaction.list",
            "im.v1.message.readUsers",
            "im.v1.message.reply",
            "im.v1.message.update",
            "im.v1.message.urgentApp",
            "im.v1.message.urgentPhone",
            "im.v1.message.urgentSms",
            "im.v1.pin.create",
            "im.v1.pin.delete",
            "im.v1.pin.list",
            "im.v1.thread.forward",
            "im.v2.appFeedCardBatch.delete",
            "im.v2.appFeedCardBatch.update",
            "im.v2.appFeedCard.create",
            "im.v2.bizEntityTagRelation.create",
            "im.v2.bizEntityTagRelation.get",
            "im.v2.bizEntityTagRelation.update",
            "im.v2.chatButton.update",
            "im.v2.feedCard.botTimeSentive",
            "im.v2.feedCard.patch",
            "im.v2.tag.create",
            "im.v2.tag.patch",
            "im.v2.urlPreview.batchUpdate"
],
    }


@mcp.tool()
def list_lark_drive_tools() -> dict:
    """List all tools available in the lark-drive MCP server (Lark Drive - file management, comments, permissions, and version control)."""
    return {
        "server": "lark-drive",
        "type": "mcp-server/stdio",
        "description": "Lark Drive - file management, comments, permissions, and version control",
        "tool_count": 52,
        "tools": [
            "drive.v1.exportTask.create",
            "drive.v1.exportTask.get",
            "drive.v1.fileComment.batchQuery",
            "drive.v1.fileComment.create",
            "drive.v1.fileComment.get",
            "drive.v1.fileComment.list",
            "drive.v1.fileComment.patch",
            "drive.v1.fileCommentReply.delete",
            "drive.v1.fileCommentReply.list",
            "drive.v1.fileCommentReply.update",
            "drive.v1.file.copy",
            "drive.v1.file.createFolder",
            "drive.v1.file.createShortcut",
            "drive.v1.file.delete",
            "drive.v1.file.deleteSubscribe",
            "drive.v1.file.getSubscribe",
            "drive.v1.file.list",
            "drive.v1.file.move",
            "drive.v1.fileStatistics.get",
            "drive.v1.file.subscribe",
            "drive.v1.fileSubscription.create",
            "drive.v1.fileSubscription.get",
            "drive.v1.fileSubscription.patch",
            "drive.v1.file.taskCheck",
            "drive.v1.file.uploadFinish",
            "drive.v1.file.uploadPrepare",
            "drive.v1.fileVersion.create",
            "drive.v1.fileVersion.delete",
            "drive.v1.fileVersion.get",
            "drive.v1.fileVersion.list",
            "drive.v1.fileViewRecord.list",
            "drive.v1.importTask.create",
            "drive.v1.importTask.get",
            "drive.v1.media.batchGetTmpDownloadUrl",
            "drive.v1.media.uploadFinish",
            "drive.v1.media.uploadPrepare",
            "drive.v1.meta.batchQuery",
            "drive.v1.permissionMember.auth",
            "drive.v1.permissionMember.batchCreate",
            "drive.v1.permissionMember.create",
            "drive.v1.permissionMember.delete",
            "drive.v1.permissionMember.list",
            "drive.v1.permissionMember.transferOwner",
            "drive.v1.permissionMember.update",
            "drive.v1.permissionPublic.get",
            "drive.v1.permissionPublicPassword.create",
            "drive.v1.permissionPublicPassword.delete",
            "drive.v1.permissionPublicPassword.update",
            "drive.v1.permissionPublic.patch",
            "drive.v2.fileLike.list",
            "drive.v2.permissionPublic.get",
            "drive.v2.permissionPublic.patch"
],
    }


@mcp.tool()
def list_lark_docx_tools() -> dict:
    """List all tools available in the lark-docx MCP server (Lark Docs - document creation, block editing, and content management)."""
    return {
        "server": "lark-docx",
        "type": "mcp-server/stdio",
        "description": "Lark Docs - document creation, block editing, and content management",
        "tool_count": 20,
        "tools": [
            "docs.v1.content.get",
            "docx.v1.chatAnnouncementBlock.batchUpdate",
            "docx.v1.chatAnnouncementBlockChildren.batchDelete",
            "docx.v1.chatAnnouncementBlockChildren.create",
            "docx.v1.chatAnnouncementBlockChildren.get",
            "docx.v1.chatAnnouncementBlock.get",
            "docx.v1.chatAnnouncementBlock.list",
            "docx.v1.chatAnnouncement.get",
            "docx.v1.documentBlock.batchUpdate",
            "docx.v1.documentBlockChildren.batchDelete",
            "docx.v1.documentBlockChildren.create",
            "docx.v1.documentBlockChildren.get",
            "docx.v1.documentBlockDescendant.create",
            "docx.v1.documentBlock.get",
            "docx.v1.documentBlock.list",
            "docx.v1.documentBlock.patch",
            "docx.v1.document.convert",
            "docx.v1.document.create",
            "docx.v1.document.get",
            "docx.v1.document.rawContent"
],
    }


@mcp.tool()
def list_lark_sheets_tools() -> dict:
    """List all tools available in the lark-sheets-core MCP server (Lark Sheets - spreadsheet creation, filter views, and sheet management)."""
    return {
        "server": "lark-sheets-core",
        "type": "mcp-server/stdio",
        "description": "Lark Sheets - spreadsheet creation, filter views, and sheet management",
        "tool_count": 27,
        "tools": [
            "sheets.v3.spreadsheet.create",
            "sheets.v3.spreadsheet.get",
            "sheets.v3.spreadsheet.patch",
            "sheets.v3.spreadsheetSheetFilterViewCondition.create",
            "sheets.v3.spreadsheetSheetFilterViewCondition.delete",
            "sheets.v3.spreadsheetSheetFilterViewCondition.get",
            "sheets.v3.spreadsheetSheetFilterViewCondition.query",
            "sheets.v3.spreadsheetSheetFilterViewCondition.update",
            "sheets.v3.spreadsheetSheetFilterView.create",
            "sheets.v3.spreadsheetSheetFilterView.delete",
            "sheets.v3.spreadsheetSheetFilterView.get",
            "sheets.v3.spreadsheetSheetFilterView.patch",
            "sheets.v3.spreadsheetSheetFilterView.query",
            "sheets.v3.spreadsheetSheetFilter.create",
            "sheets.v3.spreadsheetSheetFilter.delete",
            "sheets.v3.spreadsheetSheetFilter.get",
            "sheets.v3.spreadsheetSheetFilter.update",
            "sheets.v3.spreadsheetSheet.find",
            "sheets.v3.spreadsheetSheetFloatImage.create",
            "sheets.v3.spreadsheetSheetFloatImage.delete",
            "sheets.v3.spreadsheetSheetFloatImage.get",
            "sheets.v3.spreadsheetSheetFloatImage.patch",
            "sheets.v3.spreadsheetSheetFloatImage.query",
            "sheets.v3.spreadsheetSheet.get",
            "sheets.v3.spreadsheetSheet.moveDimension",
            "sheets.v3.spreadsheetSheet.query",
            "sheets.v3.spreadsheetSheet.replace"
],
    }


@mcp.tool()
def list_lark_wiki_tools() -> dict:
    """List all tools available in the lark-wiki MCP server (Lark Wiki - knowledge base spaces, nodes, and page management)."""
    return {
        "server": "lark-wiki",
        "type": "mcp-server/stdio",
        "description": "Lark Wiki - knowledge base spaces, nodes, and page management",
        "tool_count": 16,
        "tools": [
            "wiki.v1.node.search",
            "wiki.v2.space.create",
            "wiki.v2.space.get",
            "wiki.v2.space.getNode",
            "wiki.v2.space.list",
            "wiki.v2.spaceMember.create",
            "wiki.v2.spaceMember.delete",
            "wiki.v2.spaceMember.list",
            "wiki.v2.spaceNode.copy",
            "wiki.v2.spaceNode.create",
            "wiki.v2.spaceNode.list",
            "wiki.v2.spaceNode.move",
            "wiki.v2.spaceNode.moveDocsToWiki",
            "wiki.v2.spaceNode.updateTitle",
            "wiki.v2.spaceSetting.update",
            "wiki.v2.task.get"
],
    }


@mcp.tool()
def list_lark_calendar_tools() -> dict:
    """List all tools available in the lark-calendar MCP server (Lark Calendar - event management, ACLs, and free/busy scheduling)."""
    return {
        "server": "lark-calendar",
        "type": "mcp-server/stdio",
        "description": "Lark Calendar - event management, ACLs, and free/busy scheduling",
        "tool_count": 41,
        "tools": [
            "calendar.v4.calendarAcl.create",
            "calendar.v4.calendarAcl.delete",
            "calendar.v4.calendarAcl.list",
            "calendar.v4.calendarAcl.subscription",
            "calendar.v4.calendarAcl.unsubscription",
            "calendar.v4.calendar.create",
            "calendar.v4.calendar.delete",
            "calendar.v4.calendarEventAttendee.batchDelete",
            "calendar.v4.calendarEventAttendeeChatMember.list",
            "calendar.v4.calendarEventAttendee.create",
            "calendar.v4.calendarEventAttendee.list",
            "calendar.v4.calendarEvent.create",
            "calendar.v4.calendarEvent.delete",
            "calendar.v4.calendarEvent.get",
            "calendar.v4.calendarEvent.instanceView",
            "calendar.v4.calendarEvent.instances",
            "calendar.v4.calendarEvent.list",
            "calendar.v4.calendarEventMeetingChat.create",
            "calendar.v4.calendarEventMeetingChat.delete",
            "calendar.v4.calendarEventMeetingMinute.create",
            "calendar.v4.calendarEvent.patch",
            "calendar.v4.calendarEvent.reply",
            "calendar.v4.calendarEvent.search",
            "calendar.v4.calendarEvent.subscription",
            "calendar.v4.calendarEvent.unsubscription",
            "calendar.v4.calendar.get",
            "calendar.v4.calendar.list",
            "calendar.v4.calendar.patch",
            "calendar.v4.calendar.primary",
            "calendar.v4.calendar.search",
            "calendar.v4.calendar.subscribe",
            "calendar.v4.calendar.subscription",
            "calendar.v4.calendar.unsubscribe",
            "calendar.v4.calendar.unsubscription",
            "calendar.v4.exchangeBinding.create",
            "calendar.v4.exchangeBinding.delete",
            "calendar.v4.exchangeBinding.get",
            "calendar.v4.freebusy.list",
            "calendar.v4.setting.generateCaldavConf",
            "calendar.v4.timeoffEvent.create",
            "calendar.v4.timeoffEvent.delete"
],
    }


@mcp.tool()
def list_lark_tasks_tools() -> dict:
    """List all tools available in the lark-tasks MCP server (Lark Tasks - task and tasklist management with comments and custom fields)."""
    return {
        "server": "lark-tasks",
        "type": "mcp-server/stdio",
        "description": "Lark Tasks - task and tasklist management with comments and custom fields",
        "tool_count": 74,
        "tools": [
            "task.v1.task.batchDeleteCollaborator",
            "task.v1.task.batchDeleteFollower",
            "task.v1.taskCollaborator.create",
            "task.v1.taskCollaborator.delete",
            "task.v1.taskCollaborator.list",
            "task.v1.taskComment.create",
            "task.v1.taskComment.delete",
            "task.v1.taskComment.get",
            "task.v1.taskComment.list",
            "task.v1.taskComment.update",
            "task.v1.task.complete",
            "task.v1.task.create",
            "task.v1.task.delete",
            "task.v1.taskFollower.create",
            "task.v1.taskFollower.delete",
            "task.v1.taskFollower.list",
            "task.v1.task.get",
            "task.v1.task.list",
            "task.v1.task.patch",
            "task.v1.taskReminder.create",
            "task.v1.taskReminder.delete",
            "task.v1.taskReminder.list",
            "task.v1.task.uncomplete",
            "task.v2.attachment.delete",
            "task.v2.attachment.get",
            "task.v2.attachment.list",
            "task.v2.comment.create",
            "task.v2.comment.delete",
            "task.v2.comment.get",
            "task.v2.comment.list",
            "task.v2.comment.patch",
            "task.v2.customField.add",
            "task.v2.customField.create",
            "task.v2.customField.get",
            "task.v2.customField.list",
            "task.v2.customFieldOption.create",
            "task.v2.customFieldOption.patch",
            "task.v2.customField.patch",
            "task.v2.customField.remove",
            "task.v2.section.create",
            "task.v2.section.delete",
            "task.v2.section.get",
            "task.v2.section.list",
            "task.v2.section.patch",
            "task.v2.section.tasks",
            "task.v2.task.addDependencies",
            "task.v2.task.addMembers",
            "task.v2.task.addReminders",
            "task.v2.task.addTasklist",
            "task.v2.task.create",
            "task.v2.task.delete",
            "task.v2.task.get",
            "task.v2.task.list",
            "task.v2.task.patch",
            "task.v2.task.removeDependencies",
            "task.v2.task.removeMembers",
            "task.v2.task.removeReminders",
            "task.v2.task.removeTasklist",
            "task.v2.taskSubtask.create",
            "task.v2.taskSubtask.list",
            "task.v2.task.tasklists",
            "task.v2.tasklistActivitySubscription.create",
            "task.v2.tasklistActivitySubscription.delete",
            "task.v2.tasklistActivitySubscription.get",
            "task.v2.tasklistActivitySubscription.list",
            "task.v2.tasklistActivitySubscription.patch",
            "task.v2.tasklist.addMembers",
            "task.v2.tasklist.create",
            "task.v2.tasklist.delete",
            "task.v2.tasklist.get",
            "task.v2.tasklist.list",
            "task.v2.tasklist.patch",
            "task.v2.tasklist.removeMembers",
            "task.v2.tasklist.tasks"
],
    }


@mcp.tool()
def list_lark_base_tools() -> dict:
    """List all tools available in the lark-base MCP server (Lark Base (Bitable) - database app, tables, records, fields, and views)."""
    return {
        "server": "lark-base",
        "type": "mcp-server/stdio",
        "description": "Lark Base (Bitable) - database app, tables, records, fields, and views",
        "tool_count": 49,
        "tools": [
            "base.v2.appRole.create",
            "base.v2.appRole.list",
            "base.v2.appRole.update",
            "bitable.v1.app.copy",
            "bitable.v1.app.create",
            "bitable.v1.appDashboard.copy",
            "bitable.v1.appDashboard.list",
            "bitable.v1.app.get",
            "bitable.v1.appRole.create",
            "bitable.v1.appRole.delete",
            "bitable.v1.appRole.list",
            "bitable.v1.appRoleMember.batchCreate",
            "bitable.v1.appRoleMember.batchDelete",
            "bitable.v1.appRoleMember.create",
            "bitable.v1.appRoleMember.delete",
            "bitable.v1.appRoleMember.list",
            "bitable.v1.appRole.update",
            "bitable.v1.appTable.batchCreate",
            "bitable.v1.appTable.batchDelete",
            "bitable.v1.appTable.create",
            "bitable.v1.appTable.delete",
            "bitable.v1.appTableField.create",
            "bitable.v1.appTableField.delete",
            "bitable.v1.appTableField.list",
            "bitable.v1.appTableField.update",
            "bitable.v1.appTableFormField.list",
            "bitable.v1.appTableFormField.patch",
            "bitable.v1.appTableForm.get",
            "bitable.v1.appTableForm.patch",
            "bitable.v1.appTable.list",
            "bitable.v1.appTable.patch",
            "bitable.v1.appTableRecord.batchCreate",
            "bitable.v1.appTableRecord.batchDelete",
            "bitable.v1.appTableRecord.batchGet",
            "bitable.v1.appTableRecord.batchUpdate",
            "bitable.v1.appTableRecord.create",
            "bitable.v1.appTableRecord.delete",
            "bitable.v1.appTableRecord.get",
            "bitable.v1.appTableRecord.list",
            "bitable.v1.appTableRecord.search",
            "bitable.v1.appTableRecord.update",
            "bitable.v1.appTableView.create",
            "bitable.v1.appTableView.delete",
            "bitable.v1.appTableView.get",
            "bitable.v1.appTableView.list",
            "bitable.v1.appTableView.patch",
            "bitable.v1.app.update",
            "bitable.v1.appWorkflow.list",
            "bitable.v1.appWorkflow.update"
],
    }


@mcp.tool()
def list_lark_contacts_tools() -> dict:
    """List all tools available in the lark-contacts MCP server (Lark Contacts - users, departments, groups, roles, and org structure)."""
    return {
        "server": "lark-contacts",
        "type": "mcp-server/stdio",
        "description": "Lark Contacts - users, departments, groups, roles, and org structure",
        "tool_count": 70,
        "tools": [
            "contact.v3.customAttr.list",
            "contact.v3.department.batch",
            "contact.v3.department.children",
            "contact.v3.department.create",
            "contact.v3.department.delete",
            "contact.v3.department.get",
            "contact.v3.department.list",
            "contact.v3.department.parent",
            "contact.v3.department.patch",
            "contact.v3.department.search",
            "contact.v3.department.unbindDepartmentChat",
            "contact.v3.department.update",
            "contact.v3.department.updateDepartmentId",
            "contact.v3.employeeTypeEnum.create",
            "contact.v3.employeeTypeEnum.delete",
            "contact.v3.employeeTypeEnum.list",
            "contact.v3.employeeTypeEnum.update",
            "contact.v3.functionalRole.create",
            "contact.v3.functionalRole.delete",
            "contact.v3.functionalRoleMember.batchCreate",
            "contact.v3.functionalRoleMember.batchDelete",
            "contact.v3.functionalRoleMember.get",
            "contact.v3.functionalRoleMember.list",
            "contact.v3.functionalRoleMember.scopes",
            "contact.v3.functionalRole.update",
            "contact.v3.group.create",
            "contact.v3.group.delete",
            "contact.v3.group.get",
            "contact.v3.group.memberBelong",
            "contact.v3.groupMember.add",
            "contact.v3.groupMember.batchAdd",
            "contact.v3.groupMember.batchRemove",
            "contact.v3.groupMember.remove",
            "contact.v3.groupMember.simplelist",
            "contact.v3.group.patch",
            "contact.v3.group.simplelist",
            "contact.v3.jobFamily.create",
            "contact.v3.jobFamily.delete",
            "contact.v3.jobFamily.get",
            "contact.v3.jobFamily.list",
            "contact.v3.jobFamily.update",
            "contact.v3.jobLevel.create",
            "contact.v3.jobLevel.delete",
            "contact.v3.jobLevel.get",
            "contact.v3.jobLevel.list",
            "contact.v3.jobLevel.update",
            "contact.v3.jobTitle.get",
            "contact.v3.jobTitle.list",
            "contact.v3.scope.list",
            "contact.v3.unit.bindDepartment",
            "contact.v3.unit.create",
            "contact.v3.unit.delete",
            "contact.v3.unit.get",
            "contact.v3.unit.list",
            "contact.v3.unit.listDepartment",
            "contact.v3.unit.patch",
            "contact.v3.unit.unbindDepartment",
            "contact.v3.user.batch",
            "contact.v3.user.batchGetId",
            "contact.v3.user.create",
            "contact.v3.user.delete",
            "contact.v3.user.findByDepartment",
            "contact.v3.user.get",
            "contact.v3.user.list",
            "contact.v3.user.patch",
            "contact.v3.user.resurrect",
            "contact.v3.user.update",
            "contact.v3.user.updateUserId",
            "contact.v3.workCity.get",
            "contact.v3.workCity.list"
],
    }


@mcp.tool()
def list_lark_mail_admin_tools() -> dict:
    """List all tools available in the lark-mail-admin MCP server (Lark Mail Admin - mail groups, public mailboxes, and permission members)."""
    return {
        "server": "lark-mail-admin",
        "type": "mcp-server/stdio",
        "description": "Lark Mail Admin - mail groups, public mailboxes, and permission members",
        "tool_count": 41,
        "tools": [
            "mail.v1.mailgroupAlias.create",
            "mail.v1.mailgroupAlias.delete",
            "mail.v1.mailgroupAlias.list",
            "mail.v1.mailgroup.create",
            "mail.v1.mailgroup.delete",
            "mail.v1.mailgroup.get",
            "mail.v1.mailgroup.list",
            "mail.v1.mailgroupManager.batchCreate",
            "mail.v1.mailgroupManager.batchDelete",
            "mail.v1.mailgroupManager.list",
            "mail.v1.mailgroupMember.batchCreate",
            "mail.v1.mailgroupMember.batchDelete",
            "mail.v1.mailgroupMember.create",
            "mail.v1.mailgroupMember.delete",
            "mail.v1.mailgroupMember.get",
            "mail.v1.mailgroupMember.list",
            "mail.v1.mailgroup.patch",
            "mail.v1.mailgroupPermissionMember.batchCreate",
            "mail.v1.mailgroupPermissionMember.batchDelete",
            "mail.v1.mailgroupPermissionMember.create",
            "mail.v1.mailgroupPermissionMember.delete",
            "mail.v1.mailgroupPermissionMember.get",
            "mail.v1.mailgroupPermissionMember.list",
            "mail.v1.mailgroup.update",
            "mail.v1.publicMailboxAlias.create",
            "mail.v1.publicMailboxAlias.delete",
            "mail.v1.publicMailboxAlias.list",
            "mail.v1.publicMailbox.create",
            "mail.v1.publicMailbox.delete",
            "mail.v1.publicMailbox.get",
            "mail.v1.publicMailbox.list",
            "mail.v1.publicMailboxMember.batchCreate",
            "mail.v1.publicMailboxMember.batchDelete",
            "mail.v1.publicMailboxMember.clear",
            "mail.v1.publicMailboxMember.create",
            "mail.v1.publicMailboxMember.delete",
            "mail.v1.publicMailboxMember.get",
            "mail.v1.publicMailboxMember.list",
            "mail.v1.publicMailbox.patch",
            "mail.v1.publicMailbox.removeToRecycleBin",
            "mail.v1.publicMailbox.update"
],
    }


@mcp.tool()
def list_lark_mail_user_tools() -> dict:
    """List all tools available in the lark-mail-user MCP server (Lark Mail User - personal mailbox, folders, messages, rules, and contacts)."""
    return {
        "server": "lark-mail-user",
        "type": "mcp-server/stdio",
        "description": "Lark Mail User - personal mailbox, folders, messages, rules, and contacts",
        "tool_count": 26,
        "tools": [
            "mail.v1.userMailboxAlias.create",
            "mail.v1.userMailboxAlias.delete",
            "mail.v1.userMailboxAlias.list",
            "mail.v1.userMailbox.delete",
            "mail.v1.userMailboxEvent.subscribe",
            "mail.v1.userMailboxEvent.subscription",
            "mail.v1.userMailboxEvent.unsubscribe",
            "mail.v1.userMailboxFolder.create",
            "mail.v1.userMailboxFolder.delete",
            "mail.v1.userMailboxFolder.list",
            "mail.v1.userMailboxFolder.patch",
            "mail.v1.userMailboxMailContact.create",
            "mail.v1.userMailboxMailContact.delete",
            "mail.v1.userMailboxMailContact.list",
            "mail.v1.userMailboxMailContact.patch",
            "mail.v1.userMailboxMessageAttachment.downloadUrl",
            "mail.v1.userMailboxMessage.get",
            "mail.v1.userMailboxMessage.getByCard",
            "mail.v1.userMailboxMessage.list",
            "mail.v1.userMailboxMessage.send",
            "mail.v1.userMailboxRule.create",
            "mail.v1.userMailboxRule.delete",
            "mail.v1.userMailboxRule.list",
            "mail.v1.userMailboxRule.reorder",
            "mail.v1.userMailboxRule.update",
            "mail.v1.user.query"
],
    }


# ─────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────

if __name__ == "__main__":
    import sys
    transport = sys.argv[1] if len(sys.argv) > 1 else "stdio"
    mcp.run(transport=transport)
