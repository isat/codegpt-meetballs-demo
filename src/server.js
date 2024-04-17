// Load environment variables from the .env file.
require('dotenv').config();

// Import the express module to create a server.
const express = require('express');

// Import the helmet module for security best practices.
const helmet = require('helmet');

// Import the cors module to enable CORS (Cross-Origin Resource Sharing).
const cors = require('cors');

// Import the morgan module for logging HTTP requests.
const logger = require('morgan');

// Initialize the express application.
const app = express();

// Define the port on which the server will run. Use the value from the environment variables or default to 3000.
const PORT = process.env.PORT || 3000;

// Apply the helmet middleware to enhance API security.
app.use(helmet());

// Use CORS middleware to allow cross-origin requests.
app.use(cors());

// Apply the morgan middleware to log all requests in development mode.
app.use(logger('dev'));

// Enable express to parse JSON payloads in requests.
app.use(express.json());

// Define a route for the root path that sends a welcome message.
app.get('/', (req, res) => {
    res.send('Welcome to our API');
});

// Start the server on the defined PORT and log a message to the console.
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
