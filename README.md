
````md
# WASpammer – WhatsApp Automation Tool

WASpammer is a Python-based automation tool that uses **Selenium WebDriver** and **Google Chrome** to automate sending messages through **WhatsApp Web**.  
It opens WhatsApp Web, waits for QR login, selects a chat, and automatically sends a user-defined message multiple times.

⚠️ **This project is for personal, educational, and automation testing purposes only. Do not use for spamming or violating WhatsApp’s Terms of Service.**

---

## 📌 Badges

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-Automation-green)
![ChromeDriver](https://img.shields.io/badge/ChromeDriver-Compatible-yellow)
![License](https://img.shields.io/badge/License-MIT-purple)

---

## 🚀 Features

- Automates WhatsApp Web using Selenium  
- Detects WhatsApp UI elements with multiple fallback selectors  
- Automatically selects a chat and sends repeated messages  
- Chrome + ChromeDriver integration  
- Simple command-line interface  
- Works on Linux (Arch/Garuda, Ubuntu, Debian, Fedora)

---

## 📦 Installation

### **1. Clone this repository**
```bash
git clone https://github.com/m4verick0304/WASpammer.git
cd WASpammer
````

### **2. Create & activate virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

### **3. Install dependencies**

```bash
pip install -r requirements.txt
```

### **4. Install Google Chrome**

**Garuda/Arch:**

```bash
sudo pacman -S google-chrome
```

**Debian/Ubuntu:**

```bash
sudo apt install google-chrome-stable
```

### **5. Install matching ChromeDriver**

Check versions:

```bash
google-chrome-stable --version
chromedriver --version
```

If mismatched, download the correct ChromeDriver:
🔗 [https://googlechromelabs.github.io/chrome-for-testing/](https://googlechromelabs.github.io/chrome-for-testing/)

Move ChromeDriver to your system path:

```bash
sudo mv chromedriver /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
```

---

## ▶️ Usage

Run the script:

```bash
python WAspammer.py
```

### **Workflow**

1. Chrome opens WhatsApp Web
2. Scan your QR Code
3. Select a chat manually
4. Script detects the chat box
5. Enter your message
6. Script sends it the chosen number of times

---

## 📁 Project Structure

```
WASpammer/
│── WAspammer.py
│── README.md
│── requirements.txt
│── .gitignore
└── LICENSE
```

---

## ⚠️ Important Notes

* Do **NOT** use this tool for spamming or harassment
* WhatsApp may limit or block accounts for automated actions
* UI changes on WhatsApp Web may break selectors
* Use responsibly and ethically

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🤝 Contributions

Pull requests are welcome!
Feel free to open issues for suggestions or improvements.

---

## ⭐ Support

If you found this project helpful, consider giving it a **star** ⭐ on GitHub!

```

---

If you want, I can also generate:

✅ A logo for the project  
✅ A banner image for the README  
✅ A more advanced README with screenshots  
✅ A setup script (install.sh)

Just tell me!
```
