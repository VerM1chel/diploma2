import React, { useState, useEffect } from 'react';
import axios from 'axios';


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
    const [cpus, setCpus] = useState([]);
    const [coolers, setCoolers] = useState([]);
    const [motherboards, setMotherboards] = useState([]);
    const [rams, setRams] = useState([]);
    const [ramSize, setRamSize] = useState('');
    const [gpus, setGpus] = useState([]);
    const [ssds, setSsds] = useState([]);
    const [hdds, setHdds] = useState([]);
    const [powers, setPowers] = useState([]);
    const [casePCs, setCasePCs] = useState([]);

    const [selectedCpu, setSelectedCpu] = useState("");
    const [selectedCooler, setSelectedCooler] = useState("");
    const [selectedMotherboard, setSelectedMotherboard] = useState("");
    const [selectedRam, setSelectedRam] = useState("");
    const [selectedGpu, setSelectedGpu] = useState("");
    const [selectedSsd, setSelectedSsd] = useState("");
    const [selectedHdd, setSelectedHdd] = useState("");
    const [selectedPower, setSelectedPower] = useState("");
    const [selectedCasePC, setSelectedCasePC] = useState("");

    const [cpuPrice, setCpuPrice] = useState('');
    const [coolerPrice, setCoolerPrice] = useState('');
    const [motherboardPrice, setMotherboardPrice] = useState('');
    const [ramPrice, setRamPrice] = useState('');
    const [gpuPrice, setGpuPrice] = useState('');
    const [ssdPrice, setSsdPrice] = useState('');
    const [hddPrice, setHddPrice] = useState('');
    const [powerPrice, setPowerPrice] = useState('');
    const [casePrice, setCasePrice] = useState('');

    const [numbers, setNumbers] = useState([]);

    const [selectedCpuId, selectedCoolerId, selectedMotherboardId, selectedRamId, selectedGpuId, selectedSsdId, selectedHddId, selectedPowerId, selectedCaseId] = numbers;

    useEffect(() => {
       
    }, []);


    useEffect(() => {
        axios.get('/numbers')
            .then(response => setNumbers(response.data));
 
        axios.get('/cpus')
            .then(response => {
                setCpus(response.data);
                setSelectedCpu(response.data[selectedCpuId].name); // Выбираем первый элемент списка по умолчанию
            })
            .catch(error => console.log(error));
        axios.get('/coolers')
            .then(response => {
                setCoolers(response.data);
                setSelectedCooler(response.data[selectedCoolerId].name); // Выбираем первый элемент списка по умолчанию
            })
            .catch(error => console.log(error));
        axios.get('/motherboards')
            .then(response => {
                setMotherboards(response.data);
                setSelectedMotherboard(response.data[selectedMotherboardId].name); // Выбираем первый элемент списка по умолчанию
            })
            .catch(error => console.log(error));
        axios.get('/rams')
            .then(response => {
                setRams(response.data);
                setSelectedRam(response.data[selectedRamId].name); // Выбираем первый элемент списка по умолчанию
            })
            .catch(error => console.log(error));
        axios.get('/gpus')
            .then(response => {
                setGpus(response.data);
                setSelectedGpu(response.data[selectedGpuId].name); // Выбираем первый элемент списка по умолчанию
            })
            .catch(error => console.log(error));
        axios.get('/ssds')
            .then(response => {
                setSsds(response.data);
                setSelectedSsd(response.data[selectedSsdId].name); // Выбираем первый элемент списка по умолчанию
            })
            .catch(error => console.log(error));
        axios.get('/hdds')
            .then(response => {
                setHdds(response.data);
                setSelectedHdd(response.data[selectedHddId].name); // Выбираем первый элемент списка по умолчанию
            })
            .catch(error => console.log(error));
        axios.get('/powers')
            .then(response => {
                setPowers(response.data);
                setSelectedPower(response.data[selectedPowerId].name); // Выбираем первый элемент списка по умолчанию
            })
            .catch(error => console.log(error));
        axios.get('/casePCs')
            .then(response => {
                setCasePCs(response.data);
                setSelectedCasePC(response.data[selectedCaseId].name); // Выбираем первый элемент списка по умолчанию
            })
            .catch(error => console.log(error));
    }, []);

    const handleComponentChange = (event, component, setSelectedComponent, setPrice) => {
        const selectedComponent = component.find(item => item.name === event.target.value);
        setSelectedComponent(selectedComponent);
        setPrice(selectedComponent.price);
    };




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
                        <select value={selectedCpu.name} onChange={(e) => handleComponentChange(e, cpus, setSelectedCpu, setCpuPrice)} style={{ fontSize: "20px", width: "33.33%", minWidth: "800px" }}>
                            {cpus.map(cpu => (
                                <option value={cpu.name} key={cpu.name}>{cpu.name}</option>
                            ))}
                        </select>
                    </div>
                    <div style={{ fontSize: "20px", display: 'flex', flexDirection: 'column', marginLeft: "50px", marginTop: "-20px" }}>
                        <label htmlFor="cpuPrice">Цена (BYN)</label>
                        <input type="number" id="cpuPrice" value={selectedCpu ? selectedCpu.price : ''} readOnly style={{ width: '35%', fontSize: "20px" }} />
                    </div>
                </div>

                <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', marginBottom: "10px" }}>
                    <label htmlFor="coolers" style={{ fontSize: "20px", marginLeft: '30px', marginRight: '5px', width: '150px' }}>Кулер</label>
                    <div style={{ display: 'flex', flexDirection: 'column' }}>
                        <select value={selectedCooler.name} onChange={(e) => handleComponentChange(e, coolers, setSelectedCooler, setCoolerPrice)} style={{ fontSize: "20px", width: "33.33%", minWidth: "800px" }}>
                            {coolers.map(cooler => (
                                <option value={cooler.name} key={cooler.name}>{cooler.name}</option>
                            ))}
                        </select>
                    </div>
                    <div style={{ fontSize: "20px", display: 'flex', flexDirection: 'column', marginLeft: "50px", marginTop: "-20px" }}>
                        <input type="number" id="coolerPrice" value={selectedCooler ? selectedCooler.price : ''} readOnly style={{ width: '35%', fontSize: "20px" }} />
                    </div>
                </div>


                <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', marginBottom: "10px" }}>
                    <label htmlFor="motherboards" style={{ fontSize: "20px", marginLeft: '30px', marginRight: '5px', width: '150px' }}>Мат. плата</label>
                    <div style={{ display: 'flex', flexDirection: 'column' }}>
                        <select value={selectedMotherboard.name} onChange={(e) => handleComponentChange(e, motherboards, setSelectedMotherboard, setMotherboardPrice)} style={{ fontSize: "20px", width: "33.33%", minWidth: "800px" }}>
                            {motherboards.map(motherboard => (
                                <option value={motherboard.name} key={motherboard.name}>{motherboard.name}</option>
                            ))}
                        </select>
                    </div>
                    <div style={{ display: 'flex', flexDirection: 'column', marginLeft: "50px" }}>
                        <input type="number" id="motherboardPrice" value={selectedMotherboard ? selectedMotherboard.price : ''} readOnly style={{ width: '35%', fontSize: "20px" }} />
                    </div>
                </div>


                <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', marginBottom: "10px" }}>
                    <label htmlFor="rams" style={{ fontSize: "20px", marginLeft: '30px', marginRight: '5px', width: '150px' }}>RAM</label>
                    <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', flex: '1' }}>
                        <select value={selectedRam.name} onChange={(e) => handleComponentChange(e, rams, setSelectedRam, setRamPrice)} style={{ fontSize: "20px", width: "33.33%", minWidth: "800px" }}>
                            {rams.map(ram => (
                                <option value={ram.name} key={ram.name}>{ram.name}</option>
                            ))}
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
                    <label htmlFor="gpus" style={{ fontSize: "20px", marginLeft: '30px', marginRight: '5px', width: '150px' }}>Видеокарта</label>
                    <div style={{ display: 'flex', flexDirection: 'column' }}>
                        <select value={selectedGpu.name} onChange={(e) => handleComponentChange(e, gpus, setSelectedGpu, setGpuPrice)} style={{ fontSize: "20px", width: "33.33%", minWidth: "800px" }}>
                            {gpus.map(gpu => (
                                <option value={gpu.name} key={gpu.name}>{gpu.name}</option>
                            ))}
                        </select>
                    </div>
                    <div style={{ display: 'flex', flexDirection: 'column', marginLeft: "50px" }}>
                        <input type="number" id="gpuPrice" value={gpuPrice} readOnly style={{ width: '40%' }} />
                    </div>
                </div>

                <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', marginBottom: "10px" }}>
                    <label htmlFor="ssds" style={{ fontSize: "20px", marginLeft: '30px', marginRight: '5px', width: '150px' }}>SSD</label>
                    <div style={{ display: 'flex', flexDirection: 'column' }}>
                        <select value={selectedSsd.name} onChange={(e) => handleComponentChange(e, ssds, setSelectedSsd, setSsdPrice)} style={{ fontSize: "20px", width: "33.33%", minWidth: "800px" }}>
                            {ssds.map(ssd => (
                                <option value={ssd.name} key={ssd.name}>{ssd.name}</option>
                            ))}
                        </select>
                    </div>
                    <div style={{ display: 'flex', flexDirection: 'column', marginLeft: "50px" }}>
                        <input type="number" id="ssdPrice" value={selectedSsd ? selectedSsd.price : ''} readOnly style={{ width: '35%', fontSize: "20px" }} />
                    </div>
                </div>

                <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', marginBottom: "10px" }}>
                    <label htmlFor="hdds" style={{ fontSize: "20px", marginLeft: '30px', marginRight: '5px', width: '150px' }}>HDD</label>
                    <div style={{ display: 'flex', flexDirection: 'column' }}>
                        <select value={selectedHdd.name} onChange={(e) => handleComponentChange(e, hdds, setSelectedHdd, setHddPrice)} style={{ fontSize: "20px", width: "33.33%", minWidth: "800px" }}>
                            {hdds.map(hdd => (
                                <option value={hdd.name} key={hdd.name}>{hdd.name}</option>
                            ))}
                        </select>
                    </div>
                    <div style={{ display: 'flex', flexDirection: 'column', marginLeft: "50px" }}>
                        <input type="number" id="hddPrice" value={selectedHdd ? selectedHdd.price : ''} readOnly style={{ width: '35%', fontSize: "20px" }} />
                    </div>
                </div>

                <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', marginBottom: "10px" }}>
                    <label htmlFor="powers" style={{ fontSize: "20px", marginLeft: '30px', marginRight: '5px', width: '150px' }}>Блок питания</label>
                    <div style={{ display: 'flex', flexDirection: 'column' }}>
                        <select value={selectedPower.name} onChange={(e) => handleComponentChange(e, powers, setSelectedPower, setPowerPrice)} style={{ fontSize: "20px", width: "33.33%", minWidth: "800px" }}>
                            {powers.map(power => (
                                <option value={power.name} key={power.name}>{power.name}</option>
                            ))}
                        </select>
                    </div>
                    <div style={{ display: 'flex', flexDirection: 'column', marginLeft: "50px" }}>
                        <input type="number" id="powerPrice" value={selectedPower ? selectedPower.price : ''} readOnly style={{ width: '35%', fontSize: "20px" }} />
                    </div>
                </div>


                <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', marginBottom: "10px" }}>
                    <label htmlFor="casePCs" style={{ fontSize: "20px", marginLeft: '30px', marginRight: '5px', width: '150px' }}>Корпус</label>
                    <div style={{ display: 'flex', flexDirection: 'column' }}>
                        <select value={selectedCasePC.name} onChange={(e) => handleComponentChange(e, casePCs, setSelectedCasePC, setCasePrice)} style={{ fontSize: "20px", width: "33.33%", minWidth: "800px" }}>
                            {casePCs.map(casePC => (
                                <option value={casePC.name} key={casePC.name}>{casePC.name}</option>
                            ))}
                        </select>
                    </div>
                    <div style={{ display: 'flex', flexDirection: 'column', marginLeft: "50px" }}>
                        <input type="number" id="casePrice" value={selectedCasePC ? selectedCasePC.price : ''} readOnly style={{ width: '35%', fontSize: "20px" }} />
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