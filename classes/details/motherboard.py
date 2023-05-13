# from detail import Detail

import re

class Motherboard:
    id = 0
    name = ""
    price = 0.0
    market_launch_date = 0
    processor_support = ""
    socket = ""
    chipset = ""
    form_factor = ""
    backlight = False
    memory_type = ""
    num_of_memory_slots = 0
    max_memory = 0
    memory_mode = ""
    max_memory_frequency = 0
    pci_express_version = ""
    total_pci_express_x16 = ""
    of_which_pci_express_2dot0_x16 = ""
    total_pci_express_x1 = ""
    of_which_pci_express_2dot0_x1 = ""
    total_pci_express_x4 = ""
    of_which_pci_express_2dot0_x4 = ""
    total_pci_express_x8 = ""
    of_which_pci_express_2dot0_x8 = ""
    pci = ""
    mdot2 = ""
    sata_3dot0 = ""
    sata_2dot0 = ""
    raid = ""
    slot_for_wifi_module = ""
    wifi = ""
    bluetooth = ""
    ethernet = ""
    integrated_graphics_support = False
    sli_or_crossfire_support = ""
    builtin_sound = ""
    sound_scheme = ""
    usb_2dot0_back_panel = 0
    usb_3dot2_gen1_type_a_5Gb_s_back_panel = 0
    usb_3dot2_gen2_type_a_10Gb_s_back_panel = 0
    usb_3dot2_gen1_type_c_5Gb_s_back_panel = 0
    usb_3dot2_gen2_type_c_10Gb_s_back_panel = 0
    usb_3dot2_gen2x2_20Gb_s_back_panel = 0
    usb_c_thunderbolt_3_back_panel = 0
    usb_c_thunderbolt_4_back_panel = 0
    s_or_pdif_digital_output = 0
    audio_3dot5_mm_jack = 0
    com_back_panel = 0
    lpt_back_panel = 0
    ps2 = 0
    display_port = 0
    mini_display_port = 0
    vga_or_dsub = 0
    dvi = 0
    hdmi = 0
    usb_2dot0_internal = 0
    usb_3dot2_gen1_type_a_5Gb_s_internal = 0
    usb_3dot2_gen2_type_a_10Gb_s_internal = 0
    usb_3dot2_gen1_type_c_5Gb_s_internal = 0
    usb_3dot2_gen2_type_c_10Gb_s_internal = 0
    usb_3dot2_gen2x2_20Gb_s_internal = 0
    thunderbolt3_internal = 0
    thunderbolt4_internal = 0
    s_or_pdif_digital_output_internal = 0
    com_internal = 0
    lpt_internal = 0
    cpu_fan_connectors = 0
    lss_connectors = 0
    case_fan_connectors = 0
    argb_5v_backlight_connectors = 0
    rgb_12v_backlight_connectors = 0
    builtin_connectors_description = ""
    length = 0.0
    width = 0.0
    def __init__(self, keys, values, descriptions, reading=False):
        if reading == False:
            self.name = values[keys.index("Название")]
            self.price = float(values[keys.index("Цена")].split()[0].replace(',', '.'))
            if "Дата выхода на рынок" in keys:
                self.market_launch_date = int(values[keys.index("Дата выхода на рынок")].split()[0])
            else:
                self.market_launch_date = None
            if "Поддержка процессоров" in keys:
                self.processor_support = values[keys.index("Поддержка процессоров")]
            else:
                self.processor_support = None
            if "Сокет" in keys:
                self.socket = values[keys.index("Сокет")]
            else:
                self.socket = None
            if "Чипсет" in keys:
                self.chipset = values[keys.index("Чипсет")]
            else:
                self.chipset = None
            if "Форм-фактор" in keys:
                form_factor = values[keys.index("Форм-фактор")]
                if form_factor == "mATX":
                    form_factor = "micro-ATX"
                self.form_factor = form_factor
            else:
                self.form_factor = None
            if "Подсветка" in keys:
                self.backlight = True if values[keys.index("Подсветка")] == "Yes" else False
            else:
                self.backlight = None
            if "Тип памяти" in keys:
                self.memory_type = values[keys.index("Тип памяти")]
            else:
                self.memory_type = None
            if "Количество слотов памяти" in keys:
                self.num_of_memory_slots = int(values[keys.index("Количество слотов памяти")].split()[0])
            else:
                self.num_of_memory_slots = None
            if "Максимальный объём памяти" in keys:
                self.max_memory = int(''.join(filter(str.isdigit, values[keys.index("Максимальный объём памяти")])))
            else:
                self.max_memory = None
            if "Режим памяти" in keys:
                self.memory_mode = values[keys.index("Режим памяти")]
            else:
                self.memory_mode = None
            if "Максимальная частота памяти" in keys:
                self.max_memory_frequency = int(values[keys.index("Максимальная частота памяти")].split()[0])
            else:
                self.max_memory_frequency = None
            if "Версия PCI Express" in keys:
                self.pci_express_version = values[keys.index("Версия PCI Express")]
            else:
                self.pci_express_version = None
            if "Всего PCI Express x16" in keys:
                self.total_pci_express_x16 = values[keys.index("Всего PCI Express x16")]
            else:
                self.total_pci_express_x16 = None
            if "Из них PCI Express 2.0 x16" in keys:
                self.of_which_pci_express_2dot0_x16 = values[keys.index("Из них PCI Express 2.0 x16")]
            else:
                self.of_which_pci_express_2dot0_x16 = None
            if "Всего PCI Express x1" in keys:
                self.total_pci_express_x1 = values[keys.index("Всего PCI Express x1")]
            else:
                self.total_pci_express_x1 = None
            if "Из них PCI Express 2.0 x1" in keys:
                self.of_which_pci_express_2dot0_x1 = values[keys.index("Из них PCI Express 2.0 x1")]
            else:
                self.of_which_pci_express_2dot0_x1 = None
            if "Всего PCI Express x4" in keys:
                self.total_pci_express_x4 = values[keys.index("Всего PCI Express x4")]
            else:
                self.total_pci_express_x4 = None
            if "Из них PCI Express 2.0 x4" in keys:
                self.of_which_pci_express_2dot0_x4 = values[keys.index("Из них PCI Express 2.0 x4")]
            else:
                self.of_which_pci_express_2dot0_x4 = None
            if "Всего PCI Express x8" in keys:
                self.total_pci_express_x8 = values[keys.index("Всего PCI Express x8")]
            else:
                self.total_pci_express_x8 = None
            if "Из них PCI Express 2.0 x8" in keys:
                self.of_which_pci_express_2dot0_x8 = values[keys.index("Из них PCI Express 2.0 x8")]
            else:
                self.of_which_pci_express_2dot0_x8 = None
            if "PCI" in keys:
                self.pci = values[keys.index("PCI")]
            else:
                self.pci = None
            if "M.2" in keys:
                self.mdot2 = values[keys.index("M.2")]
            else:
                self.mdot2 = None
            if "SATA 3.0" in keys:
                self.sata_3dot0 = values[keys.index("SATA 3.0")]
            else:
                self.sata_3dot0 = None
            if "SATA 2.0" in keys:
                self.sata_2dot0 = values[keys.index("SATA 2.0")]
            else:
                self.sata_2dot0 = None
            if "RAID" in keys:
                self.raid = values[keys.index("RAID")]
            else:
                self.raid = None
            if "Слот для модуля Wi-Fi" in keys:
                self.slot_for_wifi_module = values[keys.index("Слот для модуля Wi-Fi")]
            else:
                self.slot_for_wifi_module = None
            if "Wi-Fi" in keys:
                self.wifi = values[keys.index("Wi-Fi")]
            else:
                self.wifi = None
            if "Bluetooth" in keys:
                self.bluetooth = values[keys.index("Bluetooth")]
            else:
                self.bluetooth = None
            if "Ethernet" in keys:
                self.ethernet = values[keys.index("Ethernet")]
            else:
                self.ethernet = None
            if "Поддержка встроенной графики" in keys:
                self.integrated_graphics_support = True if values[keys.index("Поддержка встроенной графики")] == "Yes" else False
            else:
                self.integrated_graphics_support = None
            if "Поддержка SLi/CrossFire" in keys:
                self.sli_or_crossfire_support = values[keys.index("Поддержка SLi/CrossFire")]
            else:
                self.sli_or_crossfire_support = None
            if "Встроенный звук" in keys:
                self.builtin_sound = values[keys.index("Встроенный звук")]
            else:
                self.builtin_sound = None
            if "Звуковая схема" in keys:
                self.sound_scheme = values[keys.index("Звуковая схема")]
            else:
                self.sound_scheme = None
            if "Разъемы на задней панели_USB 2.0" in keys:
                self.usb_2dot0_back_panel = int(values[keys.index("Разъемы на задней панели_USB 2.0")]) if values[keys.index("Разъемы на задней панели_USB 2.0")] != "No" else 0
            else:
                self.usb_2dot0_back_panel = None
            if "Разъемы на задней панели_USB 3.2 Gen1 Type-A (5 Гбит/с)" in keys:
                self.usb_3dot2_gen1_type_a_5Gb_s_back_panel = int(values[keys.index("Разъемы на задней панели_USB 3.2 Gen1 Type-A (5 Гбит/с)")]) if values[keys.index("Разъемы на задней панели_USB 3.2 Gen1 Type-A (5 Гбит/с)")] != "No" else 0
            else:
                self.usb_3dot2_gen1_type_a_5Gb_s_back_panel = None
            if "Разъемы на задней панели_USB 3.2 Gen2 Type-A (10 Гбит/с)" in keys:
                self.usb_3dot2_gen2_type_a_10Gb_s_back_panel = int(values[keys.index("Разъемы на задней панели_USB 3.2 Gen2 Type-A (10 Гбит/с)")]) if values[keys.index("Разъемы на задней панели_USB 3.2 Gen2 Type-A (10 Гбит/с)")] != "No" else 0
            else:
                self.usb_3dot2_gen2_type_a_10Gb_s_back_panel = None
            if "Разъемы на задней панели_USB 3.2 Gen1 Type-C (5 Гбит/с)" in keys:
                self.usb_3dot2_gen1_type_c_5Gb_s_back_panel = int(values[keys.index("Разъемы на задней панели_USB 3.2 Gen1 Type-C (5 Гбит/с)")]) if values[keys.index("Разъемы на задней панели_USB 3.2 Gen1 Type-C (5 Гбит/с)")] != "No" else 0
            else:
                self.usb_3dot2_gen1_type_c_5Gb_s_back_panel = None
            if "Разъемы на задней панели_USB 3.2 Gen2 Type-C (10 Гбит/с)" in keys:
                self.usb_3dot2_gen2_type_c_10Gb_s_back_panel = int(values[keys.index("Разъемы на задней панели_USB 3.2 Gen2 Type-C (10 Гбит/с)")]) if values[keys.index("Разъемы на задней панели_USB 3.2 Gen2 Type-C (10 Гбит/с)")] != "No" else 0
            else:
                self.usb_3dot2_gen2_type_c_10Gb_s_back_panel = None
            if "Разъемы на задней панели_USB 3.2 Gen 2x2 (20 Гбит/с)" in keys:
                self.usb_3dot2_gen2x2_20Gb_s_back_panel = int(values[keys.index("Разъемы на задней панели_USB 3.2 Gen 2x2 (20 Гбит/с)")]) if values[keys.index("Разъемы на задней панели_USB 3.2 Gen 2x2 (20 Гбит/с)")] != "No" else 0
            else:
                self.usb_3dot2_gen2x2_20Gb_s_back_panel = None
            if "Разъемы на задней панели_USB-C (Thunderbolt 3)" in keys:
                self.usb_c_thunderbolt_3_back_panel = int(values[keys.index("Разъемы на задней панели_USB-C (Thunderbolt 3)")]) if values[keys.index("Разъемы на задней панели_USB-C (Thunderbolt 3)")] != "No" else 0
            else:
                self.usb_c_thunderbolt_3_back_panel = None
            if "Разъемы на задней панели_USB-C (Thunderbolt 4)" in keys:
                self.usb_c_thunderbolt_4_back_panel = int(values[keys.index("Разъемы на задней панели_USB-C (Thunderbolt 4)")]) if values[keys.index("Разъемы на задней панели_USB-C (Thunderbolt 4)")] != "No" else 0
            else:
                self.usb_c_thunderbolt_4_back_panel = None
            if "Разъемы на задней панели_Цифровой выход S/PDIF" in keys:
                self.s_or_pdif_digital_output = int(values[keys.index("Разъемы на задней панели_Цифровой выход S/PDIF")]) if values[keys.index("Разъемы на задней панели_Цифровой выход S/PDIF")] != "No" else 0
            else:
                self.s_or_pdif_digital_output = None
            if "Разъемы на задней панели_Аудио (3.5 мм jack)" in keys:
                self.audio_3dot5_mm_jack = int(values[keys.index("Разъемы на задней панели_Аудио (3.5 мм jack)")]) if values[keys.index("Разъемы на задней панели_Аудио (3.5 мм jack)")] != "No" else 0
            else:
                self.audio_3dot5_mm_jack = None
            if "Разъемы на задней панели_COM" in keys:
                self.com_back_panel = int(values[keys.index("Разъемы на задней панели_COM")]) if values[keys.index("Разъемы на задней панели_COM")] != "No" else 0
            else:
                self.com_back_panel = None
            if "Разъемы на задней панели_LPT" in keys:
                self.lpt_back_panel = int(values[keys.index("Разъемы на задней панели_LPT")]) if values[keys.index("Разъемы на задней панели_LPT")] != "No" else 0
            else:
                self.lpt_back_panel = None
            if "Разъемы на задней панели_PS/2" in keys:
                self.ps2 = int(values[keys.index("Разъемы на задней панели_PS/2")]) if values[keys.index("Разъемы на задней панели_PS/2")] != "No" else 0
            else:
                self.ps2 = None
            if "Разъемы на задней панели_DisplayPort" in keys:
                self.display_port = int(values[keys.index("Разъемы на задней панели_DisplayPort")]) if values[keys.index("Разъемы на задней панели_DisplayPort")] != "No" else 0
            else:
                self.display_port = None
            if "Разъемы на задней панели_mini DisplayPort" in keys:
                self.mini_display_port = int(values[keys.index("Разъемы на задней панели_mini DisplayPort")]) if values[keys.index("Разъемы на задней панели_mini DisplayPort")] != "No" else 0
            else:
                self.mini_display_port = None
            if "Разъемы на задней панели_VGA (D-Sub)" in keys:
                self.vga_or_dsub = int(values[keys.index("Разъемы на задней панели_VGA (D-Sub)")]) if values[keys.index("Разъемы на задней панели_VGA (D-Sub)")] != "No" else 0
            else:
                self.vga_or_dsub = None
            if "Разъемы на задней панели_DVI" in keys:
                self.dvi = int(values[keys.index("Разъемы на задней панели_DVI")]) if values[keys.index("Разъемы на задней панели_DVI")] != "No" else 0
            else:
                self.dvi = None
            if "Разъемы на задней панели_HDMI" in keys:
                self.hdmi = int(values[keys.index("Разъемы на задней панели_HDMI")]) if values[keys.index("Разъемы на задней панели_HDMI")] != "No" else 0
            else:
                self.hdmi = None
            if "Внутренние разъемы_USB 2.0" in keys:
                self.usb_2dot0_internal = int(values[keys.index("Внутренние разъемы_USB 2.0")]) if values[keys.index("Внутренние разъемы_USB 2.0")] != "No" else 0
            else:
                self.usb_2dot0_internal = None
            if "Внутренние разъемы_USB 3.2 Gen1 Type-A (5 Гбит/с)" in keys:
                self.usb_3dot2_gen1_type_a_5Gb_s_internal = int(values[keys.index("Внутренние разъемы_USB 3.2 Gen1 Type-A (5 Гбит/с)")]) if values[keys.index("Внутренние разъемы_USB 3.2 Gen1 Type-A (5 Гбит/с)")] != "No" else 0
            else:
                self.usb_3dot2_gen1_type_a_5Gb_s_internal = None
            if "Внутренние разъемы_USB 3.2 Gen2 Type-A (10 Гбит/с)" in keys:
                self.usb_3dot2_gen2_type_a_10Gb_s_internal = int(values[keys.index("Внутренние разъемы_USB 3.2 Gen2 Type-A (10 Гбит/с)")]) if values[keys.index("Внутренние разъемы_USB 3.2 Gen2 Type-A (10 Гбит/с)")] != "No" else 0
            else:
                self.usb_3dot2_gen2_type_a_10Gb_s_internal = None
            if "Внутренние разъемы_USB 3.2 Gen1 Type-C (5 Гбит/с)" in keys:
                self.usb_3dot2_gen1_type_c_5Gb_s_internal = int(values[keys.index("Внутренние разъемы_USB 3.2 Gen1 Type-C (5 Гбит/с)")]) if values[keys.index("Внутренние разъемы_USB 3.2 Gen1 Type-C (5 Гбит/с)")] != "No" else 0
            else:
                self.usb_3dot2_gen1_type_c_5Gb_s_internal = None
            if "Внутренние разъемы_USB 3.2 Gen2 Type-C (10 Гбит/с)" in keys:
                self.usb_3dot2_gen2_type_c_10Gb_s_internal = int(values[keys.index("Внутренние разъемы_USB 3.2 Gen2 Type-C (10 Гбит/с)")]) if values[keys.index("Внутренние разъемы_USB 3.2 Gen2 Type-C (10 Гбит/с)")] != "No" else 0
            else:
                self.usb_3dot2_gen2_type_c_10Gb_s_internal = None
            if "Внутренние разъемы_USB 3.2 Gen 2x2 (20 Гбит/с)" in keys:
                self.usb_3dot2_gen2x2_20Gb_s_internal = int(values[keys.index("Внутренние разъемы_USB 3.2 Gen 2x2 (20 Гбит/с)")]) if values[keys.index("Внутренние разъемы_USB 3.2 Gen 2x2 (20 Гбит/с)")] != "No" else 0
            else:
                self.usb_3dot2_gen2x2_20Gb_s_internal = None
            if "Внутренние разъемы_Thunderbolt 3" in keys:
                self.thunderbolt3_internal = int(values[keys.index("Внутренние разъемы_Thunderbolt 3")]) if values[keys.index("Внутренние разъемы_Thunderbolt 3")] != "No" else 0
            else:
                self.thunderbolt3_internal = None
            if "Внутренние разъемы_Thunderbolt 4" in keys:
                self.thunderbolt4_internal = int(values[keys.index("Внутренние разъемы_Thunderbolt 4")]) if values[keys.index("Внутренние разъемы_Thunderbolt 4")] != "No" else 0
            else:
                self.thunderbolt4_internal = None
            if "Внутренние разъемы_Цифровой выход S/PDIF" in keys:
                self.s_or_pdif_digital_output_internal = int(values[keys.index("Внутренние разъемы_Цифровой выход S/PDIF")]) if values[keys.index("Внутренние разъемы_Цифровой выход S/PDIF")] != "No" else 0
            else:
                self.s_or_pdif_digital_output_internal = None
            if "Внутренние разъемы_COM" in keys:
                self.com_internal = int(values[keys.index("Внутренние разъемы_COM")]) if values[keys.index("Внутренние разъемы_COM")] != "No" else 0
            else:
                self.com_internal = None
            if "Внутренние разъемы_LPT" in keys:
                self.lpt_internal = int(values[keys.index("Внутренние разъемы_LPT")]) if values[keys.index("Внутренние разъемы_LPT")] != "No" else 0
            else:
                self.lpt_internal = None
            if "Внутренние разъемы_Разъемы для вентилятора ЦП" in keys:
                self.cpu_fan_connectors = int(values[keys.index("Внутренние разъемы_Разъемы для вентилятора ЦП")]) if values[keys.index("Внутренние разъемы_Разъемы для вентилятора ЦП")] != "No" else 0
            else:
                self.cpu_fan_connectors = None
            if "Внутренние разъемы_Разъемы для СЖО" in keys:
                self.lss_connectors = int(values[keys.index("Внутренние разъемы_Разъемы для СЖО")]) if values[keys.index("Внутренние разъемы_Разъемы для СЖО")] != "No" else 0
            else:
                self.lss_connectors = None
            if "Внутренние разъемы_Разъемы для корпусных вентиляторов" in keys:
                self.case_fan_connectors = int(values[keys.index("Внутренние разъемы_Разъемы для корпусных вентиляторов")]) if values[keys.index("Внутренние разъемы_Разъемы для корпусных вентиляторов")] != "No" else 0
            else:
                self.case_fan_connectors = None
            if "Внутренние разъемы_Разъемы для подсветки ARGB 5В" in keys:
                self.argb_5v_backlight_connectors = int(values[keys.index("Внутренние разъемы_Разъемы для подсветки ARGB 5В")]) if values[keys.index("Внутренние разъемы_Разъемы для подсветки ARGB 5В")] != "No" else 0
            else:
                self.argb_5v_backlight_connectors = None
            if "Внутренние разъемы_Разъемы для подсветки RGB 12В" in keys:
                self.rgb_12v_backlight_connectors = int(values[keys.index("Внутренние разъемы_Разъемы для подсветки RGB 12В")]) if values[keys.index("Внутренние разъемы_Разъемы для подсветки RGB 12В")] != "No" else 0
            else:
                self.rgb_12v_backlight_connectors = None
            if "Описание внутренних разъемов" in keys:
                self.builtin_connectors_description = values[keys.index("Описание внутренних разъемов")]
            else:
                self.builtin_connectors_description = None
            if "Длина" in keys:
                self.length = float(values[keys.index("Длина")].split()[0])
            else:
                self.length = None
            if "Ширина" in keys:
                self.width = float(values[keys.index("Ширина")].split()[0])
            else:
                self.width = None
        elif reading == True:
            self.id = values[keys.index("Id")]-1
            self.name = values[keys.index("Название")]
            self.price = values[keys.index("Цена")]
            self.market_launch_date = values[keys.index("Дата выхода на рынок")]
            self.processor_support = values[keys.index("Поддержка процессоров")]
            self.socket = values[keys.index("Сокет")]
            self.chipset = values[keys.index("Чипсет")]
            self.form_factor = values[keys.index("Форм-фактор")]
            self.backlight = values[keys.index("Подсветка")]
            self.memory_type = values[keys.index("Тип памяти")]
            self.num_of_memory_slots = values[keys.index("Количество слотов памяти")]
            self.max_memory = values[keys.index("Максимальный объём памяти")]
            self.memory_mode = values[keys.index("Режим памяти")]
            self.max_memory_frequency = values[keys.index("Максимальная частота памяти")]
            self.pci_express_version = values[keys.index("Версия PCI Express")]
            self.total_pci_express_x16 = values[keys.index("Всего PCI Express x16")]
            self.of_which_pci_express_2dot0_x16 = values[keys.index("Из них PCI Express 2.0 x16")]
            self.total_pci_express_x1 = values[keys.index("Всего PCI Express x1")]
            self.of_which_pci_express_2dot0_x1 = values[keys.index("Из них PCI Express 2.0 x1")]
            self.total_pci_express_x4 = values[keys.index("Всего PCI Express x4")]
            self.of_which_pci_express_2dot0_x4 = values[keys.index("Из них PCI Express 2.0 x4")]
            self.total_pci_express_x8 = values[keys.index("Всего PCI Express x8")]
            self.of_which_pci_express_2dot0_x8 = values[keys.index("Из них PCI Express 2.0 x8")]
            self.pci = values[keys.index("PCI")]
            self.mdot2 = values[keys.index("M.2")]
            self.sata_3dot0 = values[keys.index("SATA 3.0")]
            self.sata_2dot0 = values[keys.index("SATA 2.0")]
            self.raid = values[keys.index("RAID")]
            self.slot_for_wifi_module = values[keys.index("Слот для модуля Wi-Fi")]
            self.wifi = values[keys.index("Wi-Fi")]
            self.bluetooth = values[keys.index("Bluetooth")]
            self.ethernet = values[keys.index("Ethernet")]
            self.integrated_graphics_support = values[keys.index("Поддержка встроенной графики")]
            self.sli_or_crossfire_support = values[keys.index("Поддержка SLi/CrossFire")]
            self.builtin_sound = values[keys.index("Встроенный звук")]
            self.sound_scheme = values[keys.index("Звуковая схема")]
            self.usb_2dot0_back_panel = values[keys.index("Разъемы на задней панели_USB 2.0")]
            self.usb_3dot2_gen1_type_a_5Gb_s_back_panel = values[keys.index("Разъемы на задней панели_USB 3.2 Gen1 Type-A (5 Гбит/с)")]
            self.usb_3dot2_gen2_type_a_10Gb_s_back_panel = values[keys.index("Разъемы на задней панели_USB 3.2 Gen2 Type-A (10 Гбит/с)")]
            self.usb_3dot2_gen1_type_c_5Gb_s_back_panel = values[keys.index("Разъемы на задней панели_USB 3.2 Gen1 Type-C (5 Гбит/с)")]
            self.usb_3dot2_gen2_type_c_10Gb_s_back_panel = values[keys.index("Разъемы на задней панели_USB 3.2 Gen2 Type-C (10 Гбит/с)")]
            self.usb_3dot2_gen2x2_20Gb_s_back_panel = values[keys.index("Разъемы на задней панели_USB 3.2 Gen 2x2 (20 Гбит/с)")]
            self.usb_c_thunderbolt_3_back_panel = values[keys.index("Разъемы на задней панели_USB-C (Thunderbolt 3)")]
            self.usb_c_thunderbolt_4_back_panel = values[keys.index("Разъемы на задней панели_USB-C (Thunderbolt 4)")]
            self.s_or_pdif_digital_output = values[keys.index("Разъемы на задней панели_Цифровой выход S/PDIF")]
            self.audio_3dot5_mm_jack = values[keys.index("Разъемы на задней панели_Аудио (3.5 мм jack)")]
            self.com_back_panel = values[keys.index("Разъемы на задней панели_COM")]
            self.lpt_back_panel = values[keys.index("Разъемы на задней панели_LPT")]
            self.ps2 = values[keys.index("Разъемы на задней панели_PS/2")]
            self.display_port = values[keys.index("Разъемы на задней панели_DisplayPort")]
            self.mini_display_port = values[keys.index("Разъемы на задней панели_mini DisplayPort")]
            self.vga_or_dsub = values[keys.index("Разъемы на задней панели_VGA (D-Sub)")]
            self.dvi = values[keys.index("Разъемы на задней панели_DVI")]
            self.hdmi = values[keys.index("Разъемы на задней панели_HDMI")]
            self.usb_2dot0_internal = values[keys.index("Внутренние разъемы_USB 2.0")]
            self.usb_3dot2_gen1_type_a_5Gb_s_internal = values[keys.index("Внутренние разъемы_USB 3.2 Gen1 Type-A (5 Гбит/с)")]
            self.usb_3dot2_gen2_type_a_10Gb_s_internal = values[keys.index("Внутренние разъемы_USB 3.2 Gen2 Type-A (10 Гбит/с)")]
            self.usb_3dot2_gen1_type_c_5Gb_s_internal = values[keys.index("Внутренние разъемы_USB 3.2 Gen1 Type-C (5 Гбит/с)")]
            self.usb_3dot2_gen2_type_c_10Gb_s_internal = values[keys.index("Внутренние разъемы_USB 3.2 Gen2 Type-C (10 Гбит/с)")]
            self.usb_3dot2_gen2x2_20Gb_s_internal = values[keys.index("Внутренние разъемы_USB 3.2 Gen 2x2 (20 Гбит/с)")]
            self.thunderbolt3_internal = values[keys.index("Внутренние разъемы_Thunderbolt 3")]
            self.thunderbolt4_internal = values[keys.index("Внутренние разъемы_Thunderbolt 4")]
            self.s_or_pdif_digital_output_internal = values[keys.index("Внутренние разъемы_Цифровой выход S/PDIF")]
            self.com_internal = values[keys.index("Внутренние разъемы_COM")]
            self.lpt_internal = values[keys.index("Внутренние разъемы_LPT")]
            self.cpu_fan_connectors = values[keys.index("Внутренние разъемы_Разъемы для вентилятора ЦП")]
            self.lss_connectors = values[keys.index("Внутренние разъемы_Разъемы для СЖО")]
            self.case_fan_connectors = values[keys.index("Внутренние разъемы_Разъемы для корпусных вентиляторов")]
            self.argb_5v_backlight_connectors = values[keys.index("Внутренние разъемы_Разъемы для подсветки ARGB 5В")]
            self.rgb_12v_backlight_connectors = values[keys.index("Внутренние разъемы_Разъемы для подсветки RGB 12В")]
            self.builtin_connectors_description = values[keys.index("Описание внутренних разъемов")]
            self.length = values[keys.index("Длина")]
            self.width = values[keys.index("Ширина")]