# Web Dashboard

Real-time web-based dashboard for monitoring 5G core network metrics with Node.js, Express, and Socket.IO.

## Overview

This directory contains the implementation of a real-time web dashboard for monitoring 5G core network components. The dashboard provides a user-friendly interface to visualize network metrics and status information.

## Features

- Real-time metrics display using WebSocket
- Responsive web design
- Live updates every 5 seconds
- Network functions overview
- Subscriber status monitoring
- Performance metrics visualization

## Technology Stack

- **Node.js** - Server-side runtime environment
- **Express.js** - Web application framework
- **Socket.IO** - Real-time communication library
- **HTML5** - Markup language for content structure
- **CSS3** - Styling and layout
- **JavaScript** - Client-side scripting

## Directory Structure

```
web-dashboard/
├── public/              # Client-side assets
│   ├── index.html       # Main dashboard page
│   ├── styles.css       # CSS styling
│   └── script.js        # Client-side JavaScript
├── server.js            # Node.js server implementation
├── package.json         # Node.js dependencies
└── README.md            # This file
```

## Installation

### Prerequisites
- Node.js 14 or higher
- npm (Node Package Manager)

### Setup
```bash
# Navigate to the web-dashboard directory
cd web-dashboard

# Install dependencies
npm install
```

## Usage

### Starting the Server
```bash
node server.js
```

The server will start on port 3000 by default. Access the dashboard at `http://localhost:3000`.

### Configuration
The server can be configured by modifying the following parameters in [server.js](server.js):

- `PORT` - Server port (default: 3000)
- Metric update interval (default: 5000ms)
- Simulated data ranges

## Architecture

### Server-Side (server.js)
- Express.js web server
- Socket.IO for real-time communication
- Simulated metrics data generation
- Static file serving for client assets

### Client-Side (public/)
- [index.html](public/index.html) - Main dashboard page
- [styles.css](public/styles.css) - CSS styling
- [script.js](public/script.js) - Client-side JavaScript for real-time updates

### Data Flow
1. Server generates simulated metrics data
2. Server emits metrics data to all connected clients via Socket.IO
3. Clients receive data and update the UI in real-time
4. Process repeats every 5 seconds

## Components

### Main Dashboard Page (index.html)
- Header with system information
- Network functions status panels
- Subscriber information display
- Performance metrics charts
- Real-time status indicators

### Styling (styles.css)
- Responsive grid layout
- Modern color scheme
- Card-based component design
- Real-time status indicators
- Mobile-friendly design

### Client Script (script.js)
- Socket.IO client connection
- Real-time data handling
- DOM manipulation for UI updates
- Chart rendering and updates
- Error handling

## API Endpoints

### WebSocket Events
- `metrics` - Real-time metrics data
- `networkFunctions` - Network functions information
- `subscribers` - Subscriber status data
- `connect` - Client connection event
- `disconnect` - Client disconnection event

### HTTP Endpoints
- `GET /` - Serve the main dashboard page
- `GET /script.js` - Serve client-side JavaScript
- `GET /styles.css` - Serve CSS stylesheet

## Customization

### Modifying the Dashboard
1. Edit [public/index.html](public/index.html) to change the layout
2. Update [public/styles.css](public/styles.css) to modify styling
3. Modify [public/script.js](public/script.js) to change behavior
4. Adjust data simulation in [server.js](server.js)

### Adding New Metrics
1. Add new data fields in the simulation functions
2. Emit new data through Socket.IO
3. Update client-side JavaScript to handle new data
4. Modify the HTML to display new metrics

### Changing Update Interval
Modify the `setInterval` duration in [server.js](server.js):
```javascript
// Current setting (5 seconds)
setInterval(() => {
  const metrics = getMetricsData();
  io.emit('metrics', metrics);
}, 5000);
```

## Testing

### Server Testing
```bash
# Check if server starts correctly
node server.js

# Verify HTTP endpoints
curl -I http://localhost:3000
```

### Client Testing
1. Open browser to `http://localhost:3000`
2. Verify real-time updates
3. Check console for JavaScript errors
4. Test on different screen sizes

## Deployment

### Production Deployment
1. Set environment variables:
   ```bash
   export PORT=80
   ```
2. Use a process manager like PM2:
   ```bash
   npm install -g pm2
   pm2 start server.js
   ```

### Docker Deployment
Create a Dockerfile:
```dockerfile
FROM node:14
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]
```

Build and run:
```bash
docker build -t 5g-dashboard .
docker run -p 3000:3000 5g-dashboard
```

## Troubleshooting

### Common Issues

#### Server Not Starting
1. Check Node.js installation:
   ```bash
   node --version
   npm --version
   ```

2. Verify dependencies:
   ```bash
   npm install
   ```

#### Dashboard Not Loading
1. Check browser console for errors
2. Verify server is running:
   ```bash
   curl http://localhost:3000
   ```

3. Check network tab for failed requests

#### Real-Time Updates Not Working
1. Verify Socket.IO connection in browser console
2. Check server logs for Socket.IO errors
3. Confirm setInterval is working in server.js

## Security Considerations

### Production Security
- Use HTTPS in production
- Implement proper authentication
- Add rate limiting
- Sanitize all input data
- Keep dependencies updated

### Development Security
- Use localhost only for development
- Don't expose sensitive data in client code
- Regularly update npm packages

## Performance Optimization

### Client-Side Optimization
- Minimize DOM manipulations
- Use efficient JavaScript
- Optimize CSS selectors
- Implement lazy loading where appropriate

### Server-Side Optimization
- Use efficient data structures
- Optimize Socket.IO configuration
- Implement connection pooling
- Monitor memory usage

## Contributing

To contribute to the web dashboard:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Development Guidelines
- Follow existing code style
- Add comments for complex logic
- Test changes thoroughly
- Update documentation as needed

## License

This project is provided as part of the 5G Core Management Prototype for educational purposes.