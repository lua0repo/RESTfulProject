// server.js
const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(bodyParser.json());

// In-memory data store
let tasks = [];
let currentId = 1;

// Create a task
app.post('/tasks', (req, res) => {
    const task = {
        id: currentId++,
        title: req.body.title,
        completed: false,
    };
    tasks.push(task);
    res.status(201).json(task);
});

// Read all tasks
app.get('/tasks', (req, res) => {
    res.json(tasks);
});

// Read a single task
app.get('/tasks/:id', (req, res) => {
    const task = tasks.find(t => t.id === parseInt(req.params.id));
    if (!task) return res.status(404).send('Task not found');
    res.json(task);
});

// Update a task
app.put('/tasks/:id', (req, res) => {
    const task = tasks.find(t => t.id === parseInt(req.params.id));
    if (!task) return res.status(404).send('Task not found');

    task.title = req.body.title !== undefined ? req.body.title : task.title;
    task.completed = req.body.completed !== undefined ? req.body.completed : task.completed;

    res.json(task);
});

// Delete a task
app.delete('/tasks/:id', (req, res) => {
    const taskIndex = tasks.findIndex(t => t.id === parseInt(req.params.id));
    if (taskIndex === -1) return res.status(404).send('Task not found');

    tasks.splice(taskIndex, 1);
    res.status(204).send();
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
