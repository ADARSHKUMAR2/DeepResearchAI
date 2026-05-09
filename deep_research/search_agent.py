from agents import Agent, WebSearchTool, ModelSettings, function_tool
from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv(override=True)

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@function_tool
def web_search(query: str):
    """Search the web and return summarized results"""
    try:
        response = client.search(query)
        results = response.get("results", [])

        cleaned = []
        for r in results[:5]:
            cleaned.append(f"{r.get('title')}\n{r.get('content')}")

        return "\n\n".join(cleaned)

    except Exception as e:
        return f"Search failed: {str(e)}"

INSTRUCTIONS = (
    "You are a research assistant. Given a search term, you search the web for that term and "
    "produce a concise summary of the results. The summary must 2-3 paragraphs and less than 300 "
    "words. Capture the main points. Write succintly, no need to have complete sentences or good "
    "grammar. This will be consumed by someone synthesizing a report, so its vital you capture the "
    "essence and ignore any fluff. Do not include any additional commentary other than the summary itself."
)

search_agent = Agent(
    name="Search agent",
    instructions=INSTRUCTIONS,
    tools=[web_search],
    model="openai/gpt-4o-mini",
    model_settings=ModelSettings(tool_choice="required"),
)