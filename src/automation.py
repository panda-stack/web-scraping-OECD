from get_url_from_firstpage import Get_Url_From_FirstPage
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import pandas as pd
import time
# from http_request_randomizer.requests.proxy.requestProxy import RequestProxy


class Automation:
    urlsClass = Get_Url_From_FirstPage()
    urls = urlsClass.getUrl()
    # req_proxy = RequestProxy()
    # proxies = req_proxy.get_proxy_list()
    # PROXY = proxies[0].get_address()
    
    def getColumn(self):
        Automation.urls.sort()
        for url in Automation.urls:
            # webdriver.DesiredCapabilities.CHROME['proxy'] = {
                # "httpProxy":PROXY,
                # 'ftpProxy':PROXY,
                # "sslProxy":PROXY,
                # "proxyType":"MANUAL",
            # }
            driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')
            # url = Automation.urls[58] 
            if url == 'http://dx.doi.org/10.1787/0223bce2-en':
                continue
            elif url == 'http://dx.doi.org/10.1787/04e66921-en':
                continue
            elif url == 'http://dx.doi.org/10.1787/04e66921-en':
                continue
            print(url)
            driver.get(url)
            driverdata = driver
            try:
                csvlink=driver.find_element_by_link_text("CSV")
                csvlink.click()
                time.sleep(1)
                try:
                    s = driver.find_element_by_class_name("login")
                    print("Login needed")
                    
                except NoSuchElementException:
                    print("no login element exist")
                    
            except NoSuchElementException:
                print("No CSV element found")
            driver = driverdata
            
            try:
                datalink=driver.find_element_by_link_text("DATA")
                
                # for datalink in datalinks:
                datalink.click()  
                export = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "menubar-export")))
                Hover = ActionChains(driver).move_to_element(export)
                Hover.perform()
                csv = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "menuitemExportCSV")))
                csv.click()
                iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "DialogFrame")))
                driver.switch_to.frame(iframe)
                down = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "_ctl12_btnExportCSV")))
                down.click()
                time.sleep(10)
                driver.switch_to.default_content()
                driver.close()
                driver.quit()
            except NoSuchElementException:
                print("No DATA element found")
            except:
                driver.quit()
            driver.quit()
                    
        
# driver.quit()
c = Automation()
c.getColumn()