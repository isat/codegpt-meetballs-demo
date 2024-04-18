// Load environment variables from the .env file to securely manage sensitive information like database passwords or API keys.
require('dotenv').config();

// Import and set up the Express framework to handle incoming HTTP requests and responses easily.
const express = require('express');

// Use the helmet middleware to set various HTTP headers to help protect the app from well-known web vulnerabilities by default.
const helmet = require('helmet');

// Enable CORS (Cross-Origin Resource Sharing) to allow the server to accept requests from different domains, which is useful for API services where you expect front-ends on other domains to access your API.
const cors = require('cors');

// Use the morgan logging middleware configured in 'dev' mode, which logs incoming requests to the console in a concise format useful during development.
const logger = require('morgan');

// Initialize the Express app. This is the core of our server where middleware and routes are registered.
const app = express();

// Define the server's port. Prioritize the PORT environment variable (useful in production environments like Heroku), and default to 3000 for local development.
const PORT = process.env.PORT || 3000;

// Apply security-related headers to all responses using the helmet middleware.
app.use(helmet());

// Allow cross-origin requests from any origin using the CORS middleware.
app.use(cors());

// Enable HTTP request logging to help with debugging during development.
app.use(logger('dev'));

// Enable the express.json() middleware to automatically parse JSON formatted request bodies, commonly used with API POST and PUT requests.
app.use(express.json());

// Define a simple route for the root URL that sends a welcome message. Useful for a simple health check or API index.
app.get('/', (req, res) => {
    res.send('Welcome to our API');
});

// Start the server on the defined port and log a success message to the console when the server successfully starts.
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
