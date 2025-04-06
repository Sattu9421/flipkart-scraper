from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# 🔍 Enter your product search term here
search_query = "iPhone 14"

try:
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://www.flipkart.com")
    time.sleep(2)

    # ❌ Close login popup if it appears
    try:
        close_button = driver.find_element(By.XPATH, "//button[contains(text(),'✕')]")
        close_button.click()
    except:
        pass  # No popup

    # 🔍 Enter search term
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(search_query)
    search_box.submit()

    time.sleep(3)  # Wait for results

    # ✅ Get first product title and price
    product_name = driver.find_element(By.CSS_SELECTOR, "div._4rR01T").text
    product_price = driver.find_element(By.CSS_SELECTOR, "div._30jeq3._1_WHN1").text

    print("🛍️ Product:", product_name)
    print("💰 Price:", product_price)

except Exception as e:
    print("❌ Error:", e)

finally:
    driver.quit()
