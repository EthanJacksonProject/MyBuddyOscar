from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup

blacklist = [
    "Thesis",
    "Special",
    "Doctoral",
    "Research",
    "Assistantship",
    "3741",
    "3710",
    "3043",
    "2031",
    "2026"
    ]

driver = webdriver.Chrome()
try:
    # Navigate to course page for Fall 2020 ECE 
    driver.get("https://oscar.gatech.edu/pls/bprod/bwckschd.p_disp_dyn_sched")
    assert "Select Term or Date Range" in driver.title
    elem = driver.find_element_by_name("p_term")
    driver.find_element_by_xpath("//select[@name='p_term']/option[text()='Fall 2020']").click()
    driver.find_element_by_xpath("//input[@value='Submit']").click()
    driver.find_element_by_xpath("//select[@name='sel_subj']/option[text()='Electrical & Computer Engr']").click()
    driver.find_element_by_xpath("//input[@value='Class Search']").click()


    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    courses = [element.text for element in soup.find_all(class_='ddtitle')]
    courses = [course for course in courses if not any(substring in course for substring in blacklist)]
    
    for course in courses:
        print(course)
    
except Exception as e:
    print(f"Something went wrong! {e}")
    driver.close()