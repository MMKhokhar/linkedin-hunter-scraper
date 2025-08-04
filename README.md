# LinkedIn + Hunter.io Scraper (Python)

This Python script automates the process of:

1. Logging into LinkedIn
2. Scraping profiles from LinkedIn search results
3. Enriching data with professional emails using Hunter.io API

Ideal for freelancers offering:
- B2B lead generation
- Business email collection
- Sales outreach data

---

## 🛠 Requirements

- Python 3.x
- Google Chrome + ChromeDriver
- Selenium
- Hunter.io API Key
- LinkedIn account

---

## ⚙️ Setup

```bash
pip install selenium pandas requests
```

Download ChromeDriver from:  
[https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

---

## 🔧 Configuration

Edit `main.py` file:

```python
LINKEDIN_EMAIL = 'your_email_here'
LINKEDIN_PASS = 'your_password_here'
HUNTER_API_KEY = 'your_hunter_api_key_here'
KEYWORD = 'CEO Lahore'
RESULTS_LIMIT = 10
```

---

## ▶️ Run

```bash
python main.py
```

---

## 📤 Output

Script will create a file: `linkedin_leads_with_email.csv`

| name       | title             | company     | domain         | email              |
|------------|-------------------|-------------|----------------|--------------------|
| Ali Khan   | CEO at TechCorp   | TechCorp    | techcorp.com   | ali@techcorp.com   |

---

## ⚠️ Disclaimer

- LinkedIn scraping may violate their Terms of Service. Use responsibly.
- Hunter.io has daily request limits (25 requests/day on free plan).
- This script is for educational and personal use only.

---

## 👨‍💻 Author

Created by [MMKhokhar](https://github.com/MMKhokhar)
