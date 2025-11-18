# 5G Core Management Prototype - Demo Instructions

## Pre-Demo Setup
1. Ensure all servers are stopped
2. Open multiple terminal windows
3. Prepare browser for dashboard demo
4. Have Postman or curl ready for RESTCONF demo

## Demo 1: Starting NETCONF Server (2 minutes)

### Steps:
1. Open terminal and navigate to:
   ```
   cd 5g-core-management/management-plane/netconf-server
   ```

2. Start the server:
   ```
   python netconf_server.py
   ```

3. Show the console output indicating:
   - Server started on port 830
   - RESTCONF API available
   - Sample data loaded

### What to Explain:
"This starts our NETCONF server which also provides the RESTCONF API on the same port. You can see it's loaded sample data for AMF, SMF, UPF, subscribers, sessions, and QoS profiles."

## Demo 2: NETCONF Get-Config (2 minutes)

### Steps:
1. Open a new terminal
2. Show the test script:
   ```
   cat ../../test_all_components.py
   ```

3. Run the test:
   ```
   python ../../test_all_components.py
   ```

4. Or use a direct NETCONF client script if available

### What to Explain:
"This demonstrates a NETCONF get-config operation. We're retrieving the current configuration from our 5G core network functions using the standard NETCONF protocol."

## Demo 3: RESTCONF API (2 minutes)

### Steps:
1. Open browser or Postman
2. Make GET request to:
   ```
   http://192.168.0.166:830/restconf/data/network-functions
   ```

3. Show other endpoints:
   - `http://192.168.0.166:830/restconf/data/subscribers`
   - `http://192.168.0.166:830/restconf/data/sessions`

4. Show JSON response format

### What to Explain:
"This is our RESTCONF API, which provides the same functionality as NETCONF but over HTTP with JSON responses. This makes it easier for web developers to integrate with our system."

## Demo 4: SNMP Monitoring (2 minutes)

### Steps:
1. In a new terminal, navigate to:
   ```
   cd 5g-core-management/management-plane/snmp-monitor
   ```

2. Start the SNMP agent:
   ```
   python snmp_agent.py
   ```

3. In another terminal, run the poller:
   ```
   python snmp_poller.py
   ```

4. Show the generated JSON/CSV files:
   ```
   cat snmp_metrics.json
   ```

### What to Explain:
"Our SNMP monitoring system collects performance metrics from the 5G core and exports them in both JSON and CSV formats for analysis."

## Demo 5: Dashboard (2 minutes)

### Steps:
1. In a new terminal, navigate to:
   ```
   cd web-dashboard
   ```

2. Start the dashboard server:
   ```
   node server.js
   ```

3. Open browser to `http://localhost:3000`

4. Show real-time updating metrics

### What to Explain:
"This is our real-time dashboard showing live metrics from the 5G core. The data updates every 5 seconds through WebSocket connections."

## Important Notes for Viva:

### Common Questions to Prepare For:
1. "Why did you choose these specific protocols?"
2. "How does NETCONF differ from RESTCONF?"
3. "What security considerations did you implement?"
4. "How would you scale this system?"
5. "What are the limitations of using Open5GS?"

### Technical Points to Emphasize:
- Industry standard compliance (RFC 6241, RFC 8040, SNMPv2)
- Consistent data models across all interfaces through YANG
- Real-time monitoring capabilities
- Modular, extensible architecture
- Educational value for students

### Troubleshooting Tips:
- If RESTCONF doesn't respond, check if the server is running
- If dashboard doesn't load, ensure Node.js dependencies are installed
- If SNMP fails, check that the agent is running on port 161