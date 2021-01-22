import time
import json
import pathlib 
import click
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
#chrome_path = r"C:\Users\Hamza\Downloads\chromedriver_win32 (1)\chromedriver.exe"


def get_url_posts(url,n):
    options = webdriver.firefox.options.Options()
    #options.headless = True
    """function that return the urls of posts from the first n pages of forums"""
    links=[] #list of urls 
    driver = webdriver.Firefox(executable_path=r"C:\Users\Hamza\Downloads\geckodriver.exe", options=options)
    for i in range(1,n+1):
        try:
            driver.get(url+str("?page=")+str(i))
            li=driver.find_elements_by_xpath(".//div[starts-with(@class, 'message-title')]")
            post_name=driver.find_elements_by_xpath(".//div[starts-with(@class, 'message-breadcrumb')]")
            for i in range(9):
                link=post_name[i].find_elements_by_xpath(".//a[starts-with(@href, '/')]")
                links.append(link[1].get_attribute('href'))

        except:
            break
    return(list(set(links)))
def post_data(url,url1):
    options = webdriver.firefox.options.Options()
    #options.headless = True
    li=[]
    driver = webdriver.Firefox(executable_path=r"C:\Users\Hamza\Downloads\geckodriver.exe", options=options)
    driver.get(url)
    posts=driver.find_elements_by_xpath(".//div[@class= 'message message--forum js-message']")
    part1=driver.find_element_by_xpath(".//*[@class= 'message-title']")
    user_name=part1.find_element_by_xpath(".//a[contains(@class, 'message-user')]")
    users_url=[]
    if user_name.text in url1:
        for e in posts:
            part1=e.find_element_by_xpath(".//*[@class= 'message-title']")
            user_name=part1.find_element_by_xpath(".//a[contains(@class, 'message-user')]")
            user_url=part1.find_element_by_xpath(".//a[contains(@class, 'message-user')]").get_attribute("href")
            users_url.append(user_url)
            try:
                role=part1.find_element_by_xpath(".//span[contains(@class, 'text-xsmall message-role role-mod')]").text
        
            except:
                role=''
            post=e.find_element_by_xpath(".//*[contains(@class, 'message-content message-body js-message-body')]")
            date=e.find_element_by_xpath(".//div[starts-with(@class, 'message-options')]/time").get_attribute("title")
            dic={
            "name":user_name.text,
            "role":role,
            "post":post.text,
            "date":date
            }
            li.append(dic)
    else:
        pass
    driver.close()
    return(li,users_url)
def get_images(driver,n):
    """get the n first  images url for user image page"""
    li=[]
    for i in range(n):
        sc = WebDriverWait(driver, 10). until(EC.presence_of_element_located((By.CSS_SELECTOR, 'html')))
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', sc)
        part=driver.find_elements_by_xpath(".//li[@class= 'js-gallery-item isotope-image gallery-image']/figure/a/img")
        try:
            image=part[i].get_attribute('src')
            li.append(image)
            
        except:
            break
    return(li)
def save_data(data,name,folder_path):
    """save data in a specific folder path with the name as argument"""
    pathlib.Path(folder_path+name).mkdir(parents=True, exist_ok=True)
    images=data["images"]
    i=0
    print(len(images))
    for e in images:
        try:
            urllib.request.urlretrieve(e,folder_path+name+"/"+str(i) + '.png')
            i=i+1
            print("succ")
        except:
            i=i+1
            print("errr")
    with open(folder_path+name+"\data.json", "a+", encoding="utf8") as json_file:
        json_file.write("\n")
        json.dump(data, json_file, ensure_ascii=False)


   

