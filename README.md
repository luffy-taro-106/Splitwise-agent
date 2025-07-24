# Splitwise Gemini Agent

A conversational AI assistant that connects to the Splitwise API so you can manage expenses with natural-language commands (e.g. “Add lunch with John for $15” or “Show my balances in the Flatmates group”).

The agent combines:

* **Google Gemini** (LLM) via LangChain for reasoning
* **FastAPI** REST backend (`backend.py`)
* **React + Vite** chat frontend (`splitwise-chat/`)
* A suite of **domain-specific tools** that wrap the Splitwise API

---

## How it works

1. The frontend sends your message to the FastAPI `/chat` endpoint.
2. The LangChain agent receives the text and, if necessary, calls one or more custom tools (e.g. `GetFriends`, `GetGroups`, `AddExpense`).
3. Tools internally call the official Splitwise REST API. Friend / group names are automatically resolved to IDs, so you never need to provide raw IDs yourself.
4. The agent returns a final response, which is displayed in the chat UI.

Behind the scenes, the agent follows a strict workflow:

1. Fetch relevant data (friends, groups, etc.).
2. Resolve human-readable names → Splitwise IDs.
3. Perform the requested action (create expense, list balances, …).

---

## Project structure (simplified)

```text
splitwise_gemini_agent/
   ├── backend.py          # FastAPI server
   ├── main.py             # LangChain agent & tool loading
   ├── config.py           # Reads ENV variables
   ├── tools/              # Individual Splitwise tool wrappers
   ├── prompts/            # System & tool prompts
   ├── requirements.txt    # Python dependencies
   ├── splitwise-chat/     # React chat application
   ├──run_app.sh          # Convenience wrapper to start both services
   └── README.md           # This file
```

---

## Quick start

### 1. Clone & CD

```bash
git clone <repo-url>
cd Splitwise
```

### 2. Create `.env`

Create a file named `.env` in the project root (same folder as this README) and add your keys:

```dotenv
# Splitwise (https://secure.splitwise.com/apps)
CONSUMER_KEY=<your_splitwise_consumer_key>
CONSUMER_SECRET=<your_splitwise_consumer_secret>
ACCESS_TOKEN=<your_splitwise_access_token>
ACCESS_SECRET=<your_splitwise_access_secret>

# Google AI (https://ai.google.dev)
GEMINI_API_KEY=<your_gemini_api_key>
```

> 🔑  You obtain the Splitwise keys from the Splitwise developer portal, and the `GEMINI_API_KEY` from Google AI. **Never commit real keys to version control.**

### 3. Backend (Python ≥ 3.10)

```bash
# create virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# install dependencies
pip install -r splitwise_gemini_agent/requirements.txt

# run the server (auto-reload)
cd splitwise_gemini_agent
uvicorn backend:app --host 0.0.0.0 --port 8000 --reload
```

The API is now available at `http://localhost:8000`. You can visit `http://localhost:8000/docs` for interactive Swagger docs.

### 4. Frontend (Node.js ≥ 18)

```bash
cd splitwise_gemini_agent/splitwise-chat
npm install
npm run dev   # Vite default (or npm start if using CRA)
```

Open `http://localhost:3000` to chat with your agent. The frontend is configured to talk to the backend on port 8000.

---

## Scripts

```bash
# Convenience wrapper to start both services (backend & frontend)
./splitwise_gemini_agent/run_app.sh
```

---

## Troubleshooting

* **CORS errors** – ensure the backend is running on port 8000 before starting the frontend.
* **401 / 403 from Splitwise** – double-check your tokens and that they haven’t expired.
* **Quota / model errors** – verify `GEMINI_API_KEY` validity and usage limits.

---

## License

MIT – see `LICENSE` for details.
