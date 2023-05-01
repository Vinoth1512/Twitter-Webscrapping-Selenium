from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://twitter.com/sachin_rt")
    
name,username = driver.find_element(By.CSS_SELECTOR,'div[data-testid="UserName"]').text.split('\n')
following = driver.find_element(By.XPATH, "//span[contains(text(), 'Following')]/ancestor::a/span").text
followers = driver.find_element(By.XPATH, "//span[contains(text(), 'Followers')]/ancestor::a/span").text
bio = driver.find_element(By.CSS_SELECTOR,'div[data-testid="UserDescription"]').text.split('\n')

data = {'username' : username,'bio' : bio,'Followers_count' : followers,'following_count' : following} 

df = pd.Series(data)

print(df)
df.to_csv("Webscrapping-Output")
