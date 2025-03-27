# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

class TestSmokeTest():
  def setup_method(self, method):
    options = Options()
    options.add_argument("--headless=new")
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_navigateAdminPage(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.set_window_size(1550, 830)
    self.driver.find_element(By.LINK_TEXT, "Admin").click()
    elements = self.driver.find_elements(By.ID, "username")
    assert len(elements) > 0
    self.driver.find_element(By.ID, "username").send_keys("tyler")
    self.driver.find_element(By.ID, "password").send_keys("tylerspassword")
    self.driver.find_element(By.CSS_SELECTOR, ".mysubmit:nth-child(4)").click()
  
  def test_navigateDirectoryPage(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.set_window_size(1550, 830)
    self.driver.find_element(By.LINK_TEXT, "Directory").click()
    self.driver.find_element(By.ID, "directory-grid").click()
    self.driver.find_element(By.ID, "directory-grid").click()
    element = self.driver.find_element(By.ID, "directory-grid")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".gold-member:nth-child(9) > img")
    assert len(elements) > 0
    self.driver.find_element(By.ID, "directory-list").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)")
    assert len(elements) > 0
  
  def test_navigateHomePage(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.set_window_size(1550, 830)
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".header-logo img")
    assert len(elements) > 0
    self.driver.find_element(By.CSS_SELECTOR, "body").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h1").text == "Teton Idaho"
    self.driver.find_element(By.CSS_SELECTOR, ".header-title > h2").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h2").text == "Chamber of Commerce"
    assert self.driver.title == "Teton Idaho CoC"
  
  def test_navigateHomePage2(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.set_window_size(1550, 830)
    self.driver.find_element(By.CSS_SELECTOR, "body").click()
    self.driver.find_element(By.CSS_SELECTOR, "body").click()
    self.driver.find_element(By.CSS_SELECTOR, "body").click()
    elements = self.driver.find_elements(By.LINK_TEXT, "Home")
    assert len(elements) > 0
    self.driver.find_element(By.CSS_SELECTOR, "header").click()
    elements = self.driver.find_elements(By.LINK_TEXT, "Join")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.LINK_TEXT, "Directory")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.LINK_TEXT, "Admin")
    assert len(elements) > 0
    self.driver.find_element(By.CSS_SELECTOR, ".spotlight1 > .centered-image").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight1 > .centered-image")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight1 > h4")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight1 > p:nth-child(3)")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight1 > p:nth-child(4)")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight2 > h4")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight2 img")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight2 img")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight2 > p:nth-child(3)")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight2 > p:nth-child(4)")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.LINK_TEXT, "Join Us!")
    assert len(elements) > 0
    self.driver.find_element(By.CSS_SELECTOR, ".main-join > p:nth-child(2)").click()
    self.driver.find_element(By.LINK_TEXT, "Join Us!").click()
  
  def test_navigateJoinPage(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.set_window_size(1550, 830)
    self.driver.find_element(By.LINK_TEXT, "Join").click()
    elements = self.driver.find_elements(By.NAME, "fname")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "fname").click()
    self.driver.find_element(By.NAME, "fname").send_keys("Tyler")
    self.driver.find_element(By.NAME, "lname").send_keys("Allred")
    self.driver.find_element(By.NAME, "bizname").click()
    self.driver.find_element(By.NAME, "bizname").send_keys("Tyler Allred\'s All Red Paints")
    self.driver.find_element(By.NAME, "biztitle").click()
    self.driver.find_element(By.NAME, "biztitle").send_keys("Owner")
    self.driver.find_element(By.NAME, "submit").click()
    elements = self.driver.find_elements(By.NAME, "email")
    assert len(elements) > 0
  
