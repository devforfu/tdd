from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_and_empty_list_items(self):
        self.browser.get(self.server_url)
        self.browser.find_element_by_id("id_new_item").send_keys('\n')

        # home page refreshes, and there is an error message
        error = self.browser.find_element_by_css_selector(".has-error")
        self.assertEqual(error.text, "You can't have an empty list item")

        # item submission without error
        self.browser.find_element_by_id("id_new_item").send_keys("Buy milk\n")
        self.check_for_row_in_list_table("1: Buy milk")

        self.browser.find_element_by_id("id_new_item").send_keys('\n')

        # check if first item is still here
        self.check_for_row_in_list_table("1: Buy milk")

        # same error message
        error = self.browser.find_elements_by_css_selector(".has-error")
        self.assertEqual(error.text, "You can't have an empty list item")

        self.browser.find_element_by_id("id_new_item").send_keys("Make tea\n")
        self.check_for_row_in_list_table("1: Buy milk")
        self.check_for_row_in_list_table("2: Make tea")
