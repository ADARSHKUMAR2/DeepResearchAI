# Deep Research

`Deep Research` is a multi-agent research workflow built with the OpenAI Agents SDK and a Gradio UI.
It plans web searches, gathers results, writes a long-form report, and emails the final output.

## What It Does

- Takes a research prompt from a simple Gradio interface.
- Uses a planner agent to generate focused search queries.
- Runs web searches in parallel using Tavily.
- Uses a writer agent to produce a detailed markdown report.
- Uses an email agent to convert and send the report via SendGrid.

## Project Structure

- `deep_research/deep_research.py` - Gradio app entrypoint.
- `deep_research/research_manager.py` - Orchestrates the full research pipeline.
- `deep_research/planner_agent.py` - Generates a structured search plan.
- `deep_research/search_agent.py` - Performs and summarizes web searches.
- `deep_research/writer_agent.py` - Produces final report output.
- `deep_research/email_agent.py` - Sends the report as an HTML email.
- `requirements.txt` - Python dependencies.

## Requirements

- Python 3.10+ (recommended: virtual environment)
- API keys for the services listed in Environment Variables

## Installation

1. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root.

## Environment Variables

Set these in `.env`:

- `OPENAI_API_KEY`
- `TAVILY_API_KEY`
- `SENDGRID_API_KEY`

Optional/common:

- `OPENAI_BASE_URL` (if using a compatible provider endpoint)

## Run the App

From the repository root:

```bash
python deep_research/deep_research.py
```

The app launches a Gradio UI in your browser where you can submit a research topic.

## Workflow Overview

1. `ResearchManager.run(query)` starts a trace and coordinates all steps.
2. Planner agent creates a `WebSearchPlan` with multiple search items.
3. Search agent executes each search (concurrently) and summarizes results.
4. Writer agent synthesizes results into a structured markdown report.
5. Email agent formats the report as HTML and sends it using SendGrid.

## Notes

- The sender and recipient email are currently hardcoded in `deep_research/email_agent.py`.
- If you want configurable recipients, move those addresses into environment variables.
- Do not commit real secrets in `.env`; keep credentials local and rotate exposed keys.
