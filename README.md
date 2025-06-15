
# 🌦️ Real-Time Weather App

A simple, fast, and responsive weather app built with **Python** and **Streamlit**. It fetches real-time weather data using the free `wttr.in` API and stores a local search history.

---

## 📸 Preview

![weather-app-screenshot](preview.png) <!-- Add your screenshot file -->

---

## 🔧 Setup & Run

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app
```

### 2. Install Dependencies
Make sure you have Python 3 installed.

Install required packages:
```bash
pip install streamlit requests
```

### 3. Run the App
```bash
streamlit run weather_app.py
```

The app will open automatically in your browser at [http://localhost:8501](http://localhost:8501).

---

## 🗃️ Project Structure

```
weather-app/
├── weather_app.py          # Main Streamlit web app
├── search_history.txt      # (Auto-generated) file storing recent city searches
├── preview.png             # Screenshot for GitHub preview
└── README.md
```

---

## 🌐 Powered By

- [🌐 wttr.in](https://wttr.in) — Real-time weather via HTTP
- [💡 Streamlit](https://streamlit.io) — Effortless web apps in Python

---

## ✨ Features

- Live weather info for any city
- Search history stored locally
- Simple, clean Streamlit UI
- No API key or signup needed

---

## ✅ To-Do / Next Improvements

- Show more detailed weather info (humidity, wind, etc.)
- Use a cloud database for storing history
- Add unit tests
- Deploy on [Streamlit Cloud](https://streamlit.io/cloud) or [Hugging Face Spaces](https://huggingface.co/spaces)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

Made by **[Your Name](https://github.com/your-username)**  
Feel free to contribute, suggest ideas, or fork the repo!
