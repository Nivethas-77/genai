Exercise 5 – LangGraph Chatbot with Langfuse Monitoring

Aim

To integrate Langfuse monitoring and tracing into a LangGraph chatbot pipeline.

Overview

This exercise demonstrates how to add observability and monitoring to a chatbot using LangGraph, Groq LLM, and Langfuse. The chatbot processes user queries and sends tracing information to Langfuse for analysis.

Langfuse helps track:

* Prompt and response data
* Execution traces
* Model latency
* Token usage

Objective

* To understand LLM observability and tracing
* To integrate Langfuse with LangGraph
* To monitor chatbot performance
* To analyze execution traces of AI workflows

Technologies Used

* Python
* LangGraph
* LangChain
* Groq LLM API
* Langfuse
* python-dotenv

Files Used

* `main.py` – Chatbot implementation with Langfuse tracing
* `README5.md` – Documentation
* `Ex5-Screenshot.png` – Output screenshot

Environment Variables

Add these in `.env`:

```env
GROQ_API_KEY=your_api_key
GROQ_MODEL_NAME=llama-3.3-70b-versatile
LANGFUSE_PUBLIC_KEY=your_public_key
LANGFUSE_SECRET_KEY=your_secret_key
LANGFUSE_HOST=https://cloud.langfuse.com
```

Running the Application

```bash
python main.py
```

Workflow

User Input
↓
LangGraph Pipeline
↓
Groq LLM Response
↓
Langfuse Trace Recording
↓
Dashboard Visualization

Output

Refer: Ex5-Screenshot.png

Conclusion

This exercise demonstrates how Langfuse can be integrated with LangGraph pipelines to monitor chatbot interactions and performance. Observability tools are useful for debugging and improving AI systems.
