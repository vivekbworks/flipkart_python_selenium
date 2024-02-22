from selenium import webdriver


def open_browser(browser_name):
    global driver
    if browser_name.lower() == 'chrome':
        driver = webdriver.Chrome()
    elif browser_name.lower() == 'firefox':
        driver = webdriver.Firefox()
    else:
        print("invalid browser. add correct browser name for eg firefox or chrome")
    return driver


