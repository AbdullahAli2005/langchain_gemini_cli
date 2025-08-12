# AI-Powered CLI Assistant with Google Gemini API & LangChain

A Python-based command-line AI assistant that uses **Google's Gemini API** and **LangChain** to provide intelligent, conversational answers to user queries. The app supports API key authentication, structured prompt handling, and is easily extensible to other LLM providers.

---

## Features

* **Conversational AI** powered by Google Gemini API.
* **LangChain** integration for prompt templates and chain execution.
* CLI-based interface for quick and lightweight interactions.
* Modular structure to easily switch between LLM providers (Gemini, OpenAI, etc.).
* Environment variable-based API key management with `python-dotenv`.

---

## Prerequisites

* Python **3.10+** (tested with Python 3.13)
* Google Gemini API Key ([Get it here](https://ai.google.dev/))
* VS Code or any Python IDE

---

## Installation

1. **Clone the repository:**

```bash
 git clone https://github.com/your-username/gemini-cli-assistant.git
 cd gemini-cli-assistant
```

2. **Create and activate a virtual environment:**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Usage

Run the application:

```bash
python app.py
```

Example:

```
🤖 Gemini CLI is ready! Type your question or 'exit' to quit.

You: Who is the best Pakistani batsman right now?
AI: Babar Azam is widely considered the best Pakistani batsman currently...
```

---

## File Structure

```
├── app.py               # Main CLI application
├── .env                 # Environment variables
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
```

---

## Dependencies

* `langchain`
* `langchain-google-genai`
* `python-dotenv`

Install them manually if needed:

```bash
pip install langchain langchain-google-genai python-dotenv
```

---

## Possible Improvements

* Add support for streaming responses.
* Implement conversation memory.
* Extend integration to multiple LLM APIs.
* Build a simple web interface using Flask or FastAPI.

---

## License

MIT License. See [LICENSE](LICENSE) for details.
