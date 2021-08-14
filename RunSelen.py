from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options = options)

df = pd.DataFrame(columns=['College Name'])
webURL = 'https://targetstudy.com/colleges/fashion-designing-colleges-in-india.html' 
driver.get(webURL)
driver.implicitly_wait(6)
CollegeName = driver.find_elements_by_xpath('//a[@class="card-title h5"]')
AddressName = driver.find_elements_by_xpath('//p[@class="card-subtitle mt-0"]')

collegeName = []
addressName = []
phoneName = []

for p in range(len(CollegeName)):
    collegeName.append(CollegeName[p].text)

for s in range(0,len(AddressName),2):
    addressName.append(AddressName[s].text)

for t in range(1,len(AddressName)-1,2):
    phoneName.append(AddressName[t].text)

data_tuples = list(zip(collegeName[1:],addressName[1:],phoneName[1:])) 
temp_df = pd.DataFrame(data_tuples, columns=['College Name','Address','Contact Numbers'])
df = df.append(temp_df)


for i in range(1,98):
    webURL = 'https://targetstudy.com/colleges/fashion-designing-colleges-in-india.html' + f'?recNo={i*10}'
    driver.get(webURL)
    driver.implicitly_wait(6)
    CollegeName = driver.find_elements_by_xpath('//a[@class="card-title h5"]')
    AddressName = driver.find_elements_by_xpath('//p[@class="card-subtitle mt-0"]')

    collegeName = []
    addressName = []
    phoneName = []

    for p in range(len(CollegeName)):
        collegeName.append(CollegeName[p].text)

    for s in range(0,len(AddressName),2):
        addressName.append(AddressName[s].text)

    for t in range(1,len(AddressName)-1,2):
        phoneName.append(AddressName[t].text)

    data_tuples = list(zip(collegeName[1:],addressName[1:],phoneName[1:])) 
    temp_df = pd.DataFrame(data_tuples, columns=['College Name','Address','Contact Numbers'])
    df = df.append(temp_df)


driver.quit()

df.to_csv('FashionColleges.csv')

print('program finished')