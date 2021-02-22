import unittest
from selenium import webdriver


class InputFormsCheck(unittest.TestCase):

    # Opening browser.
    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\Users\swathi\Downloads\chromedriver\chromedriver')

    def test_singleInputField(self):
        pageUrl = "https://www.amazon.com/sp?seller=A2N51X1QYGFUPK"
        driver = self.driver
        driver.maximize_window()
        driver.get(pageUrl)

        # Finding "Single input form" input text field by xpath. And sending keys(entering data) in it.
        addressfromUI = driver.find_element_by_xpath("//*[@id='seller-profile-container']/div[2]/div/ul/li[2]/span/ul/li[1]/span")
        print(addressfromUI.text)

        self.assertEqual("2800 Pringle Rd SE Suite 100",addressfromUI.text,"Invalid address on UI")

    # Closing the browser.
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()