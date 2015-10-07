from selenium import webdriver
browser = webdriver.PhantomJS()
browser.set_window_size(1024,768)
browser.get('http://localhost:8000')

assert 'Django' in browser.title
