const express = require('express');
const bodyParser = require('body-parser');
const { spawn } = require('child_process');  // for calling py script

const app = express();
const port = 3200;

// parsing incoming JSON requests
app.use(bodyParser.json());

// post endpoint
app.post('/query', async (req, res) => {
  const query = req.body.query;

  if (!query) {
    return res.status(400).json({ error: 'Query is required' });
  }

  try {
    // calling py script
    const pythonProcess = spawn('python', ['../python/python_script.py', query]);

    let result = '';
    pythonProcess.stdout.on('data', (data) => {
      result += data.toString();
    });

    pythonProcess.on('close', (code) => {
      if (code !== 0) {
        return res.status(500).json({ error: 'Error executing Python script' });
      }
      res.json({ result });
    });
  } catch (error) {
    console.error('Error during query processing:', error);
    res.status(500).json({ error: 'An error occurred while processing the query' });
  }
});

// starting the express srvice
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});