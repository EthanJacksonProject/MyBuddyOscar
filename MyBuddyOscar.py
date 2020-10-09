from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
try:
    driver.get("https://oscar.gatech.edu/pls/bprod/bwckschd.p_disp_dyn_sched")
    assert "Select Term or Date Range" in driver.title
    elem = driver.find_element_by_name("p_term")
    driver.find_element_by_xpath("//select[@name='p_term']/option[text()='Fall 2020']").click()
    driver.find_element_by_xpath("//input[@value='Submit']").click()
    driver.find_element_by_xpath("//select[@name='sel_subj']/option[text()='Electrical & Computer Engr']").click()

    
except Exception as e:
    print(f"Something went wrong! {e}")
    driver.close()