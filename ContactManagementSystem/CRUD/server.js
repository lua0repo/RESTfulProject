const Contact = require('./Contact');

// Create a new contact
app.post('/contacts', async (req, res) => {
    const { name, email, phone } = req.body;
    const newContact = new Contact({ name, email, phone });
    await newContact.save();
    res.status(201).json(newContact);
});

// Read all contacts
app.get('/contacts', async (req, res) => {
    const contacts = await Contact.find();
    res.json(contacts);
});

// Read a single contact by ID
app.get('/contacts/:id', async (req, res) => {
    const contact = await Contact.findById(req.params.id);
    if (!contact) return res.status(404).send('Contact not found');
    res.json(contact);
});

// Update a contact by ID
app.put('/contacts/:id', async (req, res) => {
    const contact = await Contact.findById(req.params.id);
    if (!contact) return res.status(404).send('Contact not found');

    const { name, email, phone } = req.body;
    contact.name = name || contact.name;
    contact.email = email || contact.email;
    contact.phone = phone || contact.phone;

    await contact.save();
    res.json(contact);
});

// Delete a contact by ID
app.delete('/contacts/:id', async (req, res) => {
    const contact = await Contact.findByIdAndDelete(req.params.id);
    if (!contact) return res.status(404).send('Contact not found');
    res.status(204).send();
});
