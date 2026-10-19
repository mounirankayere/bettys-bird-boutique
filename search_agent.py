import os
from google.adk.agents import Agent
from google.adk.tools import AgentTool
from google.adk.tools.google_search import google_search

SEARCH_MODEL = "gemini-2.5-flash"

with open("search-prompt.txt", "r") as f:
    search_prompt = f.read()

search_agent = Agent(
    name="bird_research_agent",
    model=SEARCH_MODEL,
    description="Agent spécialisé dans la recherche d'informations générales sur les oiseaux via le web.",
    instruction=search_prompt,
    tools=[google_search]
)

search_tool = AgentTool(agent=search_agent)
