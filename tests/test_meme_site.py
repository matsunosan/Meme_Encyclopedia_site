import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


class TestMemeEncyclopediaSite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.get("http://127.0.0.1:5500/index.html")

    def setUp(self):
        self.driver.get("http://127.0.0.1:5500/index.html")

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_home_page_loads(self):
        """Test that the homepage loads correctly."""
        WebDriverWait(self.driver, 10).until(EC.title_contains("Meme Encyclopedia"))
        self.assertIn("Meme Encyclopedia", self.driver.title)

    def test_contact_form_navigation(self):
        """Test if the contact page link navigates correctly."""
        contact_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "contactLink")))
        contact_link.click()
        WebDriverWait(self.driver, 10).until(EC.title_contains("Contact"))

    def test_login_dropdown_functionality(self):
        """Test if login dropdown can be toggled."""
        login_button = self.driver.find_element(By.ID, "loginButton")
        login_button.click()

        dropdown = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "loginDropdown"))
        )
        self.assertTrue(dropdown.is_displayed(), "Login dropdown not visible.")

    def test_meme_category_filter(self):
        """Test if the meme filter dropdown filters the memes correctly."""
        driver = self.driver
        try:
            # Locate the filter dropdown button and click it
            filter_dropdown = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "categoryButton"))
            )
            filter_dropdown.click()

            # Select the "Trends" filter option
            trend_option = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@data-tag='trends']"))
            )
            trend_option.click()

            # Verify that only meme cards in the "Trends" category are displayed
            filtered_memes = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "card-link"))
            )

            # Check that memes are correctly filtered
            for meme in filtered_memes:
                categories = meme.get_attribute("data-tags")  # This will be a string like "trends, images"
                if "trends" in categories:
                    self.assertTrue(meme.is_displayed())  # 'trends' memes should be visible
                else:
                    self.assertFalse(meme.is_displayed())  # Non-'trends' memes should be hidden

        except Exception as e:
            self.fail(f"Dropdown filter test failed: {str(e)}")


    def test_meme_details_page(self):
        """Test if a meme details page opens when a meme is clicked."""
        driver = self.driver
        try:
            # Click on the first meme card link (assumed to be correct navigation)
            first_meme_card = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "card-link"))
            )
            first_meme_card.click()

            # Wait for the page to load by checking the URL contains 'meme1.html'
            WebDriverWait(driver, 10).until(EC.url_contains("meme1.html"))
            current_url = driver.current_url
            print(f"Current URL after click: {current_url}")

            # Wait for the H1 element in the details page to appear
            meme_title = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "h1"))
            )

            # Verify the H1 text
            self.assertEqual(meme_title.text, "Cerveza Cristal Beer")

        except Exception as e:
            self.fail(f"Meme details page test failed: {str(e)}")



if __name__ == "__main__":
    unittest.main()
