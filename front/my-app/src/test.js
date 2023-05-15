import React, { useState } from 'react';


// АВТОРИЗАЦИЯ
function LoginModal(props) {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    function handleUsernameChange(event) {
        setUsername(event.target.value);
    }

    function handlePasswordChange(event) {
        setPassword(event.target.value);
    }

    function handleLogin(event) {
        // Тут будет функционал для проверки логина и пароля
        // Если логин и пароль верны, можно закрыть модальное окно и выполнить переход на другую страницу, иначе -- выводим сообщение об ошибке
    }

    function handleClose(event) {
        // Закрываем модальное окно
        props.onClose();
    }
    return (
        <div style={{ position: "fixed", top: 0, left: 0, right: 0, bottom: 0, backgroundColor: "rgba(0, 0, 0, 0.5)", zIndex: 999 }}>
            <div style={{ position: "absolute", top: "50%", left: "50%", transform: "translate(-50%, -50%)", backgroundColor: "#fff", padding: "20px", borderRadius: "10px" }}>
                <h2>Авторизация</h2>
                <label htmlFor="username">Логин:</label>
                <input type="text" id="username" value={username} onChange={handleUsernameChange} />
                <br />
                <label htmlFor="password">Пароль:</label>
                <input type="password" id="password" value={password} onChange={handlePasswordChange} />
                <br />
                <button onClick={handleLogin}>Войти</button>
                <button onClick={handleClose}>Отмена</button>
            </div>
        </div>
    );
}


function App() {
    const [selectedItem, setSelectedItem] = useState("");
    const [secondListItems, setSecondListItems] = useState([]);

    const handleSelect = (e) => {
        const selectedValue = e.target.value;
        setSelectedItem(selectedValue);

        // определяем значения для второго списка в зависимости от выбранного элемента первого списка
        switch (selectedValue) {
            case "games":
                setSecondListItems(["World of Warcraft", "DOTA 2", "Minecraft"]);
                break;
            case "vr":
                setSecondListItems(["Visual Studio Code", "Sublime Text", "Atom", "aboba", "vp", "nice", "wp"]);
                break;
            case "it":
                setSecondListItems(["Photoshop1", "Sketch2", "Figma3"]);
                break;
            case "design":
                setSecondListItems(["Photoshop", "Sketch", "Figma"]);
                break;
            case "3d":
                setSecondListItems(["Photoshop4", "Sketch", "Figma"]);
                break;
            case "server":
                setSecondListItems(["Photoshop5", "Sketch", "Figma"]);
                break;
            case "video-audio":
                setSecondListItems(["Photoshop6", "Sketch", "Figma"]);
                break;
            case "science":
                setSecondListItems(["Photoshop7", "Sketch", "Figma"]);
                break;
            case "medicine":
                setSecondListItems(["Photoshop8", "Sketch", "Figma"]);
                break;
            case "networking":
                setSecondListItems(["Photoshop9", "Sketch", "Figma"]);
                break;
            case "office":
                setSecondListItems(["Photoshop10", "Sketch", "Figma"]);
                break;
            case "other":
                setSecondListItems(["Photoshop11", "Sketch", "Figma"]);
                break;
            default:
                setSecondListItems([]);
        }
    };

    const [selectedSecondItem, setSelectedSecondItem] = useState("");

    const handleSecondSelect = (e) => {
        const selectedValue = e.target.value;
        setSelectedSecondItem(selectedValue);
    };
    //_______________________________________________
    const [cpu, setCpu] = useState('');
    const [cooler, setCooler] = useState('');
    const [motherboard, setMotherboard] = useState('');
    const [ram, setRam] = useState('');
    const [gpu, setGpu] = useState('');
    const [ssd, setSsd] = useState('');
    const [hdd, setHdd] = useState('');
    const [power, setPower] = useState('');
    const [casePC, setCasePC] = useState('');


    const [ramSize, setRamSize] = useState('');
    const [ramPrice, setRamPrice] = useState('');
    //const [gpuSize, setGpuSize] = useState('');
    //const [gpuPrice, setGpuPrice] = useState('');
    //const [ssdSize, setSsdSize] = useState('');
    //const [ssdPrice, setSsdPrice] = useState('');
    //const [hddSize, setHddSize] = useState('');
    //const [hddPrice, setHddPrice] = useState('');
    //const [powerSize, setPowerSize] = useState('');
    //const [powerPrice, setPowerPrice] = useState('');
    //const [caseSize, setCaseSize] = useState('');
    //const [casePrice, setCasePrice] = useState('');

    //const handleCpuChange = (event) => {
    //    setCpu(event.target.value);
    //};

    //const handleCoolerChange = (event) => {
    //    setCooler(event.target.value);
    //};

    //const handleMotherboardChange = (event) => {
    //    setMotherboard(event.target.value);
    //};

    //const handleRamChange = (event) => {
    //    setRam(event.target.value);
    //};

    //const handleGraphicsCardChange = (event) => {
    //    setGpu(event.target.value);
    //};

    //const handleSsdChange = (event) => {
    //    setSsd(event.target.value);
    //};

    //const handleHddChange = (event) => {
    //    setHdd(event.target.value);
    //};

    //const handlePowerChange = (event) => {
    //    setPower(event.target.value);
    //};

    //const handlePowerChange = (event) => {
    //    setCasePC(event.target.value);
    //};


    //const handleCaseChange = (event) => {
    //    setCasePrice(event.target.value);
    //};

    const handleRamSizeChange = (event) => {
        setRamSize(event.target.value);
    };

    const handleRamPriceChange = (event) => {
        setRamPrice(event.target.value);
    };

    //const handleGraphicsCardSizeChange = (event) => {
    //    setGpuSize(event.target.value);
    //};

    //const handleGraphicsCardPriceChange = (event) => {
    //    setGpuPrice(event.target.value);
    //};

    //const handleSsdSizeChange = (event) => {
    //    setSsdSize(event.target.value);
    //};

    //const handleSsdPriceChange = (event) => {
    //    setSsdPrice(event.target.value);
    //};

    //const handleHddSizeChange = (event) => {
    //    setHddSize(event.target.value);
    //};

    //const handleHddPriceChange = (event) => {
    //    setHddPrice(event.target.value);
    //};

    //const handlePowerSupplySizeChange = (event) => {
    //    setPowerSize(event.target.value);
    //};

    //const handlePowerSupplyPriceChange = (event) => {
    //    setPowerPrice(event.target.value);
    //};

    //const handleCaseSizeChange = (event) => {
    //    setCaseSize(event.target.value);
    //};

    //const handleCasePriceChange = (event) => {
    //    setCasePrice(event.target.value);
    //};



    // Часть с авторизацией
    const [isLoginModalOpen, setIsLoginModalOpen] = useState(false);

    function handleShareClick(event) {
        setIsLoginModalOpen(true);
    }

    function handleLoginModalClose(event) {
        setIsLoginModalOpen(false);
    }


    return (
        <div style={{ marginLeft: "30px" }}>
            <div>
                <h1 style={{ textAlign: "center" }}>Название веб-сервиса</h1>
                <div style={{ display: "flex", flexDirection: "column", justifyContent: "flex-start", marginTop: "20px" }}>
                    <div style={{ fontSize: "24px", marginLeft: "25px", marginBottom: "10px" }}>Введите свой бюджет:</div>
                    <input type="text" style={{ width: "10%", marginLeft: "27px" }} />
                </div>
                <div style={{ display: "flex", justifyContent: "center", marginTop: "-60px" }}>
                    <div style={{ fontSize: "24px", marginTop: "-10px" }}>Для какого направления требуется ПК</div>
                </div>
                <div style={{ display: "flex", justifyContent: "center", marginTop: "10px" }}>
                    <select style={{ width: "300px", fontSize: "24px" }} value={selectedItem} onChange={handleSelect}>
                        <option value="">Выберите направление</option>
                        <option value="games">Игры</option>
                        <option value="vr">VR</option>
                        <option value="it">IT</option>
                        <option value="design">Графический дизайн</option>
                        <option value="3d">3D</option>
                        <option value="server">Сервер</option>
                        <option value="video-audio">Видео- и аудио-производство</option>
                        <option value="science">Научные и инженерные рассчеты</option>
                        <option value="medicine">Использование в медицине</option>
                        <option value="networking">Сетевое оборудование</option>
                        <option value="office">Для офисных задач</option>
                        <option value="other">Другое</option>
                    </select>
                </div>

                {secondListItems.length > 0 && (
                    <div style={{ display: "flex", justifyContent: "center", marginTop: "-70px", marginLeft: "1000px" }}>
                        <div>
                            <div style={{ fontSize: "24px", marginBottom: "8px" }}>Выберите поднаправление</div>
                            <select value={selectedSecondItem} onChange={handleSecondSelect} style={{ fontSize: "24px", marginLeft: "40px", marginBottom: "20px" }}>
                                <option value="">Выберите элемент</option>
                                {secondListItems.map((item, index) => (
                                    <option key={index} value={item}>
                                        {item}
                                    </option>
                                ))}
                            </select>
                        </div>
                    </div>
                )}
                <div>
                    <div>
                        <label htmlFor="keywords" style={{ fontSize: "24px", marginLeft: "25px" }}>Ключевые слова:</label>
                        <input style={{ marginLeft: "10px", width: "75%", marginTop: "15px" }} type="text" id="keywords" />
                    </div>

                </div>
            </div>

            <div>
                <h2 style={{ marginLeft: "250px" }}> Названия комплектующих</h2>
                <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', marginBottom: "10px" }}>
                    <label htmlFor="cpu" style={{ fontSize: "20px", marginLeft: '30px', marginRight: '5px', width: '150px' }}>Процессор</label>
                    <div style={{ display: 'flex', flexDirection: 'column' }}>
                        <select id="cpu" value={cpu} style={{ fontSize: "20px", width: "33.33%", minWidth: "800px" }} >
                            <option value="Intel Core i5-11600K">Intel Core i5-11600K</option>
                            <option value="Intel Core i7-11700K">Intel Core i7-11700K</option>
                            <option value="Intel Core i9-11900K">Intel Core i9-11900K</option>
                            <option value="AMD Ryzen 5 5600X">AMD Ryzen 5 5600X</option>
                            <option value="AMD Ryzen 7 5800X">AMD Ryzen 7 5800X</option>
                            <option value="AMD Ryzen 9 5900X">AMD Ryzen 9 5900X</option>
                        </select>
                    </div>
                    <div style={{ fontSize: "20px", display: 'flex', flexDirection: 'column', marginLeft: "50px", marginTop: "-20px" }}>
                        <label htmlFor="ramPrice">Цена (BYN)</label>
                        <input type="number" id="ramPrice" value={ramPrice} readOnly style={{ width: '40%' }} />
                    </div>
                </div>


                <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', marginBottom: "10px" }}>
                    <label htmlFor="cooler" style={{ fontSize: "20px", marginLeft: '30px', marginRight: '5px', width: '150px' }}>Кулер</label>
                    <div style={{ display: 'flex', flexDirection: 'column' }}>
                        <select id="cooler" value={cooler} style={{ fontSize: "20px", width: "33.33%", minWidth: "800px" }} >
                            <option value="Samsung 970 EVO Plus 1TB NVMe SSD">Samsung 970 EVO Plus 1TB NVMe SSD</option>
                            <option value="WD Black SN850 1TB NVMe SSD">WD Black SN850 1TB NVMe SSD</option>
                            <option value="Seagate IronWolf Pro 4TB NAS Hard Drive">Seagate IronWolf Pro 4TB NAS Hard Drive</option>
                        </select>
                    </div>
                    <div style={{ display: 'flex', flexDirection: 'column', marginLeft: "50px" }}>
                        <input type="number" id="ramPrice" value={ramPrice} readOnly style={{ width: '40%' }} />
                    </div>
                </div>


                <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', marginBottom: "10px" }}>
                    <label htmlFor="motherboard" style={{ fontSize: "20px", marginLeft: '30px', marginRight: '5px', width: '150px' }}>Мат. плата</label>
                    <div style={{ display: 'flex', flexDirection: 'column' }}>
                        <select id="motherboard" value={motherboard} style={{ fontSize: "20px", width: "33.33%", minWidth: "800px" }} >
                            <option value="ASUS ROG Maximus XIII Hero">ASUS ROG Maximus XIII Hero</option>
                            <option value="GIGABYTE AORUS X570 Master">GIGABYTE AORUS X570 Master</option>
                            <option value="MSI MPG B550 Gaming Edge WiFi">MSI MPG B550 Gaming Edge WiFi</option>
                            <option value="ASRock Z590 Extreme WiFi 6E">ASRock Z590 Extreme WiFi 6E</option>
                        </select>
                    </div>
                    <div style={{ display: 'flex', flexDirection: 'column', marginLeft: "50px" }}>
                        <input type="number" id="ramPrice" value={ramPrice} readOnly style={{ width: '40%' }} />
                    </div>
                </div>


                <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', marginBottom: "10px" }}>
                    <label htmlFor="ram" style={{ fontSize: "20px", marginLeft: '30px', marginRight: '5px', width: '150px' }}>RAM</label>
                    <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', flex: '1' }}>
                        <select id="ram" value={ram} style={{ fontSize: "20px", width: '33.33%', minWidth: '800px', marginRight: '10px' }}>
                            <option value="corsair vengeance rgb pro 16gb (2 x 8gb) ddr4-3200">corsair vengeance rgb pro 16gb (2 x 8gb) ddr4-3200</option>
                            <option value="g.skill ripjaws v series 32gb (2 x 16gb) ddr4-3600">g.skill ripjaws v series 32gb (2 x 16gb) ddr4-3600</option>
                            <option value="crucial ballistix 64gb (2 x 32gb) ddr4-3200">crucial ballistix 64gb (2 x 32gb) ddr4-3200</option>
                        </select>
                        <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                            <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', flex: 1 }}>
                                <label style={{ marginRight: "3px" }} htmlFor="ramSize">X</label>
                                <input type="number" id="ramSize" value={ramSize} readOnly style={{ maxWidth: "10px" }} />
                            </div>
                            <div style={{ display: 'flex', flexDirection: 'column', marginLeft: "11px" }}>
                                <input type="number" id="ramPrice" value={ramPrice} readOnly style={{ width: '40%' }} />
                            </div>
                        </div>
                    </div>
                </div>


                <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', marginBottom: "10px" }}>
                    <label htmlFor="gpu" style={{ fontSize: "20px", marginLeft: '30px', marginRight: '5px', width: '150px' }}>Видеокарта</label>
                    <div style={{ display: 'flex', flexDirection: 'column' }}>
                        <select id="gpu" value={gpu} style={{ fontSize: "20px", width: "33.33%", minWidth: "800px" }} >
                            <option value="corsair vengeance rgb pro 16gb (2 x 8gb) ddr4-3200">corsair vengeance rgb pro 16gb (2 x 8gb) ddr4-3200</option>
                            <option value="g.skill ripjaws v series 32gb (2 x 16gb) ddr4-3600">g.skill ripjaws v series 32gb (2 x 16gb) ddr4-3600</option>
                            <option value="crucial ballistix 64gb (2 x 32gb) ddr4-3200">crucial ballistix 64gb (2 x 32gb) ddr4-3200</option>
                        </select>
                    </div>
                    <div style={{ display: 'flex', flexDirection: 'column', marginLeft: "50px" }}>
                        <input type="number" id="ramPrice" value={ramPrice} readOnly style={{ width: '40%' }} />
                    </div>
                </div>

                <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', marginBottom: "10px" }}>
                    <label htmlFor="ssd" style={{ fontSize: "20px", marginLeft: '30px', marginRight: '5px', width: '150px' }}>SSD</label>
                    <div style={{ display: 'flex', flexDirection: 'column' }}>
                        <select id="ssd" value={ssd} style={{ fontSize: "20px", width: "33.33%", minWidth: "800px" }} >
                            <option value="corsair vengeance rgb pro 16gb (2 x 8gb) ddr4-3200">corsair vengeance rgb pro 16gb (2 x 8gb) ddr4-3200</option>
                            <option value="g.skill ripjaws v series 32gb (2 x 16gb) ddr4-3600">g.skill ripjaws v series 32gb (2 x 16gb) ddr4-3600</option>
                            <option value="crucial ballistix 64gb (2 x 32gb) ddr4-3200">crucial ballistix 64gb (2 x 32gb) ddr4-3200</option>
                        </select>
                    </div>
                    <div style={{ display: 'flex', flexDirection: 'column', marginLeft: "50px" }}>
                        <input type="number" id="ramPrice" value={ramPrice} readOnly style={{ width: '40%' }} />
                    </div>
                </div>

                <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', marginBottom: "10px" }}>
                    <label htmlFor="hdd" style={{ fontSize: "20px", marginLeft: '30px', marginRight: '5px', width: '150px' }}>HDD</label>
                    <div style={{ display: 'flex', flexDirection: 'column' }}>
                        <select id="hdd" value={hdd} style={{ fontSize: "20px", width: "33.33%", minWidth: "800px" }} >
                            <option value="corsair vengeance rgb pro 16gb (2 x 8gb) ddr4-3200">corsair vengeance rgb pro 16gb (2 x 8gb) ddr4-3200</option>
                            <option value="g.skill ripjaws v series 32gb (2 x 16gb) ddr4-3600">g.skill ripjaws v series 32gb (2 x 16gb) ddr4-3600</option>
                            <option value="crucial ballistix 64gb (2 x 32gb) ddr4-3200">crucial ballistix 64gb (2 x 32gb) ddr4-3200</option>
                        </select>
                    </div>
                    <div style={{ display: 'flex', flexDirection: 'column', marginLeft: "50px" }}>
                        <input type="number" id="ramPrice" value={ramPrice} readOnly style={{ width: '40%' }} />
                    </div>
                </div>

                <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', marginBottom: "10px" }}>
                    <label htmlFor="power" style={{ fontSize: "20px", marginLeft: '30px', marginRight: '5px', width: '150px' }}>Блок питания</label>
                    <div style={{ display: 'flex', flexDirection: 'column' }}>
                        <select id="power" value={power} style={{ fontSize: "20px", width: "33.33%", minWidth: "800px" }} >
                            <option value="corsair vengeance rgb pro 16gb (2 x 8gb) ddr4-3200">corsair vengeance rgb pro 16gb (2 x 8gb) ddr4-3200</option>
                            <option value="g.skill ripjaws v series 32gb (2 x 16gb) ddr4-3600">g.skill ripjaws v series 32gb (2 x 16gb) ddr4-3600</option>
                            <option value="crucial ballistix 64gb (2 x 32gb) ddr4-3200">crucial ballistix 64gb (2 x 32gb) ddr4-3200</option>
                        </select>
                    </div>
                    <div style={{ display: 'flex', flexDirection: 'column', marginLeft: "50px" }}>
                        <input type="number" id="ramPrice" value={ramPrice} readOnly style={{ width: '40%' }} />
                    </div>
                </div>


                <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', marginBottom: "10px" }}>
                    <label htmlFor="casePC" style={{ fontSize: "20px", marginLeft: '30px', marginRight: '5px', width: '150px' }}>Корпус</label>
                    <div style={{ display: 'flex', flexDirection: 'column' }}>
                        <select id="casePC" value={casePC} style={{ fontSize: "20px", width: "33.33%", minWidth: "800px" }} >
                            <option value="corsair vengeance rgb pro 16gb (2 x 8gb) ddr4-3200">corsair vengeance rgb pro 16gb (2 x 8gb) ddr4-3200</option>
                            <option value="g.skill ripjaws v series 32gb (2 x 16gb) ddr4-3600">g.skill ripjaws v series 32gb (2 x 16gb) ddr4-3600</option>
                            <option value="crucial ballistix 64gb (2 x 32gb) ddr4-3200">crucial ballistix 64gb (2 x 32gb) ddr4-3200</option>
                        </select>
                    </div>
                    <div style={{ display: 'flex', flexDirection: 'column', marginLeft: "50px" }}>
                        <input type="number" id="ramPrice" value={ramPrice} readOnly style={{ width: '40%' }} />
                    </div>
                </div>

                <div style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
                    <button style={{ width: "15%", height: "3em", margin: "5px", fontSize: "16px", marginLeft: '1050px', marginTop: "-300px" }}>
                        Отсортировать по ценам
                    </button>
                    <button style={{ width: "15%", height: "3em", margin: "5px", fontSize: "16px", marginLeft: '1050px' }}>
                        Отсортировать по названиям
                    </button>
                    <button style={{ width: "15%", height: "3em", margin: "5px", fontSize: "16px", marginLeft: '1050px' }}>
                        Отсортировать по давности появления в каталоге
                    </button>
                    <button style={{ width: "15%", height: "3em", margin: "5px", fontSize: "16px", marginLeft: '1050px' }}>
                        Сохранить конфигурацию в Excel
                    </button>
                    <div style={{ display: "flex", justifyContent: "space-between", marginTop: "125px" }}>
                        <button style={{ width: "25%", height: "3em", margin: "5px", fontSize: "20px", marginTop: "150px" }}>
                            Конфигурации, составленные другими пользователями
                        </button>
                        <button style={{ width: "15%", height: "3em", margin: "5px", fontSize: "20px", marginTop: "150px" }}>
                            СОСТАВИТЬ КОНФИГУРАЦИИ
                        </button>
                        <button style={{ width: "25%", height: "3em", margin: "5px", fontSize: "20px", marginTop: "150px" }} onClick={handleShareClick}>
                            Поделиться своей конфигурацией с другими пользователями
                        </button>
                        {isLoginModalOpen && <LoginModal onClose={handleLoginModalClose} />}
                    </div>
                </div>



            </div>
        </div>
    );
}

export default App;