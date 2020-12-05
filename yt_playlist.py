from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument("start-maximized")

#Disable Info-Bar
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

chrome_options.add_argument("--user-data-dir=C:\\Users\\Arun Venkatesh\\AppData\\Local\\Google\\Chrome\\User Data")
#chrome_options.add_argument("--profile-directory=Person 1")
browser = webdriver.Chrome(executable_path = 'C:/Users/Arun Venkatesh/Documents/Projects/Python Projects/chromedriver.exe', options=chrome_options)

#browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')

url = 'https://www.youtube.com/feed/library'
url2 = 'https://www.youtube.com/watch?v=VDvr08sCPOc&list=PLAldzxXBXnFA_k3pOlzUMtbvJi48IPMne'
browser.get(url2)

#browser.find_element_by_xpath('//*[@id="video-title"]').click()
#browser.find_element_by_id('thumbnail')