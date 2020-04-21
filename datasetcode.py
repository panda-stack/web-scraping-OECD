from get_url_from_firstpage import Get_Url_From_FirstPage
from selenium import webdriver

class datacode:
    
    urls = Get_Url_From_FirstPage.getUrl()
    print(urls)
    
d = datacode()
