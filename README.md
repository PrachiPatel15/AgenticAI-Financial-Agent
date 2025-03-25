# AI Multi-Agent Chatbot with Web & Finance Tools

This project implements a **multi-agent AI chatbot** using `phi`, powered by **Groq’s Llama 3.3-70B model**. It includes two specialized agents:

1. **Web Search Agent** – Uses **DuckDuckGo** for real-time web searches with source citations.
2. **Finance AI Agent** – Fetches **stock prices, analyst recommendations, fundamentals, and company news** via Yahoo Finance.

---

## 🚀 Features
- **Web search integration** for retrieving real-time information.
- **Financial analysis** with stock prices, recommendations, and news.
- **Multi-agent framework** using `phi`.
- **Markdown support** for structured responses.
- **Live reloading** with `serve_playground_app`.

---

## 🛠 Installation

1. **Clone the repository**:
   ```sh
   git clone [https://github.com/yourusername/your-repo.git](https://github.com/PrachiPatel15/AgenticAI-Financial-Agent).git
   cd your-repo
   ```
2. **Set up a virtual environment (optional but recommended)**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
4. **Set up API keys**:
   - Create a `.env` file in the root directory and add:
     ```env
     GROQ_API_KEY=your_groq_api_key
     ```
   - Replace `your_groq_api_key` with your actual **Groq API key**.

---

## 🎯 Usage

Run the application with:
```sh
python main.py
```
This will start the **phi Playground** with the two AI agents.

---

## 📜 Agents Overview

### 🔍 Web Search Agent
- Uses **DuckDuckGo** to fetch real-time information.
- Always provides sources.
- Uses **Llama-3.3-70B** for processing.

### 💰 Finance AI Agent
- Retrieves **real-time stock market data** via **Yahoo Finance**.
- Provides **company fundamentals, analyst recommendations, and news**.
- Displays data in structured tables.

---

## 🛠 Customization
- Modify `web_search_agent` and `finance_agent` in `main.py` to add **more tools or adjust behavior**.
- Change the **AI model** by modifying `Groq(id="llama-3.3-70b-versatile")`.

---

## 🤝 Contributing
Pull requests are welcome! For major changes, open an issue first to discuss.

---

## 📧 Contact
For questions, feel free to **open an issue** or reach out on **GitHub Discussions**.

