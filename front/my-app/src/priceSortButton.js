import React from 'react';
import { Button } from 'react-bootstrap';

function SortButton({ lists }) {
    const sortedLists = lists.map((list) => {
        // Check if the list is an array
        if (Array.isArray(list)) {
            return list.sort((a, b) => a.price - b.price);
        }
        // If the list is not an array, return an empty array
        return [];
    });

    return (
        <Button variant="primary" onClick={() => console.log(sortedLists)}>
            Sort Lists
        </Button>
    );
}

export default SortButton;
