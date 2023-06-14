import React, { useState } from 'react';
import axios from 'axios'

function BudgetInput({ onBudgetChange }) {
    const [budget, setBudget] = useState('');
    const [isButtonClicked, setIsButtonClicked] = useState(false);


    const sendBudgetToServer = async () => {
        try {
            if (budget < 400) {
                alert('Пожалуйста, увеличьте бюджет!');
                return;
            }
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
    const handleButtonClick = () => {
        if (budget !== '') {
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
        <div style={{ display: 'flex', flexDirection: 'column', justifyContent: 'flex-start', marginTop: '45px', marginBottom: '5px', fontSize: "20px" }}>Введите свой бюджет:
            <div style={{ width: '200px', display: 'flex', flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center' }}>
                <input
                    type="text"
                    style={{ width: '70%', height: '1.5em', fontSize: '24px', flexGrow: 1 }}
                    value={budget}
                    onChange={(event) => setBudget(event.target.value)}
                    onKeyDown={handleKeyDown}
                />
                <button
                    style={{ width: '30%', height: '1.5em', margin: '5px', fontSize: '20px' }}
                    onClick={handleButtonClick}
                >
                    OK
                </button>
            </div>
        </div>
    );

  
}

export default BudgetInput;
