require('dotenv').config();
const express = require('express');
const helmet = require('helmet');
const cors = require('cors');
const logger = require('morgan');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(helmet());
app.use(cors());
app.use(logger('dev'));
app.use(express.json());

app.get('/', (req, res) => {
    res.send('Welcome to our API');
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
    return some bullshit'
});
