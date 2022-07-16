#!/usr/bin/env python
# coding: utf-8

# In[195]:


import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# In[158]:


data=[]
with Chrome(executable_path=r'C:\Program Files\chromedriver.exe') as driver:
    wait = WebDriverWait(driver,2)
    driver.get("https://www.youtube.com/watch?v=1emA1EFsPMM")

    for item in range(3): 
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(5)

    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content"))):
        data.append(comment.text)
        


# In[196]:


import pandas as pd   
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud
import re   
import nltk
from nltk.corpus import stopwords

df = pd.DataFrame(data[3:59], columns=['comment'])

list = []
for i in df['comment']:
    list.append(i)


# In[244]:


str = " ".join(list)   
char = '\n~:～!！*?"<>《》）()|/的'
for i in char:
    str = str.replace(i, " ")


# In[242]:


cut_text = jieba.cut(str,cut_all=False)
result = " ".join(cut_text)
result


# In[243]:


wc = WordCloud(
        # 设置字体，不指定就会出现乱码
        # 设置背景色
        background_color='white',
        # 设置背景宽
        width=500,
        # 设置背景高
        height=350,
        # 最大字体
        max_font_size=100,
        # 最小字体
        min_font_size=10,
        font_path='C:\\Windows\\Font\\simkai.ttf',
        mode='RGBA'
        )
wc.generate(result)
plt.imshow(wc)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




