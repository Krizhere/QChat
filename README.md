# QChat 🤖 — AI-Powered Chat Application

QChat is an AI-powered chat application built with Python, Streamlit, and LangChain. It integrates large language models (LLMs) with real-time streaming, conversation history, chat history management, and conversational memory to deliver an interactive AI chat experience.

## ✨ Features

- 💬 **Interactive AI Chat** — Chat with AI models through an interactive interface.
- ⚡ **Streaming Responses** — Receive AI-generated responses in real time as they are produced.
- 🗂️ **Conversation History** — Keep track of previous conversations and revisit them.
- 💾 **Chat History Management** — Maintain and access past chat messages.
- 🔎 **Google Search Integration** — Uses the Serper API to retrieve Google Search results, enabling the AI to access relevant web information and provide more informed responses.
- 🧠 **Conversational Memory** — Retain relevant context from previous messages for more contextual conversations.
- 🔗 **Multiple LLM Integrations** — Integrate supported providers such as Groq, OpenAI, Anthropic, and Google Gemini.
- 🦜 **LangChain Integration** — Simplify LLM interactions and application orchestration.
- 🔄 **LangGraph Support** — Build stateful workflows and AI agent applications.
- 🖥️ **Streamlit UI** — A Python-powered interface for interacting with AI.
- 🔐 **Environment Configuration** — Manage API credentials through environment variables.

## 🛠️ Tech Stack

- **Language:** Python
- **Frontend:** Streamlit
- **LLM Framework:** LangChain
- **Workflow Orchestration:** LangGraph
- **LLM Providers:** Groq, OpenAI, Anthropic, Google Gemini
- **Additional Libraries:** Hugging Face Transformers, NumPy, Scikit-learn
- **Configuration:** Python Dotenv

## 🚀 Getting Started

### Prerequisites

- Python installed on your system
- Git
- API key for your chosen LLM provider

### 1. Clone the Repository

```bash
git clone https://github.com/Krizhere/QChat.git
cd QChat
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment.

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root and add the API key required by your selected provider.

Example:

```env
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
```

Replace the placeholder values with your actual API keys. Configure only the variables required by the providers you use.

**Important:** Never commit your `.env` file or expose your API keys publicly.

### 5. Run the Application

Run the Streamlit entry-point file from your project directory.

```bash
streamlit run path/to/your_app.py
```

Replace `path/to/your_app.py` with the actual path to your application's main Python file.

## 🧠 Core Capabilities

### Real-Time Streaming
AI responses are streamed as they are generated, making conversations more responsive and interactive.

### Conversation History and Memory
QChat maintains chat history and uses conversational memory to preserve relevant context, helping the AI respond with better continuity across messages.

### LLM Integration
The application uses modern LLM frameworks to connect language models with the chat interface and application logic.

## 🔮 Future Improvements

Potential enhancements include:

- Document-based question answering.
- Exporting conversations to TXT or PDF.
- Advanced memory management controls.
- Improved error handling and API usage monitoring.
- Automated testing and deployment improvements.

## 🤝 Contributing

Contributions, suggestions, and bug reports are welcome.

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push the branch to your fork.
5. Open a pull request.

## 🔒 Security

- Store API keys in environment variables.
- Keep `.env` out of version control.
- Never publish private credentials or access tokens.

## 👨‍💻 Author

**Krish Kumar**

- GitHub: [@Krizhere](https://github.com/Krizhere)
- Repository: [QChat](https://github.com/Krizhere/QChat)

---

⭐ If you find this project interesting, consider giving the repository a star!
