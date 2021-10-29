from pprint import pprint

from selenium import webdriver
import time

URL = "http://orteil.dashnet.org/experiments/cookie/"
chrome_driver_path = "/home/hiren/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)

five_min = time.time() + 60 * 5
five_seconds = time.time() + 5



cookie_button = driver.find_element_by_id("cookie")


#listed upgrades





while True:
    cookie_button.click()

    #five seconds have passed
    if time.time() > five_seconds:
        upgrades = driver.find_elements_by_css_selector("#store div b")
        upgrades_and_cost = {}
        for upgrade in upgrades:
            upgrade_text = upgrade.text.split("\n")
            if upgrade_text != ['']:
                print(f"Upgrade text is {upgrade_text}")
                upgrade_cost = (upgrade_text[0].split("-")[1].strip().replace(",", ""))
                upgrade_cost = int(upgrade_cost.rstrip())
                upgrades_and_cost[upgrade_cost] = upgrade

        # Get current cookie count
        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
            money_element = int(money_element)

        #Purchase the most expensive affordable upgrade
        list_of_costs = [cost for cost in upgrades_and_cost.keys() if int(cost) <= int(money_element)]
        if list_of_costs is not None:
            max_affordable_item = max(list_of_costs)
            item_to_buy = upgrades_and_cost[max_affordable_item]
            item_to_buy.click()
        #Add another 5 seconds until the next check
        five_seconds = time.time() + 5





    # five min are up
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        driver.quit()