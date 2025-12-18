# 🔗 LinkTools: URL Shortener & QR Generator

A lightweight, responsive web application built with **Flask** that allows users to shorten long URLs and generate downloadable QR codes instantly.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=flat&logo=flask&logoColor=white)
![Status](https://img.shields.io/badge/Status-Live-success)

## 🚀 Live Demo
Check out the live application here:
👉 **[https://kartik915.pythonanywhere.com](https://kartik915.pythonanywhere.com)**

---

## ✨ Features

* **🔗 URL Shortener:** Converts long, messy links into short, easy-to-share URLs.
* **📱 QR Code Generator:** Generates high-quality QR codes for any text or URL instantly.
* **🎨 Modern UI:** Features a "Glassmorphism" design with smooth animations.
* **📱 Fully Responsive:** Optimized for desktops, tablets, and mobile phones.
* **💾 Database:** Uses SQLite for persistent link storage.
* **⚡ Fast:** QR codes are generated in-memory (no cluttering server storage).

---

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Database:** SQLite
* **Frontend:** HTML5, CSS3 (Custom Responsive Design), Vanilla JavaScript
* **Libraries:** `qrcode`, `Pillow`

---

## 📦 How to Run Locally

If you want to run this project on your own machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Kartik915d/LinkTools.git](https://github.com/Kartik915d/LinkTools.git)
    cd LinkTools
    ```

2.  **Install dependencies:**
    ```bash
    pip install Flask qrcode[pil]
    ```

3.  **Run the app:**
    ```bash
    python app.py
    ```

4.  **Open in browser:**
    Go to `http://127.0.0.1:5000`

---

## 📂 Project Structure

```text
LinkTools/
│
├── app.py              # Main Flask application
├── database.db         # SQLite database (auto-created)
├── static/
│   └── style.css       # CSS styling
└── templates/
    └── index.html      # Frontend HTML
