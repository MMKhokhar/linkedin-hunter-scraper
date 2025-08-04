import time
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# ============ CONFIG ================
LINKEDIN_EMAIL = 'your_email_here'
LINKEDIN_PASS = 'your_password_here'
HUNTER_API_KEY = 'your_hunter_api_key_here'
KEYWORD = 'CEO Lahore'
RESULTS_LIMIT = 10

# ============ LinkedIn Login ================
def linkedin_login(driver):
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)
    driver.find_element(By.ID, "username").send_keys(LINKEDIN_EMAIL)
    driver.find_element(By.ID, "password").send_keys(LINKEDIN_PASS)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)

# ============ LinkedIn Scraping =============
def scrape_linkedin_profiles(driver, keyword, limit=10):
    search_url = f"https://www.linkedin.com/search/results/people/?keywords={keyword.replace(' ', '%20')}"
    driver.get(search_url)
    time.sleep(4)

    names = []
    titles = []
    companies = []

    profiles = driver.find_elements(By.XPATH, '//li[contains(@class, "reusable-search__result-container")]')[:limit]

    for profile in profiles:
        try:
            name = profile.find_element(By.TAG_NAME, 'span').text
            title = profile.find_element(By.CLASS_NAME, 'entity-result__primary-subtitle').text
            company = title.split(" at ")[-1] if " at " in title else "Unknown"
            names.append(name)
            titles.append(title)
            companies.append(company)
        except:
            continue

    return pd.DataFrame({'name': names, 'title': titles, 'company': companies})

# ============ Hunter.io Email =============
def get_email_from_domain(domain):
    url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={HUNTER_API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        if 'data' in data and data['data']['emails']:
            return data['data']['emails'][0]['value']
        else:
            return 'Not found'
    except:
        return 'Error'

# ============ Main ============
def main():
    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(options=options)

    linkedin_login(driver)

    df = scrape_linkedin_profiles(driver, KEYWORD, RESULTS_LIMIT)
    driver.quit()

    domains = [company.replace(" ", "").lower() + ".com" for company in df['company']]
    emails = []
    for domain in domains:
        email = get_email_from_domain(domain)
        print(f"{domain} => {email}")
        emails.append(email)
        time.sleep(1.5)

    df['domain'] = domains
    df['email'] = emails

    df.to_csv("linkedin_leads_with_email.csv", index=False)
    print("\n✅ Done! Saved to linkedin_leads_with_email.csv")

if __name__ == "__main__":
    main()
