import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature('Menu Navigation')
@allure.suite('UI Tests')
@allure.title('Test Menu Item Navigation')
@allure.description('Verifies that each menu item on the homepage navigates to the correct page and displays the correct heading.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_menu_item(driver):

    with allure.step("Opening the homepage"):
        driver.get("https://tutorialsninja.com/demo/")

    expected_menu_items = ["Desktops", "Laptops & Notebooks", "Components", "Tablets",
                           "Software", "Phones & PDAs", "Cameras", "MP3 Players"]

    with allure.step(f"Clicking on menu item: {expected_menu_items[0]}"):
        menu_item1 = driver.find_element(By.LINK_TEXT, expected_menu_items[0])
        menu_item1.click()

    with allure.step(f"Clicking on menu item: {expected_menu_items[1]}"):
        menu_item2 = driver.find_element(By.LINK_TEXT, expected_menu_items[1])
        menu_item2.click()

    with allure.step(f"Clicking on menu item: {expected_menu_items[2]}"):
        menu_item3 = driver.find_element(By.LINK_TEXT, expected_menu_items[2])
        menu_item3.click()

    with allure.step(f"Clicking on menu item: {expected_menu_items[3]}"):
        menu_item4 = driver.find_element(By.LINK_TEXT, expected_menu_items[3])
        menu_item4.click()

    with allure.step(f"Verifying the page heading for {expected_menu_items[3]}"):
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[3]

    with allure.step(f"Clicking on menu item: {expected_menu_items[4]}"):
        menu_item5 = driver.find_element(By.LINK_TEXT, expected_menu_items[4])
        menu_item5.click()

    with allure.step(f"Verifying the page heading for {expected_menu_items[4]}"):
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[4]

    with allure.step(f"Clicking on menu item: {expected_menu_items[5]}"):
        menu_item6 = driver.find_element(By.LINK_TEXT, expected_menu_items[5])
        menu_item6.click()

    with allure.step(f"Verifying the page heading for {expected_menu_items[5]}"):
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[5]

    with allure.step(f"Clicking on menu item: {expected_menu_items[6]}"):
        menu_item7 = driver.find_element(By.LINK_TEXT, expected_menu_items[6])
        menu_item7.click()

    with allure.step(f"Verifying the page heading for {expected_menu_items[6]}"):
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[6]

    with allure.step(f"Clicking on menu item: {expected_menu_items[7]}"):
        menu_item8 = driver.find_element(By.LINK_TEXT, expected_menu_items[7])
        menu_item8.click()


@allure.feature('Menu Navigation')
@allure.suite('Nested Menu Tests')
@allure.title('Test Nested Menus')
@allure.description(
    'This test checks if the nested menu navigation works correctly by verifying the page heading for each menu.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("menu_locator, submenu_locator, result_text", [
    (
            (By.PARTIAL_LINK_TEXT, 'Desktops'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[1]/a'),
            'PC'
    ),
    (
            (By.PARTIAL_LINK_TEXT, 'Desktops'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[2]/a'),
            'Mac'
    ),
    (
            (By.PARTIAL_LINK_TEXT, 'Laptops & Notebooks'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[2]/div/div/ul/li[1]/a'),
            'Macs'
    ),
    (
            (By.PARTIAL_LINK_TEXT, 'Laptops & Notebooks'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[2]/div/div/ul/li[2]/a'),
            'Windows'
    )
])
def test_nested_menu(driver, menu_locator, submenu_locator, result_text):
    with allure.step("Opening the tutorial demo site"):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step(f"Hovering over menu: {menu_locator}"):
        menu = driver.find_element(*menu_locator)

    with allure.step(f"Clicking submenu: {submenu_locator}"):
        submenu = driver.find_element(*submenu_locator)
        ActionChains(driver).move_to_element(menu).click(submenu).perform()

    with allure.step(f"Verifying the page heading: Expected '{result_text}'"):
        assert driver.find_element(By.TAG_NAME,
                                   'h2').text == result_text, f"Expected '{result_text}' but got '{driver.find_element(By.TAG_NAME, 'h2').text}'"


@allure.feature('Product Search')
@allure.suite('Search Tests')
@allure.title('Test Product Search')
@allure.description(
    'This test searches for a product and verifies that the correct items are listed in the search results.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_search_product(driver):
    with allure.step("Opening the tutorial demo site"):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step("Entering 'MacBook' in the search box"):
        search = driver.find_element(By.NAME, 'search')
        search.send_keys('MacBook')

    with allure.step("Clicking on the search button"):
        button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-default.btn-lg')
        button.click()

    with allure.step("Verifying the search results contain 'MacBook'"):
        products = driver.find_elements(By.TAG_NAME, 'h4')
        new_list = [elem.text for elem in products if 'MacBook' in elem.text]
        assert len(products) == len(new_list), "Search results don't match expected 'MacBook' products"


@allure.feature('Shopping Cart')
@allure.suite('Add to Cart Tests')
@allure.title('Test Add to Cart Functionality')
@allure.description(
    'This test adds a product to the cart, verifies the success message, and checks if the correct product is in the cart.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_add_to_cart(driver):
    with allure.step("Opening the tutorial demo site"):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step("Adding a product to the cart"):
        product = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[1]')
        product.click()

    with allure.step("Waiting for the success message to appear"):
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert.alert-success"))
        )
        assert "Success: You have added" in success_message.text, "Expected success message not found."

    with allure.step("Verifying cart has 1 item"):
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "cart-total"), "1 item(s)")
        )

    with allure.step("Clicking on the cart button"):
        cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "cart"))
        )
        cart_button.click()

    with allure.step("Checking cart contents for 'MacBook'"):
        cart_contents = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.dropdown-menu.pull-right"))
        )
        assert "MacBook" in cart_contents.text, "Expected 'MacBook' in cart, but it wasn't found."


@allure.feature('UI Interaction')
@allure.suite('Slider Functionality Tests')
@allure.title('Test Slider Functionality')
@allure.description('This test checks if the slider moves to the next image and returns to the first image correctly.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_slider_functionality(driver):
    with allure.step("Opening the tutorial demo site"):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step("Verifying the slider is visible on the page"):
        slider = driver.find_element(By.CLASS_NAME, 'swiper-container')
        assert slider.is_displayed(), "Slider is not visible on the page."

    with allure.step("Capturing the source of the first slide"):
        first_slide = driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active img")
        first_slide_src = first_slide.get_attribute("src")

    with allure.step("Clicking the next arrow to move the slider"):
        next_arrow = driver.find_element(By.CLASS_NAME, 'swiper-button-next')
        ActionChains(driver).move_to_element(slider).click(next_arrow).perform()

    with allure.step("Waiting for the slider to move to the next slide"):
        WebDriverWait(driver, 10).until_not(
            EC.element_to_be_clickable(first_slide)
        )

    with allure.step("Verifying the slider moved to the next slide"):
        new_slide = driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active img")
        new_slide_src = new_slide.get_attribute("src")
        assert first_slide_src != new_slide_src, "Slider did not move to the next image."

    with allure.step("Clicking the previous arrow to move back to the first slide"):
        prev_arrow = driver.find_element(By.CLASS_NAME, 'swiper-button-prev')
        prev_arrow.click()

    with allure.step("Waiting for the slider to return to the first slide"):
        WebDriverWait(driver, 10).until_not(
            EC.element_to_be_clickable(new_slide)
        )

    with allure.step("Verifying the slider returned to the first slide"):
        reverted_slide_src = driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active img").get_attribute("src")
        assert reverted_slide_src == first_slide_src, "Slider did not return to the first image."


@allure.feature('Wishlist')
@allure.suite('Wishlist Functionality Tests')
@allure.title('Test Adding Item to Wishlist')
@allure.description('This test adds an item to the wishlist, verifies the success message, and checks the wishlist contents.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.extended
@pytest.mark.regression
def test_add_item_to_wishlist(driver, login):
    with allure.step("Opening the tutorial demo site"):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step("Clicking the 'Add to Wishlist' button for the first product"):
        wishlist_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[2]'))
        )
        wishlist_button.click()

    with allure.step("Verifying the success message"):
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.alert.alert-success'))
        )
        assert "Success: You have added MacBook to your wish list!" in success_message.text, "Wishlist failed"

    with allure.step("Clicking the wishlist link"):
        wishlist_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="wishlist-total"]'))
        )
        wishlist_link.click()

    with allure.step("Verifying the wishlist page heading"):
        assert driver.find_element(By.TAG_NAME, 'h2').text == 'My Wish List', "Wishlist page not loaded correctly"

    with allure.step("Verifying that 'MacBook' is in the wishlist"):
        wishlist_contents = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/table'))
        )
        assert "MacBook" in wishlist_contents.text, "MacBook not found in wishlist"


@allure.feature('Bottom Menu Navigation')
@allure.suite('Bottom Menu Tests')
@allure.title('Test Bottom Menu Navigation')
@allure.description('This test verifies that each bottom menu link navigates to the correct page and displays the correct heading.')
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.extended
@pytest.mark.regression
def test_bottom_menu(driver):
    with allure.step("Opening the tutorial demo site"):
        driver.get("https://tutorialsninja.com/demo/")

    bottom_menu_items = {
        "About Us": "About Us",
        "Delivery Information": "Delivery Information",
        "Privacy Policy": "Privacy Policy",
        "Terms & Conditions": "Terms & Conditions"
    }

    for item, expected_title in bottom_menu_items.items():
        with allure.step(f"Clicking on bottom menu item: {item}"):
            link = driver.find_element(By.LINK_TEXT, item)
            link.click()

        with allure.step(f"Verifying the page heading for {item}"):
            heading = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/h1').text
            assert heading == expected_title, f"Expected heading '{expected_title}', but got '{heading}' for {item}"

