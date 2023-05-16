import React, { useState } from 'react';
import axios from 'axios';

function Keywords() {
    const [keywords, setKeywords] = useState('');

    function handleSubmit(event) {
        event.preventDefault();

        // �������� �������� ���� �� ������
        axios.post('/keywords', { keywords })
            .then(response => {
                // ��������� ��������� ������ �� �������
                console.log('Keywords submitted:', response.data);
                // �������������� �������� ����� �������� �������� ����
            })
            .catch(error => {
                // ��������� ������
                console.error('Error submitting keywords:', error);
            });

        // ������� ���� ����� ����� ��������
        setKeywords('');
    }

    function handleChange(event) {
        // ���������� ��������� �������� ���� ��� ��������� ���� �����
        setKeywords(event.target.value);
    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label htmlFor="keywords" style={{ fontSize: "24px", marginLeft: "25px" }}>�������� �����:</label>
                <input
                    style={{ marginLeft: "10px", width: "75%", marginTop: "15px" }}
                    type="text"
                    id="keywords"
                    value={keywords}
                    onChange={handleChange}
                />
                <button type="submit">���������</button>
            </form>
        </div>
    );
}

export default Keywords;