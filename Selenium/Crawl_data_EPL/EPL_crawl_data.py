from selenium import webdriver
import pandas as pd

website = "https://www.adamchoi.co.uk/overs/detailed"
path = r"C:\Users\HauMoon\Downloads\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get(website)

all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
all_matches_button.click()

date = []
home_team = []
score=[]
away_team =[]

matches = driver.find_elements_by_tag_name("tr")
for match in matches:
    if match.find_elements_by_xpath("./td[@colspan]"):
        continue
    else:
        try:
            date.append(match.find_element_by_xpath('./td[1]').text)
            home_team.append(match.find_element_by_xpath('./td[2]').text)
            score.append(match.find_element_by_xpath('./td[3]').text)
            away_team.append(match.find_element_by_xpath('./td[4]').text)
        except:
            print("row not true format")
df = pd.DataFrame({
    "date": date,
    "home_team":home_team,
    "score": score,
    "away_team":away_team
})
df.to_csv("EPL.csv",index=False)
print(df)
# driver.quit()