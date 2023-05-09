# from detail import Detail
# Done
class Ram:
    name = ""
    price = 0.0
    kit = 0
    overall_volume = 0
    one_module_volume = 0
    ram_type = ""
    ecc = ""
    frequency = 0
    pc_index = ""
    cas_latency = ""
    timings = ""
    supply_voltage = 0.0
    xmp_profiles = ""
    amp_profiles = ""
    cooling = False
    low_profile_module = False
    board_elements_illumination = False
    color = ""
    def __init__(self, keys, values, descriptions, reading=False):
        if reading == False:
            self.name = values[keys.index("Название")]
            self.price = float(values[keys.index("Цена")].split()[0].replace(',', '.'))
            if "Набор" in keys:
                self.kit = int(values[keys.index("Набор")].split()[0])
            else:
                self.kit = None
            if "Общий объем" in keys:
                self.overall_volume = int(values[keys.index("Общий объем")].split()[0])
            else:
                self.overall_volume = None
            if "Объем одного модуля" in keys:
                self.one_module_volume = int(values[keys.index("Объем одного модуля")].split()[0])
            else:
                self.one_module_volume = None
            if "Тип" in keys:
                self.ram_type = values[keys.index("Тип")]
            else:
                self.ram_type = None
            if "ECC" in keys:
                self.ecc = values[keys.index("ECC")]
            else:
                self.ecc = None
            if "Частота" in keys:
                self.frequency = int(values[keys.index("Частота")].split()[0])
            else:
                self.frequency = None
            if "PC-индекс" in keys:
                self.pc_index = values[keys.index("PC-индекс")]
            else:
                self.pc_index = None
            if "CAS Latency" in keys:
                self.cas_latency = values[keys.index("CAS Latency")]
            else:
                self.cas_latency = None
            if "Тайминги" in keys:
                self.timings = values[keys.index("Тайминги")]
            else:
                self.timings = None
            if "Напряжение питания" in keys:
                self.supply_voltage = float(values[keys.index("Напряжение питания")].split()[0])
            else:
                self.supply_voltage = None
            if "Профили XMP" in keys:
                self.xmp_profiles = values[keys.index("Профили XMP")]
            else:
                self.xmp_profiles = None
            if "Профили AMP" in keys:
                self.amp_profiles = values[keys.index("Профили AMP")]
            else:
                self.amp_profiles = None
            if "Охлаждение" in keys:
                self.cooling = True if values[keys.index("Охлаждение")] == "Yes" else False
            else:
                self.cooling = None
            if "Низкопрофильный модуль" in keys:
                self.low_profile_module = True if values[keys.index("Низкопрофильный модуль")] == "Yes" else False
            else:
                self.low_profile_module = None
            if "Подсветка элементов платы" in keys:
                self.board_elements_illumination = True if values[keys.index("Подсветка элементов платы")] == "Yes" else False
            else:
                self.board_elements_illumination = None
            if "Цвет" in keys:
                self.color = values[keys.index("Цвет")]
            else:
                self.color = None
        elif reading == True:
            self.name = values[keys.index("Название")]
            self.price = values[keys.index("Цена")]
            self.kit = values[keys.index("Набор")]
            self.overall_volume = values[keys.index("Общий объем")]
            self.one_module_volume = values[keys.index("Объем одного модуля")]
            self.ram_type = values[keys.index("Тип")]
            self.ecc = values[keys.index("ECC")]
            self.frequency = values[keys.index("Частота")]
            self.pc_index = values[keys.index("PC-индекс")]
            self.cas_latency = values[keys.index("CAS Latency")]
            self.timings = values[keys.index("Тайминги")]
            self.supply_voltage = values[keys.index("Напряжение питания")]
            self.xmp_profiles = values[keys.index("Профили XMP")]
            self.amp_profiles = values[keys.index("Профили AMP")]
            self.cooling = values[keys.index("Охлаждение")]
            self.low_profile_module = values[keys.index("Низкопрофильный модуль")]
            self.board_elements_illumination = values[keys.index("Подсветка элементов платы")]
            self.color = values[keys.index("Цвет")]
