import React, { useState } from 'react';
import axios from 'axios'

function BudgetInput({ onBudgetChange }) {
    const [budget, setBudget] = useState('');

    const sendBudgetToServer = async () => {
        try {
            const response = await axios.post('/updateBudget', { budget: budget });
            console.log('Значение бюджета отправлено на сервер');
        } catch (error) {
            console.error('Произошла ошибка при отправке значения бюджета:', error);
        }
    };


    const handleKeyDown = (event) => {
        if (event.key === 'Enter' && budget != '') {
            sendBudgetToServer();
        }
    };

    const handleInputChange = (event) => {
        const { value } = event.target;

        // Проверяем, является ли введенное значение числом или пустой строкой
        if (/^\d*\.?\d*$/.test(value) || value === '') {
            setBudget(value);
            onBudgetChange(value);
        }
    };

    return (
        <div style={{ display: 'flex', flexDirection: 'column', justifyContent: 'flex-start', marginTop: '20px' }}>
            <div style={{ fontSize: '24px', marginLeft: '25px', marginBottom: '10px' }}>Введите свой бюджет:</div>
            <input
                type="text"
                style={{ width: '10%', marginLeft: '27px' }}
                value={budget}
                onChange={(event) => setBudget(event.target.value)}
                onKeyDown={handleKeyDown}
            />
        </div>
    );
}

export default BudgetInput;
