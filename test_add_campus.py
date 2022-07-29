# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import unittest


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_campus(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_campus(self):
        wd = self.wd
        wd.get(
            "https://auth.stage.illumidesk.xyz/u/login?state=hKFo2SAzdFhTUzlFNWVEV2RhLWdXTUxJbkd0QVk2MndPdExOV6Fur3VuaXZlcnNhbC1sb2dpbqN0aWTZIDA0b2hFR0EwT2p3aFA3LXd2RktXOWVxNksxYWVXMnZio2NpZNkgOVQ2TUFuNHNJZTBXbUtwTHdjdjhpN2h4OE90ZG5yamM")
        wd.find_element(By.ID, "username").click()
        wd.find_element(By.ID, "username").clear()
        wd.find_element(By.ID, "username").send_keys("adilie.shemshedinova@gmail.com")
        wd.find_element(By.XPATH,
                        "(.//*[normalize-space(text()) and normalize-space(.)='Email address'])[1]/preceding::header[1]").click()
        wd.find_element(By.ID, "password").click()
        wd.find_element(By.ID, "password").clear()
        wd.find_element(By.ID, "password").send_keys("Adika123")
        wd.find_element(By.NAME, "action").click()
        wd.find_element(By.XPATH,
                        "//div[@id='root']/div/div/div/div/div/div/div/div/section/section/main/div/div/div/button").click()
        wd.find_element(By.NAME, "title").click()
        wd.find_element(By.NAME, "title").clear()
        wd.find_element(By.NAME, "title").send_keys("New")
        wd.find_element(By.XPATH,
                        "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::button[1]").click()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
