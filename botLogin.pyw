from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException



def mainLogin(username_input,password_input,keyword_input,location_input):
    
    username = username_input.get()
    password = password_input.get()
    keyword  = keyword_input.get()
    location = location_input.get()

    #Selenium Chrome driver
    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=OFF')
    browser = webdriver.Chrome(ChromeDriverManager().install(),options=options)

    #LinkedIn Login Page
    browser.get('https://www.linkedin.com/login')

    #Entering input
    user_submit=browser.find_element_by_id('username')
    user_submit.send_keys(username)

    password_submit = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'password')))
    password_submit.send_keys(password)

    password_submit.submit()


    try:
        jobButton=browser.find_element_by_id('jobs-nav-item')
        jobButton.click()

    except NoSuchElementException:
        print("Login Failed")

    search(browser,keyword,location)


#Submitting data for Job search page
    
def search(browser,keyword,location):

    try:
        keyword_submit = browser.find_element_by_xpath("//input[contains(@aria-label,'Search jobs')]")
        keyword_submit.send_keys(keyword)


        location_submit = browser.find_element_by_xpath("//input[contains(@aria-label,'Search location')]")
        location_submit.clear()
        location_submit.send_keys(location)

    
        search = browser.find_element_by_xpath("//button[text()='Search']")
        search.click()

    
    except NoSuchElementException:
        print(" ")



    


    
