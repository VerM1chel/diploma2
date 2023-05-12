# from detail import Detail
import re

# Done
class Cpu:
    id = 0
    name = ""
    price = 0.0
    market_launch_date = 0
    lineup = ""
    delivery_type = ""
    cooling_included = ""
    crystal_code_name = ""
    socket = ""
    num_cores = 0
    max_threads = 0
    base_clock = 0.0
    max_frequency = 0.0
    l2_cache = 0.0
    l3_cache = 0.0
    memory_support = ""
    num_memory_channels = 0
    max_memory_without_overclocking = 0
    integrated_pcie_controller = ""
    pcie_controller_configuration = ""
    integrated_graphics = ""
    estimated_thermal_power = 0.0
    process_technology = 0
    kernel_multithreading = False
    amd_v_virtualization = False
    vtx_intel_virtualization = False
    vtd_intel_virtualization = False
    intel_txt_secure_platform = False
    def __init__(self, keys, values, descriptions, reading=False):
        if reading == False:
            self.name = values[keys.index("Название")]
            self.price = float(values[keys.index("Цена")].split()[0].replace(',', '.'))
            if "Дата выхода на рынок" in keys:
                self.market_launch_date = int(values[keys.index("Дата выхода на рынок")].split()[0])
            else:
                self.market_launch_date = None
            if "Модельный ряд" in keys:
                self.lineup = values[keys.index("Модельный ряд")]
            else:
                self.lineup = None
            if "Тип поставки" in keys:
                self.delivery_type = values[keys.index("Тип поставки")]
            else:
                self.delivery_type = None
            if "Охлаждение в комплекте" in keys:
                self.cooling_included = values[keys.index("Охлаждение в комплекте")]
            else:
                self.cooling_included = None
            if "Кодовое название кристалла" in keys:
                self.crystal_code_name = values[keys.index("Кодовое название кристалла")]
            else:
                self.crystal_code_name = None
            if "Сокет" in keys:
                self.socket = values[keys.index("Сокет")]
            else:
                self.socket = None
            if "Количество ядер" in keys:
                self.num_cores = int(values[keys.index("Количество ядер")].split()[0].strip())
            else:
                self.num_cores = None
            if "Максимальное количество потоков" in keys:
                self.max_threads = int(values[keys.index("Максимальное количество потоков")])
            else:
                self.max_threads = None
            if "Базовая тактовая частота" in keys:
                self.base_clock = float(values[keys.index("Базовая тактовая частота")].split()[0])
            else:
                self.base_clock = None
            if "Максимальная частота" in keys:
                self.max_frequency = float(values[keys.index("Максимальная частота")].split()[0])
            else:
                self.max_frequency = None
            if "Кэш L2" in keys: # Некоторые характеристики могут иногда отсутствовать
                self.l2_cache = float(values[keys.index("Кэш L2")].split()[0])
            else:
                self.l2_cache = None
            if "Кэш L3" in keys:
                self.l3_cache = float(values[keys.index("Кэш L3")].split()[0])
            else:
                self.l3_cache = None
            if "Поддержка памяти" in keys:
                self.memory_support = values[keys.index("Поддержка памяти")]
            else:
                self.memory_support = None
            if "Количество каналов памяти" in keys:
                self.num_memory_channels = int(values[keys.index("Количество каналов памяти")])
            else:
                self.num_memory_channels = None
            if "Макс. частота памяти без разгона" in keys:
                index = values[keys.index("Макс. частота памяти без разгона")].index("МГц")
                self.max_memory_without_overclocking = int(''.join(re.findall(r'\d+',values[keys.index("Макс. частота памяти без разгона")][:index])))
            else:
                self.max_memory_without_overclocking = None
            if "Встроенный контроллер PCI Express" in keys:
                self.integrated_pcie_controller = values[keys.index("Встроенный контроллер PCI Express")]
            else:
                self.integrated_pcie_controller = None
            if "Конфигурация контроллера PCIe" in keys:
                self.pcie_controller_configuration = values[keys.index("Конфигурация контроллера PCIe")]
            else:
                self.pcie_controller_configuration = None
            if "Встроенная графика" in keys:
                self.integrated_graphics = values[keys.index("Встроенная графика")]
            else:
                self.integrated_graphics = None
            if "Расчетная тепловая мощность (TDP)" in keys:
                self.estimated_thermal_power = float(values[keys.index("Расчетная тепловая мощность (TDP)")].split()[0])
            else:
                self.estimated_thermal_power = None
            if "Техпроцесс" in keys:
                self.process_technology = int(values[keys.index("Техпроцесс")].split()[0])
            else:
                self.process_technology = None
            if "Многопоточность ядра" in keys:
                self.kernel_multithreading = True if values[keys.index("Многопоточность ядра")] == "Yes" else False
            else:
                self.kernel_multithreading = None
            if "Виртуализация AMD-V" in keys:
                self.amd_v_virtualization = True if values[keys.index("Виртуализация AMD-V")] == "Yes" else False
            else:
                self.amd_v_virtualization = None
            if "Виртуализация Intel VT-x" in keys:
                self.vtx_intel_virtualization = True if values[keys.index("Виртуализация Intel VT-x")] == "Yes" else False
            else:
                self.vtx_intel_virtualization = None
            if "Виртуализация Intel VT-d" in keys:
                self.vtd_intel_virtualization = True if values[keys.index("Виртуализация Intel VT-d")] == "Yes" else False
            else:
                self.vtd_intel_virtualization = None
            if "Защищенная платформа Intel TXT" in keys:
                self.intel_txt_secure_platform = True if values[keys.index("Защищенная платформа Intel TXT")] == "Yes" else False
            else:
                self.intel_txt_secure_platform = None
        elif reading == True:
            self.id = values[keys.index("Id")]
            self.name = values[keys.index("Название")]
            self.price = values[keys.index("Цена")]
            self.market_launch_date = values[keys.index("Дата выхода на рынок")]
            self.lineup = values[keys.index("Модельный ряд")]
            self.delivery_type = values[keys.index("Тип поставки")]
            self.cooling_included = values[keys.index("Охлаждение в комплекте")]
            self.crystal_code_name = values[keys.index("Кодовое название кристалла")]
            self.socket = values[keys.index("Сокет")]
            self.num_cores = values[keys.index("Количество ядер")]
            self.max_threads = values[keys.index("Максимальное количество потоков")]
            self.base_clock = values[keys.index("Базовая тактовая частота")]
            self.max_frequency = values[keys.index("Максимальная частота")]
            self.l2_cache = values[keys.index("Кэш L2")]
            self.l3_cache = values[keys.index("Кэш L3")]
            self.memory_support = values[keys.index("Поддержка памяти")]
            self.num_memory_channels = values[keys.index("Количество каналов памяти")]
            self.max_memory_without_overclocking = values[keys.index("Макс. частота памяти без разгона")]
            self.integrated_pcie_controller = values[keys.index("Встроенный контроллер PCI Express")]
            self.pcie_controller_configuration = values[keys.index("Конфигурация контроллера PCIe")]
            self.integrated_graphics = values[keys.index("Встроенная графика")]
            self.estimated_thermal_power = values[keys.index("Расчетная тепловая мощность (TDP)")]
            self.process_technology = values[keys.index("Техпроцесс")]
            self.kernel_multithreading = values[keys.index("Многопоточность ядра")]
            self.amd_v_virtualization = values[keys.index("Виртуализация AMD-V")]
            self.vtx_intel_virtualization = values[keys.index("Виртуализация Intel VT-x")]
            self.vtd_intel_virtualization = values[keys.index("Виртуализация Intel VT-d")]
            self.intel_txt_secure_platform = values[keys.index("Защищенная платформа Intel TXT")]
