from classes.configuration import Configuration

from flask import Flask, jsonify, request

import constants
from sql_code import config
from sql_code import queries
from classes.details.cpu import Cpu
from classes.details.cooler import Cooler
from classes.details.motherboard import Motherboard
from classes.details.ram import Ram
from classes.details.gpu import Gpu
from classes.details.ssd import Ssd
from classes.details.hdd import Hdd
from classes.details.case_PC import Case
from classes.details.power import Power

import inspect

import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
all_lists = []
indeces = []
prices = []

@app.route('/indeces')
def get_details():
    return jsonify(indeces)
@app.route('/prices')
def get_prices():
    return jsonify(prices)
@app.route('/cpus')
def get_cpus():
    details_list = []
    for detail in all_lists[0]:
        detail_dict = {key: value for key, value in vars(detail).items()}
        details_list.append(detail_dict)
    return jsonify(details_list)
@app.route('/coolers')
def get_coolers():
    details_list = []
    for detail in all_lists[1]:
        detail_dict = {key: value for key, value in vars(detail).items()}
        details_list.append(detail_dict)
    return jsonify(details_list)
@app.route('/motherboards')
def get_motherboards():
    details_list = []
    for detail in all_lists[2]:
        detail_dict = {key: value for key, value in vars(detail).items()}
        details_list.append(detail_dict)
    return jsonify(details_list)
@app.route('/rams')
def get_rams():
    details_list = []
    for detail in all_lists[3]:
        detail_dict = {key: value for key, value in vars(detail).items()}
        details_list.append(detail_dict)
    return jsonify(details_list)
@app.route('/gpus')
def get_gpus():
    details_list = []
    for detail in all_lists[4]:
        detail_dict = {key: value for key, value in vars(detail).items()}
        details_list.append(detail_dict)
    return jsonify(details_list)
@app.route('/ssds')
def get_ssds():
    details_list = []
    for detail in all_lists[5]:
        detail_dict = {key: value for key, value in vars(detail).items()}
        details_list.append(detail_dict)
    return jsonify(details_list)
@app.route('/hdds')
def get_hdds():
    details_list = []
    for detail in all_lists[6]:
        detail_dict = {key: value for key, value in vars(detail).items()}
        details_list.append(detail_dict)
    return jsonify(details_list)
@app.route('/powers')
def get_powers():
    details_list = []
    for detail in all_lists[7]:
        detail_dict = {key: value for key, value in vars(detail).items()}
        details_list.append(detail_dict)
    return jsonify(details_list)
@app.route('/casePCs')
def get_casePCs():
    details_list = []
    for detail in all_lists[8]:
        detail_dict = {key: value for key, value in vars(detail).items()}
        details_list.append(detail_dict)
    return jsonify(details_list)

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
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
    cursor.execute(f"SELECT * FROM USERS WHERE username = '{username}' and password = '{password}'")
    result = cursor.fetchall()
    print(result)
    print(username)
    print(password)
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
            host="localhost",
            user="root",
            passwd="password",
            database="diploma"
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
    if budget < 1400 and cpu.cooling_included == "Yes": # для дешевых конфигураций, чтобы сэкономить, можно купить процессор со встроенным кулером (то есть тут кулер не нужен)
        return []
    else:
        for cooler in coolers:
            if cooler.cooling != "водяное": # Если кулер все-таки нужен, то лучше исключить водяное охлаждение (оно подходит только под несколько типов корпусов) и то, только сборщики знают, как правильно оно собирается (там все эмпирическим путем узнается)
                if cooler.power_dissipation != None:
                    if 20 < (cooler.power_dissipation - cpu.estimated_thermal_power) < 55:  # Кулер должен рассеивать достаточно тепла, чтобы процессор не перегревался, но излишне слишком мощные кулеры нам тоже не нужны
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
def ram_logic(budget, motherboard, rams):
    result = []
    for ram in rams:
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
            if case.max_graphics_card_length != None and case.max_graphics_card_length >= gpu.video_card_length: # Также, надо, чтобы видеокарта помещалась в корпус. Если меньше даже на миллиметр -- то все равно не влезет
                if budget <= 1000 and case.power != "отсутствует" and case.power != None:  # если комп дешевый, то выбираем только корпуса со встроенным блоком питания (существенная экономия)
                    if (gpu.recommended_psu_watts < 600 and int(case.power.split()[0]) >= 600) or (gpu.recommended_psu_watts > 600 and int(case.power.split()[0]) >= gpu.recommended_psu_watts):
                        result.append(case)
                if case.power == "отсутствует" or case.power == None:
                    if power.width != None: # Если комп не слишком дешевый, то лучше все же поставить блок питания. А так как блок питания не встроенный, то он должен помещаться в корпус
                        if case.max_power_supply_length != None and case.max_power_supply_length >= power.width:
                            result.append(case)
    return result


def create_conf(details, idealPrice):
    filtered_details = []
    for d in details:
        if abs(idealPrice - d.price) <= 50:
            filtered_details.append(d)
    sorted_details = sorted(filtered_details, key=lambda d: abs(idealPrice - d.price)) # Получаем список, у которого первые элементы -- это экземпляры класса с наиболее близким совпадением к желаемой цене
    if len(sorted_details) < 1:
        print("При заданном бюждете невозможно составить конфигурацию, либо отсутствуют необходимые комплектующие из соответствующего ценового диапазона")
        exit(3)
    return sorted_details[0]

    # return sorted_details[:5] # Возвращаем топ 5 совпадений


def read_from_db(connection, table_name, my_class, keys):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    my_class_list = []
    none_item = my_class(keys, [0] + ["None"] + [0] + [None] * (len(keys) - 2), [], reading=True) # Пустая запись, пока ничего не выбрано
    for row in cursor:
        values = list(row)
        # values = [str(v) for v in values]
        my_class_list.append(my_class(keys, values, [], reading=True))
    return my_class_list, none_item

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
import json

def main():
    global all_lists
    global indeces
    global prices
    configurations = []
    # 2. Read all trebovaniya from database (read all devices)

# This part we do just once in the beginning
    # 1. Connection to database
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="password",
            database="diploma"
        )
        print('Succesfull connected')
    except mysql.connector.Error as error:
        print(f'An error {error} occured')

    create_tables(connection)

    # 3. Read all devices from database
    cpus_fromDB, none_cpu = read_from_db(connection, "cpus", Cpu, constants.cpu_keys)
    coolers_fromDB, none_cooler = read_from_db(connection, "coolers", Cooler, constants.cooler_keys)
    motherboards_fromDB, none_motherboard = read_from_db(connection, "motherboards", Motherboard, constants.motherboard_keys)
    rams_fromDB, none_ram = read_from_db(connection, "rams", Ram, constants.ram_keys)
    gpus_fromDB, none_gpu = read_from_db(connection, "gpus", Gpu, constants.gpu_keys)
    ssds_fromDB, none_ssd = read_from_db(connection, "ssds", Ssd, constants.ssd_keys)
    hdds_fromDB, none_hdd = read_from_db(connection, "hdds", Hdd, constants.hhd_keys)
    powers_fromDB, none_power = read_from_db(connection, "powers", Power, constants.power_keys)
    cases_fromDB, none_case = read_from_db(connection, "cases", Case, constants.case_keys)

    # get_details(cpus_fromDB)


    none_lists = [none_cpu, none_cooler, none_motherboard, none_ram, none_gpu, none_ssd, none_hdd, none_power, none_case]
    all_lists = [cpus_fromDB, coolers_fromDB, motherboards_fromDB, rams_fromDB, gpus_fromDB, ssds_fromDB, hdds_fromDB, powers_fromDB, cases_fromDB]
    for i,none_list in enumerate(none_lists):
        all_lists[i].insert(0, none_lists[i])

# # Then we need to get only devices, that pass to customer requirements
#     budget = 1100
#     # while budget.isdigit() == False or budget < 0: # *
#     #     budget = float(input()) # *
#
#     # CPU
#     cpus = cpu_logic(budget, cpus_fromDB)
#     cpu = None
#     if budget > 1400:
#         cpu = create_conf(details=cpus, idealPrice=budget*0.20)
#     elif budget < 1200: # если конфигурация слишком дешевая
#         cpu = create_conf(details=cpus, idealPrice=budget * (0.20 + 0.34 * 0.6 + 0.03 - 0.013))  # если процессор и со встроенной графикой, и со встроенным кулером
#     elif budget < 1400:  # если конфигурация дешевая
#         cpu = create_conf(details=cpus, idealPrice=budget*(0.20+0.34*0.60-0.013)) # если процессор со встроенной графикой
#     if cpu is None: # Если ничего не подошло по цене
#         print("При заданном бюджете невозможно составить выбранную конфигурацию CPU")
#         exit(2)
#
#     # Cooler
#     coolers = cooler_logic(budget, coolers_fromDB, cpu)
#     cooler = create_conf(details=coolers, idealPrice=budget * 0.03)
#     if cooler is None:
#         cooler = coolers_fromDB[0]
#
#     # Motherboard
#     # если проц со встроенное графикой или кулером (или, и то, и другое) и если конфигурация ДЕШЕВАЯ,
#     # то половину из части бюджета, которую мы бы потратили на GPU или кулер мы тратим на CPU
#     # и другую половину тратим на MB
#     motherboards = motherboard_logic(budget, motherboards_fromDB, cpu)
#     if budget < 1400:
#         motherboard = create_conf(details=motherboards, idealPrice=budget * (0.12 + 0.33 * 0.4))
#     else:
#         motherboard = create_conf(details=motherboards, idealPrice=budget * 0.12)
#     if motherboard is None: # Если ничего не подошло по цене
#         print("При заданном бюджете невозможно составить выбранную конфигурацию motherboard")
#         exit(2)
#
#     # RAM
#     rams = ram_logic(budget, motherboard, rams_fromDB)
#     if budget < 1400:
#         ram = create_conf(details=rams, idealPrice=budget * (0.12 * 1.5))
#     else:
#         ram = create_conf(details=rams, idealPrice=budget * 0.12)
#     if ram is None: # Если ничего не подошло по цене
#         print("При заданном бюджете невозможно составить выбранную конфигурацию RAM")
#         exit(2)
#
#
#     direction = ""
#     # GPU
#     # если комп НЕ слишком дешевый и процессор БЕЗ встроенной графики. И если дешевый комп, то должен выбраться процессор со встроенной графикой, тогда если у нас НЕ такой проц, то выбираем видеокарту
#     gpus = gpu_logic(budget, gpus_fromDB, cpu, direction)
#     if gpus is not None:
#         if cpu.cooling_included == "Yes" and cooler is None: # если проц со встроенным кулером
#             gpu = create_conf(details=gpus, idealPrice=budget * (0.33 + 0.03))     # то часть бюджета для кулера тратим на видеокарту
#         else:
#             gpu = create_conf(details=gpus, idealPrice=budget * 0.33)
#     else:
#         gpu = gpus_fromDB[0]
#     if gpu is None: # Если ничего не подошло по цене
#         print("При заданном бюджете невозможно составить выбранную конфигурацию GPU")
#         exit(2)
#
#     # SSD/HDD
#     ssds = ssd_logic(budget, ssds_fromDB, motherboard, itSeconfSSD=False)
#     hdds = hdd_logic(budget, hdds_fromDB)
#     if budget >= 400:
#         ssd = create_conf(details=ssds, idealPrice=budget * 0.07)
#         hdd = create_conf(details=hdds, idealPrice=budget * 0.06)
#     else: # если комп дешевый, то можно и только SSD
#         create_conf(details=ssds, idealPrice=budget * (0.06 + 0.07) * 1.1)
#     if ssd is None: # Если ничего не подошло по цене
#         print("При заданном бюджете невозможно составить выбранную конфигурацию SSD")
#         exit(2)
#
#     # power
#     powers = power_logic(budget, powers_fromDB, gpu)
#     if budget > 1400: # если комп не совсем дешевый, то выбираем корпус без блока питания в комплекте
#         power = create_conf(details=powers, idealPrice=budget * 0.07)
#         if power is None:  # Если ничего не подошло по цене
#             print("При заданном бюджете невозможно составить выбранную конфигурацию Power")
#             exit(2)
#     else:
#         power = create_conf(details=powers, idealPrice=budget * (0.07 + 0.07)) # иначе с БП (часть бюджета для БП отдаем на корпус)
#
#     # case
#     cases = case_logic(budget, cases_fromDB, motherboard, gpu, power)
#     casePC = create_conf(details=cases, idealPrice= budget * 0.07)
#     if casePC is None:  # Если ничего не подошло по цене
#         print("При заданном бюджете невозможно составить выбранную конфигурацию Case")
#         exit(2)
#
#     configurations.append(Configuration(cpu=cpu, cooler=cooler, motherboard=motherboard, ram=ram, gpu=gpu,
#                   ssd=ssd, hdd=hdd, power=power, casePC=casePC))
#     print(configurations[0].cpu.name+f" {configurations[0].cpu.price}")
#     print(configurations[0].cooler.name+f" {configurations[0].cooler.price}")
#     print(configurations[0].motherboard.name+f" {configurations[0].motherboard.price}")
#     print(configurations[0].ram.name+f" {configurations[0].ram.price}")
#     print(configurations[0].gpu.name+f" {configurations[0].gpu.price}")
#     print(configurations[0].ssd.name+f" {configurations[0].ssd.price}")
#     print(configurations[0].hdd.name+f" {configurations[0].hdd.price}")
#     print(configurations[0].power.name+f" {configurations[0].power.price}")
#     print(configurations[0].casePC.name+f" {configurations[0].casePC.price}")
#
#     indeces = [configurations[0].cpu.id+1, configurations[0].cooler.id+1, configurations[0].motherboard.id+1, configurations[0].ram.id+1,
#     configurations[0].gpu.id+1, configurations[0].ssd.id+1, configurations[0].hdd.id+1, configurations[0].power.id, configurations[0].casePC.id+1]
#     prices = [configurations[0].cpu.price, configurations[0].cooler.price, configurations[0].motherboard.price, configurations[0].ram.price,
#     configurations[0].gpu.price, configurations[0].ssd.price, configurations[0].hdd.price, configurations[0].power.price, configurations[0].casePC.price]
#     print(5)
#
#     none_lists = [none_cpu, none_cooler, none_motherboard, none_ram, none_gpu, none_ssd, none_hdd, none_power, none_case]
#     all_lists = [cpus_fromDB, coolers_fromDB, motherboards_fromDB, rams_fromDB, gpus_fromDB, ssds_fromDB, hdds_fromDB, powers_fromDB, cases_fromDB]
#     for i,none_list in enumerate(none_lists):
#         all_lists[i].insert(0, none_lists[i])

# корпус всегда брать без блока питания (если комп <= 1000, то комп без дискретного блока питания, только со встроенным)
# Чем дороже комп, тем больше разница между комплектующими (видюха, проц, материнка) по сравнению с другими

"""
	raznica = orientZena - v[i].getCost();
			if (cost <= orientZena && raznica < predRaznica) {
				//для кулера типа "Universal" данный тип может и не быть указанным в названии, но когда мы считывали кулеры,
				//то мы считывали только кулеры этого типа,
				//т.е. если кулер прошел все проверки, то мы его спокойно пропускаем
				//если тип детали совпадает с желаемым и цена текущего экземпляра меньше и максимально близко к ориентеровочной, то запоминаем его

				Det = v[i];//запоминаем этот экземпляр в отдельную переменную
				if (raznica == 0) //если мы нашли полное совпадение по желаемой цене
					return comment;//то дальше нет смысла искать
				predRaznica = raznica; //запоминаем прошлую разницу, чтобы допускать только те детали, цена которых более близкая к требуемой
"""

"""
		double colichestvo = atoi(quantity.c_str());
		totalWithoutNacenka = CPU1.getCost() + Cooler1.getCost() + MB1.getCost() + colichestvo * DDR1.getCost()//складываем цены всех комплектующих конфигурации
			+ GPU1.getCost() + HDD1.getCost() + SSD1.getCost() + Case1.getCost() + PSU1.getCost();
		total = totalWithoutNacenka + nacenka;
"""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
    app.run()

#
# setCpus(response.data[0].name); // Выбираем первый элемент списка по умолчанию
# setCoolers(response.data[1].name);
# setMotherboards(response.data[2].name);