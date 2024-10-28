from selenium import webdriver
import pandas as pd
import time

website = "https://www.audible.com/search"
path = r"C:\Users\HauMoon\Downloads\chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get(website)
driver.maximize_window()

pagination = driver.find_element_by_xpath('//ul[contains(@class,"pagingElements")]')
pages = pagination.find_elements_by_tag_name('li')
last_page = int(pages[-2].text)

book_title= []
book_author=[]
book_length =[]

current_page = 1

while current_page < last_page:
    time.sleep(3)
    container = driver.find_element_by_class_name("adbl-impression-container")
    products = container.find_elements_by_xpath('.//li[contains(@class,"productListItem")]')

    for product in products:
        book_title.append(product.find_element_by_xpath('.//h3[contains(@class,"bc-heading")]').text)
        book_author.append(product.find_element_by_xpath('.//li[contains(@class,"authorLabel")]').text)
        book_length.append(product.find_element_by_xpath('.//li[contains(@class,"runtimeLabel")]').text)
    
    current_page +=1
    try:
        next_page = driver.find_element_by_xpath('//span[contains(@class,"nextButton")]')
        next_page.click()
    except:
        pass

driver.quit()
df = pd.DataFrame({
    "book_title":book_title,
    "book_author": book_author,
    "book_length":book_length
})
df.to_csv("./Crawl_data_audible/Book.csv",index=False)
