# Setup Instructions

This document provides detailed instructions for setting up the 5G Core Management Prototype on Ubuntu 22.04.

## Prerequisites

Before beginning the installation, ensure your system meets the following requirements:

- Ubuntu 22.04 LTS
- At least 4GB RAM
- At least 20GB free disk space
- Internet connection

## Installation Steps

### 1. System Update

First, update your system packages:

```bash
sudo apt update
sudo apt upgrade -y
```

### 2. Install Docker and Docker Compose

Install Docker:

```bash
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
```

Install Docker Compose:

```bash
sudo apt install docker-compose -y
```

### 3. Install Python Dependencies

Install Python 3.8+ and pip:

```bash
sudo apt install python3 python3-pip -y
```

### 4. Install Node.js

Install Node.js for the web dashboard:

```bash
curl -fsSL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### 5. Install Open5GS

Navigate to the Open5GS setup directory and run the installation script:

```bash
cd open5gs-setup
chmod +x install.sh
./install.sh
```

### 6. Configure Open5GS

Run the configuration script:

```bash
chmod +x configure.sh
./configure.sh
```

### 7. Install Python Packages for Management Services

Install dependencies for each management service:

```bash
# NETCONF Server
cd ../management-plane/netconf-server
pip install -r requirements.txt

# RESTCONF API
cd ../restconf-api
pip install -r requirements.txt

# SNMP Monitor
cd ../snmp-monitor
pip install -r requirements.txt
```

### 8. Install Grafana and Prometheus

Install Grafana:

```bash
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
sudo apt update
sudo apt install grafana -y
sudo systemctl start grafana-server
sudo systemctl enable grafana-server
```

Install Prometheus:

```bash
sudo apt install prometheus -y
sudo systemctl start prometheus
sudo systemctl enable prometheus
```

## Starting the Services

### 1. Start Open5GS

```bash
sudo systemctl start open5gs
```

### 2. Start Management Services

In separate terminals, start each management service:

```bash
# Terminal 1: NETCONF Server
cd management-plane/netconf-server
python netconf_server.py

# Terminal 2: RESTCONF API
cd management-plane/restconf-api
python restconf_server.py

# Terminal 3: SNMP Agent
cd management-plane/snmp-monitor
python snmp_agent.py
```

### 3. Start Grafana Dashboard

Configure Grafana data source:

1. Open a web browser and navigate to `http://localhost:3000`
2. Log in with default credentials (admin/admin)
3. Go to Configuration > Data Sources
4. Add a new SNMP data source with the following settings:
   - Name: 5G-Core-SNMP
   - Type: SNMP
   - URL: snmp://localhost:161
   - Version: SNMPv2
   - Community: public

Import the dashboard:

1. Go to Dashboards > Import
2. Upload the dashboard.json file from the dashboard/grafana directory

## Testing the Installation

### 1. Verify Open5GS Services

Check that Open5GS services are running:

```bash
sudo systemctl status open5gs
```

### 2. Test RESTCONF API

Test the RESTCONF API endpoints:

```bash
curl http://localhost:8081/restconf/data/network-functions
```

### 3. Test SNMP Metrics

Use snmpwalk to verify SNMP metrics:

```bash
snmpwalk -v2c -c public localhost 1.3.6.1.4.1.55555
```

## Troubleshooting

### Common Issues

1. **Port conflicts**: If ports are already in use, modify the configuration files to use different ports.

2. **Permission issues**: Ensure you have sufficient permissions to run Docker and system services.

3. **Python dependencies**: If you encounter issues with Python dependencies, try creating a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Node.js issues**: Ensure you have Node.js 14 or higher installed for the web dashboard.

### Logs and Debugging

Each component outputs logs to the terminal. Check these logs for error messages and debugging information.

## Next Steps

After successfully setting up the 5G Core Management Prototype, you can:

1. Explore the YANG models using pyang
2. Configure network functions via RESTCONF
3. Monitor metrics via SNMP
4. Use the Grafana dashboard for visualization