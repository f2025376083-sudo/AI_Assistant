# Simple LLM API Command-Line Assistant

## Project Overview
This project is a small command-line AI assistant built with Python and an LLM API. The user enters a question or instruction, the Python application sends it to the language model through an API request, and the generated response is displayed in the terminal.

## Learning Objectives
- Understand what an API is.
- Understand how an LLM API works.
- Send API requests from Python.
- Receive and display an AI-generated response.
- Understand API-key authentication.
- Practice basic API security.
- Understand the application → API → LLM → response flow.

## Technologies
- Python
- OpenAI Python SDK
- OpenAI Responses API
- python-dotenv

## Setup

1. Install Python 3.10 or newer.
2. Open a terminal in this project folder.
3. Install dependencies:

   pip install -r requirements.txt

4. Copy `.env.example` to `.env`.
5. Put your private API key in `.env`:

   OPENAI_API_KEY=your_real_key

6. Run:

   python ai_assistant.py

## Example
User:
Explain what an API is in one sentence.

AI:
An API is a set of rules that allows one software application to communicate with another service.

## Security
Never put the API key directly in the Python source code, GitHub repository, screenshots, or public posts. The `.env` file is ignored by Git through `.gitignore`.

## Application Flow

User input
    ↓
Python program
    ↓
API request
    ↓
LLM
    ↓
API response
    ↓
Python program
    ↓
AI response displayed in terminal
