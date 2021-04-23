from behave import *
from selenium.webdriver.common.keys import Keys
import time

@given("i create a url <{url}>")
def step_impl(context, url):
    context.url = url


@then("i visit to url")
def step_impl(context):
    context.driver.get(context.url)


@then("i search <{search_term}>")
def step_impl(context, search_term):
    search_bar = context.driver.find_element_by_xpath("//input[@name='search']")
    search_bar.send_keys(search_term)
    search_bar.send_keys(Keys.RETURN)


@step("i assert <{count}> products has exist")
def step_impl(context, count):
    context.products = context.driver.find_elements_by_class_name('product-thumb')
    assert context.products.__len__() == int(count)


@step("i assert all search products name contains <{search_term}>")
def step_impl(context, search_term):
    for i in context.products:
        title = i.find_element_by_tag_name('h4')
        assert search_term in title.text


@then("i add first product to cart")
def step_impl(context):
    context.products[0].find_element_by_class_name('button-group').click()


@step("i assert cart has <{item_count}>")
def step_impl(context, item_count):
    time.sleep(1)
    cart = context.driver.find_element_by_id('cart-total')
    assert item_count in cart.text


@then("i fill form")
def step_impl(context):
    context.driver.find_element_by_id('input-firstname').send_keys(context.table[0][1])
    context.driver.find_element_by_id('input-lastname').send_keys(context.table[1][1])
    context.driver.find_element_by_id('input-email').send_keys(context.table[2][1])
    context.driver.find_element_by_id('input-telephone').send_keys(context.table[3][1])
    context.driver.find_element_by_id('input-password').send_keys(context.table[4][1])
    context.driver.find_element_by_id('input-confirm').send_keys(context.table[5][1])


@step("i accept Privacy Policy")
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@name='agree']").click()


@step("i click to Continue")
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@value='Continue']").click()


@step("i assert <{message}> message has exist on page title")
def step_impl(context, message):
    assert context.driver.title == message
