const mongoose = require('mongoose');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/contact_management', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log('MongoDB connected'))
.catch(err => console.error('MongoDB connection error:', err));
