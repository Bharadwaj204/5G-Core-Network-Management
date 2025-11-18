# SNMP Monitoring Guide

This document provides detailed instructions on how to use SNMP monitoring for the 5G core network.

## Overview

SNMP (Simple Network Management Protocol) is a widely used protocol for monitoring and managing network devices. This project implements an SNMP agent to expose metrics from the 5G core network functions and provides tools for collecting and analyzing these metrics.

## SNMP Agent

The SNMP agent exposes metrics from the 5G core network functions via standard SNMP operations.

### Starting the SNMP Agent

The SNMP agent runs on port 161 with the community string "public". To start the agent:

```bash
cd management-plane/snmp-monitor
python snmp_agent.py
```

### SNMP MIB Structure

The SNMP agent uses a custom MIB structure with the base OID `1.3.6.1.4.1.55555` for 5G core metrics:

#### AMF Metrics
- `1.3.6.1.4.1.55555.1.1.1` - AMF Active Sessions
- `1.3.6.1.4.1.55555.1.1.2` - AMF CPU Utilization (%)
- `1.3.6.1.4.1.55555.1.1.3` - AMF Memory Utilization (%)

#### SMF Metrics
- `1.3.6.1.4.1.55555.1.2.1` - SMF Active PDU Sessions
- `1.3.6.1.4.1.55555.1.2.2` - SMF CPU Utilization (%)
- `1.3.6.1.4.1.55555.1.2.3` - SMF Memory Utilization (%)

#### UPF Metrics
- `1.3.6.1.4.1.55555.1.3.1` - UPF Active Users
- `1.3.6.1.4.1.55555.1.3.2` - UPF Throughput (bps)
- `1.3.6.1.4.1.55555.1.3.3` - UPF Packet Loss (%)

## SNMP Polling Script

The project includes an SNMP polling script to collect metrics and export them to various formats.

### Running the SNMP Poller

To run the SNMP poller:

```bash
cd management-plane/snmp-monitor
python snmp_poller.py
```

This will perform a single poll of all metrics and export them to a JSON file.

### Continuous Polling

To enable continuous polling, uncomment the last line in the `snmp_poller.py` file:

```python
# Uncomment the following line to start continuous polling
continuous_polling(interval=30, export_format='both')
```

This will poll metrics every 30 seconds and export them in both JSON and CSV formats.

### Export Formats

The SNMP poller supports two export formats:

1. **JSON**: Structured data format suitable for programmatic processing
2. **CSV**: Comma-separated values format suitable for spreadsheet analysis

## Using SNMP Tools

### snmpwalk

To retrieve all metrics using snmpwalk:

```bash
snmpwalk -v2c -c public localhost 1.3.6.1.4.1.55555
```

### snmpget

To retrieve a specific metric using snmpget:

```bash
snmpget -v2c -c public localhost 1.3.6.1.4.1.55555.1.1.1
```

### snmpbulkwalk

To retrieve metrics efficiently using snmpbulkwalk:

```bash
snmpbulkwalk -v2c -c public localhost 1.3.6.1.4.1.55555
```

## Integrating with Monitoring Systems

### Prometheus

To integrate with Prometheus, you can use the SNMP Exporter. Configure Prometheus to scrape metrics from the SNMP Exporter, which in turn collects metrics from the 5G core SNMP agent.

Example Prometheus configuration:

```yaml
scrape_configs:
  - job_name: '5g-core-snmp'
    static_configs:
      - targets: ['localhost:161']
    metrics_path: /snmp
    params:
      module: [if_mib]
    relabel_configs:
      - source_labels: [__address__]
        target_label: __param_target
      - source_labels: [__param_target]
        target_label: instance
      - target_label: __address__
        replacement: snmp-exporter:9116
```

### Grafana

To integrate with Grafana, you can add the SNMP data source and create dashboards to visualize the metrics.

Example Grafana data source configuration:

```json
{
  "name": "5G-Core-SNMP",
  "type": "snmp",
  "access": "proxy",
  "url": "snmp://localhost:161",
  "jsonData": {
    "version": 2,
    "community": "public",
    "securityLevel": "NoAuthNoPriv"
  }
}
```

## Analyzing Metrics

### AMF Metrics

- **Active Sessions**: Number of currently active UE sessions
- **CPU Utilization**: Percentage of CPU used by the AMF
- **Memory Utilization**: Percentage of memory used by the AMF

### SMF Metrics

- **Active PDU Sessions**: Number of currently active PDU sessions
- **CPU Utilization**: Percentage of CPU used by the SMF
- **Memory Utilization**: Percentage of memory used by the SMF

### UPF Metrics

- **Active Users**: Number of currently active users
- **Throughput**: Data throughput in bits per second
- **Packet Loss**: Percentage of packets lost

## Setting Up Alerts

You can set up alerts based on metric thresholds:

1. **High CPU Utilization**: Alert when CPU utilization exceeds 80%
2. **High Memory Utilization**: Alert when memory utilization exceeds 85%
3. **Low Active Sessions**: Alert when active sessions drop below a threshold
4. **High Packet Loss**: Alert when packet loss exceeds 1%

## Performance Tuning

### Polling Interval

Adjust the polling interval based on your monitoring requirements:

- **Real-time monitoring**: 10-30 seconds
- **Operational monitoring**: 1-5 minutes
- **Trend analysis**: 15-60 minutes

### Data Retention

Configure data retention policies based on your storage capacity and analysis needs:

- **High-resolution data**: Keep for 7-30 days
- **Medium-resolution data**: Keep for 90-180 days
- **Low-resolution data**: Keep for 1-5 years

## Security Considerations

When using SNMP monitoring, consider the following security aspects:

1. **SNMP Versions**: Use SNMPv3 for authentication and encryption
2. **Community Strings**: Use strong, non-default community strings
3. **Network Access**: Restrict SNMP access to trusted networks
4. **Firewall Rules**: Configure firewall rules to limit SNMP access
5. **Monitoring**: Monitor SNMP access logs for suspicious activity

## Troubleshooting

### Common Issues

1. **No Response**: Check that the SNMP agent is running and listening on port 161.

2. **Authentication Failure**: Verify the community string is correct.

3. **OID Not Found**: Check that the OID exists in the MIB structure.

4. **Timeout**: Increase timeout values for slow responses.

### Debugging Tools

1. **snmpget**: Test individual OIDs
2. **snmpwalk**: Retrieve all OIDs under a subtree
3. **tcpdump**: Capture SNMP traffic for analysis
4. **Logs**: Check SNMP agent logs for error messages

### Log Analysis

The SNMP agent outputs logs to the console. Look for:

1. **Startup messages**: Confirm the agent started successfully
2. **Error messages**: Identify any issues with SNMP operations
3. **Metric updates**: Verify metrics are being updated

## Next Steps

After setting up SNMP monitoring, you can:

1. Integrate with existing monitoring systems
2. Set up alerting for critical metrics
3. Create custom dashboards for visualization
4. Analyze historical trends
5. Optimize network performance based on metrics