# from detail import Detail
# Done
import re

class Gpu:
    id = 0
    name = ""
    price = 0.0
    market_launch_date = 0
    gpu_description = ""
    selection_in_one_click = ""
    interface = ""
    gpu_manufacturer = ""
    microarchitecture = ""
    chip_code_name = ""
    gpu_overclocked_version = False
    ray_tracing = False
    mining_protection_or_lhr = False
    gpu_base_frequency = 0
    max_gpu_frequency = 0
    num_stream_processors = 0
    num_rt_cores = 0
    video_memory = 0
    video_memory_type = ""
    effective_memory_frequency = 0
    memory_bandwidth = 0.0
    memory_bus_width = 0
    directX_support = ""
    sli_or_crossfire_support = ""
    power_connectors = ""
    recommended_psu_watts = 0
    cooling = ""
    cooling_system_thickness = 0.0
    num_fans = 0
    video_card_length = 0.0
    video_card_height = 0.0
    low_profile = False
    functional_features = ""
    vga_or_d_sub = ""
    dvi = ""
    hdmi = ""
    hdmi_version = ""
    mini_hdmi = ""
    display_port = ""
    display_port_version = ""
    mini_display_port = ""
    vesa_stereo = ""
    usb_type_c = ""
    def __init__(self, keys, values, descriptions, reading=False):
        if reading == False:
            self.name = values[keys.index("Название")]
            self.price = float(values[keys.index("Цена")].split()[0].replace(',', '.'))
            if "Дата выхода на рынок" in keys:
                self.market_launch_date = int(values[keys.index("Дата выхода на рынок")].split()[0])
            else:
                self.market_launch_date = None
            if "Описание" in keys:
                self.gpu_description = values[keys.index("Описание")]
            else:
                self.gpu_description = None
            if "Подбор в один клик" in keys:
                self.selection_in_one_click = values[keys.index("Подбор в один клик")]
            else:
                self.selection_in_one_click = None
            if "Интерфейс" in keys:
                self.interface = values[keys.index("Интерфейс")]
            else:
                self.interface = None
            if "Производитель графического процессора" in keys:
                self.gpu_manufacturer = values[keys.index("Производитель графического процессора")]
            else:
                self.gpu_manufacturer = None
            if "Микроархитектура" in keys:
                self.microarchitecture = values[keys.index("Микроархитектура")]
            else:
                self.microarchitecture = None
            if "Графический процессор" in keys:
                self.chip_code_name = values[keys.index("Графический процессор")]
            else:
                self.chip_code_name = None
            if "«Разогнанная» версия" in keys:
                self.gpu_overclocked_version = True if values[keys.index("«Разогнанная» версия")] == "Yes" else False
            else:
                self.gpu_overclocked_version = None
            if "Трассировка лучей" in keys:
                self.ray_tracing = True if values[keys.index("Трассировка лучей")] == "Yes" else False
            else:
                self.ray_tracing = None
            if "Защита от майнинга (LHR)" in keys:
                self.mining_protection_or_lhr = True if values[keys.index("Защита от майнинга (LHR)")] == "Yes" else False
            else:
                self.mining_protection_or_lhr = None
            if "Базовая (референсная) частота графического процессора" in keys:
                self.gpu_base_frequency = int(''.join(re.findall(r'\d+', values[keys.index("Базовая (референсная) частота графического процессора")])))
            else:
                self.gpu_base_frequency = None
            if "Максимальная частота графического процессора" in keys:
                self.max_gpu_frequency = int(''.join(re.findall(r'\d+', values[keys.index("Максимальная частота графического процессора")])))
            else:
                self.max_gpu_frequency = None
            if "Количество потоковых процессоров" in keys:
                self.num_stream_processors = int(''.join(re.findall(r'\d+', values[keys.index("Количество потоковых процессоров")])))
            else:
                self.num_stream_processors = None
            if "Количество RT-ядер" in keys:
                self.num_rt_cores = int(values[keys.index("Количество RT-ядер")].split()[0])
            else:
                self.num_rt_cores = None
            if "Видеопамять" in keys:
                self.video_memory = int(values[keys.index("Видеопамять")].split()[0])
            else:
                self.video_memory = None
            if "Тип видеопамяти" in keys:
                self.video_memory_type = values[keys.index("Тип видеопамяти")]
            else:
                self.video_memory_type = None
            if "Эффективная частота памяти" in keys:
                self.effective_memory_frequency = int(''.join(re.findall(r'\d+', values[keys.index("Эффективная частота памяти")])))
            else:
                self.effective_memory_frequency = None
            if "Пропускная способность памяти" in keys:
                self.memory_bandwidth = float(values[keys.index("Пропускная способность памяти")].split()[0])
            else:
                self.memory_bandwidth = None
            if "Ширина шины памяти" in keys:
                self.memory_bus_width = int(values[keys.index("Ширина шины памяти")].split()[0])
            else:
                self.memory_bus_width = None
            if "Поддержка DirectX" in keys:
                self.directX_support = values[keys.index("Поддержка DirectX")]
            else:
                self.directX_support = None
            if "Поддержка SLI/CrossFire" in keys:
                self.sli_or_crossfire_support = values[keys.index("Поддержка SLI/CrossFire")]
            else:
                self.sli_or_crossfire_support = None
            if "Разъёмы питания" in keys:
                self.power_connectors = values[keys.index("Разъёмы питания")]
            else:
                self.power_connectors = None
            if "Рекомендуемый блок питания" in keys:
                self.recommended_psu_watts = int(values[keys.index("Рекомендуемый блок питания")].split()[0])
            else:
                self.recommended_psu_watts = None
            if "Охлаждение" in keys:
                self.cooling = values[keys.index("Охлаждение")]
            else:
                self.cooling = None
            if "Толщина системы охлаждения" in keys:
                self.cooling_system_thickness = float(values[keys.index("Толщина системы охлаждения")].split()[0])
            else:
                self.cooling_system_thickness = None
            if "Количество вентиляторов" in keys:
                self.num_fans = int(values[keys.index("Количество вентиляторов")])
            else:
                self.num_fans = None
            if "Длина видеокарты" in keys:
                self.video_card_length = float(values[keys.index("Длина видеокарты")].split()[0])
            else:
                self.video_card_length = None
            if "Высота видеокарты" in keys:
                self.video_card_height = float(values[keys.index("Высота видеокарты")].split()[0])
            else:
                self.video_card_height = None
            if "Низкопрофильная (Low Profile)" in keys:
                self.low_profile = True if values[keys.index("Низкопрофильная (Low Profile)")] == "Yes" else False
            else:
                self.low_profile = None
            if "Функциональные особенности" in keys:
                self.functional_features = values[keys.index("Функциональные особенности")]
            else:
                self.functional_features = None
            if "VGA (D-Sub)" in keys:
                self.vga_or_d_sub = values[keys.index("VGA (D-Sub)")]
            else:
                self.vga_or_d_sub = None
            if "DVI" in keys:
                self.dvi = values[keys.index("DVI")]
            else:
                self.dvi = None
            if "HDMI" in keys:
                self.hdmi = values[keys.index("HDMI")]
            else:
                self.hdmi = None
            if "Версия HDMI" in keys:
                self.hdmi_version = values[keys.index("Версия HDMI")]
            else:
                self.hdmi_version = None
            if "mini HDMI" in keys:
                self.mini_hdmi = values[keys.index("mini HDMI")]
            else:
                self.mini_hdmi = None
            if "DisplayPort" in keys:
                self.display_port = values[keys.index("DisplayPort")]
            else:
                self.display_port = None
            if "Версия DisplayPort" in keys:
                self.display_port_version = values[keys.index("Версия DisplayPort")]
            else:
                self.display_port_version = None
            if "mini Display Port" in keys:
                self.mini_display_port = values[keys.index("mini Display Port")]
            else:
                self.mini_display_port = None
            if "VESA Stereo" in keys:
                self.vesa_stereo = values[keys.index("VESA Stereo")]
            else:
                self.vesa_stereo = None
            if "USB Type-C" in keys:
                self.usb_type_c = values[keys.index("USB Type-C")]
            else:
                self.usb_type_c = None
        elif reading == True:
            self.id = values[keys.index("Id")]-1
            self.name = values[keys.index("Название")]
            self.price = values[keys.index("Цена")]
            self.market_launch_date = values[keys.index("Дата выхода на рынок")]
            self.gpu_description = values[keys.index("Описание")]
            self.selection_in_one_click = values[keys.index("Подбор в один клик")]
            self.interface = values[keys.index("Интерфейс")]
            self.gpu_manufacturer = values[keys.index("Производитель графического процессора")]
            self.microarchitecture = values[keys.index("Микроархитектура")]
            self.chip_code_name = values[keys.index("Графический процессор")]
            self.gpu_overclocked_version = values[keys.index("«Разогнанная» версия")]
            self.ray_tracing = values[keys.index("Трассировка лучей")]
            self.mining_protection_or_lhr = values[keys.index("Защита от майнинга (LHR)")]
            self.gpu_base_frequency = values[keys.index("Базовая (референсная) частота графического процессора")]
            self.max_gpu_frequency = values[keys.index("Максимальная частота графического процессора")]
            self.num_stream_processors = values[keys.index("Количество потоковых процессоров")]
            self.num_rt_cores = values[keys.index("Количество RT-ядер")]
            self.video_memory = values[keys.index("Видеопамять")]
            self.video_memory_type = values[keys.index("Тип видеопамяти")]
            self.effective_memory_frequency = values[keys.index("Эффективная частота памяти")]
            self.memory_bandwidth = values[keys.index("Пропускная способность памяти")]
            self.memory_bus_width = values[keys.index("Ширина шины памяти")]
            self.directX_support = values[keys.index("Поддержка DirectX")]
            self.sli_or_crossfire_support = values[keys.index("Поддержка SLI/CrossFire")]
            self.power_connectors = values[keys.index("Разъёмы питания")]
            self.recommended_psu_watts = values[keys.index("Рекомендуемый блок питания")]
            self.cooling = values[keys.index("Охлаждение")]
            self.cooling_system_thickness = values[keys.index("Толщина системы охлаждения")]
            self.num_fans = values[keys.index("Количество вентиляторов")]
            self.video_card_length = values[keys.index("Длина видеокарты")]
            self.video_card_height = values[keys.index("Высота видеокарты")]
            self.low_profile = values[keys.index("Низкопрофильная (Low Profile)")]
            self.functional_features = values[keys.index("Функциональные особенности")]
            self.vga_or_d_sub = values[keys.index("VGA (D-Sub)")]
            self.dvi = values[keys.index("DVI")]
            self.hdmi = values[keys.index("HDMI")]
            self.hdmi_version = values[keys.index("Версия HDMI")]
            self.mini_hdmi = values[keys.index("mini HDMI")]
            self.display_port = values[keys.index("DisplayPort")]
            self.display_port_version = values[keys.index("Версия DisplayPort")]
            self.mini_display_port = values[keys.index("mini Display Port")]
            self.vesa_stereo = values[keys.index("VESA Stereo")]
            self.usb_type_c = values[keys.index("USB Type-C")]