# import undetected_chromedriver.v2 as uc
import time
# from seleniumwire import webdriver  # 單純的selenium
from seleniumwire.undetected_chromedriver.v2 import Chrome

if __name__ == "__main__":
    driver = Chrome()
    driver.get("https://www.youtube.com/watch?v=Z2Z9V-4DMGw")
    driver.find_element_by_class_name("ytp-play-button").click()
    # 要保險的跳過廣告, 多等幾秒
    time.sleep(10)

    audiourl, videourl = None, None
    for req in driver.requests:
        print(req.url)
        if req.response is not None:
            ct = req.response.headers["Content-Type"]
            if ct is not None and "video" in ct:
                videourl = req.url
            if ct is not None and "audio" in ct:
                audiourl = req.url
        print("-" * 30)

    import re
    # r: 不做任何轉換 \n就是兩個字
    videourl = re.sub(r"range=.+&", "", videourl)
    audiourl = re.sub(r"range=.+&", "", audiourl)
    print("video:", videourl)
    print("audio:", audiourl)

