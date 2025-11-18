# Management Plane Components

The management plane provides comprehensive management capabilities for the 5G core network through standardized protocols and interfaces.

## Components Overview

### NETCONF Server
- Implementation of NETCONF protocol for configuration management
- XML-based configuration operations
- Integration with YANG data models
- Supports standard NETCONF operations (hello, get-config, edit-config)

### RESTCONF API
- HTTP-based interface following RFC 8040
- JSON data exchange format
- Full CRUD operations for all network entities
- Compatible with standard RESTCONF clients

### SNMP Monitor
- SNMP agent implementation for metrics collection
- Custom MIB for 5G core network metrics
- Polling scripts for data collection
- Export capabilities in JSON and CSV formats

### YANG Models
- Standardized data models for network configuration
- Subscriber management model
- Session management model
- QoS parameters model

## Directory Structure

```
management-plane/
├── netconf-server/     # NETCONF server implementation
├── restconf-api/       # RESTCONF API implementation
├── snmp-monitor/       # SNMP monitoring components
└── yang-models/        # YANG data models
```

## Component Details

### NETCONF Server
Location: [netconf-server/](netconf-server/)
- Primary implementation of the NETCONF protocol
- Provides both NETCONF and RESTCONF interfaces on port 830
- Manages network functions, subscribers, sessions, and QoS profiles

### RESTCONF API
Location: [restconf-api/](restconf-api/)
- HTTP-based management interface
- Implements RFC 8040 compliant RESTCONF operations
- JSON-based data exchange for easy integration

### SNMP Monitor
Location: [snmp-monitor/](snmp-monitor/)
- SNMP agent for metrics collection
- Polling scripts for periodic data collection
- Data export in multiple formats

### YANG Models
Location: [yang-models/](yang-models/)
- Subscriber management YANG model
- Session management YANG model
- QoS parameters YANG model
- Validated against YANG syntax rules

## Usage

Each component can be run independently or as part of the complete system:

1. **Start NETCONF/RESTCONF Server**:
   ```bash
   cd netconf-server
   python netconf_server.py
   ```

2. **Start SNMP Agent**:
   ```bash
   cd snmp-monitor
   python snmp_agent.py
   ```

3. **Validate YANG Models**:
   ```bash
   cd yang-models
   pyang *.yang
   ```

## API Endpoints

### RESTCONF Endpoints
- `GET /restconf/data/network-functions` - Get all network functions
- `GET /restconf/data/subscribers` - Get all subscribers
- `GET /restconf/data/sessions` - Get all sessions
- `GET /restconf/data/qos-profiles` - Get all QoS profiles

### NETCONF Operations
- `<get-config>` - Retrieve configuration data
- `<edit-config>` - Modify configuration data
- `<hello>` - Establish NETCONF session

## Testing

Each component includes unit tests in the [tests/](../tests/) directory:
```bash
cd ../tests
python test_netconf_server.py
python test_restconf_api.py
python test_snmp_monitor.py
```