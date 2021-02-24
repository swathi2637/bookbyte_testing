import unittest
from selenium import webdriver
import requests
from selenium.webdriver.support.wait import WebDriverWait


class InputFormsCheck(unittest.TestCase):

    # Opening browser.
    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\Users\swathi\Downloads\chromedriver\chromedriver')
        wait = WebDriverWait(self.driver, 10)

    def test_singleInputField(self):
        pageUrl = "https://www.amazon.com/sp?seller=A2N51X1QYGFUPK"
        driver = self.driver
        driver.maximize_window()
        driver.get(pageUrl)

        # Finding "Single input form" input text field by xpath. And sending keys(entering data) in it.
        addressfromUI = driver.find_element_by_xpath("//*[@id='seller-profile-container']/div[2]/div/ul/li[2]/span/ul/li[1]/span")
        print(addressfromUI.text)

        self.assertEqual("2800 Pringle Rd SE Suite 100",addressfromUI.text,"Invalid address on UI")

    def test_bookByteSearchBar(self):
        pageUrl = "https://www.bookbyte.com/advancedsearch.aspx"
        driver = self.driver
        driver.maximize_window()
        driver.get(pageUrl)
        input_box = driver.find_element_by_id("ctl00_ContentPlaceHolder1_tbKeywords")
        # write search string
        input_box.send_keys("college")
        # click on search
        search_button = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ibSearch')
        # sometime search button hidden behind cookies pop-up, so clicking it using java script
        driver.execute_script("arguments[0].click();", search_button)
        # get results -> number of records
        number_of_record_menu = driver.find_elements_by_id("ctl00_ContentPlaceHolder1_lblTotalRecords")

        self.assertTrue(len(number_of_record_menu) > 0, "Search is not working")

    def test_googleBookSearch(self):
        book_authors = ['Brian W. Kernighan', 'Dennis Ritchie']
        book_url = 'https://www.googleapis.com/books/v1/volumes?q=isbn=013110362'
        response = requests.request('GET', book_url)
        json_response = response.json()
        for data in json_response['items']:
            if data['volumeInfo']['title'] == 'C Programming Language':
                self.assertEqual(sorted(data['volumeInfo']['authors']), book_authors,
                                 "C Programming Language authors not matched")



    # Closing the browser.
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()