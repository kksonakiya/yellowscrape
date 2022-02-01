from selenium import webdriver
path='webdriver/chromedriver.exe'
driver=webdriver.Chrome(path)

driver.get('https://www.yellowpages.com/search?search_terms=james&geo_location_terms=TX')


# We'll get the details of the first page.

results=driver.find_elements_by_class_name('result')
print('Results: ', len(results))
for result in results:
    businessName=result.find_element_by_class_name('business-name')
    bname=businessName.text
    print(bname)

print('This change should appear in second branch only')