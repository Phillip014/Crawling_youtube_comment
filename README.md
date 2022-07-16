# Crawling_youtube_comment

```bash
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Selenium is needed here because Youtube is JavaScript rendered, which BeautifulSoup cannot deal with. (<a href="https://towardsdatascience.com/how-to-scrape-youtube-comments-with-python-61ff197115d4">refer to François St-Amant </a>,
https://towardsdatascience.com/how-to-scrape-youtube-comments-with-python-61ff197115d4
All the other modules are needed because Youtube comments are dynamically loaded, which means that they are only visible when you scroll down the page. So we want a loop that will:
1. Scroll down
2. Wait for comments to appear
3. Scrape the comments
4. Repeat for whatever range we want.
Here is the loop that does just that:
```bash
data=[]
with Chrome(executable_path=r'C:\Program Files\chromedriver.exe') as driver:
    wait = WebDriverWait(driver,2)
    driver.get("https://www.youtube.com/watch?v=1emA1EFsPMM")

    for item in range(3): 
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(5)

    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content"))):
        data.append(comment.text)
        
