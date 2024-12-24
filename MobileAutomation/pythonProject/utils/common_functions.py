from selenium.webdriver.common.by import By
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException, \
    ElementClickInterceptedException
from selenium.webdriver.remote.webelement import WebElement
from typing import Union, List

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from tests.conftest import logger


def find_element(
        driver: WebDriver, by: str, value: str, highlight: bool = False
) -> Union[WebElement, None]:
    """
    Finds an element on a mobile app screen using Appium.
    """
    # Map of supported locator strategies
    by_type = {
        "id": By.ID,
        "xpath": By.XPATH,
        "accessibility_id": By.ACCESSIBILITY_ID,
        "class_name": By.CLASS_NAME,
        "android_ui_automator": By.ANDROID_UIAUTOMATOR,
        "ios_predicate_string": By.IOS_PREDICATE,
        "ios_class_chain": By.IOS_CLASS_CHAIN,
    }

    if by not in by_type:
        logger.error(f"Locator type '{by}' is not supported in Appium.")
        raise ValueError(f"Locator type '{by}' is not supported.")

    try:
        # Locate the element
        element = driver.find_element(by_type[by], value)
        logger.info(f"Element found using {by}='{value}'.")
        return element

    except NoSuchElementException:
        logger.error(f"Element not found using {by}='{value}'.")
    except StaleElementReferenceException:
        logger.error(f"Element is no longer attached to the DOM using {by}='{value}'.")
    except Exception as e:
        logger.error(f"An error occurred while finding element by {by}='{value}': {e}")
    return None


def find_elements(
        driver: WebDriver, by: str, value: str
) -> Union[List[WebElement], None]:
    """
    Finds multiple elements on a mobile app screen using Appium.
    """
    # Map of supported locator strategies
    by_type = {
        "id": By.ID,
        "xpath": By.XPATH,
        "accessibility_id": By.ACCESSIBILITY_ID,
        "class_name": By.CLASS_NAME,
        "android_ui_automator": By.ANDROID_UIAUTOMATOR,
        "ios_predicate_string": By.IOS_PREDICATE,
        "ios_class_chain": By.IOS_CLASS_CHAIN,
    }

    if by not in by_type:
        logger.error(f"Locator type '{by}' is not supported in Appium.")
        raise ValueError(f"Locator type '{by}' is not supported.")

    try:
        # Locate the elements
        elements = driver.find_elements(by_type[by], value)
        if elements:
            logger.info(f"{len(elements)} elements found using {by}='{value}'.")
            return elements
        else:
            logger.warning(f"No elements found using {by}='{value}'.")
    except NoSuchElementException:
        logger.error(f"No elements found using {by}='{value}'.")
    except Exception as e:
        logger.error(f"An error occurred while finding elements by {by}='{value}': {e}")
    return None


def click_element(driver: WebDriver, element, highlight: bool = True) -> bool:
    """
    Waits for the given element to be clickable and performs a click operation.
    """
    try:
        # Wait until the element is present and clickable
        clickable_element = WebDriverWait(driver, timeout=5).until(
            ec.element_to_be_clickable(element)
        )
        clickable_element.click()
        logger.info(f"Element clicked: {element}")
        return True

    except TimeoutException:
        logger.error(f"Timeout: Element '{element}' was not clickable within the timeout.")
    except NoSuchElementException:
        logger.error(f"NoSuchElementException: Element '{element}' was not found in the DOM.")
    except ElementClickInterceptedException:
        logger.error(f"ElementClickInterceptedException: Element '{element}' was not clickable.")
    except Exception as e:
        logger.error(f"An error occurred while clicking the element: {e}")
    return False


def wait_until_element_visible(
    driver: WebDriver, by: str, value: str, highlight: bool = True
) -> Union[WebElement, None]:
    """
    Waits until an element is visible on the screen.
    """
    # Map of supported locator strategies
    by_type = {
        "id": By.ID,
        "xpath": By.XPATH,
        "accessibility_id": By.ACCESSIBILITY_ID,
        "class_name": By.CLASS_NAME,
        "android_ui_automator": By.ANDROID_UIAUTOMATOR,
        "ios_predicate_string": By.IOS_PREDICATE,
        "ios_class_chain": By.IOS_CLASS_CHAIN,
    }

    if by not in by_type:
        logger.error(f"Locator type '{by}' is not supported in Appium.")
        raise ValueError(f"Locator type '{by}' is not supported.")

    try:
        # Wait for the element to be visible
        wait = WebDriverWait(driver, timeout=5)
        element = wait.until(ec.visibility_of_element_located((by_type[by], value)))
        logger.info(f"Element is visible using {by}='{value}'.")
        return element

    except TimeoutException:
        logger.error(f"Timeout: Element using {by}='{value}' was not visible within the timeout.")
    except NoSuchElementException:
        logger.error(f"NoSuchElementException: Element using {by}='{value}' was not found in the DOM.")
    except Exception as e:
        logger.error(f"An error occurred while waiting for the element using {by}='{value}': {e}")
    return None


def element_get_text(driver: WebDriver, element, highlight: bool = True) -> str:
    """
    Gets the text of a specified element on the mobile app screen.
    """
    try:
        # Get the text of the element
        element_text = element.text
        logger.info(f"Element text: {element_text}")

        return element_text

    except TimeoutException:
        logger.error(f"Timeout: Element '{element}' was not found within the timeout.")
    except NoSuchElementException:
        logger.error(f"NoSuchElementException: Element '{element}' was not found in the DOM.")
    except Exception as e:
        logger.error(f"An error occurred while getting text from the element '{element}': {e}")

    return ""
