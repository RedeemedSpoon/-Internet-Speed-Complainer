from data import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SpeedTester:
    def __init__(self) -> None:
        self.get_browser()
        self.receive_result()
        self.pass_test()
        self.browser.quit()

    def get_browser(self):
        if BROWSER == "Firefox":
            self.browser = webdriver.Firefox()
        if BROWSER == "Chrome":
            self.browser = webdriver.Chrome()
        if BROWSER == "Edge":
            self.browser = webdriver.Edge()
        if BROWSER == "Safari":
            self.browser = webdriver.Safari()

    def receive_result(self):
        self.browser.get("https://www.speedtest.net/")
        self.browser.find_element(By.CSS_SELECTOR, ".start-button > a").click()
        time.sleep(AVG_SPEED)
        try:
            self.browser.find_element(By.CSS_SELECTOR, "button.pure-button").click()
        except:
            pass
            
        self.dl_speed = self.browser.find_element(By.CSS_SELECTOR, ".download-speed").text.split(".")[0]
        self.up_speed = self.browser.find_element(By.CSS_SELECTOR, ".upload-speed").text.split(".")[0]

    def pass_test(self):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        if int(self.dl_speed) < PROMISED_DL or int(self.up_speed) < PROMISED_UP:
            self.break_pormise = True
            self.passed = "Did not pass the promised internet speed"
        else:
            self.break_pormise = False
            self.passed = "Did pass the promised internet speed"

        self.log_text = f"\n{current_time}: Download Speed: {self.dl_speed}, Upload Speed: {self.up_speed} | {self.passed}"
        with open("file.log", "a") as logfile:
            logfile.write(self.log_text)

        if self.break_pormise:
            self.browser.get("https://twitter.com/i/flow/login"); time.sleep(2)
            self.browser.find_element(By.CSS_SELECTOR, ".r-30o5oe").send_keys(TWITTER_USERNAME); time.sleep(1)
            self.browser.find_element(By.CSS_SELECTOR, "div.css-18t94o4:nth-child(6)").click(); time.sleep(1)
            self.browser.find_element(By.CSS_SELECTOR, ".r-homxoj").send_keys(TWITTER_PASSWORD); time.sleep(1)
            self.browser.find_element(By.CSS_SELECTOR, ".r-19yznuf").click(); time.sleep(4)
            self.browser.find_element(By.CSS_SELECTOR, ".notranslate").send_keys(START_TWEET, f" {self.dl_speed}dl/{self.up_speed}up ", END_TWEET); time.sleep(1)
            self.browser.find_element(By.CSS_SELECTOR, "div.css-18t94o4:nth-child(4)").click(); time.sleep(1)


bot = SpeedTester()
