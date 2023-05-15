import React, { useState } from 'react';
import axios from 'axios';

function LoginModal(props) {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [isRegistering, setIsRegistering] = useState(false);

    function handleUsernameChange(event) {
        setUsername(event.target.value);
    }

    function handlePasswordChange(event) {
        setPassword(event.target.value);
    }

    function handleAction() {
        if (isRegistering) {
            handleRegistration(username, password);
        } else {
            // Here goes the functionality for login
            // ... (your code for login)
        }

        // Close the modal and navigate to another page
        props.onClose();
    }

    function toggleRegisterMode() {
        setIsRegistering(!isRegistering);
    }

    function handleClose(event) {
        // Reset the username and password fields
        setUsername("");
        setPassword("");

        // Закрываем модальное окно
        props.onClose();
    }

    function handleRegistration(username, password) {
        // Send the registration data to the backend server
        axios
            .post('/register', { username, password })
            .then(response => {
                // Registration successful
                alert('Пользователь успешно зарегистрирован!');
            })
            .catch(error => {
                // Registration failed
                alert('Не удалось зарегистрировать пользователя. Пожалуйста, попробуйте снова.');
            });
    }

    return (
        <div style={{ position: "fixed", top: 0, left: 0, right: 0, bottom: 0, backgroundColor: "rgba(0, 0, 0, 0.5)", zIndex: 999 }}>
            <div style={{ position: "absolute", top: "50%", left: "50%", transform: "translate(-50%, -50%)", backgroundColor: "#fff", padding: "20px", borderRadius: "10px" }}>
                <h2>{isRegistering ? "Регистрация" : "Авторизация"}</h2>
                <label htmlFor="username">Логин:</label>
                <input type="text" id="username" value={username} onChange={handleUsernameChange} />
                <br />
                <label htmlFor="password">Пароль:</label>
                <input type="password" id="password" value={password} onChange={handlePasswordChange} />
                <br />
                <button onClick={handleAction}>{isRegistering ? "Сохранить" : "Войти"}</button>
                {!isRegistering && (
                    <button onClick={toggleRegisterMode}>Регистрация</button>
                )}
                <button onClick={handleClose}>Отмена</button>
            </div>
        </div>
    );
}

const userDatabase = [
    { username: 'john', password: 'password1' },
    { username: 'jane', password: 'password2' },
    // Add more user entries as needed
];

function checkUserExistsInDatabase(username) {
    // Check if the user exists in the database
    return userDatabase.some(user => user.username === username);
}

function Autorization() {
    const [isLoginModalOpen, setIsLoginModalOpen] = useState(false);

    function handleShareClick(event) {
        setIsLoginModalOpen(true);
    }

    function handleLoginModalClose(event) {
        setIsLoginModalOpen(false);
    }

    return (
        <div>
            <button
                style={{
                    width: "25%",
                    height: "3em",
                    margin: "5px",
                    fontSize: "20px",
                    marginTop: "150px"
                }}
                onClick={handleShareClick}
            >
                {isLoginModalOpen ? "Регистрация" : "Поделиться своей конфигурацией с другими пользователями"}
            </button>
            {isLoginModalOpen && <LoginModal onClose={handleLoginModalClose} />}
        </div>
    );
} export default Autorization;

function handleRegistration(username, password) {
    // Send the registration data to the backend server
    axios
        .post('/register', { username, password })
        .then(response => {
            // Registration successful
            alert('Пользователь успешно зарегистрирован!');
        })
        .catch(error => {
            // Registration failed
            alert('Не удалось зарегистрировать пользователя. Пожалуйста, попробуйте снова.');
        });
}
