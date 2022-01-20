# import undetected_chromedriver.v2 as uc
import time
# from seleniumwire import webdriver  # 單純的selenium
from seleniumwire.undetected_chromedriver.v2 import Chrome

if __name__ == "__main__":
    driver = Chrome()
    driver.get("https://www.youtube.com/watch?v=Z2Z9V-4DMGw")
    driver.find_element_by_class_name("ytp-play-button").click()
    time.sleep(3)
    for req in driver.requests:
        print(req.url)
        if req.response is not None:
            print(req.response.headers["Content-Type"])
        print("-" * 30)