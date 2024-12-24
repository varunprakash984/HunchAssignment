import pytest
from utils import common_functions as cf
from selenium.common.exceptions import StaleElementReferenceException
from conftest import logger, class_setup, setup

# XPaths for login elements
login_username_text_field_xpath = '//android.widget.EditText[@resource-id="com.example.applicationform:id/loginIdInput"]'
login_password_text_field_xpath = '//android.widget.EditText[@resource-id="com.example.applicationform:id/passwordInput"]'
login_button_xpath = '//android.widget.Button[@resource-id="com.example.applicationform:id/loginButton"]'
invalid_login_or_password_text_xpath = '//android.widget.TextView[@resource-id="com.example.applicationform:id/errorMessage"]'
select_an_option_text_xpath = '//android.widget.TextView[@resource-id="android:id/text1"]'


@pytest.mark.usefixtures("setup", "class_setup")
class TestLogin:

    def test_logging_with_registered_phone_number(self):
        try:
            for row in self.data_sheet.iter_rows(min_row=2):
                valid_username_value = row[0].value
                valid_password_value = row[1].value

                username_field = cf.find_element(self.driver, 'xpath', login_username_text_field_xpath)
                username_field.clear()
                username_field.send_keys(valid_username_value)

                password_field = cf.find_element(self.driver, 'xpath', login_password_text_field_xpath)
                password_field.clear()
                password_field.send_keys(valid_password_value)

                login_button = cf.find_element(self.driver, 'xpath', login_button_xpath)
                cf.click_element(self.driver, login_button)

                select_an_option_text = cf.find_element(self.driver, 'xpath', select_an_option_text_xpath)
                assert select_an_option_text, f"Login failed for user {valid_username_value}"
        except AssertionError as e:
            logger.error(f"Assertion error: : {e}", exc_info=True)
            raise
        except StaleElementReferenceException as e:
            logger.error(f"Element is no longer attached to the DOM: {e}", exc_info=True)
            raise
        except Exception as e:
            logger.error(f"An error occurred: : {e}", exc_info=True)
            raise

    def test_logging_with_invalid_username_password(self):
        try:
            for row in self.data_sheet.iter_rows(min_row=2):
                invalid_username = row[2].value
                valid_password = row[3].value

                username_field = cf.find_element(self.driver, 'xpath', login_username_text_field_xpath)
                username_field.clear()
                username_field.send_keys(invalid_username)

                password_field = cf.find_element(self.driver, 'xpath', login_password_text_field_xpath)
                password_field.clear()
                password_field.send_keys(valid_password)

                login_button = cf.find_element(self.driver, 'xpath', login_button_xpath)
                cf.click_element(self.driver, login_button)

                error_message = cf.find_element(self.driver, 'xpath', invalid_login_or_password_text_xpath)
                assert error_message, "Error message not displayed for invalid username."
        except AssertionError as e:
            logger.error(f"Assertion error: : {e}", exc_info=True)
            raise
        except StaleElementReferenceException as e:
            logger.error(f"Element is no longer attached to the DOM: {e}", exc_info=True)
            raise
        except Exception as e:
            logger.error(f"An error occurred: : {e}", exc_info=True)
            raise

    def test_logging_with_invalid_password(self):
        try:
            for row in self.data_sheet.iter_rows(min_row=2):
                valid_username = row[0].value
                invalid_password = row[3].value

                username_field = cf.find_element(self.driver, 'xpath', login_username_text_field_xpath)
                username_field.clear()
                username_field.send_keys(valid_username)

                password_field = cf.find_element(self.driver, 'xpath', login_password_text_field_xpath)
                password_field.clear()
                password_field.send_keys(invalid_password)

                login_button = cf.find_element(self.driver, 'xpath', login_button_xpath)
                cf.click_element(self.driver, login_button)

                error_message = cf.find_element(self.driver, 'xpath', invalid_login_or_password_text_xpath)
                assert error_message, "Error message not displayed for invalid password."
        except AssertionError as e:
            logger.error(f"Assertion error: : {e}", exc_info=True)
            raise
        except StaleElementReferenceException as e:
            logger.error(f"Element is no longer attached to the DOM: {e}", exc_info=True)
            raise
        except Exception as e:
            logger.error(f"An error occurred: : {e}", exc_info=True)
            raise

    def test_logging_with_blank_username(self):
        try:
            for row in self.data_sheet.iter_rows(min_row=2):
                blank_username = ""
                valid_password = row[1].value

                username_field = cf.find_element(self.driver, 'xpath', login_username_text_field_xpath)
                username_field.clear()
                username_field.send_keys(blank_username)

                password_field = cf.find_element(self.driver, 'xpath', login_password_text_field_xpath)
                password_field.clear()
                password_field.send_keys(valid_password)

                login_button = cf.find_element(self.driver, 'xpath', login_button_xpath)
                cf.click_element(self.driver, login_button)

                error_message = cf.find_element(self.driver, 'xpath', invalid_login_or_password_text_xpath)
                assert error_message, "Error message not displayed for blank username."
        except AssertionError as e:
            logger.error(f"Assertion error: : {e}", exc_info=True)
            raise
        except StaleElementReferenceException as e:
            logger.error(f"Element is no longer attached to the DOM: {e}", exc_info=True)
            raise
        except Exception as e:
            logger.error(f"An error occurred: : {e}", exc_info=True)
            raise

    def test_logging_with_blank_password(self):
        try:
            for row in self.data_sheet.iter_rows(min_row=2):
                valid_username_value = row[0].value
                blank_password = ""

                username_field = cf.find_element(self.driver, 'xpath', login_username_text_field_xpath)
                username_field.clear()
                username_field.send_keys(valid_username_value)

                password_field = cf.find_element(self.driver, 'xpath', login_password_text_field_xpath)
                password_field.clear()
                password_field.send_keys(blank_password)

                login_button = cf.find_element(self.driver, 'xpath', login_button_xpath)
                cf.click_element(self.driver, login_button)

                error_message = cf.find_element(self.driver, 'xpath', invalid_login_or_password_text_xpath)
                assert error_message, "Error message not displayed for blank password."
        except AssertionError as e:
            logger.error(f"Assertion error: : {e}", exc_info=True)
            raise
        except StaleElementReferenceException as e:
            logger.error(f"Element is no longer attached to the DOM: {e}", exc_info=True)
            raise
        except Exception as e:
            logger.error(f"An error occurred: : {e}", exc_info=True)
            raise

    def test_logging_with_blank_username_and_password(self):
        try:
            blank_username = ""
            blank_password = ""

            username_field = cf.find_element(self.driver, 'xpath', login_username_text_field_xpath)
            username_field.clear()
            username_field.send_keys(blank_username)

            password_field = cf.find_element(self.driver, 'xpath', login_password_text_field_xpath)
            password_field.clear()
            password_field.send_keys(blank_password)

            login_button = cf.find_element(self.driver, 'xpath', login_button_xpath)
            cf.click_element(self.driver, login_button)

            error_message = cf.find_element(self.driver, 'xpath', invalid_login_or_password_text_xpath)
            assert error_message, "Error message not displayed for blank username and password."
        except AssertionError as e:
            logger.error(f"Assertion error: : {e}", exc_info=True)
            raise
        except StaleElementReferenceException as e:
            logger.error(f"Element is no longer attached to the DOM: {e}", exc_info=True)
            raise
        except Exception as e:
            logger.error(f"An error occurred: : {e}", exc_info=True)
            raise
