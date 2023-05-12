# from detail import Detail
# Done
import re

class Ssd:
    id = 0
    name = ""
    price = 0.0
    market_launch_date = 0
    ssd_description = ""
    volume = 0.0
    form_factor = ""
    interface = ""
    chip_type_flash = ""
    controller = ""
    m2_device_sizes = ""
    write_resource = 0.0
    buffer_size = ""
    hardware_encryption = ""
    sequential_read_speed = 0
    sequential_write_speed = 0
    average_random_read_speed = 0
    average_random_write_speed = 0
    power_consumption_read_or_write = 0.0
    power_consumption_cooling = 0.0
    time_between_failures = 0
    thickness = 0.0
    cooling = False
    backlight = False
    ps5_compatible = False
    delivery_option = ""
    delivery_contents = ""
    adapter_3dot5inch = False
    def __init__(self, keys, values, descriptions, reading=False):
        if reading == False:
            self.name = values[keys.index("Название")]
            self.price = float(values[keys.index("Цена")].split()[0].replace(',', '.'))
            if "Дата выхода на рынок" in keys:
                self.market_launch_date = int(values[keys.index("Дата выхода на рынок")].split()[0])
            else:
                self.market_launch_date = None
            if "Описание" in keys:
                self.ssd_description = values[keys.index("Описание")]
            else:
                self.ssd_description = None
            if "Объём" in keys:
                volume = values[keys.index("Объём")].split()[0]
                if len(volume) == 1: # Если объем в Тб
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
            if "Тип микросхем Flash" in keys:
                self.chip_type_flash = values[keys.index("Тип микросхем Flash")]
            else:
                self.chip_type_flash = None
            if "Контроллер" in keys:
                self.controller = values[keys.index("Контроллер")]
            else:
                self.controller = None
            if "Размеры устройств M.2" in keys:
                self.m2_device_sizes = values[keys.index("Размеры устройств M.2")]
            else:
                self.m2_device_sizes = None
            if "Ресурс записи" in keys:
                self.write_resource = float(values[keys.index("Ресурс записи")].split()[0])
            else:
                self.write_resource = None
            if "Буфер" in keys:
                self.buffer_size = values[keys.index("Буфер")].split()[0]
            else:
                self.buffer_size = None
            if "Аппаратное шифрование" in keys:
                self.hardware_encryption = values[keys.index("Аппаратное шифрование")]
            else:
                self.hardware_encryption = None
            if "Скорость последовательного чтения" in keys:
                self.sequential_read_speed = int(''.join(re.findall(r'\d+', values[keys.index("Скорость последовательного чтения")])))
            else:
                self.sequential_read_speed = None
            if "Скорость последовательной записи" in keys:
                self.sequential_write_speed = int(''.join(re.findall(r'\d+', values[keys.index("Скорость последовательной записи")])))
            else:
                self.sequential_write_speed = None
            if "Средняя скорость случайного чтения" in keys:
                self.average_random_read_speed = int(''.join(re.findall(r'\d+', values[keys.index("Средняя скорость случайного чтения")])))
            else:
                self.average_random_read_speed = None
            if "Средняя скорость случайной записи" in keys:
                self.average_random_write_speed = int(''.join(re.findall(r'\d+', values[keys.index("Средняя скорость случайной записи")])))
            else:
                self.average_random_write_speed = None
            if "Энергопотребление (чтение/запись)" in keys:
                self.power_consumption_read_or_write = float(values[keys.index("Энергопотребление (чтение/запись)")].split()[0])
            else:
                self.power_consumption_read_or_write = None
            if "Энергопотребление (ожидание)" in keys:
                self.power_consumption_cooling = float(values[keys.index("Энергопотребление (ожидание)")].split()[0])
            else:
                self.power_consumption_cooling = None
            if "Время наработки на отказ (МТBF)" in keys:
                self.time_between_failures = int(''.join(re.findall(r'\d+', values[keys.index("Время наработки на отказ (МТBF)")])))
            else:
                self.time_between_failures = None
            if "Толщина" in keys:
                self.thickness = float(values[keys.index("Толщина")].split()[0])
            else:
                self.thickness = None
            if "Охлаждение" in keys:
                self.cooling = True if values[keys.index("Охлаждение")] == "Yes" else False
            else:
                self.cooling = None
            if "Подсветка" in keys:
                self.backlight = True if values[keys.index("Подсветка")] == "Yes" else False
            else:
                self.backlight = None
            if "Совместимость с PS5" in keys:
                self.ps5_compatible = True if values[keys.index("Совместимость с PS5")] == "Yes" else False
            else:
                self.ps5_compatible = None
            if "Вариант поставки" in keys:
                self.delivery_option = values[keys.index("Вариант поставки")]
            else:
                self.delivery_option = None
            if "Комплект поставки" in keys:
                self.delivery_contents = values[keys.index("Комплект поставки")]
            else:
                self.delivery_contents = None
            if 'Адаптер 3.5"' in keys:
                self.adapter_3dot5inch = True if values[keys.index('Адаптер 3.5"')] == "Yes" else False
            else:
                self.adapter_3dot5inch = None
        elif reading == True:
            self.id = values[keys.index("Id")]
            self.name = values[keys.index("Название")]
            self.price = values[keys.index("Цена")]
            self.market_launch_date = values[keys.index("Дата выхода на рынок")]
            self.ssd_description = values[keys.index("Описание")]
            self.volume = values[keys.index("Объём")]
            self.form_factor = values[keys.index("Форм-фактор")]
            self.interface = values[keys.index("Интерфейс")]
            self.chip_type_flash = values[keys.index("Тип микросхем Flash")]
            self.controller = values[keys.index("Контроллер")]
            self.m2_device_sizes = values[keys.index("Размеры устройств M.2")]
            self.write_resource = values[keys.index("Ресурс записи")]
            self.buffer_size = values[keys.index("Буфер")]
            self.hardware_encryption = values[keys.index("Аппаратное шифрование")]
            self.sequential_read_speed = values[keys.index("Скорость последовательного чтения")]
            self.sequential_write_speed = values[keys.index("Скорость последовательной записи")]
            self.average_random_read_speed = values[keys.index("Средняя скорость случайного чтения")]
            self.average_random_write_speed = values[keys.index("Средняя скорость случайной записи")]
            self.power_consumption_read_or_write = values[keys.index("Энергопотребление (чтение/запись)")]
            self.power_consumption_cooling = values[keys.index("Энергопотребление (ожидание)")]
            self.time_between_failures = values[keys.index("Время наработки на отказ (МТBF)")]
            self.thickness = values[keys.index("Толщина")]
            self.cooling = values[keys.index("Охлаждение")]
            self.backlight = values[keys.index("Подсветка")]
            self.ps5_compatible = values[keys.index("Совместимость с PS5")]
            self.delivery_option = values[keys.index("Вариант поставки")]
            self.delivery_contents = values[keys.index("Комплект поставки")]
            self.adapter_3dot5inch = values[keys.index('Адаптер 3.5"')]