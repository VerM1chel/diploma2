import constants
from sqlConfigAndQueries import config
from sqlConfigAndQueries import queries
from classes.details.cpu import Cpu
from classes.details.cooler import Cooler
from classes.details.motherboard import Motherboard
from classes.details.ram import Ram
from classes.details.gpu import Gpu
from classes.details.ssd import Ssd
from classes.details.hdd import Hdd
from classes.details.case_PC import Case
from classes.details.power import Power
from classes.configuration import Configuration
from classes.reqs import Requirements

import numpy as np
from flask import Flask, jsonify, request
import re
import difflib
import mysql.connector


app = Flask(__name__)
budget = 0
just_one = 0
total_price = 0
data_fromDB, legacyDevices, none_details = [], [], []
indeces, selectedItems, prices, keywords = [], [], [], []
min_reqs, rec_reqs = [], []


@app.route('/indeces')
def get_details():
    return jsonify(indeces)
@app.route('/prices')
def get_prices():
    return jsonify(prices)
@app.route('/cpus')
def get_cpus():
    details_list = []
    for detail in data_fromDB[0]:
        detail_dict = {key: value for key, value in vars(detail).items()}
        details_list.append(detail_dict)
    return jsonify(details_list)
@app.route('/coolers')
def get_coolers():
    details_list = []
    for detail in data_fromDB[1]:
        detail_dict = {key: value for key, value in vars(detail).items()}
        details_list.append(detail_dict)
    return jsonify(details_list)
@app.route('/motherboards')
def get_motherboards():
    details_list = []
    for detail in data_fromDB[2]:
        detail_dict = {key: value for key, value in vars(detail).items()}
        details_list.append(detail_dict)
    return jsonify(details_list)
@app.route('/rams')
def get_rams():
    details_list = []
    for detail in data_fromDB[3]:
        detail_dict = {key: value for key, value in vars(detail).items()}
        details_list.append(detail_dict)
    return jsonify(details_list)
@app.route('/gpus')
def get_gpus():
    details_list = []
    for detail in data_fromDB[4]:
        detail_dict = {key: value for key, value in vars(detail).items()}
        details_list.append(detail_dict)
    return jsonify(details_list)
@app.route('/ssds')
def get_ssds():
    details_list = []
    for detail in data_fromDB[5]:
        detail_dict = {key: value for key, value in vars(detail).items()}
        details_list.append(detail_dict)
    return jsonify(details_list)
@app.route('/hdds')
def get_hdds():
    details_list = []
    for detail in data_fromDB[6]:
        detail_dict = {key: value for key, value in vars(detail).items()}
        details_list.append(detail_dict)
    return jsonify(details_list)
@app.route('/powers')
def get_powers():
    details_list = []
    for detail in data_fromDB[7]:
        detail_dict = {key: value for key, value in vars(detail).items()}
        details_list.append(detail_dict)
    return jsonify(details_list)
@app.route('/casePCs')
def get_casePCs():
    details_list = []
    for detail in data_fromDB[8]:
        detail_dict = {key: value for key, value in vars(detail).items()}
        details_list.append(detail_dict)
    return jsonify(details_list)

@app.route('/selectedItems', methods=['POST'])
def getSelectedItems():
    global selectedItems
    selectedItems = request.get_json()  # Получаем данные postData из POST-запроса
    response_data = {'message': 'Success'}  # Пример данных для ответа
    return jsonify(response_data), 200  # Отправляем ответ в формате JSON
@app.route('/sortBy/<sortType>', methods=['GET'])
def sort_by_price(sortType):
    global indeces, data_fromDB, selectedItemsx
    old_data = data_fromDB
    sorted_data, new_indeces, sorted_data_response, new_selectedItemsIndeces, new_selectedItems_response = [], [], [], [], []
    for sublist in data_fromDB: # Сортируем сами списки
        if sortType == 'price':
            sorted_type = sorted(sublist, key=lambda x: x.price)
        elif sortType == 'name':
            sorted_type = sorted(sublist, key=lambda x: x.name)
        elif sortType == 'id':
            sorted_type = sorted(sublist, key=lambda x: x.id)
        sorted_data.append(sorted_type)
    for i, idx in enumerate(indeces): # Сортируем индексы от рекомендованной конфгурации
        element = old_data[i][idx]
        element_index = sorted_data[i].index(element)
        new_indeces.append(element_index)

    for i, si in enumerate(selectedItems): # Выбираем элементы, которые были текущими до сортировки
        for idx, item in enumerate(sorted_data[i]):
            if item.name == si["name"]:
                index = idx
                break
        new_selectedItemsIndeces.append(index)
    new_selectedItems = []
    for i,newItemsIdx in enumerate(new_selectedItemsIndeces):
        new_selectedItems.append(sorted_data[i][newItemsIdx])
    for i,details in enumerate(sorted_data): # Отсортированные списки представляем в пересылаемом виде
        sorted_data_response.append([])
        for detail in details:
            detail_dict = {key: value for key, value in vars(detail).items()}
            sorted_data_response[i].append(detail_dict)

    for nsi in new_selectedItems: # Также создаем список из текущих элементов для передачи
        detail_dict = {key: value for key, value in vars(nsi).items()}
        new_selectedItems_response.append(detail_dict)
    indeces = new_indeces
    data_fromDB = sorted_data
    response_data = {
        "cpus": sorted_data_response[0],
        "coolers": sorted_data_response[1],
        "motherboards": sorted_data_response[2],
        "rams": sorted_data_response[3],
        "gpus": sorted_data_response[4],
        "ssds": sorted_data_response[5],
        "hdds": sorted_data_response[6],
        "powers": sorted_data_response[7],
        "casePCs": sorted_data_response[8],
        "selectedItems": new_selectedItems_response,
        "numbers": new_indeces
    }
    return jsonify(response_data)


@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
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
    cursor.execute(f"SELECT * FROM USERS WHERE username = '{username}' and password = '{password}'")
    result = cursor.fetchall()
    if result:
        return jsonify({'message': 'Такой пользователь уже существует'}), 409
    cursor.execute("INSERT INTO USERS (username, password) VALUES (%s, %s)", (username, password))
    connection.commit()
    cursor.close()
    return jsonify({'message': 'Пользователь успешно зарегистрирован'}), 200

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
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
    cursor.execute(f"SELECT * FROM USERS WHERE username = '{username}' and password = '{password}'")
    result = cursor.fetchall()
    if result:
        return jsonify({'success': True, 'message': 'Вход выполнен успешно'})
    return jsonify({'success': False, 'message': 'Неверное имя пользователя или пароль'}), 401

@app.route('/saveConfiguration', methods=['POST'])
def save_configuration():
    # Get the selectedItems from the request body
    selected_items = request.json.get('selectedItems')
    username = request.json.get('username')
    print(username) #!
    try:
        connection = mysql.connector.connect(
            host=config.host,
            user=config.user,
            passwd=config.password,
            database=config.database
        )
        print('Succesfull connected')
        cursor = connection.cursor()
        user_id = getUserIdByUsername(cursor, username)
        values_conf = user_id, selected_items["selectedItems"][0] + 1, selected_items["selectedItems"][1] + 1, \
                      selected_items["selectedItems"][2] + 1, selected_items["selectedItems"][3] + 1, \
                      selected_items["selectedItems"][4] + 1, selected_items["selectedItems"][5] + 1, \
                      selected_items["selectedItems"][6] + 1, selected_items["selectedItems"][7] + 1, \
                      selected_items["selectedItems"][8] + 1
        sql_conf = """
                  INSERT INTO CONFIGURATIONS (user_id, cpu_id, cooler_id, motherboard_id, ram_id, gpu_id, ssd_id, hdd_id, power_id, case_id)
                  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
        cursor.execute(sql_conf, values_conf)
        connection.commit()
        cursor.close()
        return {'message': 'Configuration saved successfully'}
    except mysql.connector.Error as error:
        print(f'An error {error} occured')
        return {'message': "Configuration haven't wroten"}

@app.route('/getConfigurations', methods=['GET'])
def get_configurations():
    try:
        connection = mysql.connector.connect(
            host=config.host,
            user=config.user,
            passwd=config.password,
            database=config.database
        )
        print('Succesfull connected')
        cursor = connection.cursor()
        cursor.execute(queries.get_configurations_from_db)
        configurations = cursor.fetchall()
        # print(configurations)
        cursor.close()
        connection.close()
    except mysql.connector.Error as error:
        print(f'An error {error} occured')
    return jsonify(configurations)

@app.route('/keywords', methods=['POST'])
def handle_keywords():
    global keywords
    keywords = request.json.get('keywords')
    keywords = [kword.strip() for kword in keywords.lower().split(",")]
    return {'message': 'Keywords received successfully'}

@app.route('/checkConfiguration', methods=['POST'])
def check_configuration():
    data = request.get_json()
    selected_items = data['selectedItems']['selectedItems']
    username = data['username']
    try:
        connection = mysql.connector.connect(
            host=config.host,
            user=config.user,
            passwd=config.password,
            database=config.database
        )
        print('Succesfull connected')
        cursor = connection.cursor()
        cursor.execute(queries.check_configuration, (username, selected_items[0]+1, selected_items[1]+1, selected_items[2]+1, selected_items[3]+1, selected_items[4]+1,
            selected_items[5]+1, selected_items[6]+1, selected_items[7]+1, selected_items[8]+1))
        result = cursor.fetchall()
    except mysql.connector.Error as error:
        print(f'An error {error} occured')
    if len(result) == 0:
        return jsonify({'isSaved': False})
    else:
        return jsonify({'isSaved': True})

@app.route('/updateBudget', methods=['POST'])
def update_budget():
    global indeces, prices, total_price, just_one, data_fromDB, legacyDevices, none_details
    try:
        data = request.get_json()
        budget = float(data.get('budget'))
        main(budget, data_fromDB, legacyDevices, none_details)  # Вызов функции main() с передачей значения budget
        return {'success': True}
    except Exception as e:
        return {'success': False, 'error': str(e)}


def getUserIdByUsername(cursor, username):
    user_id = None
    get_user_id_query = """
    SELECT id
    FROM USERS
    WHERE username = %s
    """
    cursor.execute(get_user_id_query, (username,))
    result = cursor.fetchone()
    if result:
        user_id = result[0]
    print(f"user_id {user_id}")
    return user_id

def longest_common_subsequence(str1, str2):
    m = len(str1)
    n = len(str2)
    lcs = [[0] * (n + 1) for _ in range(m + 1)] # Создаем матрицу размером (m+1) x (n+1)
    for i in range(1, m + 1): # Заполняем матрицу по правилам алгоритма LCS
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
    return lcs[m][n]

def string_similarity(str1, str2):
    lcs_length = longest_common_subsequence(str1, str2)
    similarity = lcs_length / len(str2)
    return similarity
#
# def check_common_element(list0, list1):
#     ratio = 0.0
#     for item0 in list0:
#         for item1 in list1:
#             ratio12 = string_similarity(item0, item1)
#             ratio21 = string_similarity(item1, item0)
#             if ratio12 > 0.8 or ratio21 > 0.8:
#                 return True
#     return False
#
# def check_element_in_str(list0, string):
#     ratio = 0.0
#     for item in list0:
#         ratio12 = string_similarity(item, string)
#         ratio21 = string_similarity(string, item)
#         if ratio12 > 0.8 or ratio21 > 0.8:
#             return True
#     return False
#
# def find_reqs_by_keywords():
#     global min_reqs, rec_reqs, keywords
#     result_min, result_req = [], []
#     keywords = [k.lower() for k in keywords]
#     for mr in min_reqs:
#         if mr.program_name == 'the witcher 2: assassins of kings enhanced edition':
#             print(9)
#         if check_element_in_str(keywords, mr.program_name) or check_common_element(keywords, mr.keywords):
#             result_min.append(mr)
#     for rr in rec_reqs:
#         if mr.program_name == 'the witcher 2: assassins of kings enhanced edition':
#             print(9)
#         if check_element_in_str(keywords, rr.program_name) or check_common_element(keywords, rr.keywords):
#             result_req.append(rr)
#     return result_min, result_req

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def check_common_element(list0, list1):
    coincidences = 0
    for item0 in list0:
        for item1 in list1:
            if item0 in item1:
                coincidences += 1
    return coincidences

def check_element_in_str(list0, string):
    coincidences = 0
    for item0 in list0:
        if item0 in string:
            coincidences += 1
    return coincidences

def find_reqs_by_keywords():
    global min_reqs, rec_reqs, keywords
    result_min, result_rec = [], []
    last_max_sum_min, last_max_sum_rec = 0, 0
    for mr in min_reqs:
        coincidences_by_name = check_element_in_str(keywords, mr.program_name)
        coincidences_by_keywords = check_common_element(keywords, mr.keywords)
        if coincidences_by_name or coincidences_by_keywords:
            if coincidences_by_name + coincidences_by_keywords > last_max_sum_min:
                result_min = mr
                last_max_sum_min = coincidences_by_name + coincidences_by_keywords
    for rr in rec_reqs:
        coincidences_by_name = check_element_in_str(keywords, rr.program_name)
        coincidences_by_keywords = check_common_element(keywords, rr.keywords)
        if coincidences_by_name or coincidences_by_keywords:
            if coincidences_by_name + coincidences_by_keywords > last_max_sum_rec:
                result_rec = rr
            last_max_sum_rec = coincidences_by_name + coincidences_by_keywords
    return result_min, result_rec

def get_specified_cpu(cpus, suitable_cpu_name_min, suitable_cpu_name_rec):
    try: suitable_cpu_name_min = suitable_cpu_name_min.cpu
    except: suitable_cpu_name_min = None
    try: suitable_cpu_name_rec = suitable_cpu_name_rec.cpu
    except: suitable_cpu_name_rec = None
    delimiters = [' or ', ' или ']
    for delimiter in delimiters:
        if suitable_cpu_name_min != None:
            suitable_cpu_name_min = suitable_cpu_name_min.replace(delimiter, '/')
        if suitable_cpu_name_rec != None:
            suitable_cpu_name_rec = suitable_cpu_name_rec.replace(delimiter, '/')
    if suitable_cpu_name_min != None:
        suitable_cpu_min = [item.strip().lower() for item in suitable_cpu_name_min.split('/')]
    if suitable_cpu_name_rec != None:
        suitable_cpu_rec = [item.strip().lower() for item in suitable_cpu_name_rec.split('/')]
    for cpu in cpus:
        cpu_name = cpu.name.lower()
        if "процессор " in cpu_name:
            cpu_name = cpu_name.replace("процессор ", "")
        if " core " in cpu_name:
            cpu_name = cpu_name.replace(" core", "")
        if suitable_cpu_name_rec != None:
            for scr in suitable_cpu_rec:
                if scr in cpu_name:
                    return cpu
        if suitable_cpu_name_min != None:
            for scm in suitable_cpu_min:
                if scm in cpu_name:
                    return cpu
    return None

def get_specified_gpu(gpus, suitable_gpu_name_min, suitable_gpu_name_rec):
    try: suitable_gpu_name_min = suitable_gpu_name_min.gpu
    except: suitable_gpu_name_min = None
    try: suitable_gpu_name_rec = suitable_gpu_name_rec.gpu
    except: suitable_gpu_name_rec = None
    delimiters = [" or ", " или ", ", "]
    for delimiter in delimiters:
        if suitable_gpu_name_min != None:
            suitable_gpu_name_min = suitable_gpu_name_min.replace(delimiter, '/')
        if suitable_gpu_name_rec != None:
            suitable_gpu_name_rec = suitable_gpu_name_rec.replace(delimiter, '/')
    if suitable_gpu_name_min != None:
        suitable_gpu_min = [item.strip().lower() for item in suitable_gpu_name_min.split('/')]
    if suitable_gpu_name_rec != None:
        suitable_gpu_rec = [item.strip().lower() for item in suitable_gpu_name_rec.split('/')]
    for gpu in gpus:
        gpu_name = gpu.name.lower()
        if "amd" in gpu_name or "radeon" in gpu_name: # Видеокарты от AMD в данный момент не стоят своих денег и уступают по функционалу Intel
            continue
        if "nvidia " in gpu_name:
            gpu_name = gpu_name.replace("nvidia ", "")
        if suitable_gpu_name_rec != None:
            for scr in suitable_gpu_rec:
                if scr in gpu_name:
                    return gpu
        if suitable_gpu_name_min != None:
            for scm in suitable_gpu_min:
                if scm in gpu_name:
                    return gpu
    return None

def get_same_cpu(requiredLegacyCpu, cpus): # Функция для нахождения процессора, аналогичного процессору, указанному в требоваинях
    min_difference = float('inf')
    selected_cpu = None
    suitableCpus = []
    features_for_comparison = [requiredLegacyCpu.num_cores, requiredLegacyCpu.max_threads, requiredLegacyCpu.base_clock, requiredLegacyCpu.l2_cache, requiredLegacyCpu.l3_cache]
    for i in range(len(features_for_comparison)):
        if features_for_comparison[i] == None:
            features_for_comparison[i] = 0
    requiredLegacyCpu.num_cores = features_for_comparison[0]
    requiredLegacyCpu.max_threads = features_for_comparison[1]
    requiredLegacyCpu.base_clock = features_for_comparison[2]
    requiredLegacyCpu.l2_cache = features_for_comparison[3]
    requiredLegacyCpu.l3_cache = features_for_comparison[4]

    for cpu in cpus:
        features_for_comparison = [cpu.num_cores, cpu.max_threads, cpu.base_clock, cpu.l2_cache, cpu.l3_cache]
        for i in range(len(features_for_comparison)):
            if features_for_comparison[i] == None:
                features_for_comparison[i] = 0
        cpu.num_cores = features_for_comparison[0]
        cpu.max_threads = features_for_comparison[1]
        cpu.base_clock = features_for_comparison[2]
        cpu.l2_cache = features_for_comparison[3]
        cpu.l3_cache = features_for_comparison[4]
        if (cpu.num_cores >= requiredLegacyCpu.num_cores and
                cpu.max_threads >= requiredLegacyCpu.max_threads and
                cpu.base_clock >= requiredLegacyCpu.base_clock and
                cpu.l2_cache >= requiredLegacyCpu.l2_cache and
                cpu.l3_cache >= requiredLegacyCpu.l3_cache):
            suitableCpus.append(cpu)
    min_price = float('inf')
    for sCpu in suitableCpus:
        difference = (abs(sCpu.num_cores - requiredLegacyCpu.num_cores) +
                      abs(sCpu.max_threads - requiredLegacyCpu.max_threads) +
                      abs(sCpu.base_clock - requiredLegacyCpu.base_clock) +
                      abs(sCpu.l2_cache - requiredLegacyCpu.l2_cache) +
                      abs(sCpu.l3_cache - requiredLegacyCpu.l3_cache))
        if difference < min_difference and sCpu.price <= min_price:
            min_difference = difference
            selected_cpu = sCpu
            min_price = sCpu.price
    return selected_cpu

def get_same_gpu(requiredLegacyGpu, gpus):
    min_difference = float('inf')
    selected_gpu = None
    suitableGpus = []
    for gpu in gpus:
        features_for_comparison = [gpu.video_memory, gpu.gpu_base_frequency, gpu.cooling, gpu.num_stream_processors,
                                   gpu.memory_bandwidth]
        for i in range(len(features_for_comparison)):
            if features_for_comparison[i] == None:
                features_for_comparison[i] = 0
        gpu.video_memory = features_for_comparison[0]
        gpu.gpu_base_frequency = features_for_comparison[1]
        gpu.cooling = features_for_comparison[2]
        gpu.num_stream_processors = features_for_comparison[3]
        gpu.memory_bandwidth = features_for_comparison[4]
        if (gpu.video_memory >= requiredLegacyGpu.video_memory and
                gpu.gpu_base_frequency >= requiredLegacyGpu.gpu_base_frequency and
                gpu.cooling == requiredLegacyGpu.cooling and
                gpu.num_stream_processors >= requiredLegacyGpu.num_stream_processors and
                gpu.memory_bandwidth >= requiredLegacyGpu.memory_bandwidth):
            suitableGpus.append(gpu)
    min_price = float('inf')
    for sGpu in suitableGpus:
        difference = (abs(sGpu.video_memory - requiredLegacyGpu.video_memory) +
                      abs(sGpu.gpu_base_frequency - requiredLegacyGpu.gpu_base_frequency) +
                      int(sGpu.cooling != requiredLegacyGpu.cooling) +
                      abs(sGpu.num_stream_processors - requiredLegacyGpu.num_stream_processors) +
                      abs(sGpu.memory_bandwidth - requiredLegacyGpu.memory_bandwidth))
        if difference < min_difference and sGpu.price <= min_price:
            min_difference = difference
            selected_gpu = sGpu
            min_price = sGpu.price
    return selected_gpu

# Done
def cpu_logic(budget, cpus): # Функция возвращает список потенциально возможных комплектующих
    result = []
    for cpu in cpus:
        if budget < 1700 and cpu.cooling_included != "No":  # для дешевых конфигураций, чтобы сэкономить, можно купить процессор со встроенным кулером
            result.append(cpu)
        else:
            result.append(cpu)
    return result

# Done
def cooler_logic(budget, coolers, cpu):
    result = []
    if budget < 1300 and cpu.cooling_included == "Yes": # для дешевых конфигураций, чтобы сэкономить, можно купить процессор со встроенным кулером (то есть тут кулер не нужен)
        return []
    else:
        for cooler in coolers:
            if cooler.cooling != "водяное": # Если кулер все-таки нужен, то лучше исключить водяное охлаждение (оно подходит только под несколько типов корпусов) и то, только сборщики знают, как правильно оно собирается (там все эмпирическим путем узнается)
                if cooler.power_dissipation != None:
                    if 20 < (cooler.power_dissipation - cpu.estimated_thermal_power): #??? () < 55 # Кулер должен рассеивать достаточно тепла, чтобы процессор не перегревался, но излишне слишком мощные кулеры нам тоже не нужны
                        result.append(cooler)
    return result

# Done
def motherboard_logic(budget, motherboards, cpu):
    result = []
    for motherboard in motherboards:
        if cpu.socket == motherboard.socket: # Сокеты процессора и материнской платы должны совпадать
            if budget < 1400 and cpu.integrated_graphics != "No" and motherboard.integrated_graphics_support == "Yes": # Если выбран процессор со встроенной графикой, то материнская плата должна это поддерживать
                result.append(motherboard)
            else:
                result.append(motherboard)
    return result

# . Для мощных -- только RTX и выше
def gpu_logic(budget, gpus, cpu, direction):
    result = []
    # Если основной целью ПК не является активное использование приложений, требующих мощного графического процессора и значение бюджета мало, то можно обойтись только встроенной в процессор граффикой
    if (direction != "игровой" or direction != "графический дизайн" or direction != "3d" or "видео- и аудио-производство") and budget < 1400 and cpu.integrated_graphics != "No":  # Если бюджет маловат и процессор имеет встроенную графику, то грех этим не воспользоваться (дискретную видеокарту не берем)
        return result
    for gpu in gpus:
        if gpu.recommended_psu_watts != None: # Надо знать, какая видеокарта, чтобы выбрать подходящий блок питания
            if gpu.gpu_manufacturer != "AMD": # AMD -- нет raytrace и сильнее греются
                if direction == "игровой" or direction == "графический дизайн" or direction == "3d" or "видео- и аудио-производство":
                    if "GTX" not in gpu.name:
                        result.append(gpu)
                else:
                    result.append(gpu)
    return result

# Done
def ram_logic(budget, motherboard, suitable_req_min, rams):
    result = []
    if suitable_req_min != []:
        srm_volume = suitable_req_min.ram
        srm_volume = int(re.sub(" gb", "", srm_volume))
    else:
        srm_volume = 0
    try:
        for ram in rams:
            if ram.overall_volume == None:
                ram.overall_volume = 0
            if ram.overall_volume > srm_volume:
                # SO-DIMM -- для ноутбуков, их пропускаем
                if "DDR4" in ram.ram_type and "SO-DIMM" not in ram.ram_type:  # DDR3 устарели, а DDR5 -- неоправдано дорогие (переплачиваем за отдельное питание на модуле памяти, за бесполезное ЕСС, за маркетинг, а получаете большие задержки и отсутствие практического смысла от слова совсем)
                    if not (ram.kit == 1 and ram.overall_volume == 4): # Одна планка памяти на 4 Гб это слишком мало, т.е. нужно чтобы DDR была на 8+ Гб
                        if budget > 1700: # если комп от 600 баксов, то частота DDR минимум 3000
                            if ram.frequency >= 3000 and ram.frequency < 4200: # Но слишком большая частота избыточна
                                if motherboard.num_of_memory_slots >= ram.kit and motherboard.max_memory >= ram.overall_volume: # Материнская плата должна обеспечивать то, что планки памяти. До частоты 3200 оперативной памяти, частота материнской платы может быть существенно ниже, но после значения в 3400 у RAM значения частоты не должны сильно различаться
                                    if ram.frequency >= 3200 and (motherboard.max_memory_frequency - ram.frequency) > -100:
                                        result.append(ram)
                                    elif ram.frequency < 3200:
                                        result.append(ram)
                        else:
                            if motherboard.num_of_memory_slots >= ram.kit and motherboard.max_memory >= ram.overall_volume and ram.frequency <= 3200:
                                result.append(ram)
    except:
        print(10)
    return result

# Done
def ssd_logic(budget, ssds, motherboard, itSeconfSSD=False): # Всегда (даже если бюджет ограничен, берем 512 Гб SSD) (256 Гб для совсем дешевок)
# Чекнуть разъемы M.2 (M.2 дорогие и крутые для игровых) (М.2 ssd (операционка и прога в которой ты работаешь) и SATA ssd для остального
    result = []
    for ssd in ssds:
        if budget < 1000:
            if ssd.volume == 256:
                result.append(ssd)
        else:
            if ssd.volume >= 512:
                if budget > 4500:
                    if itSeconfSSD == False and motherboard.mdot2 != "No": # Для мощного компьютера в качестве основного SSD выберем M.2. Если надо больше дискового пространства, то ставим SATA. Ну, и надо, чтобы в материнской плате поддерживался данный разъем
                        if ssd.form_factor == "M.2":
                            result.append(ssd)
                    else:
                        if ssd.form_factor != "M.2":
                            result.append(ssd)
            else:
                result.append(ssd)
    return result

# Done
def hdd_logic(budget, hdds): # HDD опциональная опция)
    result = []
    for hdd in hdds:
        if hdd.spindle_speed != None:
            if budget > 1700:  # брать ТОЛЬКО с частотой 7200 (hdd нужен если надо много чего хранить
                if hdd.spindle_speed >= 7200:
                    result.append(hdd)
            else:
                result.append(hdd)
    return result

# Done
def power_logic(budget, powers, gpu):
    certificate_types = ["бронзовый", "серебряный", "золотой", "платиновый", "титановый"]
    result = []
    for power in powers:
        if power.width != None:
            if gpu != None:
                if gpu.recommended_psu_watts != None:
                    if (gpu.recommended_psu_watts < 600 and power.power >= 600) or (gpu.recommended_psu_watts > 600 and power.power >= gpu.recommended_psu_watts): # Если видеокарта требует <600 Вт, то ставим блок на 600. Если видеокарта требует >600, то берем блок с мощностью ровно (или чутка больше), чем нужно для видеокарты
                        if budget > 1200:  # Если комп не полная дешевка, то берем минимум бронзовый сертификат
                            if power.certificate_80plus != None:
                                if power.certificate_80plus.strip() in certificate_types:
                                    result.append(power)
                        else:
                            result.append(power)
            elif (power.power >= 600):
                result.append(power)
    return result

#Done
# корпус всегда брать без блока питания (если комп <= 1000, то комп без дискретного блока питания, только со встроенным)
def case_logic(budget, cases, motherboard, gpu, power):
    result = []
# Вообще, лучше брать только ATX, потому что особого смысла брать microATX и miniATX нет -- они дорогие, а цены не оправданы
    for case in cases:
        if case.portable_power_supplies != None and motherboard.form_factor in case.portable_power_supplies: # Надо, чтобы материнская плата помещалась в корпус (являлась совместимой для данного корпуса)
            if gpu != None:
                if case.max_graphics_card_length != None and case.max_graphics_card_length >= gpu.video_card_length: # Также, надо, чтобы видеокарта помещалась в корпус. Если меньше даже на миллиметр -- то все равно не влезет
                    if budget <= 1000 and case.power != "отсутствует" and case.power != None:  # если комп дешевый, то выбираем только корпуса со встроенным блоком питания (существенная экономия)
                        if (gpu.recommended_psu_watts < 600 and int(case.power.split()[0]) >= 600) or (gpu.recommended_psu_watts > 600 and int(case.power.split()[0]) >= gpu.recommended_psu_watts):
                            result.append(case)
                    if budget > 1000 and (case.power == "отсутствует" or case.power == None): # Если все же ставим блок питания
                        if power.width != None: # Если комп не слишком дешевый, то лучше все же поставить блок питания. А так как блок питания не встроенный, то он должен помещаться в корпус
                            if case.max_power_supply_length != None and case.max_power_supply_length >= power.width:
                                result.append(case)
            else:
                if budget <= 1000 and case.power != "отсутствует" and case.power != None:  # если комп дешевый, то выбираем только корпуса со встроенным блоком питания (существенная экономия)
                        result.append(case)
                if budget > 1000 and (case.power == "отсутствует" or case.power == None): # Если все же ставим блок питания
                    if power.width != None:  # Если комп не слишком дешевый, то лучше все же поставить блок питания. А так как блок питания не встроенный, то он должен помещаться в корпус
                        if case.max_power_supply_length != None and case.max_power_supply_length >= power.width:
                            result.append(case)
    return result

def create_conf(details, idealPrice, maybeDontNeedDetail=False):
    filtered_details = []
    # for d in details:
        # if abs(idealPrice - d.price) <= 50:
        #     filtered_details.append(d)
    sorted_details = sorted(details, key=lambda d: abs(idealPrice - d.price)) # Получаем список, у которого первые элементы -- это экземпляры класса с наиболее близким совпадением к желаемой цене
    print()
    # for s in sorted_details:
        # print(f"{s.price} raznnica= {idealPrice - d.price}")
    if maybeDontNeedDetail == False:
        if len(sorted_details) < 1:
            print("При заданном бюждете невозможно составить конфигурацию, либо отсутствуют необходимые комплектующие из соответствующего ценового диапазона")
            exit(3)
    if len(sorted_details) == 0:
        return []
    return sorted_details[0]

    # return sorted_details[:5] # Возвращаем топ 5 совпадений

def read_from_db(connection, table_name, my_class, keys):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    my_class_list, legacyDevices = [], []
    none_item = my_class(keys, [0] + ["None"] + [0] + [None] * (len(keys) - 2), [], reading=True) # Пустая запись, пока ничего не выбрано
    for row in cursor:
        values = list(row)
        if values[keys.index("Цена")] is not None:
            my_class_list.append(my_class(keys, values, [], reading=True))
        elif (my_class == Cpu or my_class == Gpu) and values[keys.index("Цена")] is None:
            legacyDevices.append(my_class(keys, values, [], reading=True))
    cursor.close()
    return my_class_list, legacyDevices, none_item

def prepare_data():
    connection = None
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

    # 3. Read all devices from database
    cpus_fromDB, legacy_cpus, none_cpu = read_from_db(connection, "cpus", Cpu, constants.cpu_keys)
    coolers_fromDB, _, none_cooler = read_from_db(connection, "coolers", Cooler, constants.cooler_keys)
    motherboards_fromDB, _, none_motherboard = read_from_db(connection, "motherboards", Motherboard, constants.motherboard_keys)
    rams_fromDB, _, none_ram = read_from_db(connection, "rams", Ram, constants.ram_keys)
    gpus_fromDB, legacy_gpus, none_gpu = read_from_db(connection, "gpus", Gpu, constants.gpu_keys)
    ssds_fromDB, _, none_ssd = read_from_db(connection, "ssds", Ssd, constants.ssd_keys)
    hdds_fromDB, _, none_hdd = read_from_db(connection, "hdds", Hdd, constants.hhd_keys)
    powers_fromDB, _, none_power = read_from_db(connection, "powers", Power, constants.power_keys)
    cases_fromDB, _, none_case = read_from_db(connection, "cases", Case, constants.case_keys)
    data_fromDB = cpus_fromDB, coolers_fromDB, motherboards_fromDB, rams_fromDB, gpus_fromDB, ssds_fromDB, hdds_fromDB, powers_fromDB, cases_fromDB
    legacy_datails = legacy_cpus, legacy_gpus
    none_details = none_cpu, none_cooler, none_motherboard, none_ram, none_gpu, none_ssd, none_hdd, none_power, none_case
    for i, none_list in enumerate(none_details):
        data_fromDB[i].insert(0, none_details[i])

    min_reqs, rec_reqs = [], []
    cursor = connection.cursor()
    cursor.execute(f"SELECT program_name, cpu, ram, gpu, ssd, directions FROM min_reqs")
    for row in cursor:
        values = list(row)
        min_reqs.append(Requirements(program_name=values[0], cpu=values[1], ram=values[2], gpu=values[3], ssd=values[4], keywords=values[5]))
    cursor.execute(f"SELECT program_name, cpu, ram, gpu, ssd, directions FROM recommended_reqs")
    for row in cursor:
        values = list(row)
        rec_reqs.append(Requirements(program_name=values[0], cpu=values[1], ram=values[2], gpu=values[3], ssd=values[4], keywords=values[5]))
    return data_fromDB, legacy_datails, none_details, min_reqs, rec_reqs


def main(budget, data_fromDB, legacyDevices, none_details):
    cpus_fromDB, coolers_fromDB, motherboards_fromDB, rams_fromDB, gpus_fromDB, ssds_fromDB, hdds_fromDB, powers_fromDB, cases_fromDB = data_fromDB
    none_cpu, none_cooler, none_motherboard, none_ram, none_gpu, none_ssd, none_hdd, none_power, none_case = none_details
    print(f"I am main budget is {budget}")
    global indeces
    global prices
    global total_price
    configurations = []

    # get_details(cpus_fromDB)

    suitable_req_min, suitable_req_rec = find_reqs_by_keywords()

    cpu, cooler, motherboard, ram, gpu, ssd, hdd, power, casePC = None, None, None, None, None, None, None, None, None
    # CPU
    specified_cpu = get_specified_cpu(cpus_fromDB[1:], suitable_req_min, suitable_req_rec) # Сначала ищем требуемый процессор из списка актуальных комплектующих
    if specified_cpu == None:
        legacyCpu = get_specified_cpu(legacyDevices[0], suitable_req_min, suitable_req_rec)
        if legacyCpu != None:
            specified_cpu = get_same_cpu(legacyCpu, cpus_fromDB[1:]) # Если не нашли, то ищем аналогичный процессор, чтобы по характеристикам был примерно похож на искомый
    if specified_cpu == None:
        cpus = cpu_logic(budget, cpus_fromDB[1:]) # Если, несмотря на все поиски, ничего найдено не было, то процессор выбирается так, если бы ключевые слова не были введены
        if budget >= 1400:
            cpu = create_conf(details=cpus, idealPrice=budget * 0.20)
        elif budget < 1300:  # если конфигурация слишком дешевая
            cpu = create_conf(details=cpus, idealPrice=budget * (0.20 + 0.26 + 0.03))  # если процессор и со встроенной графикой, и со встроенным кулером
        elif budget < 1400:  # если конфигурация дешевая
            cpu = create_conf(details=cpus, idealPrice=budget * (0.20 + 0.26))  # если процессор со встроенной графикой
    else:
        if budget >= 1400:
            if specified_cpu.price <= budget*0.20:
                cpu = specified_cpu
        elif budget < 1300 and specified_cpu.integrated_graphics != "No" and specified_cpu.delivery_type.lower() != "box": # если конфигурация слишком дешевая
            if specified_cpu.price <= budget * (0.20 + 0.26 + 0.03):
                cpu = specified_cpu
        elif budget < 1400 and specified_cpu.integrated_graphics != "No":  # если конфигурация дешевая
            if specified_cpu.price <= budget*(0.20+0.26):
                cpu = specified_cpu
    if cpu == None: # Если ничего не подошло по цене
        print("Не хватает бюджета на CPU")
        # exit(11)

    # Cooler
    # if budget < 1300 and cpu.delivery_type.lower() != "box":
    #     coolers = cooler_logic(budget, coolers_fromDB[1:], cpu)
    #     cooler = create_conf(details=coolers, idealPrice=budget * 0.03, maybeDontNeedDetail=True)
    if budget >= 1300:
        coolers = cooler_logic(budget, coolers_fromDB[1:], cpu)
        cooler = create_conf(details=coolers, idealPrice=budget * 0.03, maybeDontNeedDetail=True)

    # Motherboard
    # если проц со встроенное графикой или кулером (или, и то, и другое) и если конфигурация ДЕШЕВАЯ,
    # то половину из части бюджета, которую мы бы потратили на GPU или кулер мы тратим на CPU
    # и другую половину тратим на MB
    motherboards = motherboard_logic(budget, motherboards_fromDB[1:], cpu)
    if budget < 1400:
        motherboard = create_conf(details=motherboards, idealPrice=budget * (0.12 + 0.26))
    else:
        motherboard = create_conf(details=motherboards, idealPrice=budget * 0.12)


    # RAM
    rams = ram_logic(budget, motherboard, suitable_req_min, rams_fromDB[1:])
    if budget < 1400:
        ram = create_conf(details=rams, idealPrice=budget * (0.12))
    else:
        ram = create_conf(details=rams, idealPrice=budget * 0.12)

    # GPU
    direction = ""
    # если комп НЕ слишком дешевый и процессор БЕЗ встроенной графики. И если дешевый комп, то должен выбраться процессор со встроенной графикой, тогда если у нас НЕ такой проц, то выбираем видеокарту
    specified_gpu = get_specified_gpu(gpus_fromDB[1:], suitable_req_min, suitable_req_rec)  # Сначала ищем требуемую видеокарту из списка актуальных комплектующих
    if specified_gpu == None:
        legacyGpu = get_specified_gpu(legacyDevices[1], suitable_req_min, suitable_req_rec)
        if legacyGpu != None:
            specified_gpu = get_same_gpu(legacyGpu, gpus_fromDB[1:])  # Если не нашли, то ищем аналогичную видеокарту, чтобы по характеристикам была примерно похожа на искомую
    if specified_gpu == None:
        gpus = gpu_logic(budget, gpus_fromDB[1:], cpu, direction)
        if len(gpus) > 0:
            if cpu.cooling_included == "Yes" and cooler is None: # если проц со встроенным кулером и отдельный кулер решили не брать
                gpu = create_conf(details=gpus, idealPrice=budget * (0.26 + 0.03), maybeDontNeedDetail=True) # то часть бюджета для кулера тратим на видеокарту
            else:
                gpu = create_conf(details=gpus, idealPrice=budget * 0.26, maybeDontNeedDetail=True)
    else:
        if budget >= 1400:
            if specified_gpu.price <= budget * 0.20:
                gpu = specified_gpu

    # SSD/HDD
    ssds = ssd_logic(budget, ssds_fromDB[1:], motherboard, itSeconfSSD=False)
    hdds = hdd_logic(budget, hdds_fromDB[1:])
    if budget >= 1400:
        ssd = create_conf(details=ssds, idealPrice=budget * 0.07)
        hdd = create_conf(details=hdds, idealPrice=budget * 0.06, maybeDontNeedDetail=True)
    else: # если комп дешевый, то можно и только SSD
        ssd = create_conf(details=ssds, idealPrice=budget * (0.06 + 0.07))

    # power
    powers = power_logic(budget, powers_fromDB[1:], gpu)
    if budget >= 1000: # если комп не совсем дешевый, то надо взять отдельный блок питания (а не встроенный в корпус)
        power = create_conf(details=powers, idealPrice=budget * 0.07, maybeDontNeedDetail=True)


    # case
    cases = case_logic(budget, cases_fromDB[1:], motherboard, gpu, power)
    if budget >= 1400 and power is not None:  # если комп не совсем дешевый, то выбираем отдельный блок питания
        casePC = create_conf(details=cases, idealPrice=budget * 0.07)
    else:
        casePC = create_conf(details=cases, idealPrice=budget * (0.07 + 0.07)) # иначе выбираем корпус со встроенным БП (часть бюджета для БП отдаем на корпус)




    configurations.append(Configuration(cpu=cpu, cooler=cooler, motherboard=motherboard, ram=ram, gpu=gpu,
                  ssd=ssd, hdd=hdd, power=power, casePC=casePC))

    cooler_idx = 0 if cooler is None else configurations[0].cooler.id + 1
    gpu_idx = 0 if gpu is None else configurations[0].gpu.id + 1
    hdd_idx = 0 if hdd is None else configurations[0].hdd.id + 1
    power_idx = 0 if power is None else configurations[0].power.id + 1
    cooler_price = None if cooler is None else configurations[0].cooler.price
    gpu_price = None if gpu is None else configurations[0].gpu.price
    hdd_price = None if hdd is None else configurations[0].hdd.price
    power_price = None if power is None else configurations[0].power.price
    cooler_name = "None" if cooler is None else configurations[0].cooler.name
    gpu_name = "None" if gpu is None else configurations[0].gpu.name
    hdd_name = "None" if hdd is None else configurations[0].hdd.name
    power_name = "None" if power is None else configurations[0].power.name

    print(configurations[0].cpu.name+f" {configurations[0].cpu.price}")
    if (cooler_price is not None):
        print(cooler_name+f" {cooler_price}")
    print(configurations[0].motherboard.name+f" {configurations[0].motherboard.price}")
    print(configurations[0].ram.name+f" {configurations[0].ram.price}")
    if (gpu_price is not None):
        print(gpu_name+f" {gpu_price}")
    print(configurations[0].ssd.name+f" {configurations[0].ssd.price}")
    if (hdd_price is not None):
        print(hdd_name+f" {hdd_price}")
    if (power_price is not None):
        print(power_name+f" {power_price}")
    print(configurations[0].casePC.name+f" {configurations[0].casePC.price}")
    indeces = [configurations[0].cpu.id+1, cooler_idx, configurations[0].motherboard.id+1, configurations[0].ram.id+1,
    gpu_idx, configurations[0].ssd.id+1, hdd_idx, power_idx, configurations[0].casePC.id+1]
    prices = [configurations[0].cpu.price, cooler_price, configurations[0].motherboard.price, configurations[0].ram.price,
    gpu_price, configurations[0].ssd.price, hdd_price, power_price, configurations[0].casePC.price]
    total_price = 0
    for price in prices:
        if price != None:
            total_price += price
    print(f"total_price = {total_price}")


if __name__ == '__main__':
    data_fromDB, legacyDevices, none_details, min_reqs, rec_reqs = prepare_data()
    app.run()