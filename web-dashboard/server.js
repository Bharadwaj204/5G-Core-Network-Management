const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const path = require('path');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

// Serve static files from the public directory
app.use(express.static(path.join(__dirname, 'public')));

// Serve the main page
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Simulate metrics data
function getMetricsData() {
  return {
    timestamp: new Date().toISOString(),
    amf: {
      activeSessions: Math.floor(Math.random() * 500) + 1000,
      cpuUtilization: Math.floor(Math.random() * 40) + 30,
      memoryUtilization: Math.floor(Math.random() * 30) + 50
    },
    smf: {
      activePduSessions: Math.floor(Math.random() * 400) + 900,
      cpuUtilization: Math.floor(Math.random() * 35) + 25,
      memoryUtilization: Math.floor(Math.random() * 30) + 45
    },
    upf: {
      activeUsers: Math.floor(Math.random() * 400) + 800,
      throughput: Math.floor(Math.random() * 50000000) + 100000000,
      packetLoss: (Math.random() * 0.05 + 0.01).toFixed(2)
    }
  };
}

// Simulate network functions data
function getNetworkFunctionsData() {
  return {
    amf: [
      { id: 'amf-001', status: 'active', capacity: 45, mcc: '001', mnc: '01' },
      { id: 'amf-002', status: 'active', capacity: 30, mcc: '001', mnc: '01' }
    ],
    smf: [
      { id: 'smf-001', status: 'active', capacity: 35, upf: ['upf-001', 'upf-002'] },
      { id: 'smf-002', status: 'maintenance', capacity: 0, upf: [] }
    ],
    upf: [
      { id: 'upf-001', status: 'active', capacity: 25, address: '10.0.0.10' },
      { id: 'upf-002', status: 'active', capacity: 40, address: '10.0.0.11' }
    ]
  };
}

// Simulate subscribers data
function getSubscribersData() {
  return {
    subscribers: [
      { imsi: '001010000000001', msisdn: '1234567890', status: 'active', apn: 'internet' },
      { imsi: '001010000000002', msisdn: '1234567891', status: 'active', apn: 'internet' },
      { imsi: '001010000000003', msisdn: '1234567892', status: 'inactive', apn: 'internet' }
    ]
  };
}

// Send real-time metrics to connected clients
setInterval(() => {
  const metrics = getMetricsData();
  io.emit('metrics', metrics);
}, 5000);

// Handle socket connections
io.on('connection', (socket) => {
  console.log('A user connected');
  
  // Send initial data
  socket.emit('networkFunctions', getNetworkFunctionsData());
  socket.emit('subscribers', getSubscribersData());
  socket.emit('metrics', getMetricsData());
  
  socket.on('disconnect', () => {
    console.log('A user disconnected');
  });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`5G Core Dashboard server running on port ${PORT}`);
});