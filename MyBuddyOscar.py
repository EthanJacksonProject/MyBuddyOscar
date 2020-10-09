from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# This requires a selenium web driver to function. See here:
# https://www.selenium.dev/documentation/en/webdriver/driver_requirements/

# These have to match what Oscar has in the HTML
term = "fall 2020"
major = "Electrical & Computer Engr"

# Ignores 100's of irrelevant courses - modify as needed
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
    "2026",
]

driver = webdriver.Chrome()
try:
    driver.get("https://oscar.gatech.edu/pls/bprod/bwckschd.p_disp_dyn_sched")
    assert "Select Term or Date Range" in driver.title
    elem = driver.find_element_by_name("p_term")
    driver.find_element_by_xpath(
        f"//select[@name='p_term']/option[text()={term}]"
    ).click()  # get term
    driver.find_element_by_xpath("//input[@value='Submit']").click()  # submit
    driver.find_element_by_xpath(
        f"//select[@name='sel_subj']/option[text()={major}]"
    ).click()  # select major
    driver.find_element_by_xpath("//input[@value='Class Search']").click()  # submit

    # Pass the loaded html to beautifulSoup for parsing
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    courses = [element.text for element in soup.find_all(class_="ddtitle")]
    courses = [
        course
        for course in courses
        if not any(substring in course for substring in blacklist)
    ]  # apply blacklist

    for course in courses:
        print(course)

except Exception as e:
    print(f"Something went wrong! {e}")
    driver.close()
