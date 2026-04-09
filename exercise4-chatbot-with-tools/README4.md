 Exercise 4 – LangGraph Chatbot with Tools

Aim

To build a LangGraph chatbot that can use external tools for answering user queries.

 Overview

This exercise demonstrates how to build a chatbot using LangGraph and Groq LLM with tool integration. The chatbot can automatically call tools when the user asks for tasks such as checking weather or performing calculations.

 Objective

* To understand how tool calling works in LLM applications
* To integrate external tools with a chatbot
* To build an agent workflow using LangGraph
* To allow the model to dynamically select tools when needed

Tools Implemented

1. Weather Tool

This tool returns weather information for a given location.

Example:
User: What is the weather in Chennai?
Tool Output: The weather in Chennai is currently 72°F and sunny.

2. Calculator Tool

This tool performs a simple addition between two numbers.

Example:
User: Add 5 and 7
Tool Output: 12

Technologies Used

* Python
* LangGraph
* LangChain
* Groq LLM API
* python-dotenv

Files Used

* `main.py` – Main chatbot implementation with tool integration
* `README4.md` – Documentation
* `Ex4-Screenshot.png` – Output screenshot

 Running the Application

```bash
python main.py
```

Example Interaction

You: What is the weather in Delhi?
Agent calls `get_weather`
Tool returns weather result
Groq Bot displays the answer

You: Add 8 and 12
Agent calls `calculate_sum`
Tool returns result
Groq Bot displays the answer

Workflow

User Input
↓
Chatbot Node
↓
Check if Tool is Needed
↓
Execute Tool
↓
Return Result
↓
AI Response

Output

Refer: Ex4-Screenshot.png

Conclusion

This exercise demonstrates how a chatbot can interact with external tools to perform specific tasks such as calculations and information retrieval. Tool integration is an important concept for building intelligent AI agents.
