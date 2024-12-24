import random
import pytest
from selenium.common import StaleElementReferenceException

from tests.conftest import logger
from tests.test_form import TestForm
from utils import common_functions as cf

# XPATHS
input_text_text_xpath = '//android.widget.TextView[@resource-id="com.example.applicationform:id/inputTextView"]'
dropdown_selection_text_xpath = '//android.widget.TextView[@resource-id="com.example.applicationform:id/dropdownTextView"]'
radio_button_selection_text_xpath = '//android.widget.TextView[@resource-id="com.example.applicationform:id/radioTextView"]'
checkbox_selection_text_xpath = '//android.widget.TextView[@resource-id="com.example.applicationform:id/checkboxesTextView"]'

@pytest.mark.usefixtures("setup", "class_setup")
class TestResult(TestForm):

    def test_saved_results(self):
        try:
            valid_username_value, dropdown_random_choice_text, radio_button_random_choice_text, checkbox_random_choice_text = self.fill_all_fields()
            input_text_text = (cf.find_element(self.driver, "xpath", input_text_text_xpath)).text
            dropdown_selection_text = (cf.find_element(self.driver, "xpath", dropdown_selection_text_xpath)).text
            radio_button_selection_text = (cf.find_element(self.driver, "xpath", radio_button_selection_text_xpath)).text
            checkbox_selection_text = (cf.find_element(self.driver, "xpath", checkbox_selection_text_xpath)).text

            assert input_text_text == f"Input Text: {valid_username_value}", "Data Mismatch"
            assert dropdown_selection_text == f"Dropdown Selection: {dropdown_random_choice_text}", "Data Mismatch"
            assert radio_button_selection_text == f"Selected Radio Option: {radio_button_random_choice_text}", "Data Mismatch"
            assert checkbox_selection_text == f"Selected Checkboxes: {checkbox_random_choice_text}", "Data Mismatch"

        except AssertionError as e:
            logger.error(f"Assertion error: : {e}", exc_info=True)
            raise
        except StaleElementReferenceException as e:
            logger.error(f"Element is no longer attached to the DOM: {e}", exc_info=True)
            raise
        except Exception as e:
            logger.error(f"An error occurred: : {e}", exc_info=True)
            raise