from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

''' A game has a click a cookie to earn points. We will use Selenium to
    automatcally do this for us so we can upgrade certain items. The
    program will also auto upgrade the upgrades when the points are 
    equal to or greater than cost to upgrade.'''

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get('https://orteil.dashnet.org/cookieclicker/')       #target site

driver.implicitly_wait(5)                               #wait 5 seconds before continueing

cookie = driver.find_element_by_id("bigCookie")         #Find the element.
cookie_count = driver.find_element_by_id("cookies")
#We will now make a list with th upgradess so we can loop to see if we can upgrade.
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1,-1,-1)]

actions = ActionChains(driver)                          #action chain, begin a sequence of events
actions.click(cookie)                                   #Create the action to click

for i in range(50000):                                   #count for clicks in the range
    actions.perform()                                   #Perform action
    count = int(cookie_count.text.split(" ")[0])        #count and split the number in the cookie amount
    print(count)
    for item in items:                                  #check the items for upgrades nd the cost to upgrade
        value = int(item.text)                          #isolate the cost
        if value <= count:                              #If statement to check the cost to the toal amount of clicked cookies
            upgrade_actions = ActionChains(driver)      #get driver action
            upgrade_actions.move_to_element(item)       #Move the cursor
            upgrade_actions.click()                     #Click upgrade button
            upgrade_actions.perform()                   #Perform the upgrade
        