//import React, { useState, useEffect } from 'react';


//function Sorts({ cpus, coolers, motherboards, rams, gpus, ssds, hdds, powers, casePCs }) {
//    const [cpuSortOrder, setCpuSortOrder] = useState("");
//    const [coolerSortOrder, setCoolerSortOrder] = useState("");
//    const [motherboardSortOrder, setMotherboardSortOrder] = useState("");
//    const [ramSortOrder, setRamSortOrder] = useState("");
//    const [gpuSortOrder, setGpuSortOrder] = useState("");
//    const [ssdSortOrder, setSsdSortOrder] = useState("");
//    const [hddSortOrder, setHddSortOrder] = useState("");
//    const [powerSortOrder, setPowerSortOrder] = useState("");
//    const [caseSortOrder, setCaseSortOrder] = useState("");

//    const handleSortByPrice = () => {
//        const sortedCpus = [...cpus].sort((a, b) => a.price.toString().localeCompare(b.price.toString()));
//        const sortedCoolers = [...coolers].sort((a, b) => a.price.toString().localeCompare(b.price.toString()));
//        const sortedMotherboards = [...motherboards].sort((a, b) => a.price.toString().localeCompare(b.price.toString()));
//        const sortedRams = [...rams].sort((a, b) => a.price.toString().localeCompare(b.price.toString()));
//        const sortedGpus = [...gpus].sort((a, b) => a.price.toString().localeCompare(b.price.toString()));
//        const sortedSsds = [...ssds].sort((a, b) => a.price.toString().localeCompare(b.price.toString()));
//        const sortedHdds = [...hdds].sort((a, b) => a.price.toString().localeCompare(b.price.toString()));
//        const sortedPowers = [...powers].sort((a, b) => a.price.toString().localeCompare(b.price.toString()));
//        const sortedCasePCs = [...casePCs].sort((a, b) => a.price.toString().localeCompare(b.price.toString()));

//        setCpuSortOrder("price");
//        setCoolerSortOrder("price");
//        setMotherboardSortOrder("price");
//        setRamSortOrder("price");
//        setGpuSortOrder("price");
//        setSsdSortOrder("price");
//        setHddSortOrder("price");
//        setPowerSortOrder("price");
//        setCaseSortOrder("price");

//        setCpuSortOrder(sortedCpus);
//        setCoolerSortOrder(sortedCoolers);
//        setMotherboardSortOrder(sortedMotherboards);
//        setRamSortOrder(sortedRams);
//        setGpuSortOrder(sortedGpus);
//        setSsdSortOrder(sortedSsds);
//        setHddSortOrder(sortedHdds);
//        setPowerSortOrder(sortedPowers);
//        setCaseSortOrder(sortedCasePCs);

//      cpuSortOrder: sortedCpus,
//      coolerSortOrder: sortedCoolers,
//      motherboardSortOrder: sortedMotherboards,
//      ramSortOrder: sortedRams,
//      gpuSortOrder: sortedGpus,
//      ssdSortOrder: sortedSsds,
//      hddSortOrder: sortedHdds,
//      powerSortOrder: sortedPowers,
//      caseSortOrder: sortedCasePCs
//    });
//    };

//    const handleSortByName = () => {
//        const sortedCpus = [...cpus].sort((a, b) => a.name.localeCompare(b.name));
//        const sortedCoolers = [...coolers].sort((a, b) => a.name.localeCompare(b.name));
//        const sortedMotherboards = [...motherboards].sort((a, b) => a.name.localeCompare(b.name));
//        const sortedRams = [...rams].sort((a, b) => a.name.localeCompare(b.name));
//        const sortedGpus = [...gpus].sort((a, b) => a.name.localeCompare(b.name));
//        const sortedSsds = [...ssds].sort((a, b) => a.name.localeCompare(b.name));
//        const sortedHdds = [...hdds].sort((a, b) => a.name.localeCompare(b.name));
//        const sortedPowers = [...powers].sort((a, b) => a.name.localeCompare(b.name));
//        const sortedCasePCs = [...casePCs].sort((a, b) => a.name.localeCompare(b.name));

//        setCpuSortOrder("name");
//        setCoolerSortOrder("name");
//        setMotherboardSortOrder("name");
//        setRamSortOrder("name");
//        setGpuSortOrder("name");
//        setSsdSortOrder("name");
//        setHddSortOrder("name");
//        setPowerSortOrder("name");
//        setCaseSortOrder("name");

//        setCpuSortOrder(sortedCpus);
//        setCoolerSortOrder(sortedCoolers);
//        setMotherboardSortOrder(sortedMotherboards);
//        setRamSortOrder(sortedRams);
//        setGpuSortOrder(sortedGpus);
//        setSsdSortOrder(sortedSsds);
//        setHddSortOrder(sortedHdds);
//        setPowerSortOrder(sortedPowers);
//        setCaseSortOrder(sortedCasePCs);
//    };

//    const handleSortById = () => {
//        const sortedCpus = [...cpus].sort((a, b) => a.id.localeCompare(b.id));
//        const sortedCoolers = [...coolers].sort((a, b) => a.id.localeCompare(b.id));
//        const sortedMotherboards = [...motherboards].sort((a, b) => a.id.localeCompare(b.id));
//        const sortedRams = [...rams].sort((a, b) => a.id.localeCompare(b.id));
//        const sortedGpus = [...gpus].sort((a, b) => a.id.localeCompare(b.id));
//        const sortedSsds = [...ssds].sort((a, b) => a.id.localeCompare(b.id));
//        const sortedHdds = [...hdds].sort((a, b) => a.id.localeCompare(b.id));
//        const sortedPowers = [...powers].sort((a, b) => a.id.localeCompare(b.id));
//        const sortedCasePCs = [...casePCs].sort((a, b) => a.id.localeCompare(b.id));

//        setCpuSortOrder("id");
//        setCoolerSortOrder("id");
//        setMotherboardSortOrder("id");
//        setRamSortOrder("id");
//        setGpuSortOrder("id");
//        setSsdSortOrder("id");
//        setHddSortOrder("id");
//        setPowerSortOrder("id");
//        setCaseSortOrder("id");

//        setCpuSortOrder(sortedCpus);
//        setCoolerSortOrder(sortedCoolers);
//        setMotherboardSortOrder(sortedMotherboards);
//        setRamSortOrder(sortedRams);
//        setGpuSortOrder(sortedGpus);
//        setSsdSortOrder(sortedSsds);
//        setHddSortOrder(sortedHdds);
//        setPowerSortOrder(sortedPowers);
//        setCaseSortOrder(sortedCasePCs);
//    };

//    return (
//        <div>
//            <button onClick={handleSortByPrice}>Отсортировать по ценам</button>
//            <button onClick={handleSortByName}>Отсортировать по названиям</button>
//            <button onClick={handleSortById}>Отсортировать по давности появления в каталоге</button>
//        </div>
//    );
//} export default Sorts;