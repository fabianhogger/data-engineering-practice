import requests
import pandas
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import argparse
import os


class downloader():
    def __init__(self,path=os.getcwd()+"/Downloads/",link="https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/",last_modified="2024-01-19 09:51",filename ="01001099999.csv"):
            self.path= os.getcwd()+"/Downloads/" if path is None else path
            self.link="https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/" if link is None else link
            self.last_modified="2024-01-19 09:51" if last_modified is None else last_modified 
            self.filename=filename 

    def driver_setup(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_argument("--disable-background-timer-throttling")
        chrome_options.add_argument("--disable-backgrounding-occluded-windows")
        chrome_options.add_argument("--disable-breakpad")
        chrome_options.add_argument("--disable-client-side-phishing-detection")
        chrome_options.add_argument("--disable-component-update")
        chrome_options.add_argument("--disable-default-apps")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-features=site-per-process")
        chrome_options.add_argument("--disable-hang-monitor")
        chrome_options.add_argument("--disable-ipc-flooding-protection")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-prompt-on-repost")
        chrome_options.add_argument("--disable-renderer-backgrounding")
        chrome_options.add_argument("--disable-sync")
        chrome_options.add_argument("--disable-translate")
        chrome_options.add_argument("--metrics-recording-only")
        chrome_options.add_argument("--no-first-run")
        chrome_options.add_argument("--safebrowsing-disable-auto-update")
        chrome_options.add_argument("--safebrowsing-disable-download-protection")
        chrome_options.add_argument("--disable-crash-reporter")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_experimental_option("prefs", {
        "download.default_directory": self.path
        })
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
    def find_file(self,driver):
        rows = driver.find_elements(By.TAG_NAME ,"td")
        for i in range(0,len(rows)):
            if rows[i].text==self.last_modified:
                row=rows[i-1]
                row.click()
                time.sleep(15)
                return row.text
        print("Didn't find file on the website")
        return None
    def analyze(self,filename):
        try:
                df = pd.read_csv(self.path+filename, low_memory=False)
                print(f"CSV file successfully read! {self.path+ filename}")
                df['HourlyDryBulbTemperature']=df['HourlyDryBulbTemperature'].apply(pd.to_numeric, errors='coerce').astype(float)
                maxval=df['HourlyDryBulbTemperature'].max()
                df=df.loc[df['HourlyDryBulbTemperature']==maxval]
                print(df)
        except FileNotFoundError:
                print(f"File not found: {self.path+ filename}")
                return None
    def download(self):
        driver=dn.driver_setup()
        try:
            driver.get(self.link)
            #wait for website to load
            driver.implicitly_wait(13)
            filename= dn.find_file(driver)
            if(filename):
                    dn.analyze(filename)
        except selenium.common.exceptions.NoSuchElementException:
            print("The link does not exist.")
        except selenium.common.exceptions.WebDriverException:
            print("An error occurred while navigating to the link.")
   

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Give link  directory where you wish to download  the file and last modified  value')
    # Define the arguments
    parser.add_argument('--timestamp', type=str, help='last modified')
    parser.add_argument('--path', type=str, help='download path')
    parser.add_argument('--link', type=str, help='link to scrap')
    parser.add_argument('--filename', type=str, help='filename optional')
    # Parse the arguments
    args = parser.parse_args()
    download_path=args.path 
    last_modified=args.timestamp
    filename=args.filename 
    link= args.link  
    print(args)
    print(filename)
    dn=downloader(path=download_path,link=link,last_modified=last_modified,filename=filename)
    dn.download()


    