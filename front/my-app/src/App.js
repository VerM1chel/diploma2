import React, { useState } from 'react';
import Selects from './Selects.js';
import Authorization from './Authorization.js';
import UsersConfigurationsWindow from './UsersConfigurationsWindow.js';

function App() {
    const [selectedItemsIds, setSelectedItemsIds] = useState([]);

    const handleSelectedItemsChange = (items) => {
        const itemIds = items.map((item) => item.id);
        setSelectedItemsIds(itemIds);
    };

    return (
        <div>
            <Selects onSelectedItemsChange={handleSelectedItemsChange} />
            <Authorization selectedItems={selectedItemsIds} />
            <UsersConfigurationsWindow />
        </div>
    );
}

export default App;
