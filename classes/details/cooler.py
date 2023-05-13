# from detail import Detail
# Done
class Cooler:
    id = 0
    name = ""
    price = 0.0
    market_launch_date = 0
    cooler_type = ""
    cooling = ""
    color = ""
    socket = ""
    power_dissipation = 0
    radiator_material = ""
    num_heat_pipes = ""
    evaporation_chambers = 0
    fan_diameter = 0
    num_of_fans = 0
    bearing = ""
    minimum_rotation_speed = 0
    maximum_rotation_speed = 0
    max_airflow = 0.0
    rotational_speed_control = False
    thermal_control = False
    connection_type = ""
    backlight_connection_type = ""
    led_backlight = ""
    vibration_isolation = False
    maximum_noise_level = 0.0
    width = 0.0
    depth = 0.0
    height_or_thickness = 0.0
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
            if "Тип" in keys:
                self.cooler_type = values[keys.index("Тип")]
            else:
                self.cooler_type = None
            if "Охлаждение" in keys:
                self.cooling = values[keys.index("Охлаждение")]
            else:
                self.cooling = None
            if "Цвет" in keys:
                self.color = values[keys.index("Цвет")]
            else:
                self.color = None
            if "Сокет" in keys:
                self.socket = values[keys.index("Сокет")]
            else:
                self.socket = None
            if "Рассеиваемая мощность" in keys:
                self.power_dissipation = int(values[keys.index("Рассеиваемая мощность")].split()[0])
            else:
                self.power_dissipation = None
            if "Материал радиатора" in keys:
                self.radiator_material = values[keys.index("Материал радиатора")]
            else:
                self.radiator_material = None
            if "Тепловые трубки" in keys:
                self.num_heat_pipes = values[keys.index("Тепловые трубки")] if values[keys.index("Тепловые трубки")] != "No" else "-"
            else:
                self.num_heat_pipes = None
            if "Испарительные камеры" in keys:
                self.evaporation_chambers = int(values[keys.index("Испарительные камеры")]) if values[keys.index("Испарительные камеры")] != "No" else 0
            else:
                self.evaporation_chambers = None
            if "Диаметр вентилятора" in keys:
                self.fan_diameter = int(values[keys.index("Диаметр вентилятора")].split()[0])
            else:
                self.fan_diameter = None
            if "Количество вентиляторов" in keys:
                self.num_of_fans = int(values[keys.index("Количество вентиляторов")].split()[0])
            else:
                self.num_of_fans = None
            if "Подшипник" in keys:
                self.bearing = values[keys.index("Подшипник")]
            else:
                self.bearing = None
            if "Минимальная скорость вращения" in keys:
                self.minimum_rotation_speed = int(values[keys.index("Минимальная скорость вращения")].split()[0])
            else:
                self.minimum_rotation_speed = None
            if "Максимальная скорость вращения" in keys:
                self.maximum_rotation_speed = int(values[keys.index("Максимальная скорость вращения")].split()[0])
            else:
                self.maximum_rotation_speed = None
            if "Максимальный воздушный поток" in keys:
                self.max_airflow = float(values[keys.index("Максимальный воздушный поток")].split()[0])
            else:
                self.max_airflow = None
            if "Контроль скорости вращения (PWM)" in keys:
                self.rotational_speed_control = True if values[keys.index("Контроль скорости вращения (PWM)")] == "Yes" else False
            else:
                self.rotational_speed_control = None
            if "Термоконтроль" in keys:
                self.thermal_control = True if values[keys.index("Термоконтроль")] == "Yes" else False
            else:
                self.thermal_control = None
            if "Тип подключения" in keys:
                self.connection_type = values[keys.index("Тип подключения")]
            else:
                self.connection_type = None
            if "Тип подключения подсветки" in keys:
                self.backlight_connection_type = values[keys.index("Тип подключения подсветки")]
            else:
                self.backlight_connection_type = None
            if "LED-подсветка" in keys:
                self.led_backlight = values[keys.index("LED-подсветка")]
            else:
                self.led_backlight = None
            if "Виброизоляция" in keys:
                self.vibration_isolation = True if values[keys.index("Виброизоляция")] == "Yes" else False
            else:
                self.vibration_isolation = None
            if "Максимальный уровень шума" in keys:
                self.maximum_noise_level = float(values[keys.index("Максимальный уровень шума")].split()[0])
            else:
                self.maximum_noise_level = None
            if "Ширина" in keys:
                self.width = float(values[keys.index("Ширина")].split()[0])
            else:
                self.width = None
            if "Глубина" in keys:
                self.depth = float(values[keys.index("Глубина")].split()[0])
            else:
                self.depth = None
            if "Высота (толщина)" in keys:
                self.height_or_thickness = float(values[keys.index("Высота (толщина)")].split()[0])
            else:
                self.height_or_thickness = None
            if "Вес" in keys:
                self.weight = float(values[keys.index("Вес")].split()[0])
            else:
                self.weight = None
            if "Комплектация" in keys:
                self.equipment = values[keys.index("Комплектация")]
            else:
                self.equipment = None
        elif reading == True:
            self.id = values[keys.index("Id")]-1
            self.name = values[keys.index("Название")]
            self.price = values[keys.index("Цена")]
            self.market_launch_date = values[keys.index("Дата выхода на рынок")]
            self.cooler_type = values[keys.index("Тип")]
            self.cooling = values[keys.index("Охлаждение")]
            self.color = values[keys.index("Цвет")]
            self.socket = values[keys.index("Сокет")]
            self.power_dissipation = values[keys.index("Рассеиваемая мощность")]
            self.radiator_material = values[keys.index("Материал радиатора")]
            self.num_heat_pipes = values[keys.index("Тепловые трубки")]
            self.evaporation_chambers = values[keys.index("Испарительные камеры")]
            self.fan_diameter = values[keys.index("Диаметр вентилятора")]
            self.num_of_fans = values[keys.index("Количество вентиляторов")]
            self.bearing = values[keys.index("Подшипник")]
            self.minimum_rotation_speed = values[keys.index("Минимальная скорость вращения")]
            self.maximum_rotation_speed = values[keys.index("Максимальная скорость вращения")]
            self.max_airflow = values[keys.index("Максимальный воздушный поток")]
            self.rotational_speed_control = values[keys.index("Контроль скорости вращения (PWM)")]
            self.thermal_control = values[keys.index("Термоконтроль")]
            self.connection_type = values[keys.index("Тип подключения")]
            self.backlight_connection_type = values[keys.index("Тип подключения подсветки")]
            self.led_backlight = values[keys.index("LED-подсветка")]
            self.vibration_isolation = values[keys.index("Виброизоляция")]
            self.maximum_noise_level = values[keys.index("Максимальный уровень шума")]
            self.width = values[keys.index("Ширина")]
            self.depth = values[keys.index("Глубина")]
            self.height_or_thickness = values[keys.index("Высота (толщина)")]
            self.weight = values[keys.index("Вес")]
            self.equipment = values[keys.index("Комплектация")]