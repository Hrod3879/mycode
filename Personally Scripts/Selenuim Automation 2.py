from seleniumbase import BaseCase

class GoogleSearchAndNavigation(BaseCase):
    def test_google_search_and_navigation(self):
        # Open the Google website
        self.open("https://www.google.com")

        # Find the search input element by XPath and type "Python"
        self.type('//*[@id="tsf"]//input[@name="q"]', "Python")
        self.press_enter()

        # Wait for the search results to load
        self.sleep(5)

        # Click on the link containing "Downloads"
        self.click('partial link=Downloads')

        # Wait for the page to load
        self.sleep(7)

        # Refresh the web page
        self.refresh_page()

        # Use the back button
        self.go_back()

        # Wait for the page to load
        self.sleep(5)

        # Use the forward button
        self.go_forward()

        # Wait for the page to load
        self.sleep(3)

        # Scroll down to the bottom of the page
        self.scroll_to_bottom()

        # Wait for a few seconds
        self.sleep(2)

        # Scroll back up to the top of the page
        self.scroll_to_top()
