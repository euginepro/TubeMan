import random
import time
import traceback
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from user_agents import UserAgents
from android_user_agents import UserAgentManager

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium import webdriver
from tube_links import TubeLinkManager

siteLinkMain = "https://hub.euginetech.com/"


def loop():
    try:
        while True:
            run_browser()
    except:
        loop()


def run_browser():
    global custom_ua, browser, mobile_device
    try:

        print("=====session start=====")
        numb = random.choice([0, 1])
        print("Selected Choice: " + str(numb))
        if numb == 0:
            custom_ua = UserAgentManager().get_phone_user_agent()
            mobile_device = True
            print("Using Android Mobile: " + custom_ua)
        else:
            custom_ua = UserAgents().get_user_agent()
            print("Using PC / iOS: " + custom_ua)

        chrome_options = Options()
        chrome_options.add_argument(f"user-agent={custom_ua}")
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

        browser.set_window_size(random.randint(900, 2000), random.randint(900, 1080))
        browser.get(TubeLinkManager().get_link())
        # browser.get("https://www.youtube.com/watch?v=L7G0OfJUON8")

        print("> Wait 5 seconds")
        time.sleep(5)
        print("Done")
        print("Current Page: " + browser.title)

        try:
            cookie_consent_button = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                "/html/body/div[2]/ytm-consent-bump-v2-renderer/div/div[2]/div[3]/ytm-button-renderer[1]/button/yt-touch-feedback-shape/div/div[2]")
                                               ))
            cookie_consent_button.click()
            print("Consent Success")
        except:
            print("No Cookie Consent Button")
        time.sleep(2)

        try:
            cookie_consent_button2 = WebDriverWait(browser, 1).until(
                EC.presence_of_element_located((By.XPATH,
                                                "/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")
                                               ))
            cookie_consent_button2.click()
            print("Consent Success")
        except:
            print("No Cookie Consent Button2")
        time.sleep(2)

        try:
            aria_label_value = "Play"
            play_button = WebDriverWait(browser, 60).until(
                EC.presence_of_element_located((By.XPATH,
                                                f"//*[@aria-label='{aria_label_value}']")
                                               ))
            play_button.click()
            print("Play Success")
        except:
            print("No Play Button")

        try:
            play_button = WebDriverWait(browser, 1).until(
                EC.presence_of_element_located((By.XPATH,
                                                "//*[@id=\"movie_player\"]/div[2]/button")
                                               ))
            play_button.click()
            print("Play2 Success")
        except:
            print("No Play Button2")
        time.sleep(2)
        try:
            unmute_button = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.XPATH,
                                                "//*[@id=\"movie_player\"]/button/div")
                                               ))
            unmute_button.click()
            print("Unmute Success")
        except:
            print("No Unmute Button")

        print("Trying to enter full screen")
        doc_body = browser.find_element(By.TAG_NAME, "body")
        doc_body.send_keys("f")

        print("Watching Video")
        time.sleep(random.randint(200, 1500))
        print("> Done")
        browser.quit()
        print("====End Session====")
        wait_time = random.randint(30, 120)
        print(f"Waiting for {wait_time}s ..")
        time.sleep(wait_time)

    except Exception as e:
        print("Error occurred. Retrying")
        traceback.print_exc()
        browser.quit()


loop()
