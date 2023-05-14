﻿import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Selects() {
    const [cpus, setCpus] = useState([]);
    const [coolers, setCoolers] = useState([]);
    const [motherboards, setMotherboards] = useState([]);
    const [rams, setRams] = useState([]);
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

    const [cpuPrice, setCpuPrice] = useState("");
    const [coolerPrice, setCoolerPrice] = useState("");
    const [motherboardPrice, setMotherboardPrice] = useState("");
    const [ramSize, setRamSize] = useState("");
    const [ramPrice, setRamPrice] = useState("");
    const [gpuPrice, setGpuPrice] = useState("");
    const [ssdPrice, setSsdPrice] = useState("");
    const [hddPrice, setHddPrice] = useState("");
    const [powerPrice, setPowerPrice] = useState("");
    const [casePrice, setCasePrice] = useState("");

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
        axios.get('/coolers')
            .then(response => {
                setCoolers(response.data);
                setSelectedCooler(response.data[0].name); // Выбираем первый элемент списка по умолчанию
            })
            .catch(error => console.log(error));
        axios.get('/motherboards')
            .then(response => {
                setMotherboards(response.data);
                setSelectedMotherboard(response.data[0].name); // Выбираем первый элемент списка по умолчанию
            })
            .catch(error => console.log(error));
        axios.get('/rams')
            .then(response => {
                setRams(response.data);
                setSelectedRam(response.data[0].name); // Выбираем первый элемент списка по умолчанию
            })
            .catch(error => console.log(error));
        axios.get('/gpus')
            .then(response => {
                setGpus(response.data);
                setSelectedGpu(response.data[0].name); // Выбираем первый элемент списка по умолчанию
            })
            .catch(error => console.log(error));
        axios.get('/ssds')
            .then(response => {
                setSsds(response.data);
                setSelectedSsd(response.data[0].name); // Выбираем первый элемент списка по умолчанию
            })
            .catch(error => console.log(error));
        axios.get('/hdds')
            .then(response => {
                setHdds(response.data);
                setSelectedHdd(response.data[0].name); // Выбираем первый элемент списка по умолчанию
            })
            .catch(error => console.log(error));
        axios.get('/powers')
            .then(response => {
                setPowers(response.data);
                setSelectedPower(response.data[0].name); // Выбираем первый элемент списка по умолчанию
            })
            .catch(error => console.log(error));
        axios.get('/casePCs')
            .then(response => {
                setCasePCs(response.data);
                setSelectedCasePC(response.data[0].name); // Выбираем первый элемент списка по умолчанию
            })
            .catch(error => console.log(error));
    }, []);


    const handleComponentChange = (event, components, setOutput, setSelectedComponent, setPrice, setSize) => {
        setOutput(0);
        const selectedComponent = components.find((component) => component.name === event.target.value);
        setSelectedComponent(selectedComponent);
        setPrice(selectedComponent.price);
        if (setSize) { setSize(selectedComponent.kit) }
    };


    const [output0, setOutput0] = useState(0);
    const [output1, setOutput1] = useState(0);
    const [output2, setOutput2] = useState(0);
    const [output3, setOutput3] = useState(0);
    const [output4, setOutput4] = useState(0);
    const [output5, setOutput5] = useState(0);
    const [output6, setOutput6] = useState(0);
    const [output7, setOutput7] = useState(0);
    const [output8, setOutput8] = useState(0);



    useEffect(() => {
        if (output0) { setCpuPrice(output0.price); }
        if (output1) { setCoolerPrice(output1.price); }
        if (output2) { setMotherboardPrice(output2.price); }
        if (output3) { setRamPrice(output3.price); setRamSize(output3.kit) }
        if (output4) { setGpuPrice(output4.price); }
        if (output5) { setSsdPrice(output5.price); }
        if (output6) { setHddPrice(output6.price); }
        if (output7) { setPowerPrice(output7.price); }
        if (output8) { setCasePrice(output8.price); }
    }, [output0, output1, output2, output3, output4, output5, output6, output7, output8]);


    const createConfClick = () => {
        if (cpus.length > 0 && numbers.length > 0) {
            const selectedCpu = cpus[numbers[0]];
            const selectedCooler = coolers[numbers[1]];
            const selectedMotherboard = motherboards[numbers[2]];
            const selectedRam = rams[numbers[3]];
            const selectedGpu = gpus[numbers[4]];
            const selectedSsd = ssds[numbers[5]];
            const selectedHdd = hdds[numbers[6]];
            const selectedPower = powers[numbers[7]];
            const selectedCasePC = casePCs[numbers[8]];
            setOutput0(selectedCpu);
            setOutput1(selectedCooler);
            setOutput2(selectedMotherboard);
            setOutput3(selectedRam);
            setOutput4(selectedGpu);
            setOutput5(selectedSsd);
            setOutput6(selectedHdd);
            setOutput7(selectedPower);
            setOutput8(selectedCasePC);
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
                            <select onChange={(e) => handleComponentChange(e, cpus, setOutput0, setSelectedCpu, setCpuPrice)} style={{ fontSize: "20px", width: "33.33%", minWidth: "800px" }}>
                                {cpus.map((cpu, index) => (
                                    <option value={cpu.name} selected={index === output0?.id + 1}>
                                        {cpu.name}
                                    </option>
                                ))}
                            </select>
                        </div>
                        <div style={{ fontSize: "20px", display: 'flex', flexDirection: 'column', marginLeft: "50px", marginTop: "-20px" }}>
                            <label htmlFor="cpuPrice">Цена (BYN)</label>
                            <input type="number" id="cpuPrice" value={cpuPrice} selected={output0?.id + 1} readOnly style={{ width: '35%', fontSize: "20px" }} />
                        </div>
                    </div>

                    <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', marginBottom: "10px" }}>
                        <label htmlFor="coolers" style={{ fontSize: "20px", marginLeft: '30px', marginRight: '5px', width: '150px' }}>Кулер</label>
                        <div style={{ display: 'flex', flexDirection: 'column' }}>
                            <select onChange={(e) => handleComponentChange(e, coolers, setOutput1, setSelectedCooler, setCoolerPrice)} style={{ fontSize: "20px", width: "33.33%", minWidth: "800px" }}>
                                {coolers.map((cooler, index) => (
                                    <option value={cooler.name} selected={index === output1?.id + 1}>
                                        {cooler.name}
                                    </option>
                                ))}
                            </select>
                        </div>
                        <div style={{ fontSize: "20px", display: 'flex', flexDirection: 'column', marginLeft: "50px", marginTop: "-20px" }}>
                            <input type="number" id="coolerPrice" value={coolerPrice} selected={output1?.id + 1} readOnly style={{ width: '35%', fontSize: "20px" }} />
                        </div>
                    </div>


                    <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', marginBottom: "10px" }}>
                        <label htmlFor="motherboards" style={{ fontSize: "20px", marginLeft: '30px', marginRight: '5px', width: '150px' }}>Мат. плата</label>
                        <div style={{ display: 'flex', flexDirection: 'column' }}>
                            <select onChange={(e) => handleComponentChange(e, motherboards, setOutput2, setSelectedMotherboard, setMotherboardPrice)} style={{ fontSize: "20px", width: "33.33%", minWidth: "800px" }}>
                                {motherboards.map((motherboard, index) => (
                                    <option value={motherboard.name} selected={index === output2?.id + 1}>
                                        {motherboard.name}
                                    </option>
                                ))}
                            </select>
                        </div>
                        <div style={{ fontSize: "20px", display: 'flex', flexDirection: 'column', marginLeft: "50px", marginTop: "-20px" }}>
                            <input type="number" id="motherboardPrice" value={motherboardPrice} selected={output2?.id + 1} readOnly style={{ width: '35%', fontSize: "20px" }} />
                        </div>
                    </div>


                    <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', marginBottom: "10px" }}>
                        <label htmlFor="rams" style={{ fontSize: "20px", marginLeft: '30px', marginRight: '5px', width: '150px' }}>RAM</label>
                        <div style={{ display: 'flex', flexDirection: 'column' }}>
                            <select onChange={(e) => handleComponentChange(e, rams, setOutput3, setSelectedRam, setRamPrice, setRamSize)} style={{ fontSize: "20px", width: "33.33%", minWidth: "800px" }}>
                                {rams.map((ram, index) => (
                                    <option value={ram.name} selected={index === output3?.id + 1}>
                                        {ram.name}
                                    </option>
                                ))}
                            </select>
                        </div>
                        <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', flex: 1 }}>
                            <label style={{ marginRight: "3px" }} htmlFor="ramSize">X</label>
                            <input type="number" id="ramSize" value={ramSize} selected={output3?.id + 1} readOnly style={{ width: '35%', fontSize: "20px" }} />
                        </div>
                        <div style={{ fontSize: "20px", display: 'flex', flexDirection: 'column', marginLeft: "50px", marginTop: "-20px" }}>
                            <input type="number" id="ramPrice" value={ramPrice} selected={output3?.id + 1} readOnly style={{ width: '35%', fontSize: "20px" }} />
                        </div>
                    </div>


                    <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', marginBottom: "10px" }}>
                        <label htmlFor="gpus" style={{ fontSize: "20px", marginLeft: '30px', marginRight: '5px', width: '150px' }}>Видеокарта</label>
                        <div style={{ display: 'flex', flexDirection: 'column' }}>
                            <select onChange={(e) => handleComponentChange(e, gpus, setOutput4, setSelectedGpu, setGpuPrice)} style={{ fontSize: "20px", width: "33.33%", minWidth: "800px" }}>
                                {gpus.map((gpu, index) => (
                                    <option value={gpu.name} selected={index === output4?.id + 1}>
                                        {gpu.name}
                                    </option>
                                ))}
                            </select>
                        </div>
                        <div style={{ fontSize: "20px", display: 'flex', flexDirection: 'column', marginLeft: "50px", marginTop: "-20px" }}>
                            <input type="number" id="gpuPrice" value={gpuPrice} selected={output4?.id + 1} readOnly style={{ width: '35%', fontSize: "20px" }} />
                        </div>
                    </div>

                    <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', marginBottom: "10px" }}>
                        <label htmlFor="ssds" style={{ fontSize: "20px", marginLeft: '30px', marginRight: '5px', width: '150px' }}>SSD</label>
                        <div style={{ display: 'flex', flexDirection: 'column' }}>
                            <select onChange={(e) => handleComponentChange(e, ssds, setOutput5, setSelectedSsd, setSsdPrice)} style={{ fontSize: "20px", width: "33.33%", minWidth: "800px" }}>
                                {ssds.map((ssd, index) => (
                                    <option value={ssd.name} selected={index === output5?.id + 1}>
                                        {ssd.name}
                                    </option>
                                ))}
                            </select>
                        </div>
                        <div style={{ fontSize: "20px", display: 'flex', flexDirection: 'column', marginLeft: "50px", marginTop: "-20px" }}>
                            <input type="number" id="ssdPrice" value={ssdPrice} selected={output5?.id + 1} readOnly style={{ width: '35%', fontSize: "20px" }} />
                        </div>
                    </div>

                    <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', marginBottom: "10px" }}>
                        <label htmlFor="hdds" style={{ fontSize: "20px", marginLeft: '30px', marginRight: '5px', width: '150px' }}>HDD</label>
                        <div style={{ display: 'flex', flexDirection: 'column' }}>
                            <select onChange={(e) => handleComponentChange(e, hdds, setOutput6, setSelectedHdd, setHddPrice)} style={{ fontSize: "20px", width: "33.33%", minWidth: "800px" }}>
                                {hdds.map((hdd, index) => (
                                    <option value={hdd.name} selected={index === output6?.id + 1}>
                                        {hdd.name}
                                    </option>
                                ))}
                            </select>
                        </div>
                        <div style={{ fontSize: "20px", display: 'flex', flexDirection: 'column', marginLeft: "50px", marginTop: "-20px" }}>
                            <input type="number" id="hddPrice" value={hddPrice} selected={output6?.id + 1} readOnly style={{ width: '35%', fontSize: "20px" }} />
                        </div>
                    </div>

                    <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', marginBottom: "10px" }}>
                        <label htmlFor="powers" style={{ fontSize: "20px", marginLeft: '30px', marginRight: '5px', width: '150px' }}>Блок питания</label>
                        <div style={{ display: 'flex', flexDirection: 'column' }}>
                            <select onChange={(e) => handleComponentChange(e, powers, setOutput7, setSelectedPower, setPowerPrice)} style={{ fontSize: "20px", width: "33.33%", minWidth: "800px" }}>
                                {powers.map((power, index) => (
                                    <option value={power.name} selected={index === output7?.id + 1}>
                                        {power.name}
                                    </option>
                                ))}
                            </select>
                        </div>
                        <div style={{ fontSize: "20px", display: 'flex', flexDirection: 'column', marginLeft: "50px", marginTop: "-20px" }}>
                            <input type="number" id="powerPrice" value={powerPrice} selected={output7?.id + 1} readOnly style={{ width: '35%', fontSize: "20px" }} />
                        </div>
                    </div>

                    <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', marginBottom: "10px" }}>
                        <label htmlFor="casePCs" style={{ fontSize: "20px", marginLeft: '30px', marginRight: '5px', width: '150px' }}>Корпус</label>
                        <div style={{ display: 'flex', flexDirection: 'column' }}>
                            <select onChange={(e) => handleComponentChange(e, casePCs, setOutput8, setSelectedCasePC, setCasePrice)} style={{ fontSize: "20px", width: "33.33%", minWidth: "800px" }}>
                                {casePCs.map((casePC, index) => (
                                    <option value={casePC.name} selected={index === output8?.id + 1}>
                                        {casePC.name}
                                    </option>
                                ))}
                            </select>
                        </div>
                        <div style={{ fontSize: "20px", display: 'flex', flexDirection: 'column', marginLeft: "50px", marginTop: "-20px" }}>
                            <input type="number" id="casePrice" value={casePrice} selected={output8?.id + 1} readOnly style={{ width: '35%', fontSize: "20px" }} />
                        </div>
                    </div>
                </div>
                <button style={{ width: "15%", height: "3em", margin: "5px", fontSize: "20px", marginTop: "150px" }} onClick={createConfClick}>
                    СОСТАВИТЬ КОНФИГУРАЦИЮ
                </button>
            </div>
        </div>
    );
} export default Selects;