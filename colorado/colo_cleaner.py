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
# from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

input_file_name = F'colorado\HOA-Active'

downloaded_csv_file = F'{input_file_name}.csv'

pre_clean_csv_file = F'{input_file_name}_pre_clean.csv'

remove_row_csv_file = F'{input_file_name}_remove_row.csv'

convert_ascii_to_utf8_csv_file = F'{input_file_name}_convert_ascii_to_utf8.csv'

clean_csv_file = F'{input_file_name}_clean.csv'

def colo_clean():
    print('\ncolo_clean started....')
    
    remove_bad_rows(downloaded_csv_file, remove_row_csv_file)
    
    encode_utf8(remove_row_csv_file, convert_ascii_to_utf8_csv_file)
    
    print('\ncolo_clean done.')


def remove_bad_rows(input_file, output_file):
    
    print('\nremove_bad_rows begins....')
    
    clean_data = []
    reader = None
    with open(input_file, 'r') as f:
        reader = f.readlines()
        
    print(f'\nreader size: {len(reader)}')
    
    for i in range(len(reader)):
        if i == 7132:
            print(F'\nrow found: {reader[i]}')
            continue
        else:
            clean_data.append(reader[i])

    print(f'\nclean_data size: {len(clean_data)}')

    with open(output_file, 'w') as f:
        f.writelines(clean_data)
    
    print('\nremove_bad_rows done.')


def encode_utf8(input_file, output_file):
    
    print('\ncencode_utf8 begins....')
    
    decoded_data = []
    with open(input_file, 'r') as f:
        reader = f.readlines()
        
        for row in reader:
            row = row.replace('&amp;', '&')
            decoded_data.append(row)
            
    with open(output_file, 'w') as f:
        f.writelines(decoded_data)
    
    print('\nencode_utf8 done.')


def convert_ascii_to_utf8(input_file, output_file):

    print('\nconvert_ascii_to_utf8 begins....')

    decoded_data = []
    with open(input_file, 'r') as f:
        reader = f.readlines()
        
        for row in reader:
            decoded_row = str(row).encode('utf-8')
            decoded_data.append(decoded_row)
            
    with open(output_file, 'w') as f:
        f.writelines(decoded_data)

    print('\nconvert_ascii_to_utf8 done.')
