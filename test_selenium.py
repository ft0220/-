from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://jp.kabumap.com/servlets/kabumap/Action?SRC=basic/top/base&codetext=7203")
unit=driver.find_element_by_css_selector('#minUnit').text
print(unit)