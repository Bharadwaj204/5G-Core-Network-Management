# SNMP Monitor

SNMP-based monitoring system for 5G core network components with agent and polling capabilities.

## Overview

The SNMP monitor provides a comprehensive monitoring solution for 5G core network functions using the Simple Network Management Protocol (SNMP). It includes both an SNMP agent for exposing metrics and polling scripts for collecting data.

## Features

- SNMP agent implementation for metrics exposure
- Custom MIB for 5G core network metrics
- Polling scripts for data collection
- Data export in JSON and CSV formats
- Real-time metrics for AMF, SMF, and UPF
- Compatible with standard SNMP tools

## Requirements

- Python 3.8 or higher
- pysnmp
- JSON library (standard library)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Starting the SNMP Agent

```bash
python snmp_agent.py
```

The agent will start on port 161 and expose 5G core network metrics via SNMP.

### Running the Polling Script

```bash
python snmp_poller.py
```

The poller will collect metrics from the SNMP agent and export them to JSON and CSV files.

## SNMP MIB Structure

The system uses a custom MIB structure for 5G core metrics:

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

## Configuration

The SNMP agent can be configured by modifying the following parameters in [snmp_agent.py](snmp_agent.py):

- `SNMP_PORT` - Port for SNMP agent (default: 161)
- `COMMUNITY` - SNMP community string (default: "public")
- Metric values are currently simulated but can be connected to real data sources

## Polling Script

The polling script ([snmp_poller.py](snmp_poller.py)) collects metrics at regular intervals and exports them to:

1. `snmp_metrics.json` - JSON format for programmatic access
2. `snmp_metrics.csv` - CSV format for spreadsheet analysis

### Polling Configuration

Modify the following parameters in [snmp_poller.py](snmp_poller.py):

- `POLLING_INTERVAL` - Time between polls in seconds (default: 10)
- `SNMP_TARGET` - Target SNMP agent IP (default: "localhost")
- `SNMP_PORT` - Target SNMP agent port (default: 161)
- `SNMP_COMMUNITY` - SNMP community string (default: "public")

## Testing

Run the test suite to verify functionality:
```bash
cd ../../tests
python test_snmp_monitor.py
```

## Integration with Grafana

The SNMP monitor can be integrated with Grafana for visualization:

1. Configure Grafana to use SNMP data source
2. Import the dashboard configuration from [../../dashboard/grafana/](../../dashboard/grafana/)
3. Connect to the SNMP agent at `snmp://localhost:161`

## Example SNMP Queries

### Get AMF Active Sessions
```bash
snmpget -v2c -c public localhost 1.3.6.1.4.1.55555.1.1.1
```

### Get SMF CPU Utilization
```bash
snmpget -v2c -c public localhost 1.3.6.1.4.1.55555.1.2.2
```

### Get UPF Throughput
```bash
snmpget -v2c -c public localhost 1.3.6.1.4.1.55555.1.3.3
```

## Data Export Formats

### JSON Format
```json
{
  "timestamp": "2025-11-18T10:30:45Z",
  "amf": {
    "active_sessions": 1250,
    "cpu_utilization": 35,
    "memory_utilization": 55
  },
  "smf": {
    "active_pdu_sessions": 1100,
    "cpu_utilization": 30,
    "memory_utilization": 50
  },
  "upf": {
    "active_users": 1050,
    "throughput": 150000000,
    "packet_loss": 0.02
  }
}
```

### CSV Format
```
timestamp,amf_active_sessions,amf_cpu_utilization,amf_memory_utilization,smf_active_pdu_sessions,smf_cpu_utilization,smf_memory_utilization,upf_active_users,upf_throughput,upf_packet_loss
2025-11-18T10:30:45Z,1250,35,55,1100,30,50,1050,150000000,0.02
```