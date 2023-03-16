import random
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TinderBot:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')

        time.sleep(2)

        try:
            cookies_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
            cookies_btn.click()
        except:
            pass

        time.sleep(2)

        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        fb_btn.click()

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys('YOUR FACEBOOK EMAIL')
        password_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_in.send_keys('YOUR FACEBOOK PASSWORD')
        password_in.send_keys(Keys.ENTER)

        self.driver.switch_to_window(base_window)

        time.sleep(5)

        try:
            popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            popup_1.click()
        except:
            pass

        time.sleep(2)

        try:
            popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            popup_2.click()
        except:
            pass

        time.sleep(2)

        try:
            popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button')
            popup_3.click()
        except:
            pass

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            time.sleep(1)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()


if __name__ == '__main__':
    bot = TinderBot()
    bot.login()
    bot.auto_swipe()
