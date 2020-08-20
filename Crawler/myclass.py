from methods import *
class Personne():
    def __init__(self):
        """Constructeur de notre classe"""
        pass
    
    def user_info(self,url):
        driver = webdriver.Chrome(chrome_path)
        driver.get(url)
        c=driver.find_element_by_xpath(".//*[@class= 'authorCard-name']").text
        name=c.split()[0]
        role=c.split()[2]
        td=driver.find_elements_by_xpath(".//td[@class= 'table__td']")
        info=driver.find_element_by_xpath(".//ul[@class= 'user-bits__list']")
        li=info.find_elements_by_xpath(".//li")
        ch=[] # list contain 
        for e in li:
            ch.append(e.text)
        dic={
        "name":name,
        "role":role,
        "forum_posts":td[0].text,
        "following":td[1].text,
        "followers":td[2].text,
        "more_info":ch
        }
        n=20
        driver.get(url+"/images")
        images=get_images(driver,n)
        print(len(images))
        dic['images']=images
        self.user_details=dic
        driver.close()  
    def user_posts(self,url,n):
        urls=[]
        ta={}
        l=get_url_posts(url,n)
        print(len(l))
        i=1
        for e in l:
            po=post_data(e,url)
            if po[0]==[]:
                pass
            else:
                dic={"Post"+str(i):po[0]}
                ta.update(dic)
                urls+=po[1]
                i=i+1
        self.users_url=urls
        self.data=ta
        driver.close()     

        

