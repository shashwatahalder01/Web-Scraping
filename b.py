import pandas as pd
import unittest
import os.path
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from a import getdiff
import xlsxwriter
from bs4 import BeautifulSoup 

# def search():
#     options = Options()
#     options.add_argument('--no-sandbox')
#     options.add_argument('disable-infobars')
#     options.add_argument("--disable-extensions")
#     driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
#     driver.get("https://www.google.com/")

#     res = getdiff()
#     # print(res)
#     time.sleep(3)
#     qs = driver.find_element_by_xpath(
#         '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
#     qs.send_keys(res[2])
#     qs.send_keys(Keys.RETURN)
#     time.sleep(3)

#     products= driver.find_elements_by_class_name("LC20lb DKV0Md")
#     products = driver.find_elements_by_class_name("LC20lb DKV0Md")
#     productsname = []
#     for product in products:
#             productsname.append(product.text)
      

#     print(productsname)

#     time.sleep(3)


# search()


class BaseTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        # self.driver.get("https://www.google.com/")

    def test_page_item(self):
        res= getdiff()
        print(res)
        # # print(res);
        # time.sleep(3)
        # qs=self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        # qs.send_keys(res[2])
        # qs.send_keys(Keys.RETURN)
        # time.sleep(3)
        # # self.driver.find_element_by_xpath("//a[@aria-label='Page 2']").click()
        # products =self.driver.find_elements_by_class_name("LC20lb ")
        # # urls=self.driver.find_elements_by_tag_name("cite")
        # urls=self.driver.find_elements_by_class_name("tjvcx")
        # name = []
        # nurl=[]
        # for product,url in zip(products,urls):
        #     # print(product.text)
        #     name.append(product.text)
        #     nurl.append(url.text)
      
        # # del nurl[1::2]
        # print(len(name),nurl)
        # print(len(nurl))
        # # df=pd.DataFrame()
        # # df['Title']=name
        # # df['urls']=nurl
        # # df.to_excel(os.path.join(os.getcwd(),'data','c.xlsx'), index=False)
        # # time.sleep(3)

        # query = 'Mobile_10'

        title=[]
        links = [] # Initiate empty list to capture final results
            # Specify number of pages on google search, each page contains 10 #links
        for query in res:
            n_pages = 5 
            for page in range(0, n_pages):
                url = "http://www.google.com/search?q=" + query + "&start=" +      str((page - 1) * 10)
                self.driver.get(url)
                soup = BeautifulSoup(self.driver.page_source, 'html.parser')
                # soup = BeautifulSoup(r.text, 'html.parser')
                
                titles = soup.find_all('h3',class_="LC20lb DKV0Md")
                for l in titles:
                    title.append(l.text)
                # print(title)
                search = soup.find_all('div', class_="yuRUbf")
                for h in search:
                    links.append(h.a.get('href'))
                # print(links)
        print(len(title),len(links))
        df=pd.DataFrame()
        df['Title']=title
        df['urls']=links
        df.to_excel(os.path.join(os.getcwd(),'data','c.xlsx'), index=False)
            

    def tearDown(self):
        # self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    # unittest.TextTestRunner(verbosity=1).run(suite)
    unittest.main()
