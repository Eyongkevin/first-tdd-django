# from django.test import LiveServerTestCase
# from selenium import webdriver

# class StudentTestCase(LiveServerTestCase):
#     def setUp(self) -> None:
#         """Sets before tests"""
#         self.browser = webdriver.Firefox()
#         self.browser.implicitly_wait(2)

#     def test_student_find_solos(self) -> None:
#         """
#         Test that a user can search for solos
#         """
#         # visit the home page of JMAD
#         home_page = self.browser.get(self.live_server_url + '/')
#         # see the name of the site in he heading.
#         brand_element = self.browser.find_element_by_css_selector('.navbar-brand')
#         self.assertEqual('JMAD', brand_element.text)
#         self.fail('Incomplete Test')

#     def tearDown(self) -> None:
#         """Clean after each test"""
#         self.browser.quit()
