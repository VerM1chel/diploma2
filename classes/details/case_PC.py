# from detail import Detail

class Case:
    name = ""
    price = 0.0
    market_launch_date = 0
    power = ""
    case_description = ""
    case_type = ""
    case_for_games = False
    case_color = ""
    case_material = ""
    transparent_window = False
    window_material = ""
    case_front_panel = ""
    max_board_size = ""
    portable_power_supplies = ""
    power_supply_location = ""
    liquid_cooling_support = False
    supported_lss = ""
    fans_included = False
    num_places_for_fans = 0
    installed_fans = 0
    fan_configuration = ""
    fan_light_color = ""
    noise_isolation = False
    bays_5dot25inch = ""
    external_3dot5_inch_bays = ""
    internal_3dot5_inch_bays = ""
    inch_bays_2dot5 = ""
    inch_combo_bay_2dot5_or_3dot5 = ""
    removable_drive_cage = False
    screwless_disc_mounting = False
    horizontal_expansion_slots = ""
    dust_filters = False
    case_illumination = False
    backlight_controller = False
    fan_rotation_controller = False
    video_card_holder = False
    max_graphics_card_length = 0
    max_cpu_cooler_height = 0
    max_power_supply_length = 0
    vesa_mount = False
    door = False
    case_lock = False
    information_display = False
    usb_2dot0 = ""
    usb_3dot2_gen1_Type_a_or_5Gb_s = ""
    usb_3dot2_gen2_Type_a_or_10Gb_s = ""
    usb_3dot2_gen1_Type_c_or_5Gb_s = ""
    usb_3dot2_gen2_Type_c_or_10Gb_s = ""
    usb_3dot2_gen_2x2_or_20Gb_s = ""
    firewire = ""
    esata = ""
    docking_station_for_hard_drives = ""
    card_reader = ""
    audio_output = ""
    microphone_input = ""
    height = 0.0
    width = 0.0
    depth = 0.0
    weight = 0.0


    def __init__(self, keys, values, descriptions, reading=False):
        if reading == False:
            self.name = values[keys.index("Название")]
            self.price = float(values[keys.index("Цена")].split()[0].replace(',', '.'))
            if "Дата выхода на рынок" in keys:
                self.market_launch_date = int(values[keys.index("Дата выхода на рынок")].split()[0])
            else:
                self.market_launch_date = None
            if "Блок питания" in keys:
                self.power = values[keys.index("Блок питания")]
            else:
                self.power = None
            if "Описание" in keys:
                self.case_description = values[keys.index("Описание")]
            else:
                self.case_description = None
            if "Тип корпуса" in keys:
                self.case_type = values[keys.index("Тип корпуса")]
            else:
                self.case_type = None
            if "Игровой" in keys:
                self.case_for_games = True if values[keys.index("Игровой")] == "Yes" else False
            else:
                self.case_for_games = None
            if "Цвет корпуса" in keys:
                self.case_color = values[keys.index("Цвет корпуса")]
            else:
                self.case_color = None
            if "Материал корпуса" in keys:
                self.case_material = values[keys.index("Материал корпуса")]
            else:
                self.case_material = None
            if "Прозрачное окно" in keys:
                self.transparent_window = True if values[keys.index("Прозрачное окно")] == "Yes" else False
            else:
                self.transparent_window = None
            if "Материал окна" in keys:
                self.window_material = values[keys.index("Материал окна")]
            else:
                self.window_material = None
            if "Передняя панель корпуса" in keys:
                self.case_front_panel = values[keys.index("Передняя панель корпуса")]
            else:
                self.case_front_panel = None
            if "Макс. размер материнской платы" in keys:
                self.max_board_size = values[keys.index("Макс. размер материнской платы")]
            else:
                self.max_board_size = None
            if "Совместимые материнские платы" in keys:
                self.portable_power_supplies = values[keys.index("Совместимые материнские платы")]
            else:
                self.portable_power_supplies = None
            if "Расположение блока питания" in keys:
                self.power_supply_location = values[keys.index("Расположение блока питания")]
            else:
                self.power_supply_location = None
            if "Поддержка жидкостного охлаждения" in keys:
                self.liquid_cooling_support = True if values[keys.index("Поддержка жидкостного охлаждения")] == "Yes" else False
            else:
                self.liquid_cooling_support = None
            if "Поддерживаемые СЖО" in keys:
                self.supported_lss = values[keys.index("Поддерживаемые СЖО")]
            else:
                self.supported_lss = None
            if "Вентиляторы в комплекте" in keys:
                self.fans_included = True if values[keys.index("Вентиляторы в комплекте")] == "Yes" else False
            else:
                self.fans_included = None
            if "Количество мест для вентиляторов" in keys:
                self.num_places_for_fans = int(values[keys.index("Количество мест для вентиляторов")].split()[0])
            else:
                self.num_places_for_fans = None
            if "Установленные вентиляторы" in keys:
                self.installed_fans = int(values[keys.index("Установленные вентиляторы")].split()[0])
            else:
                self.installed_fans = None
            if "Конфигурация вентиляторов" in keys:
                self.fan_configuration = values[keys.index("Конфигурация вентиляторов")]
            else:
                self.fan_configuration = None
            if "Цвет подсветки вентилятора" in keys:
                self.fan_light_color = values[keys.index("Цвет подсветки вентилятора")]
            else:
                self.fan_light_color = None
            if "Шумоизоляция" in keys:
                self.noise_isolation = True if values[keys.index("Шумоизоляция")] == "Yes" else False
            else:
                self.noise_isolation = None
            if "Отсеки 5.25 дюймов" in keys:
                self.bays_5dot25inch = values[keys.index("Отсеки 5.25 дюймов")]
            else:
                self.bays_5dot25inch = None
            if "Внешние отсеки 3.5 дюймов" in keys:
                self.external_3dot5_inch_bays = values[keys.index("Внешние отсеки 3.5 дюймов")]
            else:
                self.external_3dot5_inch_bays = None
            if "Внутренние отсеки 3.5 дюймов" in keys:
                self.internal_3dot5_inch_bays = values[keys.index("Внутренние отсеки 3.5 дюймов")]
            else:
                self.internal_3dot5_inch_bays = None
            if "Отсеки 2.5 дюймов" in keys:
                self.inch_bays_2dot5 = values[keys.index("Отсеки 2.5 дюймов")]
            else:
                self.inch_bays_2dot5 = None
            if "Комбинированный отсек для 2.5/3.5 дюймов" in keys:
                self.inch_combo_bay_2dot5_or_3dot5 = values[keys.index("Комбинированный отсек для 2.5/3.5 дюймов")]
            else:
                self.inch_combo_bay_2dot5_or_3dot5 = None
            if "Съёмная корзина для накопителей" in keys:
                self.removable_drive_cage = True if values[keys.index("Съёмная корзина для накопителей")] == "Yes" else False
            else:
                self.removable_drive_cage = None
            if "Безвинтовое крепление дисков" in keys:
                self.screwless_disc_mounting = True if values[keys.index("Безвинтовое крепление дисков")] == "Yes" else False
            else:
                self.screwless_disc_mounting = None
            if "Горизонтальные слоты расширения" in keys:
                self.horizontal_expansion_slots = values[keys.index("Горизонтальные слоты расширения")]
            else:
                self.horizontal_expansion_slots = None
            if "Пылевые фильтры" in keys:
                self.dust_filters = True if values[keys.index("Пылевые фильтры")] == "Yes" else False
            else:
                self.dust_filters = None
            if "Подсветка корпуса" in keys:
                self.case_illumination = True if values[keys.index("Подсветка корпуса")] == "Yes" else False
            else:
                self.case_illumination = None
            if "Контроллер подсветки" in keys:
                self.backlight_controller = True if values[keys.index("Контроллер подсветки")] == "Yes" else False
            else:
                self.backlight_controller = None
            if "Контроллер вращения вентиляторов" in keys:
                self.fan_rotation_controller = True if values[keys.index("Контроллер вращения вентиляторов")] == "Yes" else False
            else:
                self.fan_rotation_controller = None
            if "Держатель видеокарты" in keys:
                self.video_card_holder = True if values[keys.index("Держатель видеокарты")] == "Yes" else False
            else:
                self.video_card_holder = None
            if "Макс. длина видеокарты" in keys:
                self.max_graphics_card_length = int(values[keys.index("Макс. длина видеокарты")].split()[0])
            else:
                self.max_graphics_card_length = None
            if "Макс. высота процессорного кулера" in keys:
                self.max_cpu_cooler_height = int(values[keys.index("Макс. высота процессорного кулера")].split()[0])
            else:
                self.max_cpu_cooler_height = None
            if "Макс. длина блока питания" in keys:
                self.max_power_supply_length = int(values[keys.index("Макс. длина блока питания")].split()[0])
            else:
                self.max_power_supply_length = None
            if "Крепление VESA" in keys:
                self.vesa_mount = True if values[keys.index("Крепление VESA")] == "Yes" else False
            else:
                self.vesa_mount = None
            if "Дверца" in keys:
                self.door = True if values[keys.index("Дверца")] == "Yes" else False
            else:
                self.door = None
            if "Замок" in keys:
                self.case_lock = True if values[keys.index("Замок")] == "Yes" else False
            else:
                self.case_lock = None
            if "Информационный дисплей" in keys:
                self.information_display = True if values[keys.index("Информационный дисплей")] == "Yes" else False
            else:
                self.information_display = None
            if "USB 2.0" in keys:
                self.usb_2dot0 = values[keys.index("USB 2.0")]
            else:
                self.usb_2dot0 = None
            if "USB 3.2 Gen1 Type-A (5 Гбит/с)" in keys:
                self.usb_3dot2_gen1_Type_a_or_5Gb_s = values[keys.index("USB 3.2 Gen1 Type-A (5 Гбит/с)")]
            else:
                self.usb_3dot2_gen1_Type_a_or_5Gb_s = None
            if "USB 3.2 Gen2 Type-A (10 Гбит/с)" in keys:
                self.usb_3dot2_gen2_Type_a_or_10Gb_s = values[keys.index("USB 3.2 Gen2 Type-A (10 Гбит/с)")]
            else:
                self.usb_3dot2_gen2_Type_a_or_10Gb_s = None
            if "USB 3.2 Gen1 Type-C (5 Гбит/с)" in keys:
                self.usb_3dot2_gen1_Type_c_or_5Gb_s = values[keys.index("USB 3.2 Gen1 Type-C (5 Гбит/с)")]
            else:
                self.usb_3dot2_gen1_Type_c_or_5Gb_s = None
            if "USB 3.2 Gen2 Type-C (10 Гбит/с)" in keys:
                self.usb_3dot2_gen2_Type_c_or_10Gb_s = values[keys.index("USB 3.2 Gen2 Type-C (10 Гбит/с)")]
            else:
                self.usb_3dot2_gen2_Type_c_or_10Gb_s = None
            if "USB 3.2 Gen 2x2 (20 Гбит/с)" in keys:
                self.usb_3dot2_gen_2x2_or_20Gb_s = values[keys.index("USB 3.2 Gen 2x2 (20 Гбит/с)")]
            else:
                self.usb_3dot2_gen_2x2_or_20Gb_s = None
            if "FireWire (IEEE 1394, iLink)" in keys:
                self.firewire = values[keys.index("FireWire (IEEE 1394, iLink)")]
            else:
                self.firewire = None
            if "eSATA" in keys:
                self.esata = values[keys.index("eSATA")]
            else:
                self.esata = None
            if "Док-станция для винчестеров" in keys:
                self.docking_station_for_hard_drives = values[keys.index("Док-станция для винчестеров")]
            else:
                self.docking_station_for_hard_drives = None
            if "Кардридер" in keys:
                self.card_reader = values[keys.index("Кардридер")]
            else:
                self.card_reader = None
            if "Аудиовыход" in keys:
                self.audio_output = values[keys.index("Аудиовыход")]
            else:
                self.audio_output = None
            if "Вход для микрофона" in keys:
                self.microphone_input = values[keys.index("Вход для микрофона")]
            else:
                self.microphone_input = None
            if "Высота" in keys:
                self.height = float(values[keys.index("Высота")].split()[0])
            else:
                self.height = None
            if "Ширина" in keys:
                self.width = float(values[keys.index("Ширина")].split()[0])
            else:
                self.width = None
            if "Глубина" in keys:
                self.depth = float(values[keys.index("Глубина")].split()[0])
            else:
                self.depth = None
            if "Вес" in keys:
                self.weight = float(values[keys.index("Вес")].split()[0])
            else:
                self.weight = None
        elif reading == True:
            self.name = values[keys.index("Название")]
            self.price = values[keys.index("Цена")]
            self.market_launch_date = values[keys.index("Дата выхода на рынок")]
            self.power = values[keys.index("Блок питания")]
            self.case_description = values[keys.index("Описание")]
            self.case_type = values[keys.index("Тип корпуса")]
            self.case_for_games = values[keys.index("Игровой")]
            self.case_color = values[keys.index("Цвет корпуса")]
            self.case_material = values[keys.index("Материал корпуса")]
            self.transparent_window = values[keys.index("Прозрачное окно")]
            self.window_material = values[keys.index("Материал окна")]
            self.case_front_panel = values[keys.index("Передняя панель корпуса")]
            self.max_board_size = values[keys.index("Макс. размер материнской платы")]
            self.portable_power_supplies = values[keys.index("Совместимые материнские платы")]
            self.power_supply_location = values[keys.index("Расположение блока питания")]
            self.liquid_cooling_support = values[keys.index("Поддержка жидкостного охлаждения")]
            self.supported_lss = values[keys.index("Поддерживаемые СЖО")]
            self.fans_included = values[keys.index("Вентиляторы в комплекте")]
            self.num_places_for_fans = values[keys.index("Количество мест для вентиляторов")]
            self.installed_fans = values[keys.index("Установленные вентиляторы")]
            self.fan_configuration = values[keys.index("Конфигурация вентиляторов")]
            self.fan_light_color = values[keys.index("Цвет подсветки вентилятора")]
            self.noise_isolation = values[keys.index("Шумоизоляция")]
            self.bays_5dot25inch = values[keys.index("Отсеки 5.25 дюймов")]
            self.external_3dot5_inch_bays = values[keys.index("Внешние отсеки 3.5 дюймов")]
            self.internal_3dot5_inch_bays = values[keys.index("Внутренние отсеки 3.5 дюймов")]
            self.inch_bays_2dot5 = values[keys.index("Отсеки 2.5 дюймов")]
            self.inch_combo_bay_2dot5_or_3dot5 = values[keys.index("Комбинированный отсек для 2.5/3.5 дюймов")]
            self.removable_drive_cage = values[keys.index("Съёмная корзина для накопителей")]
            self.screwless_disc_mounting = values[keys.index("Безвинтовое крепление дисков")]
            self.horizontal_expansion_slots = values[keys.index("Горизонтальные слоты расширения")]
            self.dust_filters = values[keys.index("Пылевые фильтры")]
            self.case_illumination = values[keys.index("Подсветка корпуса")]
            self.backlight_controller = values[keys.index("Контроллер подсветки")]
            self.fan_rotation_controller = values[keys.index("Контроллер вращения вентиляторов")]
            self.video_card_holder = values[keys.index("Держатель видеокарты")]
            self.max_graphics_card_length = values[keys.index("Макс. длина видеокарты")]
            self.max_cpu_cooler_height = values[keys.index("Макс. высота процессорного кулера")]
            self.max_power_supply_length = values[keys.index("Макс. длина блока питания")]
            self.vesa_mount = values[keys.index("Крепление VESA")]
            self.door = values[keys.index("Дверца")]
            self.case_lock = values[keys.index("Замок")]
            self.information_display = values[keys.index("Информационный дисплей")]
            self.usb_2dot0 = values[keys.index("USB 2.0")]
            self.usb_3dot2_gen1_Type_a_or_5Gb_s = values[keys.index("USB 3.2 Gen1 Type-A (5 Гбит/с)")]
            self.usb_3dot2_gen2_Type_a_or_10Gb_s = values[keys.index("USB 3.2 Gen2 Type-A (10 Гбит/с)")]
            self.usb_3dot2_gen1_Type_c_or_5Gb_s = values[keys.index("USB 3.2 Gen1 Type-C (5 Гбит/с)")]
            self.usb_3dot2_gen2_Type_c_or_10Gb_s = values[keys.index("USB 3.2 Gen2 Type-C (10 Гбит/с)")]
            self.usb_3dot2_gen_2x2_or_20Gb_s = values[keys.index("USB 3.2 Gen 2x2 (20 Гбит/с)")]
            self.firewire = values[keys.index("FireWire (IEEE 1394, iLink)")]
            self.esata = values[keys.index("eSATA")]
            self.docking_station_for_hard_drives = values[keys.index("Док-станция для винчестеров")]
            self.card_reader = values[keys.index("Кардридер")]
            self.audio_output = values[keys.index("Аудиовыход")]
            self.microphone_input = values[keys.index("Вход для микрофона")]
            self.height = values[keys.index("Высота")]
            self.width = values[keys.index("Ширина")]
            self.depth = values[keys.index("Глубина")]
            self.weight = values[keys.index("Вес")]