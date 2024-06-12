const mongoose = require('mongoose');
const Book = require('./models/Book'); // Adjust path if needed

const uri = 'mongodb://localhost:27017/bookstore'; // Your MongoDB connection string

mongoose.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => {
    console.log('MongoDB connected');
    addBooks();
  })
  .catch(err => console.error('MongoDB connection error:', err));

const books = [
  { title: 'Book 1', author: 'Author 1', price: 10 },
  { title: 'Book 2', author: 'Author 2', price: 15 },
  { title: 'Book 3', author: 'Author 3', price: 20 },
  { title: 'Book 4', author: 'Author 4', price: 25 },
  { title: 'Book 5', author: 'Author 5', price: 30 },
  { title: 'Book 6', author: 'Author 6', price: 35 },
  { title: 'Book 7', author: 'Author 7', price: 40 },
  { title: 'Book 8', author: 'Author 8', price: 45 },
  { title: 'Book 9', author: 'Author 9', price: 50 },
  { title: 'Book 10', author: 'Author 10', price: 55 }
];

async function addBooks() {
  try {
    await Book.insertMany(books);
    console.log('Books added successfully');
    mongoose.connection.close();
  } catch (error) {
    console.error('Error adding books:', error);
    mongoose.connection.close();
  }
}
