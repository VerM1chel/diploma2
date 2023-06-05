import React, { useState } from 'react';
import axios from 'axios';

function Keywords() {
    const [keywords, setKeywords] = useState('');

    function handleSubmit(event) {
        event.preventDefault();

        // Отправка ключевых слов на сервер
        axios.post('/keywords', { keywords })
            .then(response => {
                // Обработка успешного ответа от сервера
                console.log('Keywords submitted:', response.data);
                // Дополнительные действия после отправки ключевых слов
            })
            .catch(error => {
                // Обработка ошибки
                console.error('Error submitting keywords:', error);
            });
    }

    function handleChange(event) {
        // Обновление состояния ключевых слов при изменении поля ввода
        setKeywords(event.target.value);
    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label htmlFor="keywords" style={{ fontSize: "24px", marginLeft: "25px" }}>Ключевые слова:</label>
                <input
                    style={{ fontSize: "20px", marginLeft: "10px", width: "70%", marginTop: "15px", marginRight: "10px" }}
                    type="text"
                    id="keywords"
                    value={keywords}
                    onChange={handleChange}
                    autocomplete="off"
                />
                <button style={{ fontSize: "20px" }} type="submit">Отправить</button>
            </form>
        </div>
    );
}

export default Keywords;