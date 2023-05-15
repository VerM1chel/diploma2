import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Selects from './Selects.js';
import Autorization from './Autorization.js';

function App() {
    return (
        <div>
            <Selects />
            <Autorization />
        </div>
    );
}

export default App;
