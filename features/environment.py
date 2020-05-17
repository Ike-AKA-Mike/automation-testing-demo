from selenium import webdriver
from selenium.webdriver.firefox.options import options

def before_all(context):
	context.browser = webdriver.Firefox()
	context.browser.maximize_window()

def after_all(context):
	context.browser.quit()