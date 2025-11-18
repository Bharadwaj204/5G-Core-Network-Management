# Open5GS Setup

Installation scripts and configuration files for deploying Open5GS, an open-source 5G core network implementation.

## Overview

This directory contains all necessary scripts and configuration files for installing and configuring Open5GS, which serves as the 5G core network in this management prototype. Open5GS is a free and open-source implementation of the 5G core network.

## Components

### Installation Scripts
- [install_open5gs.sh](install_open5gs.sh) - Automated installation script for Ubuntu
- [install_dependencies.sh](install_dependencies.sh) - Dependency installation script

### Configuration Files
- [amf.yaml](amf.yaml) - Access and Mobility Management Function configuration
- [smf.yaml](smf.yaml) - Session Management Function configuration
- [upf.yaml](upf.yaml) - User Plane Function configuration

### Service Management
- [start_open5gs.sh](start_open5gs.sh) - Script to start all Open5GS services
- [stop_open5gs.sh](stop_open5gs.sh) - Script to stop all Open5GS services
- [restart_open5gs.sh](restart_open5gs.sh) - Script to restart all Open5GS services

## Prerequisites

- Ubuntu 20.04 LTS or later
- Minimum 4GB RAM
- Minimum 20GB disk space
- Internet connectivity for package installation

## Installation

### Automated Installation
```bash
chmod +x install_open5gs.sh
./install_open5gs.sh
```

### Manual Installation
1. Install dependencies:
   ```bash
   chmod +x install_dependencies.sh
   ./install_dependencies.sh
   ```

2. Install Open5GS:
   ```bash
   # Add Open5GS repository
   sudo apt update
   sudo apt install software-properties-common
   sudo add-apt-repository ppa:open5gs/latest
   sudo apt update
   sudo apt install open5gs
   ```

## Configuration

### AMF Configuration
File: [amf.yaml](amf.yaml)
- Network interface configuration
- MCC/MNC settings
- Security parameters
- NGAP settings

### SMF Configuration
File: [smf.yaml](smf.yaml)
- PFCP settings
- GTP-C settings
- DNS configuration
- UPF selection parameters

### UPF Configuration
File: [upf.yaml](upf.yaml)
- PFCP settings
- GTP-U settings
- Network interface configuration
- QoS parameters

## Service Management

### Starting Services
```bash
chmod +x start_open5gs.sh
./start_open5gs.sh
```

### Stopping Services
```bash
chmod +x stop_open5gs.sh
./stop_open5gs.sh
```

### Restarting Services
```bash
chmod +x restart_open5gs.sh
./restart_open5gs.sh
```

### Checking Service Status
```bash
sudo systemctl status open5gs-amfd
sudo systemctl status open5gs-smfd
sudo systemctl status open5gs-upfd
```

## Default Configuration

### Network Settings
- MCC: 001
- MNC: 01
- TAC: 1
- SST: 1
- SD: 0x000001

### Interfaces
- NGAP: eth0 (port 38412)
- GTP-C: eth0 (port 2123)
- GTP-U: eth0 (port 2152)
- PFCP: eth0 (port 8805)

### Security
- Default security keys for testing
- Authentication algorithms
- Integrity protection settings

## Testing Connectivity

### Verify Installation
```bash
# Check if services are running
ps aux | grep open5gs

# Check listening ports
netstat -tuln | grep -E "(38412|2123|2152|8805)"
```

### Test with UERANSIM
1. Install UERANSIM gNB and UE
2. Configure UERANSIM to connect to Open5GS
3. Establish PDU session

## Troubleshooting

### Common Issues

#### Services Not Starting
1. Check system logs:
   ```bash
   sudo journalctl -u open5gs-amfd
   sudo journalctl -u open5gs-smfd
   sudo journalctl -u open5gs-upfd
   ```

2. Verify configuration files:
   ```bash
   sudo open5gs-amfd -c /etc/open5gs/amf.yaml
   sudo open5gs-smfd -c /etc/open5gs/smf.yaml
   sudo open5gs-upfd -c /etc/open5gs/upf.yaml
   ```

#### Network Connectivity Issues
1. Check firewall settings:
   ```bash
   sudo ufw status
   sudo ufw allow 38412/tcp
   sudo ufw allow 2123/udp
   sudo ufw allow 2152/udp
   sudo ufw allow 8805/udp
   ```

2. Verify network interfaces:
   ```bash
   ip addr show
   ```

#### Database Issues
1. Check MongoDB status:
   ```bash
   sudo systemctl status mongodb
   ```

2. Verify database connectivity:
   ```bash
   mongo open5gs
   ```

## Integration with Management Plane

### NETCONF Integration
- Open5GS configuration via NETCONF
- Real-time configuration updates
- Configuration validation

### RESTCONF Integration
- HTTP-based configuration management
- JSON configuration format
- API-driven service management

### SNMP Integration
- Performance metrics exposure
- Health monitoring
- Alerting capabilities

## Customization

### Modifying Configuration
1. Edit the YAML configuration files
2. Restart the affected services
3. Verify the changes

### Adding New Network Functions
1. Install additional Open5GS components
2. Configure the new components
3. Integrate with management plane

## Security Considerations

### Production Deployment
- Change default security keys
- Implement proper authentication
- Enable encryption
- Configure firewall rules
- Regular security updates

### Testing Environment
- Isolated network environment
- Test-specific security keys
- Controlled access

## Performance Tuning

### Resource Allocation
- CPU allocation for each network function
- Memory limits and reservations
- Network interface optimization

### Scaling
- Horizontal scaling options
- Load balancing
- High availability configuration

## Backup and Recovery

### Configuration Backup
```bash
# Backup configuration files
sudo cp /etc/open5gs/*.yaml /backup/open5gs-config/
```

### Database Backup
```bash
# Backup MongoDB
mongodump --db open5gs --out /backup/open5gs-db/
```

## Monitoring

### Built-in Monitoring
- Log file analysis
- Service status monitoring
- Performance metrics

### External Monitoring
- Integration with management plane
- SNMP monitoring
- Custom dashboards

## Contributing

To contribute to the Open5GS setup:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## References

- [Open5GS Official Documentation](https://open5gs.org)
- [3GPP 5G Standards](https://www.3gpp.org/specifications)
- [Open5GS GitHub Repository](https://github.com/open5gs/open5gs)