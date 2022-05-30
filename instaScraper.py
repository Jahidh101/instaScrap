from time import sleep
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import formInfo
import testHtml
import pandas as pd



if __name__ == "__main__":
    options = uc.ChromeOptions()
    options.add_argument("--auto-open-devtools-for-tabs")
    driver = uc.Chrome(options=options)
    # driver.maximize_window()
    # sleep(5)
    driver.set_window_size(width=950, height=1020)
    wsize = driver.get_window_size()
    
    driver.get('https://www.instagram.com/')
    sleep(10)
    driver.implicitly_wait(10)

    uname = driver.find_element(by=By.XPATH, value='/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
    uname.send_keys(formInfo.username)
    sleep(2)
    password = driver.find_element(by=By.XPATH, value='/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
    password.send_keys(formInfo.password)
    sleep(2)
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button').click()
    sleep(5)
    driver.implicitly_wait(10)
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/section/main/div/div/div/div/button').click()
    driver.implicitly_wait(10)
    driver.find_element(by=By.XPATH, value='/html/body/div[5]/div/div/div/div[3]/button[2]').click()
    sleep(6)

    url ='https://www.instagram.com/cristiano_c_r7_/'
    driver.get(url)
    sleep(8)
    
    # followers_num = driver.find_element(by=By.XPATH, value='/html/body/div[1]/section/main/div/ul/li[2]/a/div/span')
    followers = driver.find_element(by=By.XPATH, value='/html/body/div[1]/section/main/div/ul/li[2]/a')
    # followers_count = followers_num.text
    followers.click()


    # print(followers_count)
    sleep(45)
    html = driver.page_source
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')
    list = soup.find_all('li', class_ = 'wo9IH')
    print(len(list))
    all_followers = []
    for person in list:
        username = person.find('span', class_ = '_7UhW9').text
        name = person.find('div', class_ = 'wFPL8').text

        data = {
            'username' : username,
            'name' : name
        }
        all_followers.append(data)

        
    df = pd.DataFrame(all_followers)
    df.to_csv('files/anri_Followers.csv', index=False)



