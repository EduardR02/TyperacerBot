from selenium import webdriver
import time
import random
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException


class Typeracer:
    def __init__(self):
        self.driver = webdriver.Chrome("Your_path_to_chromedriver")
        self.play()

    def play(self):
        self.driver.get("https://play.typeracer.com/")
        time.sleep(2)

    def repeat_part(self):
        enter_race = self.driver.find_element_by_xpath('//*[@id="gwt-uid-1"]/a')
        enter_race.click()

        text = ""
        bar = None
        time.sleep(1)
        i = 0
        for i in range(5):
            try:
                remove_field = self.driver.find_element_by_xpath('/html/body/div[5]')
                remove_field.click()
                break
            except NoSuchElementException:
                time.sleep(1)
        found = False
        while not found:
            try:
                text = self.driver.find_element_by_xpath(f'//*[@id="gwt-uid-{i}"]/table/tbody/tr['
                                                         '2]/td/table/tbody/tr[1]/td/table/tbody/tr['
                                                         '1]/td/div/div/span[1]').text
                text += self.driver.find_element_by_xpath(f'//*[@id="gwt-uid-{i}"]/table/tbody/tr['
                                                          '2]/td/table/tbody/tr[1]/td/table/tbody/tr['
                                                          '1]/td/div/div/span[2]').text
                text += " "
                text += self.driver.find_element_by_xpath(f'//*[@id="gwt-uid-{i}"]/table/tbody/tr[2]/td/table/tbody/tr['
                                                          '1]/td/table/tbody/tr[1]/td/div/div/span[3]').text
                bar = self.driver.find_element_by_xpath(f'//*[@id="gwt-uid-{i}"]/table/tbody/tr[2]/td/table/tbody/tr['
                                                        f'2]/td/input')
                found = True
                print(i)
            except NoSuchElementException:
                i += 1
        print(text)

        bar.click()
        sending_text = False
        while not sending_text:
            try:
                t = time.time()
                increment = 6  # last working is 6
                for i in range(0, len(text), increment):
                    bar.send_keys(text[i:i + increment])
                    print(text[i: i + increment], end="", sep="")
                    time.sleep(random.randint(3, 5) * 0.033)
                sending_text = True
                print(time.time() - t)
            except ElementNotInteractableException:
                time.sleep(0.1)


if __name__ == "__main__":
    bot = Typeracer()
    while True:
        if input() == "q":
            print("lets go again")
            bot.repeat_part()
