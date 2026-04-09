Exercise 3 – Basic LangGraph Chatbot

Aim

To build a simple chatbot using LangGraph and Groq LLM.

Overview

This exercise demonstrates how to create a basic chatbot using LangGraph workflow and Groq Large Language Model. The chatbot accepts user input from the terminal and generates AI responses.

Objective

* To understand the basics of LangGraph pipelines
* To integrate Groq LLM with Python
* To build a simple chatbot for user interaction
* To understand how messages are stored and processed in a graph workflow

Technologies Used

* Python
* LangGraph
* LangChain
* Groq LLM API
* python-dotenv

Files Used

* `main.py` – LangGraph chatbot implementation
* `README3.md` – Documentation
* `Ex3-Screenshot.png` – Output screenshot

Code Explanation

* Loads environment variables using `dotenv`
* Creates a LangGraph state to manage messages
* Connects Groq LLM using `ChatGroq`
* Builds a simple graph with start, chatbot node, and end
* Accepts user input and prints AI response

Running the Program

```bash
python main.py
```

Workflow

User Input
↓
LangGraph State
↓
Groq LLM Processing
↓
AI Response
↓
Output in Terminal

Output

Refer: Ex3-Screenshot.png

Conclusion

Successfully implemented a basic LangGraph chatbot using Groq LLM and understood the working of graph-based conversational AI.
