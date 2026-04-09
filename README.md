# GENAI Essentials Exercises

This repository contains a series of beginner-friendly exercises to understand how Generative AI applications are built using:

* Groq API
* OpenAI-compatible APIs
* LangChain
* LangGraph
* Langfuse (Tracing & Monitoring)

---

## Exercises Overview

### Exercise 1: Basic LLM Call

* Uses Groq API with OpenAI-compatible client
* Sends a simple prompt to the model
* Displays response

**Concepts Learned:**

* API usage
* Environment variables
* Model invocation

---

### Exercise 2: LangChain Agent with Tool

* Creates a simple AI agent
* Uses a custom tool (`get_word_length`)
* Agent decides when to use tool

**Concepts Learned:**

* Agents
* Tools
* Prompt handling

---

### Exercise 3: LangGraph Basic Chatbot

* Builds chatbot using LangGraph
* Uses state-based message flow

**Concepts Learned:**

* Graph-based workflows
* State management
* Streaming responses

---

### Exercise 4: LangGraph with Tools

* Integrates tools inside LangGraph

**Agent can:**

* Call tools (weather, sum)
* Return responses dynamically

**Concepts Learned:**

* ToolNode
* Conditional edges
* Tool execution flow

---

### Exercise 5: Langfuse Integration

* Adds tracing & monitoring
* Tracks model calls and responses

**Concepts Learned:**

* Observability
* Debugging AI workflows
* Logging with Langfuse

---

## Setup Instructions

### 1 Install Python Packages

```bash
python -m pip install openai langchain langchain-groq langgraph python-dotenv langfuse
```

### 2 Create `.env` File

```env
GROQ_API_KEY=your_api_key_here
GROQ_MODEL_NAME=llama-3.3-70b-versatile

# Langfuse (for Exercise 5)
LANGFUSE_PUBLIC_KEY=your_public_key
LANGFUSE_SECRET_KEY=your_secret_key
LANGFUSE_HOST=https://cloud.langfuse.com
```

### 3 Run Exercises

```bash
python main.py
```

---

## Notes

* Always use latest Groq models
* Ensure `.env` is properly configured
* Restart terminal after updating environment variables

---

## Conclusion

These exercises provide a step-by-step approach to understanding:

Basic AI calls → Agents → Graph workflows → Tools → Monitoring

This forms the foundation for building real-world AI applications


