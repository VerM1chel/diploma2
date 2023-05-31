from sqlConfigAndQueries import config
from sqlConfigAndQueries import queries
from classes.details.cpu import Cpu
from classes.details.cooler import Cooler
from classes.details.motherboard import Motherboard
from classes.details.ram import Ram
from classes.details.gpu import Gpu
from classes.details.ssd import Ssd
from classes.details.hdd import Hdd
from classes.details.power import Power
from classes.details.case_PC import Case

import inspect
import constants
import time
import re
import random

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import mysql.connector
from mysql.connector import Error

def get_html(driver, main_devices_link, scrolls_number):
    driver.get(main_devices_link)
    last_height = driver.execute_script("return document.body.scrollHeight")  # Get scroll height
    while scrolls_number > 0:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Scroll down to bottom
        time.sleep(constants.SCROLL_PAUSE_TIME)  # Wait to load page
        new_height = driver.execute_script("return document.body.scrollHeight")  # Calculate new scroll height and compare with last scroll height
        if new_height == last_height:
            break
        last_height = new_height
        scrolls_number -= 1
    print(f"scrolls_number -- {scrolls_number}")
    return driver.page_source

def clear_cache_cookies(driver):
    """Clear the cookies and cache for the ChromeDriver instance."""
    driver.get('chrome://settings/clearBrowserData') # for old chromedriver versions use cleardriverData
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB*9)
    actions.perform()
    actions.send_keys(Keys.ENTER)  # send right combination
    actions.perform()

["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:11.0) Gecko Firefox/11.0",
 "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.9200",
 "Mozilla/5.0 (X11; U; Linux i686; cs-CZ; rv:1.8.0.11) Gecko/20070327 Ubuntu/dapper-security Firefox/1.5.0.11",
 "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; ja-jp) AppleWebKit/531.22.7 (KHTML, like Gecko) Version/4.0.5 Safari/531.22.7",
 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19577",
 ]

def getClassNamesAndValues(c):
    class_attributes_names, class_attributes_values = [], []
    for i in inspect.getmembers(c):
        if i[0] == "__dict__":
            class_attributes_names = list(i[1].keys())
            class_attributes_values = list(i[1].values())
            return class_attributes_names, class_attributes_values

def create_tables(connection):
    cursor = connection.cursor()
    table_queries = [queries.create_cpus_table, queries.create_coolers_table, queries.create_motherboards_table, queries.create_rams_table,
        queries.create_gpus_table, queries.create_ssds_table, queries.create_hhds_table, queries.create_powers_table, queries.create_cases_table,
                     queries.create_min_reqs_table, queries.create_recommended_reqs_table, queries.create_configuration_table, queries.create_users_table]
    for query in table_queries:
        try:
            cursor.execute(query)
            print("Query executed succesfully")
        except Error as err:
            print(f"The error {err} occured")
            cursor.close()
    cursor.close()

def write_devices(connection, cursor, page, i, tables_names, devices):
    if page == 0:
        tmp_index = 0
    else:
        tmp_index = (page * 30) - 1
    for device in devices[i][tmp_index:]:  # Каждый элемент класса мы записываем как строку
        classAttributesNames, classAttributesValues = getClassNamesAndValues(device)
        placeholders = ', '.join(['%s'] * len(classAttributesValues))
        classAttributesNames = ', '.join(classAttributesNames)
        write_data_to_table_query = f"INSERT INTO {tables_names[i]} ({classAttributesNames}) VALUES ({placeholders})"
        try:
            cursor.execute(write_data_to_table_query, classAttributesValues)
            connection.commit()
        except:
            print("Problems with cursor")
    print("Data wroten succesfully")
    return cursor

def main():
    connection, cursor = None, None
    try:
        connection = mysql.connector.connect(
            host=config.host,
            user=config.user,
            passwd=config.password,
            database=config.database
        )
        print('Succesfull connected')
    except mysql.connector.Error as error:
        print(f'An error {error} occured')

    create_tables(connection)
    main_devices_links = [constants.all_cpus_link, constants.all_coolers_link, constants.all_motherboards_link, constants.all_motherboards_link, constants.all_rams_link, constants.all_gpus_link, constants.all_ssds_link, constants.all_hdds_link, constants.all_powers_link,constants.all_cases_link]
    cpus, coolers, motherboards, motherboards, rams, gpus, ssds, hdds, powers, cases = [], [], [], [], [], [], [], [], [], []
    devices = [cpus, coolers, motherboards, motherboards, rams, gpus, ssds, hdds, powers, cases]
    Device_classes = [Cpu, Cooler, Motherboard, Ram, Gpu, Ssd, Hdd, Power, Case]
    tables_names = ["cpus", "coolers", "motherboards", "rams", "gpus", "ssds", "hdds", "powers", "cases"]
    time.sleep(5)
    for i, main_devices_link in enumerate(main_devices_links): # Для каждого типа комплектующих
        driver = webdriver.Chrome(ChromeDriverManager().install())
        clear_cache_cookies(driver) # Чистим кеш и cookies
        driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": UserAgent().random}) # Используем случайный user agent, чтобы избежать попадания в черный список сайта
        print(driver.execute_script("return navigator.userAgent;"))
        page = 0
        condition = True
        while condition: # Пока можно переходить на следующую страницу каталога
            time.sleep(5)
            print(f"page number {page}")
            driver.get(main_devices_link+f"?page={page+1}")
            time.sleep(3)
            soup = BeautifulSoup(driver.page_source, features="html.parser")
            device_links = soup.find_all('a', class_="js-product-title-link", href=True) # Получаем все нужные ссылки
            device_links = [device_link.attrs['href'] for device_link in device_links]  # Приводим их в вид, позволяющий работать с этими ссылками
            if len(device_links) < 30:
                if cursor != None:
                    write_devices(connection, cursor, page, i, tables_names, devices)
                condition = False
            time.sleep(3)
            for j, device_link in enumerate(device_links): # Для каждого экземпляра данного типа выполняется переход на страницу с описанием, возвращается html-код и выбираются нужные характеристики
                print(f"It is type {i} device {j} and page {[page]}")
                driver.get(device_link)
                time.sleep(3)
                content = driver.page_source
                little_soup = BeautifulSoup(content, features="html.parser")
                table = little_soup.find('table', class_="product-specs__table")
                our_tables = table.find_all('tbody')
                ks, vs, ds = [], [], []  # keys, values, descriptions
                device_name = little_soup.find('h1', class_="catalog-masthead__title js-nav-header").text.strip()
                try:
                    price = little_soup.find('a', class_="offers-description__link offers-description__link_nodecor js-description-price-link").text.strip()
                except:
                    if cursor != None:
                        write_devices(connection, cursor, page, i, tables_names, devices)
                    condition = False
                    break
                ks.append("Название")
                ks.append("Цена")
                vs.append(device_name)
                vs.append(price)
                ds.append("Полное название комплектующей")
                ds.append("Наименьшая доступная цена комплектующей")
                print(f"device name: {device_name}")
                for k in range(len(our_tables)):
                    our_table = table.find_all('tbody')[k]
                    trs = our_table.find_all('tr')
                    for qqq, tr in enumerate(trs[1:]):
                        td = tr.find_all('td')
                        if len(td) == 1:
                            # try:
                            if td[0].find_all('p')[0].text.strip() == "Описание":
                                p = td[0].find_all('p')
                                ks.append(p[0].text.strip())
                                vs.append('\n'.join(p[2].stripped_strings))
                                ds.append(p[1].text.strip())
                                continue
                        li = re.sub('\n+', '\n', td[0].text.strip()).split('\n')
                        li = [l.strip() for l in li]
                        li = [l for l in li if l != ""]
                        if i == 2 and trs[0].text.strip() == "Разъемы на задней панели": # Если материнская плата и подтаблица с названием "Разъемы на задней панели"
                            ks.append("Разъемы на задней панели_" + li[0])
                        elif i == 2 and trs[0].text.strip() == "Внутренние разъемы":  # Если материнская плата и подтаблица с названием "Внутренние разъемы"
                            ks.append("Внутренние разъемы_" + li[0])
                        else:
                            ks.append(li[0])
                        if len(li) == 3:
                            ds.append(li[2])
                        else:
                            ds.append("")
                        if td[1].find('span', class_="i-x"):
                            try:
                                vs.append(td.find('span', class_="value__text").text.strip())
                            except:
                                vs.append("No")
                            continue
                        elif td[1].find('span', class_="i-tip"):
                            try:
                                try:
                                    vs.append(td[1].find('span', class_="value__text").text.strip() + ' ' + td[1].find('span', class_="value__text").next_sibling.strip())
                                except:
                                    vs.append(td[1].find('span', class_="value__text").text.strip())
                            except:
                                vs.append("Yes")
                            continue
                        for br_tag in td[1].find_all('br'):
                            br_tag.replace_with('\n')
                        vs.append(td[1].text.strip())
                devices[i].append(Device_classes[i](ks, vs, ds))
                time.sleep(random.uniform(4, 8))
            time.sleep(random.uniform(7, 15))
            if connection is None:
                try:
                    connection = mysql.connector.connect(
                        host=config.host,
                        user=config.user,
                        passwd=config.password,
                        database=config.database
                    )
                    print('Succesfull connected')
                    cursor = connection.cursor()
                except mysql.connector.Error as error:
                    print(f'An error {error} occured')
            write_devices(connection, cursor, page, i, tables_names, devices)
            page += 1
    cursor.close()
    connection.close()

if __name__ == '__main__':
    main()

# RAM, HDD


    # if vs[i] == "Комплектация" то сделать переносы строк

    # device_links = ["https://catalog.onliner.by/cpu/amd/ryzen77700x", #!
    #                 "https://catalog.onliner.by/fan/idcooling/se224xtsargb",
    #                 "https://catalog.onliner.by/motherboard/asrock/b550mpro4",
    #                 "https://catalog.onliner.by/dram/gskill/f55600j3036d16g5",
    #                 "https://catalog.onliner.by/videocard/palit/ne6166s018j91161",
    #                 "https://catalog.onliner.by/ssd/kingston/skc3000s1024g",
    #                 "https://catalog.onliner.by/hdd/seagate/st1000dm010",
    #                 "https://catalog.onliner.by/powersupply/zalman/zm500xeii",
    #                 "https://catalog.onliner.by/chassis/powercase/caxbl4"]