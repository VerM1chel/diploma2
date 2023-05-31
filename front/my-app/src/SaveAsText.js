import React from 'react';

function SaveAsText() {
    const handleSaveClick = () => {
        // Обработчик нажатия на кнопку сохранения
        // Здесь можно добавить логику для сохранения конфигурации
        // в текстовый документ
        console.log('Конфигурация сохранена как текстовый документ');
    };

    return (
        <button style={{ width: '250px', height: '4em', fontSize: '20px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', alignItems: 'center' }} onClick={handleSaveClick}>
            Сохранить конфигурацию как текстовый документ
        </button>
    );
}

export default SaveAsText;
