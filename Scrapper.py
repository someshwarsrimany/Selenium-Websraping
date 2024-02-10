import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_id()->list:
    driver = webdriver.Chrome()
    id_list = []

    try:
        driver.get("https://www.dailymotion.com/tseries2")
        wait = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )
        wait = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.PageLayout__pageGrid___ToE9k'))
        )

        while True:
            id_list = []
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            new_links = set(driver.find_elements(By.CSS_SELECTOR, '.PageLayout__pageGrid___ToE9k a'))
            id_set = set()

            for link in new_links:
                href_value = link.get_attribute('href')
                id_set.add(href_value.split('/')[-1])

            id_list = list(id_set)[:500]
            # print(len(id_list))

            if len(id_list) == 500:
                break

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()
        return id_list if id_list else []

def char_counter(id_list)->dict:
    char_count = {}
    for word in id_list:
        for char in word:
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

if __name__ == "__main__":
    id_list = get_id()
    count = char_counter(id_list)
    max_char = max(count, key=count.get)
    max_count = count[max_char]
    print(f"{max_char}:{max_count}",end="")