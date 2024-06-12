# Book Management MERN Application

This is a full-stack application for managing books, built with the MERN stack (MongoDB, Express, React, Node.js). It includes CRUD operations for books and integrates Stripe for payment processing.

## Features

- Add, update, delete, and list books
- Add books to a cart
- Checkout with Stripe
- Responsive design

## Technologies Used

- MongoDB
- Express.js
- React.js
- Node.js
- Stripe

## Getting Started

### Prerequisites

- Node.js
- MongoDB
- Stripe account

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AtharvaJadhav/book-management-crud-stripe.git
   cd book-management-mern
   ```
   
2. Install dependencies for the backend:

  ```bash
  npm install
  ```

3. Install dependencies for the frontend:

  ```bash
  cd client
  npm install
  cd ..
  ```

4. Set up environment variables:

Create a .env file in the root directory and add the following:

MONGODB_URI=your-mongodb-uri
STRIPE_SECRET_KEY=your-stripe-secret-key
PORT=5001

### Running the Application

1. Start the backend server:

```bash
npm start
```

2. Start the frontend development server:

```bash
cd client
npm start
```

3. Open your browser and navigate to http://localhost:3000

