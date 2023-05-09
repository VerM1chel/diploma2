"https://ru.wikipedia.org/wiki/%D0%9A%D0%BB%D0%B0%D1%81%D1%81%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D1%8F_%D0%BA%D0%BE%D0%BC%D0%BF%D1%8C%D1%8E%D1%82%D0%B5%D1%80%D0%BD%D1%8B%D1%85_%D0%B8%D0%B3%D1%80#%D0%9F%D0%BE_%D0%9A%D1%80%D0%BE%D1%83%D1%84%D0%BE%D1%80%D0%B4%D1%83_(1984)"
games_description = ["""Поиск правильного решения на основе перебора вариантов. Противодействие отсутствует. Игровая среда — абстрактная. Игровая семантика — выхолощенная.""",
    """Имитация шахмат, шашек, го, реверси и т. п. Игровая среда — абстрактная. Игровая семантика — условная.""",
    """Имитация азартных игр на поиск оптимальной вероятностной стратегии.""",
    """Игры на просчет последствий и рисков, распределение и торговля ресурсами. Игровая среда — текстовый диалог.""",
    """Управление транспортом в режиме реального времени""",
    """Имитация игр с мячом. Игра заключается в расчете траекторий. """,
    """Игра на нанесение и избегание урона. Имитируют обзор от первого лица""",
    """Игра на нанесение и избегание урона. Тренажеры для военных летчиков, операторов танков и т. п.""",
    """Игра на нанесение и избегание урона. Тренажеры для военных летчиков, операторов танков и т. п.""",
    """Нанесение урона с помощью рук, ног, холодного оружия""",
    """Прохождение лабиринтов с избеганием сильных врагов и преследованием слабых.""",
    """Игры с неполнотой знаний об игровой среде и множеством препятствий. Вид сверху. Акцент на избегании, борьбе и локомоторных задачах.""",
    """Игры с неполнотой знаний об игровой среде и множеством препятствий. Вид от первого лица. Необходимость моделировать схему игрового пространства.""",
    """Игры с неполнотой знаний об игровой среде и множеством препятствий. Текстовое представление.""",
    """Игры с неполнотой знаний об игровой среде и множеством препятствий. Текстовое представление. Акцент на расследовании ситуации, исследование ветвлений задачи.""",
    """Противостояние неодушевленной динамической среде. Предполагает простые регламентированные реакции.""",
    """Игра с признаками конвейера и конструктивной игры (поиск оптимального решения задачи).""",
    """Текстовые игры в виде диалога. Элементы семантической игры. Элементы игры самоанализа.""",
    """Игры на освоение технологического процесса."""]

games = {"Головоломки": ([],games_description[0]), "Настольные интеллектуальные игры в компьютерном варианте": ([],games_description[1]),
"Азартные шансовые игры": ([],games_description[2]), "Управленческо-экономические": ([],games_description[3]),
 "Спортивные игры": (["Локомоторные спортивные игры", "Баллистические спортивные игры"],games_description[4]),
 "Военные игры": (["Диарамные военные игры", "Локомоторные военные игры", "Баллистические военные игры"],games_description[5]),
 "Единоборства":([],games_description[6]), "Игры преследования-избегания": ([],games_description[7]),
 "Авантюрные игры": (["Зрительный лабиринт", "Диарамный лабиринт", "Логико-пространственный лабиринт", "Детектив"],games_description[8]),
 "Конвейерные игры": ([],games_description[9]), "Конструктивно-динамические игры": ([],games_description[10]), "Диалоговые познавательные окна": ([],games_description[11]),
 "Учебно-технологические центры": ([],games_description[12])}


"""
Гонки
Экшен
Ролевые
Квесты
Драки
Аркады
Спортивные
Стратегии
Симулятор
Приключения
Хоррор
Выживание
Стелс
Шутер
Другое
"""




video_editing = {}
streaming = {} # надо немного больше ядер процессора и оперативки (ведь обычно открыто много окошек) + наличие 2х мониторов (вообще -- игровой комп подходит) (посмотреть карту видеозахвата)

# https://virtualrift.net/vybor-pk-dlya-vr-pochemu-takie-vysokie-trebovaniya-k-zhelezu
# https://maff.io/vr_dlya_dizayna/#%D0%9A%D0%B0%D0%BA%D0%B8%D0%B5_%D0%B7%D0%B0%D0%B4%D0%B0%D1%87%D0%B8_%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D1%82_VR_%D0%B4%D0%BB%D1%8F_%D0%B4%D0%B8%D0%B7%D0%B0%D0%B9%D0%BD%D0%B0
vr = {"работы с графикой высокого разрешения (NVIDIA Holodeck)", "Визуальный редактор виртуальной реальности (Sketchbox)",
      "Интеграция с традиционными программами (The Wild)", "трехмерная конференц-связь (STAGE)", "Дополненная реальность для рабочего места (Spatial)"}

software_development = {"Фронтенд разработка": [], "Бэкенд разработка": [], "Мобильная разработка": [], "Сетевое администрирование": [],
                        "Десктопная разработка": [], "Наукоёмкая разработка (специализированное ПО или сервисы)": [],
                        "Data Science": [], "Разработка игр": [], "интернет вещей (IoT)": [],
                        "Программирование встроенных систем (embedded) и микроконтроллеров": [], "Автоматизация тестирования": [],
                        "Программирование для финансовых и бухгалтерских продуктов": [], "Программирование баз данных": [],
                        "другие": []}

graphics_design = {"графический дизайн в визуальной идентификации бренда": [], "графический дизайн публикаций": [],
                    "графический дизайн пользовательских интерфейсов (UI)": [], "рекламная графика": [],
                    "графический дизайн окружения": [], "искусство и иллюстрации в графическом дизайне": [],
                    "графический дизайн упаковок": [], "моушн-дизайн": [], "Графический дизайн пространств": [], "Графический дизайн цифровых коммуникаций": []}

min_assembly_3d = {"cpu": "4 ядра от 3 GHz",
            "ram": "8 Гб",
            "gpu": "с поддержкой OpenGL 4.3 на 4 Гб памяти",
            "motherboard": "",
            "ssd_hdd": "минимум 50 Гб",
            "power": "",
            "cooling": "",
            "case": ""}

optimal_assembly_3d = {"cpu": "AMD Ryzen 9 5950X",
            "ram": "32 Гб (Patriot Viper Steel — 2х16 Гб)",
            "gpu": "NVidia RTX 3080 Ti на 12 Гб",
            "motherboard": "MSI MPG B550 GAMING CARBON WIFI",
            "ssd_hdd": "SSD Samsung 980 Pro 1 TB и HDD Seagate Backup Plus Hub",
            "power": "Deepcool DQ850",
            "cooling": "MSI MAG CORELIQUID 360R",
            "case": "Cooler Master MasterBox MB511 RGB"}

ideal_assembly_3d = {"cpu": "AMD Ryzen 7 3700X.",
            "ram": "32 Гб (Corsair Vengeance LPX — 2х16 Гб)",
            "gpu": "GeForce RTX 2070",
            "motherboard": "GIGABYTE X570 GAMING X",
            "ssd_hdd": "SSD Samsung 970 PRO",
            "power": "Corsair CX550",
            "cooling": "AMD Wraith Prism",
            "case": "Phanteks Full Tower Case ATX"}
modeling_3d = {"3d printing": [], "science": [], "architecture": [], "mechanical_engineering": [],
               "networks of engineering and technological support (pipelines, electrics)": [], "web-design": [],
               "VR visualization of interiors": [], "Landscape modeling": [], "Skinning": []}

surfing = {}
office = {}

# https://habr.com/ru/company/bimeister/blog/663048/
CAD = {"CAD (Computer-aided design) - системные комплексы для проектирования",
       "CAE (Computer-aided engineering) - современные системы инженерного анализа",
       "CAM (Computer-aided manufacturing) – прописывания алгоритма действий станков с ЧПУ"}
sound_recording = {}
media_center = {} # 'nj jabcysq

# https://galtsystems.com/blog/start/osnovnye_vidy_serverov_naznachenie_i_osobennosti/
# Классификация серверов по назначению
server_by_usage = {"Сервер рабочей группы", "Сервер контроллер домена", "Прокси сервер", "Сервер электронной почты",
          "Веб сервер", "Терминальный сервер", "Сервер базы данных", "Серверы приложений", "Брандмауэр(Файрволл)",
          "Сервер DHCP", "Сервер FTP",
          "Принт-сервер", "Домашний сервер"}
# Классификация серверов по классу
server_by_classification = {"Серверы начального уровня (Entry-level server)", "Серверы для рабочих групп (Workgroup-level server)",
                            "Серверы уровня департамента (Department-level server)", "Серверы уровня предприятия (Enterprise-level server)"}
# Классификация серверов по типу серверного шасси
server_by_shassie = {"Стоечные серверы (Rack-серверы)", "Блейд-серверы", 'Серверы башенного типа "Tower"'}


"https://ihackline.com/2019/06/15/hackintosh-vybor-hardware/"
cpu_description = """
1) Только Intel! Отлично подходят любые процессоры из линейки: i3 / i5 / i7 / i9
2) Для всех конфигураций на процессорах Pentium, Rocket Lake, Alder Lake - наличие дискретной видеокарты обязательно!
3) Чипсет Х79, С602, X99 не рекомендуется
4) Очень желательно, иметь также наличие встроенное графики (для технологии Intel Quick Sync Video. Позволяет быстрее и эффективней обрабатывать видео, а также нужна для интерфейса самой macOS и множества профессиональных программ)
5) Celeron / Atom -- не подходят
                     """
motherboard_description = """
Вообще, подходят любые чипсеты любых производителей, однако есть возможность брака
1) Подходят: Asus / Asrock / Gigabyte / MSI
2) Чипсеты: H110 / B150 / Z170 / B250 / Z270 / H310 / B360/ B365 / H370 / Z370 / Z390 / X299 / H410 / H470 / Z490 / H510 / B560 / H570 / Z590 / H610 / B660 / H670 / Z690 / Z790
"""

gpu_description = """
1) Видеокарта должна быть НЕ Nvidia (цитата: "Начиная с 10.13 High Sierra, Nvidia Fermi потеряли поддержку. Для поколения Nvidia GTX 9XX и 10XX максимум - 10.13.6 / для поколения Nvidia GTX 20XX - поддержки нет!"
2) Подходящие видеокарты AMD RADEON (желательно Sapphire): RX 550 / RX 560 / RX 570 / RX 580 / RX 590 / серия PRO / Vega 56 / Vega 64 / Vega FE / 5500 XT / 5600 XT / 5700 XT / 6600 XT / 6800 XT / 6900 XT / 6650 XT / 6950 XT
3) Также с поправкой подходят (Редко, но бывают проблемы именно у этих производителей): Asus / MSI / Gigabyte
"""

ssd_description = """
1) Работают с "повреждённым" TRIM (т.е. либо не включать TRIM в системе, либо использовать как хранилище данных, в ином случае с включённым TRIM будет долгая загрузка системы):
Samsung 950 Pro, Samsung 960 Evo/Pro, Samsung 970 Evo/Pro
2) Работают хорошо с включённым TRIM:
Western Digital Blue SN550, Western Digital Black SN700, Western Digital Black SN720, Western Digital Black SN750 (aka SanDisk Extreme PRO),
Western Digital Black SN850 (need more tests), Intel 760p (including OEM models, e.g. SSDPEMKF512G8), Crucial P1 1TB NVME (SM2263EN) (need more tests)
3) Работают хорошо с включённым TRIM (SATA):
SATA PLEXTOR M5Pro, SATA Samsung 850 PRO, SATA Samsung 870 EVO 
4) Работают хорошо с включённым TRIM (Unbranded SSDs):
KingDian S280, Kingchuxing 512GB
5) Не совместимые с IONVMeFamily (умирают под большой нагрузкой):
GIGABYTE 512 GB M.2 PCIe SSD (e.g. GP-GSM2NE8512GNTD), ADATA Swordfish 2 TB M.2-2280, SK Hynix HFS001TD9TNG-L5B0B, 
Samsung PM981 models, Micron 2200V MTFDHBA512TCK, Asgard AN3+ (STAR1000P)"""

hdd_description = "Если дополнительно нужен жесткий диск, то на этом сайте можно найти самые надежные: https://www.backblaze.com/blog/hard-drive-stats-for-2018/"

ram_description = """
1) Производитель не имеет никакого значения. Частоты и тайминги естественно влияют на аппаратно-программное быстродействие
2) Для базового использования – 1Gb RAM на одно ядро CPU. Т.е например на 8 потоков CPU, 8Gb RAM
3) Для хорошей производительности – 2Gb RAM на одно ядро CPU. Т.е на теже 8 потоков CPU, уже 16Gb RAM
"""

power_description = "Рассчитывается на это сайте https://outervision.com/power-supply-calculator"

cooling_description = "Можно любые, но в идеале: Be Quiet (эталон тишины и отличной эффективности) / Noctua / Cooler Master"

case_description = "Corsair / Cooler Master / Fractal Designe / Be Quiet"

hackintosh = {"cpu_description": cpu_description,
              "motherboard_description": motherboard_description,
              "gpu_description": gpu_description,
              "ssd_description": ssd_description,
              "hdd_description": hdd_description,
              "ram_description": ram_description,
              "power_description": power_description,
              "cooling_description": cooling_description,
              "case_description": case_description}

# Как я понял, хакинтош -- это суперкомп с MacOS. Используется в том числе и в категориях выше. И тогда, когда использование макбука нецелесообразно (например, при рендере 4К видео)
# https://wylsa.com/hackintosh-sierra/