from selenium import webdriver

# Set up the driver
driver = webdriver.Firefox()

# Navigate to the website
driver.get("https://analyticsindiamag.com")

# Take a screenshot of the entire page
driver.save_screenshot("screenshot.png")

# Close the driver
driver.quit()