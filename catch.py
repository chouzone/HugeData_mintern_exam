# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    url = 'https://statfy.mol.gov.tw/index02.aspx'
    try:
        options = webdriver.ChromeOptions()
        
        #讓瀏覽器在背景執行（不會顯示出瀏覽器執行畫面）
        options.add_argument('--disable-javascript')
        
        # executable_path 輸入 web driver 執行檔的位置
        driver = webdriver.Chrome(chrome_options=options, \
                                  executable_path='chromedriver.exe')
        driver.set_page_load_timeout(60)
        driver.get(url)

        # 定位日期輸入欄位, 並輸入日期
        #element = driver.find_element_by_id('fromdate_TextBox')
        #element.send_keys('1090101')
        #element = driver.find_element_by_id('todate_TextBox')
        #element.send_keys('1101201')
        
        # 定位選單所在欄位並點擊
        element = driver.find_element_by_id('DropDownList3')
        element.click()
        
        element = driver.find_element_by_id('DropDownList4')
        element.click()

        # 巡覽選單, 點擊對應選項
        for option in element.find_elements_by_tag_name('option'):
            if option.text == '100':
                option.click()
# =============================================================================
#         for option in element.find_element_by_tag_name('option'):
#             if option.text == '1':
#                 option.click()
# =============================================================================

        # 點擊送出按鈕
        element = driver.find_element_by_id('Button1').click()

        # 等待目標表格出現
        #element = WebDriverWait(driver, 5).until(
        #    expected_conditions.presence_of_element_located((By.ID, 'House_GridView'))
        #)

        # page_source 可以回傳目前瀏覽器所看到的網頁文件
# =============================================================================
#         soup = BeautifulSoup(driver.page_source, 'html5lib')
#         table = soup.find(id='House_GridView')
#         for row in table.find_all('tr'):
#             print([s for s in row.stripped_strings])
# =============================================================================
    finally:
        driver = webdriver.Chrome(chrome_options=options, \
                                  executable_path='chromedriver.exe')
        driver.quit()  # 關閉瀏覽器, 結束 webdriver process