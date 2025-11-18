# Dashboard

Real-time monitoring and visualization dashboard for 5G core network metrics using Grafana and custom web interface.

## Overview

The dashboard component provides visual monitoring capabilities for the 5G core network management system. It includes both a custom web-based dashboard and Grafana configuration for professional monitoring and alerting.

## Components

### Custom Web Dashboard
Location: [../../web-dashboard/](../../web-dashboard/)
- Real-time web interface built with Node.js, Express, and Socket.IO
- Displays live metrics for AMF, SMF, and UPF
- Responsive design for various screen sizes
- WebSocket-based real-time updates

### Grafana Dashboard
Location: [grafana/](grafana/)
- Pre-configured Grafana dashboard for 5G core metrics
- Custom panels for network function monitoring
- Integration with SNMP data source
- Professional visualization and alerting capabilities

## Custom Web Dashboard

### Features
- Real-time metrics display
- Network functions overview
- Subscriber status monitoring
- Auto-refreshing data (5-second intervals)
- Responsive web design

### Technology Stack
- Node.js
- Express.js
- Socket.IO for real-time communication
- HTML5, CSS3, JavaScript

### Installation
```bash
cd ../../web-dashboard
npm install
```

### Usage
```bash
cd ../../web-dashboard
node server.js
```

Access the dashboard at `http://localhost:3000`

### Architecture
The web dashboard consists of:
1. **Server** - Node.js server with Express and Socket.IO
2. **Client** - HTML/CSS/JavaScript frontend
3. **Data Flow** - Real-time updates via WebSocket

## Grafana Dashboard

### Features
- Professional monitoring dashboard
- Custom panels for 5G core metrics
- Historical data visualization
- Alerting capabilities
- Multiple data source support

### Configuration
The Grafana configuration includes:
- [dashboard.json](grafana/dashboard.json) - Dashboard layout and panels
- [datasource.yaml](grafana/datasource.yaml) - SNMP data source configuration

### Installation
1. Install Grafana
2. Import the dashboard configuration:
   ```bash
   cp grafana/dashboard.json /var/lib/grafana/dashboards/
   cp grafana/datasource.yaml /etc/grafana/provisioning/datasources/
   ```

### Usage
1. Start Grafana server
2. Access Grafana at `http://localhost:3000`
3. The 5G Core dashboard will be available in the dashboard list

## Integration

### With SNMP Monitor
The dashboard integrates with the SNMP monitor component:
- Custom Web Dashboard: Connects via REST API to SNMP agent
- Grafana: Uses SNMP data source directly

### With Management Plane
The dashboard displays data from all management plane components:
- Network functions status (AMF, SMF, UPF)
- Subscriber information
- Session details
- QoS profiles

## Data Visualization

### AMF Metrics
- Active Sessions
- CPU Utilization
- Memory Utilization

### SMF Metrics
- Active PDU Sessions
- CPU Utilization
- Memory Utilization

### UPF Metrics
- Active Users
- Throughput
- Packet Loss

## Customization

### Web Dashboard
To customize the web dashboard:
1. Modify [../../web-dashboard/public/index.html](../../web-dashboard/public/index.html) for layout changes
2. Update [../../web-dashboard/public/styles.css](../../web-dashboard/public/styles.css) for styling
3. Modify [../../web-dashboard/public/script.js](../../web-dashboard/public/script.js) for behavior

### Grafana Dashboard
To customize the Grafana dashboard:
1. Edit [grafana/dashboard.json](grafana/dashboard.json) to modify panels
2. Update [grafana/datasource.yaml](grafana/datasource.yaml) for data source changes

## Testing

To verify the dashboard functionality:
```bash
# Test web dashboard
curl -I http://localhost:3000

# Test Grafana configuration
# Import dashboard.json in Grafana UI
```

## Screenshots

### Web Dashboard
![Web Dashboard](../docs/dashboard-screenshot.png)

### Grafana Dashboard
![Grafana Dashboard](../docs/grafana-screenshot.png)

## Troubleshooting

### Web Dashboard Issues
1. Ensure Node.js is installed
2. Check that all dependencies are installed (`npm install`)
3. Verify the server is running (`node server.js`)
4. Check browser console for JavaScript errors

### Grafana Issues
1. Ensure Grafana is properly installed
2. Verify data source configuration
3. Check that SNMP agent is running
4. Validate dashboard JSON syntax

## Contributing

To contribute to the dashboard development:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request