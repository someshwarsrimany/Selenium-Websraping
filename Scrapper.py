import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_id()->list:
    driver = webdriver.Chrome()
    driver.get("https://www.dailymotion.com/tseries2")
    wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    for _ in range(50):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
    # time.sleep(30)
    video_links = driver.find_elements(By.CSS_SELECTOR, '.PageLayout__pageGrid___ToE9k a')
    n = 500
    id_list = []
    for link in video_links:
        href_value = link.get_attribute('href')
        id = href_value.split('/')[-1]
        id = id_list.append(id)
        n=n-1
        if n == 0:
            break
    print(len(id_list))
    driver.quit()
    return id_list

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