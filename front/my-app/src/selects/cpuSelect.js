import React, { useState, useEffect } from 'react';
import axios from 'axios';


function App() {
    const [cpus, setCpus] = useState([]);
    const [selectedCpu, setSelectedCpu] = useState("");

    const [numbers, setNumbers] = useState([0, 0, 0, 0, 0, 0, 0, 0, 0]);

    useEffect(() => {
        axios.get('/indeces')
            .then(response => {
                console.log(response.data);
                setNumbers(response.data);
            })
            .catch(error => console.log(error));

        axios.get('/cpus')
            .then(response => {
                setCpus(response.data);
                setSelectedCpu(response.data[0].name); // Выбираем первый элемент списка по умолчанию
            })
            .catch(error => console.log(error));
    }, []);

    const [cpuPrice, setCpuPrice] = useState("");

    const handleComponentChange = (event, components, setSelectedComponent, setPrice) => {
        setOutput(0);
        const selectedComponent = components.find((component) => component.name === event.target.value);
        setSelectedComponent(selectedComponent);
        setPrice(selectedComponent.price);
    };


    const [output, setOutput] = useState(0);


    useEffect(() => {
        if (output) {
            setCpuPrice(output.price);
        }
    }, [output]);

    const createConfClick = () => {
        if (cpus.length > 0 && numbers.length > 0) {
            const selectedCpu = cpus[numbers[0]];
            setOutput(selectedCpu);
        }
    };

    return (
        <div style={{ marginLeft: "30px" }}>
            <div>
                <div>
                    <h2 style={{ marginLeft: "250px" }}> Названия комплектующих</h2>
                    <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', marginBottom: "10px" }}>
                        <label htmlFor="cpu" style={{ fontSize: "20px", marginLeft: '30px', marginRight: '5px', width: '150px' }}>Процессор</label>
                        <div style={{ display: 'flex', flexDirection: 'column' }}>
                            <select onChange={(e) => handleComponentChange(e, cpus, setSelectedCpu, setCpuPrice)} style={{ fontSize: "20px", width: "33.33%", minWidth: "800px" }}>
                                {cpus.map((cpu, index) => (
                                    <option value={cpu.name} selected={index === output.id + 1}>
                                        {cpu.name}
                                    </option>
                                ))}
                            </select>
                        </div>
                        <div style={{ fontSize: "20px", display: 'flex', flexDirection: 'column', marginLeft: "50px", marginTop: "-20px" }}>
                            <label htmlFor="cpuPrice">Цена (BYN)</label>
                            <input type="number" id="cpuPrice" value={cpuPrice} selected={output.id + 1} readOnly style={{ width: '35%', fontSize: "20px" }} />
                        </div>
                    </div>
                </div>
                <button style={{ width: "15%", height: "3em", margin: "5px", fontSize: "20px", marginTop: "150px" }} onClick={createConfClick}>
                    СОСТАВИТЬ КОНФИГУРАЦИИ
                </button>
            </div>
        </div>
    );
}
export default App;