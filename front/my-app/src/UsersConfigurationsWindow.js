import React, { useState, useEffect } from 'react';
import Modal from 'react-modal';
import axios from 'axios';


Modal.setAppElement('#root');

function ConfigurationList({ configurations }) {
    const [expandedConfigurations, setExpandedConfigurations] = useState([]);

    const toggleConfiguration = (configurationId) => {
        if (expandedConfigurations.includes(configurationId)) {
            setExpandedConfigurations((prevExpandedConfigurations) =>
                prevExpandedConfigurations.filter((id) => id !== configurationId)
            );
        } else {
            setExpandedConfigurations((prevExpandedConfigurations) => [...prevExpandedConfigurations, configurationId]);
        }
    };

    return (
        <div>
            <h1>Configurations</h1>
            {configurations.map((configuration) => {
                const configurationId = configuration[0];
                const username = configuration[1];
                const configurationTitle = `Configuration by ${username}`;

                return (
                    <div key={configurationId}>
                        <h2>{configurationTitle}</h2>
                        {expandedConfigurations.includes(configurationId) ? (
                            <>
                                <h3>CPU: {configuration[2]}</h3>
                                <h3>Cooler: {configuration[3]}</h3>
                                <h3>Motherboard: {configuration[4]}</h3>
                                <h3>RAM: {configuration[5]}</h3>
                                <h3>GPU: {configuration[6]}</h3>
                                <h3>SSD: {configuration[7]}</h3>
                                <h3>HDD: {configuration[8]}</h3>
                                <h3>Power: {configuration[9]}</h3>
                                <h3>Case: {configuration[10]}</h3>
                            </>
                        ) : null}
                        <hr />
                        <button onClick={() => toggleConfiguration(configurationId)}>
                            {expandedConfigurations.includes(configurationId) ? 'Hide Details' : 'Show Details'}
                        </button>
                    </div>
                );
            })}
        </div>
    );
}

function UsersConfigurations() {
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [configurations, setConfigurations] = useState([]);

    useEffect(() => {
        openModal();
    }, []);

    const openModal = async () => {
        try {
            const response = await axios.get('/getConfigurations');
            const data = response.data;
            setConfigurations(data);
            setIsModalOpen(true);
        } catch (error) {
            console.log('An error occurred while fetching configurations:', error);
        }
    };

    const closeModal = () => {
        setIsModalOpen(false);
    };

    return (
        <div>
            <Modal isOpen={isModalOpen} onRequestClose={closeModal}>
                <ConfigurationList configurations={configurations} />
                <button onClick={closeModal}>Close</button>
            </Modal>
        </div>
    );
}

export default UsersConfigurations;