import re

class Hdd:
    id = 0
    name = ""
    price = 0.0
    drive_type = ""
    volume = 0.0
    form_factor = ""
    interface = ""
    spindle_speed = 0
    num_plates = 0
    buffer = 0
    hardware_encryption = False
    sector_size = ""
    sequential_read_speed = 0
    sequential_write_speed = 0
    noise_level_when_reading_or_writing = 0
    noise_level_in_standby_mode = 0
    shock_load_at_work = 0
    shock_load_in_non_operating_state = 0
    power_consumption_read_or_write = 0.0
    power_consumption_standby = 0.0
    time_between_failures = 0
    thickness = 0.0
    def __init__(self, keys, values, descriptions, reading=False):
        if reading == False:
            self.name = values[keys.index("Название")]
            self.price = float(values[keys.index("Цена")].split()[0].replace(',', '.'))
            if "Тип накопителя" in keys:
                self.drive_type = values[keys.index("Тип накопителя")]
            else:
                self.drive_type = None
            if "Объём" in keys:
                volume = values[keys.index("Объём")].split()[0]
                if len(volume) == 1:  # Если объем в Тб
                    volume = float(volume) * 1024
                self.volume = float(volume)
            else:
                self.volume = None
            if "Форм-фактор" in keys:
                self.form_factor = values[keys.index("Форм-фактор")]
            else:
                self.form_factor = None
            if "Интерфейс" in keys:
                self.interface = values[keys.index("Интерфейс")]
            else:
                self.interface = None
            if "Скорость вращения шпинделя" in keys:
                self.spindle_speed = int(''.join(re.findall(r'\d+', values[keys.index("Скорость вращения шпинделя")])))
            else:
                self.spindle_speed = None
            if "Количество пластин" in keys:
                self.num_plates = int(values[keys.index("Количество пластин")].split()[0])
            else:
                self.num_plates = None
            if "Буфер" in keys:
                self.buffer = int(values[keys.index("Буфер")].split()[0])
            else:
                self.buffer = None
            if "Аппаратное шифрование" in keys:
                self.hardware_encryption = True if values[keys.index("Аппаратное шифрование")] == "Yes" else False
            else:
                self.hardware_encryption = None
            if "Размер сектора" in keys:
                self.sector_size = values[keys.index("Размер сектора")]
            else:
                self.sector_size = None
            if "Скорость последовательного чтения" in keys:
                self.sequential_read_speed = int(values[keys.index("Скорость последовательного чтения")].split()[0])
            else:
                self.sequential_read_speed = None
            if "Скорость последовательной записи" in keys:
                self.sequential_write_speed = int(values[keys.index("Скорость последовательной записи")].split()[0])
            else:
                self.sequential_write_speed = None
            if "Уровень шума при чтении/записи" in keys:
                self.noise_level_when_reading_or_writing = int(values[keys.index("Уровень шума при чтении/записи")].split()[0])
            else:
                self.noise_level_when_reading_or_writing = None
            if "Уровень шума в режиме ожидания" in keys:
                self.noise_level_in_standby_mode = int(values[keys.index("Уровень шума в режиме ожидания")].split()[0])
            else:
                self.noise_level_in_standby_mode = None
            if "Ударная нагрузка при работе" in keys:
                self.shock_load_at_work = int(values[keys.index("Ударная нагрузка при работе")].split()[0])
            else:
                self.shock_load_at_work = None
            if "Ударная нагрузка в нерабочем состоянии" in keys:
                self.shock_load_in_non_operating_state = int(values[keys.index("Ударная нагрузка в нерабочем состоянии")].split()[0])
            else:
                self.shock_load_in_non_operating_state = None
            if "Энергопотребление (чтение/запись)" in keys:
                self.power_consumption_read_or_write = float(values[keys.index("Энергопотребление (чтение/запись)")].split()[0])
            else:
                self.power_consumption_read_or_write = None
            if "Энергопотребление (ожидание)" in keys:
                self.power_consumption_standby = float(values[keys.index("Энергопотребление (ожидание)")].split()[0])
            else:
                self.power_consumption_standby = None
            if "Время наработки на отказ (МТBF)" in keys:
                self.time_between_failures = int(values[keys.index("Время наработки на отказ (МТBF)")].split()[0])
            else:
                self.time_between_failures = None
            if "Толщина" in keys:
                self.thickness = float(values[keys.index("Толщина")].split()[0])
            else:
                self.thickness = None
        elif reading == True:
            self.id = values[keys.index("Id")]
            self.name = values[keys.index("Название")]
            self.price = values[keys.index("Цена")]
            self.drive_type = values[keys.index("Тип накопителя")]
            self.volume = values[keys.index("Объём")]
            self.form_factor = values[keys.index("Форм-фактор")]
            self.interface = values[keys.index("Интерфейс")]
            self.spindle_speed = values[keys.index("Скорость вращения шпинделя")]
            self.num_plates = values[keys.index("Количество пластин")]
            self.buffer = values[keys.index("Буфер")]
            self.hardware_encryption = values[keys.index("Аппаратное шифрование")]
            self.sector_size = values[keys.index("Размер сектора")]
            self.sequential_read_speed = values[keys.index("Скорость последовательного чтения")]
            self.sequential_write_speed = values[keys.index("Скорость последовательной записи")]
            self.noise_level_when_reading_or_writing = values[keys.index("Уровень шума при чтении/записи")]
            self.noise_level_in_standby_mode = values[keys.index("Уровень шума в режиме ожидания")]
            self.shock_load_at_work = values[keys.index("Ударная нагрузка при работе")]
            self.shock_load_in_non_operating_state = values[keys.index("Ударная нагрузка в нерабочем состоянии")]
            self.power_consumption_read_or_write = values[keys.index("Энергопотребление (чтение/запись)")]
            self.power_consumption_standby = values[keys.index("Энергопотребление (ожидание)")]
            self.time_between_failures = values[keys.index("Время наработки на отказ (МТBF)")]
            self.thickness = values[keys.index("Толщина")]