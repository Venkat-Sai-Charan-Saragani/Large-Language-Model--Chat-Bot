# 🤖 AI Programming Tutor Chatbot

An intelligent programming tutor chatbot built with **Groq API**, **Llama 3.3 70B**, and **Streamlit**. Ask any programming question and get clear, beginner-friendly explanations with examples.

---

## 🚀 Live Demo

👉 [Click here to try the app](https://chat-bhot.streamlit.app/)

---

## ✨ Features

- 💬 **Conversational AI** — Chat naturally about any programming topic
- 🧠 **Powered by Llama 3.3 70B** — State-of-the-art open-source LLM via Groq
- ⚡ **Blazing Fast** — Groq's LPU hardware delivers 300+ tokens/second
- 🎛️ **Adjustable Temperature** — Control response creativity with a slider
- 🔄 **Reset Chat** — Start a fresh conversation anytime
- 🔒 **Secure** — API keys stored safely, never exposed in code

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| [Streamlit](https://streamlit.io) | Frontend UI & deployment |
| [Groq API](https://groq.com) | LLM inference engine |
| [Llama 3.3 70B](https://groq.com/models) | Language model |
| [Python](https://python.org) | Backend logic |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Local environment variables |

---

## 📁 Project Structure

```
├── app.py              # Main Streamlit application
├── functions.py        # Helper functions (get_secret, reset_chat)
├── requirements.txt    # Python dependencies
├── .env                # Local API keys (never committed to GitHub)
├── .gitignore          # Ignores .env and other sensitive files
└── README.md           # Project documentation
```

---

## ⚙️ Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/Venkat-Sai-Charan-Saragani/Large-Language-Model--Chat-Bot.git
cd Large-Language-Model--Chat-Bot
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Create a `.env` file**
```
API_KEY=your_groq_api_key_here
```
> Get your free API key at [console.groq.com](https://console.groq.com)

**4. Run the app**
```bash
streamlit run app.py
```

---

## 🔒 Environment Variables

| Variable | Description |
|---|---|
| `API_KEY` | Your Groq API key from [console.groq.com](https://console.groq.com) |

> ⚠️ Never commit your `.env` file to GitHub. It is already added to `.gitignore`.

---

## ☁️ Deploy on Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **"New app"** and select your repository
4. Set **Main file** to `app.py`
5. Go to **Settings → Secrets** and add:
```toml
API_KEY = "your_groq_api_key_here"
```
6. Click **Deploy**

---

## 📸 Screenshot


---

## 🙌 Acknowledgements

- [Groq](https://groq.com) for the blazing fast free LLM API
- [Streamlit](https://streamlit.io) for the easy deployment platform
- [Meta](https://ai.meta.com) for the open-source Llama 3.3 model

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
