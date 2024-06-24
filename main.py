import time
import os
from bs4 import BeautifulSoup
from selenium import webdriver

path = os.path.abspath("source-page.html")

def get_source_html(url):
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get(url=url)
        time.sleep(3)

        with open("source-page.html", "w") as file:
            file.write(driver.page_source)

    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()


def get_items_TX_DATE(path, TX_arr, DATE_arr):
    path = open(path)
    soup = BeautifulSoup(path, "lxml")

    all_tags = soup.find_all("td", class_="row-align")[0:12]
    num = 1

    for tag in all_tags:
        tags_data = tag.text
        if num % 2 == 0:
            DATE_arr.append(tags_data)
        else:
            TX_arr.append(tags_data)
        num += 1


def get_items_TRANSFER(path, who, to, how_much, id):
    path = open(path)
    soup = BeautifulSoup(path, "lxml")

    all_tags = soup.find_all("div", class_="token-transfer")[0:6]

    for tag in all_tags:
        tags_data = (tag.text).split()
        who.append(tags_data[0])
        to.append(tags_data[2])
        how_much.append(tags_data[3])
        id.append(tags_data[5])


def main():
    who, to, how_much, id, TX_arr, DATE_Arr = [], [], [], [], [], []

    get_source_html(url="https://bloks.io/account/tttingenesis")
    get_items_TX_DATE(
        path=path,
        TX_arr=TX_arr,
        DATE_arr=DATE_Arr,
    )
    get_items_TRANSFER(
        path=path,
        who=who,
        to=to,
        how_much=how_much,
        id=id,
    )

    for ind in range(len(TX_arr)):
        print(
            f"TX:{TX_arr[ind]}; DATE:{DATE_Arr[ind]}; DATA: {who[ind]} -> {to[ind]} {how_much[ind]}TTT {id[ind]}"
        )


if __name__ == "__main__":
    main()
