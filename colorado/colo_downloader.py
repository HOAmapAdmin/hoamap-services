from asyncio.windows_events import NULL
from calendar import c
from multiprocessing.dummy import current_process
from operator import contains
import os
import time
import csv
import json
import pandas as pd
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def colo_downloader():
    
    print('\ncolo_downloader begins....')
    
    ## variables for downloading and moving the downloaded csv file
    download_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
    csv_file = 'HOA_-_Home_Owner\'s_Association_-_Active.csv'
    destination_file = r'C:\Users\Tim Fuller\GitHub\hoamap\homap-services\colorado\HOA-Active.csv'

    ## Initialize webdriver and options
    driver = webdriver.Chrome()                      
        
    ## launch state website and wait till UI elements are loaded
    driver.get("https://apps.colorado.gov/dre/licensing/Lookup/GenerateRoster.aspx")
    if not "eLicense Online" in driver.title:
        raise Exception("Unable to load GenerateRoster page!")

    ## Select 'Home Owners Associations' option,
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "ctl00_MainContentPlaceHolder_Label1").click()
    driver.implicitly_wait(10)

    ## Select 'HOA - Home Owner's Association - Active' option,
    driver.find_element(By.ID, "ctl00_MainContentPlaceHolder_ckbRoster3").click()
    driver.implicitly_wait(10)

    ## Select 'Continue' to generate list....
    driver.find_element(By.ID, "ctl00_MainContentPlaceHolder_btnRosterContinue").click()
    driver.implicitly_wait(120)

    ## Once the 'DownloadRoster' page has loaded, click CSV option,
    radioButton = driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='Comma']").click() 
    driver.implicitly_wait(120)

    ## Then click 'Download' option and download list of HOAs.
    downloadButton = driver.find_element(By.CLASS_NAME, "FileButtons").click()
    driver.implicitly_wait(240)
    driver.close()

    ## Wait for the download to finish
    while not os.path.exists(os.path.join(download_dir, csv_file)):
        time.sleep(1)

    ## Move CSV list to script dir
    source_file = download_dir + '\\' + csv_file
    os.rename(source_file, destination_file)
    
    print('\n.... colo_downloader complete.')
