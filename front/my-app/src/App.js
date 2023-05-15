import React, { useState } from 'react';
import Selects from './Selects.js';
import Authorization from './Authorization.js';

function App() {
    const [selectedItems, setSelectedItems] = useState([]);

    const handleSelectedItemsChange = (items) => {
        setSelectedItems(items);
    };

    return (
        <div>
            <Selects onSelectedItemsChange={handleSelectedItemsChange} />
            <Authorization selectedItems={selectedItems} />
        </div>
    );
}

export default App;
