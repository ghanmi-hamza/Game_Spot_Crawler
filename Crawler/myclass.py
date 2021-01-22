from methods import *
from abc import ABC
class Driver(ABC):

    def get_user_info(self,url):
        pass
    
    def get_publications(self,url,n):
        pass
    
    def get_images(self,driver,n):
        pass

class GamespotDriver(Driver):
    def __init__(self):
        """Constructeur de notre classe"""
        pass
    
    def get_user_info(self,url,nb_images):
        options = webdriver.firefox.options.Options()
        #options.headless = True
        driver = webdriver.Firefox(executable_path=r"C:\Users\Hamza\Downloads\geckodriver.exe", options=options)
        driver.get(url)
        c=driver.find_element_by_xpath(".//*[@class= 'authorCard-name']").text
        name=c.split()[0]
        role=c.split()[2]
        td=driver.find_elements_by_xpath(".//td[@class= 'table__td']")
        info=driver.find_element_by_xpath(".//ul[@class= 'user-bits__list']")
        li=info.find_elements_by_xpath(".//li")
        ch=[]  
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
        driver.get(url+"images")
        images=self.get_images(driver,nb_images)
        #print(len(images))
        dic['images']=images
        self.user_details=dic
        driver.close()  
    def get_publications(self,url,n):
        urls=[]
        ta={}
        l=get_url_posts(url,n)
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
    def get_images(self,driver,n):
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

        

