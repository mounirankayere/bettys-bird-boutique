import os
from google.adk.agents import Agent
from google.adk.sessions import InMemorySessionService
from toolbox_core import ToolboxSyncClient

from datastore import search_store_documents
from search_agent import search_tool

AGENT_MODEL = "gemini-2.5-flash"

with open("agent-prompt.txt", "r") as f:
    root_prompt = f.read()

toolbox_url = os.environ.get("TOOLBOX_URL", "http://127.0.0.1:5000")
db_client = ToolboxSyncClient(toolbox_url)
db_tools = db_client.load_tool("get-product-price")

session_service = InMemorySessionService()

root_agent = Agent(
    name="bettys_bird_boutique_agent",
    model=AGENT_MODEL,
    description="Agent de service client pour Betty's Bird Boutique.",
    instruction=root_prompt,
    tools=[db_tools, search_store_documents, search_tool],
    session_service=session_service
)
