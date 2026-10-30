"""
Layer 4 — Agents (optional).

Only add this layer if agents genuinely earn their place in your project.
The brief warns: agents add cost, unreliability, and risk.
If a simpler design works better, explain why in what_i_left_out.md.

This scaffold uses the Anthropic tool-use API to build a basic agent loop.
"""

import os
import json
import anthropic

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
MODEL = "claude-opus-4-5"

# Define the tools your agent may call.
# Keep this list minimal — state explicitly what the agent may NOT do without you.
TOOLS = [
    {
        "name": "search_collection",
        "description": "Search the curated collection for relevant passages.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "The search query"}
            },
            "required": ["query"],
        },
    },
    # Add more tools here only if they earn their place
]

SYSTEM_PROMPT = """You are an assistant for [YOUR PROJECT].
You have access to a search tool for the curated collection.
Always cite your sources.
Do not perform any action that requires human judgment without asking first."""


def search_collection(query: str) -> str:
    # TODO: connect this to your RAG layer (src/03_rag/query.py)
    return f"[TODO: implement search for '{query}']"


def dispatch_tool(name: str, inputs: dict) -> str:
    if name == "search_collection":
        return search_collection(inputs["query"])
    return f"Unknown tool: {name}"


def run_agent(user_message: str) -> str:
    messages = [{"role": "user", "content": user_message}]
    while True:
        response = client.messages.create(
            model=MODEL,
            max_tokens=2048,
            system=SYSTEM_PROMPT,
            tools=TOOLS,
            messages=messages,
        )
        if response.stop_reason == "end_turn":
            return response.content[0].text

        tool_uses = [b for b in response.content if b.type == "tool_use"]
        if not tool_uses:
            return response.content[0].text

        messages.append({"role": "assistant", "content": response.content})
        tool_results = []
        for tool_use in tool_uses:
            result = dispatch_tool(tool_use.name, tool_use.input)
            tool_results.append({
                "type": "tool_result",
                "tool_use_id": tool_use.id,
                "content": result,
            })
        messages.append({"role": "user", "content": tool_results})


if __name__ == "__main__":
    question = "TODO: replace with one of your evaluation questions"
    print(run_agent(question))
