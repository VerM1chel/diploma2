import React, { useState, useEffect } from 'react';

function Sorts({ cpus }) {
    const [cpuSortOrder, setCpuSortOrder] = useState("");
    const [coolerSortOrder, setCoolerSortOrder] = useState("");
    const [motherboardSortOrder, setMotherboardSortOrder] = useState("");
    const [ramSortOrder, setRamSortOrder] = useState("");
    const [gpuSortOrder, setGpuSortOrder] = useState("");
    const [ssdSortOrder, setSsdSortOrder] = useState("");
    const [hddSortOrder, setHddSortOrder] = useState("");
    const [powerSortOrder, setPowerSortOrder] = useState("");
    const [caseSortOrder, setCaseSortOrder] = useState("");

    const handleSortByPrice = () => {
        const sortedList = [...cpus].sort((a, b) => a.price - b.price);
        setCpuSortOrder(sortedList);
        

        setCpuSortOrder("price");
        
    };

    const handleSortByName = () => {
        const sortedList = [...cpus].sort((a, b) => a.name.localeCompare(b.name));
        setCpuSortOrder(sortedList);
        setCpuSortOrder("name");
    };

    const handleSortById = () => {
        const sortedList = [...cpus].sort((a, b) => a.id - b.id);
        setCpuSortOrder(sortedList);
        setCpuSortOrder("id");
    };

    return (
        <div>
            <button onClick={() => handleSortByPrice(cpus)}>Отсортировать по ценам</button>
            <button onClick={() => handleSortByName(cpus)}>Отсортировать по названиям</button>
            <button onClick={() => handleSortById(cpus)}>Отсортировать по давности появления в каталоге</button>
        </div>
    );
}

export default Sorts;