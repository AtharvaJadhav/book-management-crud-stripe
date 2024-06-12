const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const bodyParser = require('body-parser');
require('dotenv').config();

const app = express();

app.use(cors());
app.use(bodyParser.json());

const bookRoutes = require('./routes/books');
const stripeRoutes = require('./routes/stripe');

app.use('/books', bookRoutes);
app.use('/stripe', stripeRoutes);

const PORT = process.env.PORT || 5001;
const uri = process.env.MONGODB_URI;

mongoose.connect(uri)
  .then(() => console.log("MongoDB connected successfully"))
  .catch(err => console.error("MongoDB connection error:", err));

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
