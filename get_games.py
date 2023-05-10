from classes.configuration import Configuration
import os
import constants
import time
import logging
import random
import inspect

import mysql.connector
import csv
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# class One_game_requirements:
#     def __init__(self, *args):
#         self.operation_system = args[0]
#         self.cpu = args[1]
#         self.ram = args[2]
#         self.gpu = args[3]
#         self.directx = args[4]
#         self.network = args[5]
#         self.capacity = args[6]
#         self.additional = args[7]
#
#     def get_all(self):
#         return self.operation_system, self.cpu, self.ram, self.gpu, \
#             self.directx, self.network, self.capacity, self.additional
#
# minimum_requirements = One_game_requirements()
# recommended_requirements = One_game_requirements()


def clear_cache_cookies(driver):
    """Clear the cookies and cache for the ChromeDriver instance."""
    driver.get('chrome://settings/clearBrowserData') # for old chromedriver versions use cleardriverData
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB*9)
    actions.perform()
    actions.send_keys(Keys.ENTER)  # send right combination
    actions.perform()


def concat_notempty(*args):
    return pd.concat([x for x in args if not x.empty], axis=1)

def getClassNamesAndValues(c):
    class_attributes_names, class_attributes_values = [], []
    for i in inspect.getmembers(c):
        if i[0] == "__dict__":
            class_attributes_names = list(i[1].keys())
            class_attributes_values = list(i[1].values())
            return class_attributes_names, class_attributes_values

def write_data(connection, cursor, table_name, req_dicts_list, directions_list, games_names_list):
    for i, game_name in enumerate(games_names_list):
        try: cpu = req_dicts_list[i]["процессор"]
        except: cpu = None
        try: ram = req_dicts_list[i]["оперативная память"]
        except: ram = None
        try: gpu = req_dicts_list[i]["видео карта"]
        except: gpu = None
        try: ssd = req_dicts_list[i]["диск"]
        except: ssd = None
        values_to_write = [game_name, cpu, None, None, ram, gpu, ssd, None, None, None, directions_list[i]]
        placeholders = ', '.join(['%s'] * len(values_to_write))
        write_data_to_table_query = f"INSERT INTO {table_name} (program_name, cpu, cooler, motherboard, ram, gpu, ssd, hdd, power, casePC, directions) VALUES ({placeholders})"
        try:
            cursor.execute(write_data_to_table_query, values_to_write)
            connection.commit()
        except:
            print("Problems with cursor")
    print("Data wroten succesfully")
    return

def parse_games():
    device_info_lists = []
    connection = None
    logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w")
    csv.Dialect.skipinitialspace = True
    main_devices_links = ["https://sysrqmts.com/ru/games"]
    all_games_types = {}
    for iii, main_devices_link in enumerate(main_devices_links):
        driver = webdriver.Chrome()
        # clear_cache_cookies(driver) # Чистим кеш и cookies
        # driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": UserAgent().random}) # Используем случайный user agent, чтобы избежать попадания в черный список сайта
        # print(driver.execute_script("return navigator.userAgent;"))
        i = 4
        while True:
            print(f"page number {i + 1}")
            driver.get(main_devices_link+f"?page={i+1}")
            content = driver.page_source
            soup = BeautifulSoup(content, features="html.parser")
            games_names = soup.find_all(class_="game-card__name")
            games_links = soup.find_all('a', class_="game-card", href=True)
            # try:
            game_type = main_devices_link[30:]
            path = os.path.join(r"D:\PycharmProjects\Diploma", game_type)
            if not os.path.exists(path):
                os.makedirs(path)
            os.chdir(path)
            all_games_types[game_type] = {}
            req_dicts_min_win_list, req_dicts_req_win_list, directions_list, games_names_list = [], [], [], []
            for game_link in games_links:
                game_link = game_link.attrs['href']
                driver.get(game_link)
                game_content = driver.page_source
                soup_game = BeautifulSoup(game_content, features="html.parser")

                is_os_text = soup_game.find_all('h2', class_="page-section__title") # Узнаем какие ОС поддерживают данную игру
                is_os_text = [o.text.lower().strip() for o in is_os_text]
                is_win, is_mac, is_lin = False, False, False
                is_os_list = [is_win, is_mac, is_lin]
                if is_os_text is None:
                    continue
                try:
                    if "win" in is_os_text[0]:
                        is_os_list[0] = True
                except:
                    print("nice")
                else:
                    continue
                game_name = soup_game.find('h1').text[22:].rstrip()

                req_keys = soup_game.find_all(class_="game-requirements-table__name")
                req_keys = [rk.text.strip().lower() for rk in req_keys]
                req_values = soup_game.find_all(class_="game-requirements-table__value")
                req_values = [rv.text.strip().lower() for rv in req_values]

                indices = list(np.where(np.array(req_keys) == "операционная система")[0]) # Тут получаем индексы всех вхождений фразу "операционная система"
                if len(indices) == 0:
                    indices = [0]
                is_req_win, is_req_mac, is_req_lin = False, False, False
                conditions_req = [is_req_win, is_req_mac, is_req_lin]
                ii = 0

                j = 0
                while j < len(indices)-1:
                    if indices[j+1] == indices[j]+1: # Если в таблице и минимальные и рекомендованные требования, то нам нужен только первый индекс из данной таблицы
                        indices.remove(indices[j+1]) # Поэтому удаляем дубликаты
                        j -= 1
                        conditions_req[ii] = True
                    elif ii < len(indices):
                        ii += 1
                    j += 1
                if len(indices) > 1:
                    indices.remove(indices[0]) # Самый первый индекс тоже не особо нужен, потому что он и так присутствует всегда


                req_dict_min_win, req_dict_min_mac, req_dict_min_lin = {}, {}, {}
                req_dict_req_win, req_dict_req_mac, req_dict_req_lin = {}, {}, {}
                req_dicts_min = [req_dict_min_win, req_dict_min_mac, req_dict_min_lin]
                req_dicts_req = [req_dict_req_win, req_dict_req_mac, req_dict_req_lin]

                current_idx = 0
                current_os = 0
                ii = 0
                new_os_index = indices[current_idx] # !!! надо добавить, чтобы еще и для рекомендованной конфигурации был отдельный словарь
                j = 0
                while j < len(req_keys):
                    if len(indices) > 1 and j == new_os_index:  # Если дошли до момента, когда начинаются требования для новой OC
                        current_os += 1
                        if current_os > 1:
                            break
                        current_idx += 1
                        ii += 1
                        if current_idx < len(indices):
                            new_os_index = indices[current_idx]
                    if is_os_list[0] == True: # Это надо для ситуаций, когда отсутствуют mac-требования, но есть linux-требования (чтобы записывалось только для нужной OS
                        req_dicts_min[current_os][req_keys[j]] = req_values[j]  # В словарь с текущей ОС добавляем новую пару ключ-значение
                    if conditions_req[ii] == True:
                        req_dicts_req[current_os][req_keys[j+1]] = req_values[j+1]
                        if j < len(req_keys):
                            j += 1
                    if j < len(req_keys):
                        j += 1
                req_dicts_min_win_list.append(req_dict_min_win)
                req_dicts_req_win_list.append(req_dict_req_win)
                time.sleep(1)
                try:
                    genres_dd = soup_game.find('dt', string=' Жанры ').find_next_sibling('dd') # Находим список жанров
                    genres = [a.text for a in genres_dd.find_all('a')]
                except:
                    try:
                        genres_dd = soup_game.find('dt', string=' Жанр ').find_next_sibling('dd')  # Находим список жанров
                        genres = [a.text for a in genres_dd.find_all('a')]
                    except:
                        genres = [""]
                genres_string = ", ".join(genres)
                genres_string = genres_string + ".\n"
                try:
                    categories_dd = soup_game.find('dt', string=' Категории ').find_next_sibling('dd') # Находим список категорий
                    categories = [a.text for a in categories_dd.find_all('a')]
                except:
                    try:
                        categories_dd = soup_game.find('dt', string=' Категория ').find_next_sibling('dd')  # Находим список категорий
                        categories = [a.text for a in categories_dd.find_all('a')]
                    except:
                        categories = [""]
                categories_string = ", ".join(categories)
                directions = genres_string + categories_string
                directions_list.append(directions)
                games_names_list.append(game_name)

                print(f"this is {game_name}")
                time.sleep(random.uniform(7, 15))

            if connection is None:
                try:
                    connection = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        passwd="password",
                        database="diploma"
                    )
                    print('Succesfull connected')
                    cursor = connection.cursor()
                except mysql.connector.Error as error:
                    print(f'An error {error} occured')
            write_data(connection, cursor, "min_reqs", req_dicts_min_win_list, directions_list, games_names_list)
            write_data(connection, cursor, "recommended_reqs", req_dicts_req_win_list, directions_list, games_names_list)
            i += 1



if __name__ == '__main__':
    parse_games()