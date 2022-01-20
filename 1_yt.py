import undetected_chromedriver.v2 as uc
import time

if __name__ == "__main__":
    driver = uc.Chrome()
    driver.get("https://irs.thsrc.com.tw/IMINT/?locale=tw")
    time.sleep(20)