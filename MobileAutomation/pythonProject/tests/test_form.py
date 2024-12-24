import random
import pytest
from selenium.common import StaleElementReferenceException

from tests.test_login import TestLogin
from utils import common_functions as cf
from conftest import logger, class_setup, setup



# XPATHS
input_text_field_id_xpath = '//android.widget.EditText[@resource-id="com.example.applicationform:id/inputField"]'
submit_button_xpath = '//android.widget.Button[@resource-id="com.example.applicationform:id/submitButton"]'
select_an_option_text_dropdown_button_xpath = '//android.widget.Spinner[@resource-id="com.example.applicationform:id/dropdown"]'
dropdown_options_xpath = '//android.widget.CheckedTextView[@resource-id="android:id/text1"]'
radio_button_xpath = '//*[@class="android.widget.RadioButton"]'
checkbox_xpath = '//*[@class="android.widget.CheckBox"]'
enter_all_fields_error_message_text_xpath = '//android.widget.TextView[@resource-id="com.example.applicationform:id/errorText"]'


@pytest.mark.usefixtures("setup", "class_setup")
class TestForm(TestLogin):

    def fill_all_fields(self):
        try:
            for row in self.data_sheet.iter_rows(min_row=2):
                valid_username_value = row[4].value
                self.test_logging_with_registered_phone_number()

                input_field = cf.find_element(self.driver, "xpath", input_text_field_id_xpath)
                input_field.send_keys(valid_username_value)

                select_an_option_text_dropdown_button = cf.find_element(self.driver, "xpath", select_an_option_text_dropdown_button_xpath)
                cf.click_element(self.driver, select_an_option_text_dropdown_button)

                dropdown_options = cf.find_elements(self.driver, "xpath", dropdown_options_xpath)
                dropdown_random_choice = random.choice(dropdown_options)
                dropdown_random_choice_text = dropdown_random_choice.text
                cf.click_element(self.driver, dropdown_random_choice)

                radio_button = cf.find_elements(self.driver, "xpath", radio_button_xpath)
                radio_button_random_choice = random.choice(radio_button)
                radio_button_random_choice_text = radio_button_random_choice.text
                cf.click_element(self.driver, radio_button_random_choice)

                checkbox = cf.find_elements(self.driver, "xpath", checkbox_xpath)
                checkbox_random_choice = random.choice(checkbox)
                checkbox_random_choice_text = checkbox_random_choice.text
                cf.click_element(self.driver, checkbox_random_choice)

                submit_button = cf.find_element(self.driver, "xpath", submit_button_xpath)
                cf.click_element(self.driver, submit_button)
            return valid_username_value, dropdown_random_choice_text, radio_button_random_choice_text, checkbox_random_choice_text
        except AssertionError as e:
            logger.error(f"Assertion error: : {e}", exc_info=True)
            raise
        except StaleElementReferenceException as e:
            logger.error(f"Element is no longer attached to the DOM: {e}", exc_info=True)
            raise
        except Exception as e:
            logger.error(f"An error occurred: : {e}", exc_info=True)
            raise

    def test_missing_input_field(self):
        try:
            self.test_logging_with_registered_phone_number()

            select_an_option_text_dropdown_button = cf.find_element(self.driver, "xpath", select_an_option_text_dropdown_button_xpath)
            cf.click_element(self.driver, select_an_option_text_dropdown_button)

            dropdown_options = cf.find_elements(self.driver, "xpath", dropdown_options_xpath)
            dropdown_random_choice = random.choice(dropdown_options)
            cf.click_element(self.driver, dropdown_random_choice)

            radio_button = cf.find_elements(self.driver, "xpath", radio_button_xpath)
            radio_button_random_choice = random.choice(radio_button)
            cf.click_element(self.driver, radio_button_random_choice)

            checkbox = cf.find_elements(self.driver, "xpath", checkbox_xpath)
            checkbox_random_choice = random.choice(checkbox)
            cf.click_element(self.driver, checkbox_random_choice)

            submit_button = cf.find_element(self.driver, "xpath", submit_button_xpath)
            cf.click_element(self.driver, submit_button)

            error_message = cf.find_element(self.driver, "xpath", enter_all_fields_error_message_text_xpath)
            assert error_message.text == "Please enter all the fields.", "Error message not displayed as expected."
        except AssertionError as e:
            logger.error(f"Assertion error: : {e}", exc_info=True)
            raise
        except StaleElementReferenceException as e:
            logger.error(f"Element is no longer attached to the DOM: {e}", exc_info=True)
            raise
        except Exception as e:
            logger.error(f"An error occurred: : {e}", exc_info=True)
            raise

    def test_missing_dropdown(self):
        try:
            for row in self.data_sheet.iter_rows(min_row=2):
                valid_username_value = row[4].value
                self.test_logging_with_registered_phone_number()

                input_field = cf.find_element(self.driver, "xpath", input_text_field_id_xpath)
                input_field.send_keys(valid_username_value)

                radio_button = cf.find_elements(self.driver, "xpath", radio_button_xpath)
                radio_button_random_choice = random.choice(radio_button)
                cf.click_element(self.driver, radio_button_random_choice)

                checkbox = cf.find_elements(self.driver, "xpath", checkbox_xpath)
                checkbox_random_choice = random.choice(checkbox)
                cf.click_element(self.driver, checkbox_random_choice)

                submit_button = cf.find_element(self.driver, "xpath", submit_button_xpath)
                cf.click_element(self.driver, submit_button)

                error_message = cf.find_element(self.driver, "xpath", enter_all_fields_error_message_text_xpath)
                assert error_message.text == "Please enter all the fields.", "Error message not displayed as expected."
        except AssertionError as e:
            logger.error(f"Assertion error: : {e}", exc_info=True)
            raise
        except StaleElementReferenceException as e:
            logger.error(f"Element is no longer attached to the DOM: {e}", exc_info=True)
            raise
        except Exception as e:
            logger.error(f"An error occurred: : {e}", exc_info=True)
            raise

    def test_missing_radio_button(self):
        try:
            for row in self.data_sheet.iter_rows(min_row=2):
                valid_username_value = row[4].value
                self.test_logging_with_registered_phone_number()

                input_field = cf.find_element(self.driver, "xpath", input_text_field_id_xpath)
                input_field.send_keys(valid_username_value)

                select_an_option_text_dropdown_button = cf.find_element(self.driver, "xpath", select_an_option_text_dropdown_button_xpath)
                cf.click_element(self.driver, select_an_option_text_dropdown_button)

                dropdown_options = cf.find_elements(self.driver, "xpath", dropdown_options_xpath)
                dropdown_random_choice = random.choice(dropdown_options)
                cf.click_element(self.driver, dropdown_random_choice)

                checkbox = cf.find_elements(self.driver, "xpath", checkbox_xpath)
                checkbox_random_choice = random.choice(checkbox)
                cf.click_element(self.driver, checkbox_random_choice)

                submit_button = cf.find_element(self.driver, "xpath", submit_button_xpath)
                cf.click_element(self.driver, submit_button)

                error_message = cf.find_element(self.driver, "xpath", enter_all_fields_error_message_text_xpath)
                assert error_message.text == "Please enter all the fields.", "Error message not displayed as expected."
        except AssertionError as e:
            logger.error(f"Assertion error: : {e}", exc_info=True)
            raise
        except StaleElementReferenceException as e:
            logger.error(f"Element is no longer attached to the DOM: {e}", exc_info=True)
            raise
        except Exception as e:
            logger.error(f"An error occurred: : {e}", exc_info=True)
            raise

    def test_missing_checkbox(self):
        try:
            for row in self.data_sheet.iter_rows(min_row=2):
                valid_username_value = row[4].value
                self.test_logging_with_registered_phone_number()

                input_field = cf.find_element(self.driver, "xpath", input_text_field_id_xpath)
                input_field.send_keys(valid_username_value)

                select_an_option_text_dropdown_button = cf.find_element(self.driver, "xpath", select_an_option_text_dropdown_button_xpath)
                cf.click_element(self.driver, select_an_option_text_dropdown_button)

                dropdown_options = cf.find_elements(self.driver, "xpath", dropdown_options_xpath)
                dropdown_random_choice = random.choice(dropdown_options)
                cf.click_element(self.driver, dropdown_random_choice)

                radio_button = cf.find_elements(self.driver, "xpath", radio_button_xpath)
                radio_button_random_choice = random.choice(radio_button)
                cf.click_element(self.driver, radio_button_random_choice)

                submit_button = cf.find_element(self.driver, "xpath", submit_button_xpath)
                cf.click_element(self.driver, submit_button)

                error_message = cf.find_element(self.driver, "xpath", enter_all_fields_error_message_text_xpath)
                assert error_message.text == "Please enter all the fields.", "Error message not displayed as expected."
        except AssertionError as e:
            logger.error(f"Assertion error: : {e}", exc_info=True)
            raise
        except StaleElementReferenceException as e:
            logger.error(f"Element is no longer attached to the DOM: {e}", exc_info=True)
            raise
        except Exception as e:
            logger.error(f"An error occurred: : {e}", exc_info=True)
            raise

    def test_empty_form_submission(self):
        try:
            self.test_logging_with_registered_phone_number()

            submit_button = cf.find_element(self.driver, "xpath", submit_button_xpath)
            cf.click_element(self.driver, submit_button)

            error_message = cf.find_element(self.driver, "xpath", enter_all_fields_error_message_text_xpath)
            assert error_message.text == "Please enter all the fields.", "Error message not displayed for empty form submission."
        except AssertionError as e:
            logger.error(f"Assertion error: : {e}", exc_info=True)
            raise
        except StaleElementReferenceException as e:
            logger.error(f"Element is no longer attached to the DOM: {e}", exc_info=True)
            raise
        except Exception as e:
            logger.error(f"An error occurred: : {e}", exc_info=True)
            raise
