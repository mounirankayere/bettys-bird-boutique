import os
from google.adk.agents import Agent
from .search_agent import search_tool

AGENT_MODEL = "gemini-3.8-flash"

with open(os.path.join(os.path.dirname(__file__), "agent-prompt.txt"), "r") as f:
    agent_prompt = f.read()

root_agent = Agent(
    name="bettys_bird_boutique_agent",
    model=AGENT_MODEL,
    description="Agent principal de la boutique Betty's Bird Boutique.",
    instruction=agent_prompt,
    tools=[search_tool]
)