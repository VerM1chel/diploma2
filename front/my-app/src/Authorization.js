import React, { useState, useEffect } from 'react';
import UsersConfigurationsWindow from './UsersConfigurationsWindow';
import axios from 'axios';

function LoginModal(props) {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [isRegistering, setIsRegistering] = useState(false);
    const [error, setError] = useState(null);
    const [isSuccessful, setIsSuccessful] = useState(false);

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
            handleLogin(username, password);
        }
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
        if (username.trim() === "" || password.trim() === "") {
            alert("Пожалуйста, введите имя пользователя и пароль");
            return;
        }
        axios
            .post('/register', { username, password })
            .then(response => {
                // Registration successful
                alert('Пользователь успешно зарегистрирован!');
                // Clear the username and password fields
                setUsername("");
                setPassword("");
                // Close the modal and navigate to another page
                props.onClose();
            })
            .catch(error => {
                // Registration failed
                alert('Не удалось зарегистрировать пользователя. Пожалуйста, попробуйте снова.');
            });
    }

    function handleLogin(username, password) {
        // Send the login data to the backend server
        axios
            .post('/login', { username, password })
            .then(response => {
                // Login successful
                if (response.data.success) {
                    // Open the "User Configurations" window

                    // Clear the username and password fields
                    setUsername("");
                    setPassword("");
                    // Close the modal and navigate to another page
                    props.onClose();
                    props.onSuccessfulLogin(true, username); // Вызов функции обратного вызова для передачи значения isSuccessful
                } else {
                    // Login failed
                    alert('Неверное имя пользователя или пароль. Пожалуйста, попробуйте снова');
                    // Clear the password field
                    setPassword("");
                }
            })
            .catch(error => {
                // Login failed
                alert('Ошибка при попытке входа. Пожалуйста, попробуйте снова');
            });
    }

    useEffect(() => {
        if (isSuccessful && props.onSuccessfulLogin) {
            props.onSuccessfulLogin(isSuccessful); // Передача значения isSuccessful через функцию обратного вызова
        }
    }, [isSuccessful, props]);

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

function Authorization(selectedItems) {
    const [isLoginModalOpen, setIsLoginModalOpen] = useState(false);
    const [isSuccessful, setIsSuccessful] = useState(false);
    const [loggedInUser, setLoggedInUser] = useState(""); // Добавлено состояние loggedInUser
    const [showUsersConfigurations, setShowUsersConfigurations] = useState(false); // Добавлено состояние для отображения окна с конфигурациями пользователей

    function handleShareClick(event) {
        setIsLoginModalOpen(true);
    }
    function handleLoginModalClose(event) {
        setIsLoginModalOpen(false);
    }

    function handleSuccessfulLogin(success, username) {
        setIsSuccessful(success); // Обновление значения isSuccessful в компоненте Authorization
        setLoggedInUser(username); // Сохранение имени пользователя в состоянии
        setShowUsersConfigurations(false); // Сброс флага отображения окна с конфигурациями пользователей при успешном входе
    }
    function handleShowUsersConfigurations() {
        setShowUsersConfigurations(true); // Устанавливаем флаг отображения окна с конфигурациями пользователей
    }
    function handleHideUsersConfigurations() {
        setShowUsersConfigurations(false);
    }

    useEffect(() => {
        if (isSuccessful) {
            saveConfiguration(selectedItems); // Вызываем функцию saveConfiguration, когда isSuccessful равно true
        }
    }, [isSuccessful, selectedItems]);

    function saveConfiguration(selectedItems) {
        // Send the selectedItems to the Flask backend
        axios
            .post('/saveConfiguration', { selectedItems, username: loggedInUser })
            .then(response => {
                // Configuration saved successfully
                alert('Конфигурация сохранена!');
                setIsSuccessful(true); // Обновляем переменную состояния
            })
            .catch(error => {
                // Error occurred while saving configuration
                alert('Ошибка при сохранении конфигурации');
            });
    }

    return (
        <div>
            {showUsersConfigurations && (
                <div style={{ position: "fixed", top: 0, left: 0, right: 0, bottom: 0, backgroundColor: "rgba(0, 0, 0, 0.5)", zIndex: 999 }}>
                    <div style={{ position: "absolute", top: "50%", left: "50%", transform: "translate(-50%, -50%)", backgroundColor: "#fff", padding: "20px", borderRadius: "10px" }}>
                        <UsersConfigurationsWindow />
                        <button onClick={handleHideUsersConfigurations}>Закрыть</button>
                    </div>
                </div>
            )}

            {!showUsersConfigurations && (
                <button
                    style={{ width: "25%", height: "3em", margin: "5px", fontSize: "20px", marginTop: "150px" }}
                    onClick={handleShowUsersConfigurations}
                >
                    Посмотреть конфигурации других пользователей
                </button>
            )}
            <button
                style={{ width: "25%", height: "3em", margin: "5px", fontSize: "20px", marginTop: "150px" }}
                onClick={handleShareClick}
            >
                {isLoginModalOpen ? "Регистрация" : "Поделиться своей конфигурацией с другими пользователями"}
            </button>
            {isLoginModalOpen && <LoginModal onClose={handleLoginModalClose} onSuccessfulLogin={handleSuccessfulLogin} />}
        </div>
    );
}
export default Authorization;