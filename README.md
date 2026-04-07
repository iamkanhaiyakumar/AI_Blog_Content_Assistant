# 🤖 AI Blog Content Assistant

## 🚀 Overview

AI Blog Content Assistant is an end-to-end Generative AI web application that helps users generate blog titles and full-length articles using Large Language Models (LLMs).

Built using LangChain, Hugging Face, and Streamlit, the application provides a clean UI with real-time content generation, streaming output, and export features.

---

## ✨ Features

* 🎯 Generate creative and engaging blog titles from a topic
* 📝 Generate full blog content with keywords and word limit
* ⚡ Real-time streaming output (typing effect)
* 📋 Copy blog content easily
* 📄 Download generated blog as PDF
* 🎨 Clean and responsive Streamlit UI
* 🔐 Secure API key management using environment variables

---

## 🛠 Tech Stack

* Python
* Streamlit
* LangChain
* Hugging Face LLMs
* ReportLab (PDF generation)

---

## 📁 Project Structure

```
AI_Blog_Content_Assistant/
│
├── app.py          # Main application
├── ui.py           # UI components
├── utils.py        # PDF generation
├── requirements.txt
├── .env            # API keys (not pushed to GitHub)
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/iamkanhaiyakumar/AI_Blog_Content_Assistant.git
cd AI_Blog_Content_Assistant
```

### 2. Create environment file

Create a `.env` file and add your Hugging Face API key:

```
HUGGINGFACEHUB_API_TOKEN=your_api_key_here
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. User enters topic → LLM generates blog titles
2. User selects title + keywords → LLM generates blog
3. Content is streamed in real-time
4. User can copy or download blog as PDF

---

## ⚠️ Limitations

* Output quality depends on the selected LLM
* Generated content may require minor edits
* API-based model usage may have rate limits

---

## 🔐 Security Note

* API keys are managed using `.env` file locally
* For deployment (e.g., Streamlit Cloud), use **Secrets Manager** instead

---

## 🌐 Deployment

The app can be deployed easily on:

* Streamlit Cloud
* Render
* Vercel (frontend)

---

## 🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit pull requests.

---

## 👨‍💻 Author

**Kanhaiya Kumar**
🚀 AI/ML Enthusiast | Generative AI Developer

GitHub: https://github.com/iamkanhaiyakumar
