import React, { useState } from 'react';
import axios from 'axios';

function Directions() {
    const [selectedValue, setSelectedValue] = useState('');
    const handleSelectChange = (event) => {
        const selectedOptionValue = event.target.value;
        setSelectedValue(selectedOptionValue);
        // Отправка выбранного значения на сервер Flask
        axios.post('/direction', { value: selectedOptionValue })
            .then(response => {
                console.log('Значение отправлено на сервер:', response.data);
            })
            .catch(error => {
                console.error('Ошибка при отправке значения на сервер:', error);
            });
    };

    return (
        <div style={{ marginTop: '47px', marginBottom: '100px', fontSize: '20px'}}> Выберите направление
            <div>
                <select style={{ fontSize: '20px' }} value={selectedValue} onChange={handleSelectChange}>
                    <option value="none">Не выбрано</option>
                    <option value="games">Игры</option>
                    <option value="vr">VR</option>
                    <option value="design">Графический дизайн</option>
                    <option value="3d">3D</option>
                    <option value="video editing">Монтаж видео</option>
                    <option value="video editing">Профессиональная</option>
                    <option value="office">Для офисных задач</option>
                    <option value="other">Другое</option>
                </select>
            </div>
        </div>
    );
}

export default Directions;
