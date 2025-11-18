# 5G Core Management Prototype

A comprehensive management system for 5G core network components using industry-standard protocols including NETCONF, RESTCONF, and SNMP.

## Project Overview

This prototype demonstrates end-to-end management capabilities for 5G core networks with a complete implementation of management interfaces, monitoring systems, and visualization dashboards. The system provides a solid foundation for 5G core network management using standard protocols.

## Key Components

1. **Open5GS Setup** - Installation and configuration scripts for the 5G core network
2. **Management Plane** - NETCONF, RESTCONF, and SNMP implementations for network management
3. **Dashboard** - Grafana-based visualization for real-time monitoring
4. **YANG Models** - Data models for subscriber, session, and QoS management
5. **Testing Suite** - Comprehensive tests for all system components

## Directory Structure

```
5g-core-management/
├── open5gs-setup/          # Open5GS installation and configuration
├── management-plane/       # Core management implementations
│   ├── netconf-server/     # NETCONF server implementation
│   ├── restconf-api/       # RESTCONF API implementation
│   ├── snmp-monitor/       # SNMP monitoring components
│   └── yang-models/        # YANG data models
├── dashboard/              # Monitoring and visualization
├── docs/                   # Documentation and guides
├── tests/                  # Test suite for all components
├── start_system.py         # System startup script
└── README.md              # This file
```

## Prerequisites

- Python 3.8 or higher
- Node.js 14+ (for web dashboard)
- Docker (for Open5GS deployment)
- Grafana (for dashboard visualization)

## Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r management-plane/netconf-server/requirements.txt
   pip install -r management-plane/snmp-monitor/requirements.txt
   ```

2. **Start the Management Server**:
   ```bash
   cd management-plane/netconf-server
   python netconf_server.py
   ```

3. **Start the Web Dashboard**:
   ```bash
   cd web-dashboard
   node server.js
   ```

4. **Access the System**:
   - RESTCONF API: `http://192.168.0.166:830/restconf/data/`
   - Web Dashboard: `http://localhost:3000`

## API Endpoints

- `GET /restconf/data/network-functions` - Get all network functions
- `GET /restconf/data/subscribers` - Get all subscribers
- `GET /restconf/data/sessions` - Get all sessions
- `GET /restconf/data/qos-profiles` - Get all QoS profiles

## Documentation

See the [docs](docs/) directory for detailed documentation on:
- Setup instructions
- Open5GS configuration guide
- YANG models usage
- NETCONF/RESTCONF API usage
- SNMP monitoring guide
- End-to-end connectivity testing

## Testing

Run the test suite to verify system functionality:
```bash
python test_all_components.py
python api_usage_examples.py
```

## Contributing

This project is a prototype for educational and demonstration purposes. Contributions are welcome for improvements and extensions.

## License

This project is provided as a prototype for educational purposes.