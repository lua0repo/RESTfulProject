const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// In-memory contact storage
let contacts = [];

// CRUD Operations

// Create a new contact
app.post('/contacts', (req, res) => {
    const { name, email, phone } = req.body;
    const newContact = { id: contacts.length + 1, name, email, phone };
    contacts.push(newContact);
    res.status(201).json(newContact);
});

// Read all contacts
app.get('/contacts', (req, res) => {
    res.json(contacts);
});

// Read a single contact by ID
app.get('/contacts/:id', (req, res) => {
    const contact = contacts.find(c => c.id === parseInt(req.params.id));
    if (!contact) return res.status(404).send('Contact not found');
    res.json(contact);
});

// Update a contact by ID
app.put('/contacts/:id', (req, res) => {
    const contact = contacts.find(c => c.id === parseInt(req.params.id));
    if (!contact) return res.status(404).send('Contact not found');

    const { name, email, phone } = req.body;
    contact.name = name || contact.name;
    contact.email = email || contact.email;
    contact.phone = phone || contact.phone;

    res.json(contact);
});

// Delete a contact by ID
app.delete('/contacts/:id', (req, res) => {
    const contactIndex = contacts.findIndex(c => c.id === parseInt(req.params.id));
    if (contactIndex === -1) return res.status(404).send('Contact not found');

    contacts.splice(contactIndex, 1);
    res.status(204).send();
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
