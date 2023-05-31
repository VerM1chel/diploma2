import React, { useState } from 'react';
import Selects from './Selects.js';
import Directions from './Directions.js'
import SaveAsText from './SaveAsText.js'
import Keywords from './Keywords.js'
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
            <div style={{ display: 'flex' }}>
                <Selects onSelectedItemsChange={handleSelectedItemsChange} />
                <div style={{marginLeft: '-115px'}}>
                    <Directions />
                    <SaveAsText />
                    <BudgetInput onBudgetChange={handleBudgetChange} />
                </div>
            </div>
            <Keywords />
           
            <Authorization selectedItems={selectedItemsIds} />
            
        </div>
    );
} 

export default App;