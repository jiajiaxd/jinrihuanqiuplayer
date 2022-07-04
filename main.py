import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By as by
from webdriver_manager.chrome import ChromeDriverManager

if __name__ == '__main__':
    print("今日环球自动播放器 播放最新新闻 正在初始化...")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    print("初始化完毕，开始执行任务")
    driver.maximize_window()
    driver.get("https://tv.cctv.com/lm/index.shtml?spm=C28340.P2qo7O8Q1Led.EEfEAhEnQFPl.25#datapd=&datafl=%E6%96%B0%E9%97%BB&dataszm=")
    driver.find_element(by.CSS_SELECTOR,
                        "li:nth-of-type(15) > .text > .biref > a[target='_blank']").click()
    os.system("pause")

