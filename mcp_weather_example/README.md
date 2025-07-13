# 🧠 Minimal Model Context Protocol (MCP) Demo

This project demonstrates a **minimal example of the Model Context Protocol (MCP)** using a simple weather assistant. It shows how to **enrich prompts** with relevant context before sending them to an LLM (e.g., OpenAI GPT-4).

Rather than relying on external APIs, the weather data is mocked using a simple Python dictionary — so you can focus entirely on the **roles** played by the client, server, and LLM.

---

![diagram](resources/Minimal%20MCP%20Demo.png)

## 🚀 What This Demo Covers

- MCP **Client**: Detects intent and enriches prompts.
- MCP **Server**: Resolves external context (weather info).
- OpenAI **LLM**: Receives the enriched prompt and generates the final answer.

---
🛠️ How to Run

    Install dependencies:
        pip install -r requirements.txt

    Add your OpenAI API key to config.py:
        OPENAI_API_KEY = "your-api-key"

    Start the MCP server:
        python mcp_server.py

    In a second terminal, run the client:
        python mcp_client.py


