# NETCONF Server

Implementation of the NETCONF protocol for 5G core network management, including integrated RESTCONF API support.

## Overview

The NETCONF server provides a standards-compliant interface for configuring and managing 5G core network functions. It implements the NETCONF protocol as defined in RFC 6241 and includes an integrated RESTCONF API following RFC 8040.

## Features

- Full NETCONF protocol implementation
- Integrated RESTCONF API on the same port
- Support for standard NETCONF operations
- XML-based configuration management
- JSON-based RESTCONF API
- Pre-loaded sample data for immediate testing

## Requirements

- Python 3.8 or higher
- Flask
- ncclient
- lxml
- pyang

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Starting the Server

```bash
python netconf_server.py
```

The server will start on port 830 and provide both NETCONF and RESTCONF interfaces.

### NETCONF Interface

Connect to the server using any standard NETCONF client on port 830.

Supported operations:
- `<hello>` - Establish session
- `<get-config>` - Retrieve configuration
- `<edit-config>` - Modify configuration

### RESTCONF Interface

Access the RESTCONF API at `http://192.168.0.166:830/restconf/data/`

Supported endpoints:
- `GET /restconf/data/network-functions` - Get all network functions
- `GET /restconf/data/network-functions/amf/<amf_id>` - Get specific AMF
- `GET /restconf/data/subscribers` - Get all subscribers
- `GET /restconf/data/sessions` - Get all sessions
- `GET /restconf/data/qos-profiles` - Get all QoS profiles

## API Examples

### Get Network Functions
```bash
curl http://192.168.0.166:830/restconf/data/network-functions
```

### Get Specific AMF
```bash
curl http://192.168.0.166:830/restconf/data/network-functions/amf/amf-001
```

### Create New AMF
```bash
curl -X POST http://192.168.0.166:830/restconf/data/network-functions/amf \
  -H "Content-Type: application/json" \
  -d '{"id": "amf-002", "status": "active", "capacity": 30, "mcc": "001", "mnc": "01"}'
```

## Sample Data

The server is pre-loaded with sample data:
- 1 AMF (Access and Mobility Management Function)
- 1 SMF (Session Management Function)
- 1 UPF (User Plane Function)
- 1 Subscriber with complete security parameters
- 1 PDU Session
- 1 QoS Profile

## Testing

Run the test suite to verify functionality:
```bash
cd ../../tests
python test_netconf_server.py
```

## Architecture

The server implements a dual-interface approach:
1. **NETCONF Interface** - Traditional XML-based protocol
2. **RESTCONF Interface** - Modern HTTP/JSON-based protocol

Both interfaces share the same underlying data store and provide consistent management capabilities.