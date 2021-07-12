from time import sleep
from selenium import webdriver  # pip install selenium
from selenium.webdriver import ActionChains
from secret import username, password
from selenium.webdriver.common.keys import Keys

# instructions for the bot will be the following
# open up UNBC login website with the use of chromedriver
# log into UNBC -> enter username, password
# navigate to add courses
# select all courses
# search
# get the source of the page which has all classes
# save page source to automated_scrape.txt
# done


def store_data_to_file(html):
    f = open("automated_scrape.txt", "w+")
    f.write(html)
    f.close()


class ScrapeBot:
    def __init__(self, username, pw):
        self.username = username
        self.pw = pw
        self.driver = webdriver.Chrome()

    def login(self):    # open up the unbc website and log in with provided username and password
        driver = self.driver
        driver.maximize_window()
        driver.get('https://www.unbc.ca/login')
        sleep(2)
        student_alumni_online_services_link = driver.find_element_by_xpath("//a[contains(text(), 'Student / Alumni Online Services')]")
        student_alumni_online_services_link.click()
        sleep(2)
        login_field = driver.find_element_by_xpath('//input[@name=\"username\"]')
        login_field.send_keys(username)
        sleep(1)
        pw_field = driver.find_element_by_xpath('//input[@name=\"password\"]')
        pw_field.send_keys(password)
        pw_field.send_keys(Keys.ENTER)
        sleep(2)

    def navigate(self):  # navigate through to add courses, get source of the page with all classes selected
        driver = self.driver
        driver.get('https://ssb.unbc.ca/ssb/bwskfcls.p_sel_crse_search')
        sleep(2)
        term_dropdown = driver.find_element_by_xpath("//select[@name=\"p_term\"]")  # select drop down
        term_dropdown.click()
        sleep(1)
        desired_term = driver.find_element_by_xpath("//option[@value=\"202001\"]")  # The format here is Year# Semester# where Semester# = 01 -> January Semester, 05 -> September Semester, 03 -> May Semester
        desired_term.click()
        sleep(1)
        submit_button = driver.find_element_by_xpath('//input[@value=\"Submit\"]')  # click submit
        submit_button.click()
        sleep(2)
        select_all_classes = driver.find_element_by_xpath("//select[@id='subj_id']/option[1]")  # this will select the very first element
        select_all_classes.click()
        sleep(1)
        ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()   # this is like hitting CTRL + a on the keyboard to select all classes
        sleep(1)
        section_search_button = driver.find_element_by_xpath('//input[@value=\"Section Search\"]')  # search all classes
        section_search_button.click()
        print('Page is loading, data will be extracted soon!')
        sleep(5)   # let everything load

    def get_data(self):
        driver = self.driver
        html_source = driver.page_source  # get the source of the page when all classes are loaded
        store_data_to_file(html_source)   # store data to text file


def run_get_source():  # assign the username and password that is in the secret file, let the bot scrape and save the data
    u = username
    p = password
    bot = ScrapeBot(u, p)
    bot.login()
    bot.navigate()
    bot.get_data()
    print('Page source has been saved successfully!')
