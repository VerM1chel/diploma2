# from detail import Detail

class Power:
    name = ""
    price = 0.0
    market_launch_date = 0
    power_description = ""
    purpose = ""
    power = 0
    power_supply_standard = ""
    input_voltage_range = ""
    number_of_individual_12v_lines = 0
    max_line_current_12v = 0.0
    combined_12v_load = 0.0
    power_factor_correction_efficiency = ""
    efficiency = 0.0
    certificate_80plus = ""
    power_supply_fan_size = 0
    num_fans = 0
    fan_backlight = False
    case_backlight = False
    power_cable_length_12V = 0.0
    modular_connection_power_cables = False
    motherboard_power = ""
    cpu_4pin = ""
    cpu_8pin = ""
    fdd_4pin = ""
    ide_4pin = ""
    sata = ""
    pcie_6pin = ""
    pcie_8pin = ""
    pcie_gen5_16pin = ""
    usb_power = False
    height = 0.0
    width = 0.0
    depth = 0.0
    weight = 0.0
    equipment = ""
    def __init__(self, keys, values, descriptions, reading=False):
        if reading == False:
            self.name = values[keys.index("Название")]
            self.price = float(values[keys.index("Цена")].split()[0].replace(',', '.'))
            if "Дата выхода на рынок" in keys:
                self.market_launch_date = int(values[keys.index("Дата выхода на рынок")].split()[0])
            else:
                self.market_launch_date = None
            if "Описание" in keys:
                self.power_description = values[keys.index("Описание")]
            else:
                self.power_description = None
            if "Назначение" in keys:
                self.purpose = values[keys.index("Назначение")]
            else:
                self.purpose = None
            if "Мощность" in keys:
                self.power = int(values[keys.index("Мощность")].split()[0])
            else:
                self.power = None
            if "Стандарт блока питания" in keys:
                self.power_supply_standard = values[keys.index("Стандарт блока питания")]
            else:
                self.power_supply_standard = None
            if "Диапазон входного напряжения сети" in keys:
                self.input_voltage_range = values[keys.index("Диапазон входного напряжения сети")]
            else:
                self.input_voltage_range = None
            if "Количество отдельных линий +12V" in keys:
                self.number_of_individual_12v_lines = int(values[keys.index("Количество отдельных линий +12V")].split()[0])
            else:
                self.number_of_individual_12v_lines = None
            if "Макс. ток по линии +12V" in keys:
                self.max_line_current_12v = float(values[keys.index("Макс. ток по линии +12V")].split()[0])
            else:
                self.max_line_current_12v = None
            if "Комбинированная нагрузка по +12V" in keys:
                self.combined_12v_load = float(values[keys.index("Комбинированная нагрузка по +12V")].split()[0])
            else:
                self.combined_12v_load = None
            if "Коррекция фактора мощности (PFC)" in keys:
                self.power_factor_correction_efficiency = values[keys.index("Коррекция фактора мощности (PFC)")]
            else:
                self.power_factor_correction_efficiency = None
            if "КПД" in keys:
                self.efficiency = float(values[keys.index("КПД")].split()[0])
            else:
                self.efficiency = None
            if "Сертификат 80 PLUS" in keys:
                self.certificate_80plus = values[keys.index("Сертификат 80 PLUS")]
            else:
                self.certificate_80plus = None
            if "Размер вентилятора блока питания" in keys:
                self.power_supply_fan_size = int(values[keys.index("Размер вентилятора блока питания")].split()[0])
            else:
                self.power_supply_fan_size = None
            if "Количество вентиляторов" in keys:
                self.num_fans = int(values[keys.index("Количество вентиляторов")].split()[0])
            else:
                self.num_fans = None
            if "Подсветка вентилятора" in keys:
                self.fan_backlight = True if values[keys.index("Подсветка вентилятора")] == "Yes" else False
            else:
                self.fan_backlight = None
            if "Подсветка корпуса" in keys:
                self.case_backlight = True if values[keys.index("Подсветка корпуса")] == "Yes" else False
            else:
                self.case_backlight = None
            if "Длина кабеля питания 12В" in keys:
                self.power_cable_length_12V = float(values[keys.index("Длина кабеля питания 12В")].split()[0])
            else:
                self.power_cable_length_12V = None
            if "Модульное подключение кабелей питания" in keys:
                self.modular_connection_power_cables = True if values[keys.index("Модульное подключение кабелей питания")] == "Yes" else False
            else:
                self.modular_connection_power_cables = None
            if "Питание материнской платы" in keys:
                self.motherboard_power = values[keys.index("Питание материнской платы")]
            else:
                self.motherboard_power = None
            if "CPU 4 pin" in keys:
                self.cpu_4pin = values[keys.index("CPU 4 pin")]
            else:
                self.cpu_4pin = None
            if "CPU 8 pin" in keys:
                self.cpu_8pin = values[keys.index("CPU 8 pin")]
            else:
                self.cpu_8pin = None
            if "FDD 4 pin" in keys:
                self.fdd_4pin = values[keys.index("FDD 4 pin")]
            else:
                self.fdd_4pin = None
            if "IDE 4 pin" in keys:
                self.ide_4pin = values[keys.index("IDE 4 pin")]
            else:
                self.ide_4pin = None
            if "SATA" in keys:
                self.sata = values[keys.index("SATA")]
            else:
                self.sata = None
            if "PCIe 6 pin" in keys:
                self.pcie_6pin = values[keys.index("PCIe 6 pin")]
            else:
                self.pcie_6pin = None
            if "PCIe 8 pin" in keys:
                self.pcie_8pin = values[keys.index("PCIe 8 pin")]
            else:
                self.pcie_8pin = None
            if "PCIe Gen5 (16 pin)" in keys:
                self.pcie_gen5_16pin = values[keys.index("PCIe Gen5 (16 pin)")]
            else:
                self.pcie_gen5_16pin = None
            if "PCIe Gen5 (16 pin)" in keys:
                self.usb_power = True if values[keys.index("USB Power")] == "Yes" else False
            else:
                self.usb_power = None
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
            if "Комплектация" in keys:
                self.equipment = values[keys.index("Комплектация")]
            else:
                self.equipment = None
        elif reading == True:
            self.name = values[keys.index("Название")]
            self.price = values[keys.index("Цена")]
            self.market_launch_date = values[keys.index("Дата выхода на рынок")]
            self.power_description = values[keys.index("Описание")]
            self.purpose = values[keys.index("Назначение")]
            self.power = values[keys.index("Мощность")]
            self.power_supply_standard = values[keys.index("Стандарт блока питания")]
            self.input_voltage_range = values[keys.index("Диапазон входного напряжения сети")]
            self.number_of_individual_12v_lines = values[keys.index("Количество отдельных линий +12V")]
            self.max_line_current_12v = values[keys.index("Макс. ток по линии +12V")]
            self.combined_12v_load = values[keys.index("Комбинированная нагрузка по +12V")]
            self.power_factor_correction_efficiency = values[keys.index("Коррекция фактора мощности (PFC)")]
            self.efficiency = values[keys.index("КПД")]
            self.certificate_80plus = values[keys.index("Сертификат 80 PLUS")]
            self.power_supply_fan_size = values[keys.index("Размер вентилятора блока питания")]
            self.num_fans = values[keys.index("Количество вентиляторов")]
            self.fan_backlight = values[keys.index("Подсветка вентилятора")]
            self.case_backlight = values[keys.index("Подсветка корпуса")]
            self.power_cable_length_12V = values[keys.index("Длина кабеля питания 12В")]
            self.modular_connection_power_cables = values[keys.index("Модульное подключение кабелей питания")]
            self.motherboard_power = values[keys.index("Питание материнской платы")]
            self.cpu_4pin = values[keys.index("CPU 4 pin")]
            self.cpu_8pin = values[keys.index("CPU 8 pin")]
            self.fdd_4pin = values[keys.index("FDD 4 pin")]
            self.ide_4pin = values[keys.index("IDE 4 pin")]
            self.sata = values[keys.index("SATA")]
            self.pcie_6pin = values[keys.index("PCIe 6 pin")]
            self.pcie_8pin = values[keys.index("PCIe 8 pin")]
            self.pcie_gen5_16pin = values[keys.index("PCIe Gen5 (16 pin)")]
            self.usb_power = values[keys.index("USB Power")]
            self.height = values[keys.index("Высота")]
            self.width = values[keys.index("Ширина")]
            self.depth = values[keys.index("Глубина")]
            self.weight = values[keys.index("Вес")]
            self.equipment = values[keys.index("Комплектация")]