import React, { useState } from 'react';
import Selects from './Selects.js';
import Authorization from './Authorization.js';
import BudgetInput from './BudgetInput.js';

function App() {
    const [selectedItemsIds, setSelectedItemsIds] = useState([]);
    const handleSelectedItemsChange = (items) => {
        const itemIds = items.map((item) => item.id);
        setSelectedItemsIds(itemIds);
    };

    const [budget, setBudget] = useState('');
    const handleBudgetChange = (value) => {
        setBudget(value);
    };

    return (
        <div>
            <Selects onSelectedItemsChange={handleSelectedItemsChange} />
            <Authorization selectedItems={selectedItemsIds} />
            <BudgetInput onBudgetChange={handleBudgetChange} />
        </div>
    );
}

export default App;