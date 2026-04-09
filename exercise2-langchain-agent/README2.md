Exercise 2 – LangChain Agent with Groq LLM

Aim

To build a simple AI agent using LangChain and Groq LLM with a custom tool.

Overview

This exercise demonstrates how to create a LangChain agent that uses a custom tool to calculate the length of a word. The agent receives a user query, decides whether the tool is needed, and returns the final answer.

Technologies Used

* Python
* LangChain
* LangChain Groq
* Groq API
* python-dotenv

Files Used

* `agent.py` – Agent and tool implementation
* `README2.md` – Documentation
* `Ex2-Screenshot.png` – Output screenshot

 Code Explanation

* Loads API key and model name from `.env`
* Connects Groq model using `ChatGroq`
* Defines a custom tool `get_word_length()`
* Creates an agent with the tool
* Sends a user question to the agent
* Prints the final response

 Input Question

How many letters are in the word 'Generative'?

Expected Output

The agent uses the tool and returns the number of letters in the given word.

Conclusion

Successfully created a LangChain agent integrated with Groq LLM and a custom tool.
