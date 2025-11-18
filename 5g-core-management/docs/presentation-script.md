# 5G Core Management Prototype - Presentation Script

## Slide 1 - Title Slide
**Title:** End-to-End 5G Core Management Prototype

**Speaker Notes:**
"Good morning/afternoon everyone. Today I'm going to present my project on 'End-to-End 5G Core Management Prototype'. This project aims to build a hands-on 5G core management system using industry-standard protocols like NETCONF, RESTCONF, SNMP, YANG models, along with Open5GS as the 5G core implementation."

---

## Slide 2 - Problem Statement
**Title:** Problem Statement

**Content:**
- Students have theoretical knowledge of 5G Core, but no hands-on platform to learn management
- Real telecom systems are expensive and complex
- Need a lightweight, open-source, manageable 5G Core

**Speaker Notes:**
"The motivation behind this project stems from a significant gap in current educational resources. While students learn about 5G core networks theoretically, they rarely get hands-on experience with actual management systems. Real telecom equipment is expensive and complex to set up, making it inaccessible for most educational institutions. This project addresses this by providing a lightweight, open-source solution that demonstrates real management capabilities."

---

## Slide 3 - Project Objective
**Title:** Project Objective

**Content:**
- Deploy Open5GS (a free 5G Core implementation)
- Manage it using industry-standard protocols:
  * NETCONF
  * RESTCONF
  * SNMP
- Build YANG models
- Create dashboards and monitoring
- Provide easy test scripts

**Speaker Notes:**
"The primary objectives of this project were to deploy Open5GS, which is a free and open-source 5G core implementation, and then build a comprehensive management system around it using industry-standard protocols. We focused on implementing NETCONF for configuration management, RESTCONF for HTTP-based access, SNMP for monitoring, and creating proper YANG models to define our data structures. Additionally, we developed dashboards for visualization and provided easy-to-use test scripts for validation."

---

## Slide 4 - 5G Core Architecture (Block Diagram)
**Title:** 5G Core Architecture

**Content:**
- AMF (Access and Mobility Management Function)
- SMF (Session Management Function)
- UPF (User Plane Function)
- NRF, UDM, AUSF
- N2/N3 interfaces
- UE/gNB (User Equipment and Base Station)

**Speaker Notes:**
"Let me briefly explain the 5G core architecture we're managing. The 5G core consists of several network functions: The AMF handles access and mobility management, the SMF manages sessions, and the UPF handles user plane traffic. We also have supporting functions like the NRF for network function discovery, UDM for user data management, and AUSF for authentication. The N2 interface connects the gNB to the AMF, while N3 connects the gNB to the UPF for user data."

---

## Slide 5 - What We Built (System Architecture)
**Title:** System Architecture

**Content:**
Two main layers:
1. **5G Core Plane** (Open5GS: AMF/SMF/UPF/etc.)
2. **Management Plane**:
   * NETCONF Server
   * RESTCONF API
   * SNMP Monitor
   * YANG Models
   * Dashboard

**Speaker Notes:**
"Our implementation consists of two main layers. The first is the 5G Core Plane, which is Open5GS implementing all the necessary network functions. The second is our Management Plane, which is the core contribution of this project. This includes our NETCONF server for configuration management, RESTCONF API for HTTP-based access, SNMP monitoring for performance metrics, YANG models that define our data structures, and dashboards for visualization. These layers communicate through standardized interfaces."

---

## Slide 6 - Management Technologies
**Title:** Management Technologies

**Content:**
### 1. YANG Models
* Data modeling language
* Defines structure of subscribers, sessions, QoS profiles

### 2. NETCONF
* XML, SSH-based network configuration
* Used by telecom vendors (Nokia, Ericsson, Huawei)

### 3. RESTCONF
* HTTP/JSON version of NETCONF
* Lightweight, easier for developers

### 4. SNMP
* Used for monitoring only
* Metrics and performance statistics

**Speaker Notes:**
"Let me explain the four key management technologies we implemented. First, YANG models are data modeling languages that define the structure of our network data, including subscribers, sessions, and QoS profiles. Second, NETCONF is an XML and SSH-based protocol used by major telecom vendors for configuration management. Third, RESTCONF is the HTTP/JSON equivalent of NETCONF, making it more accessible to developers. Finally, SNMP is used exclusively for monitoring, collecting metrics and performance statistics from our network functions."

---

## Slide 7 - YANG Models Created
**Title:** YANG Models

**Content:**
- subscribers.yang
- sessions.yang
- qos-profiles.yang
- network-functions.yang

Example snippet:
```
container subscribers {
   list subscriber {
      key "imsi"
      leaf imsi { type string; }
      leaf msisdn { type string; }
   }
}
```

**Speaker Notes:**
"We created four comprehensive YANG models to define our data structures. These include models for subscribers, sessions, QoS profiles, and network functions. Each model precisely defines the data structure and relationships. For example, in our subscriber model, we define a container with a list of subscribers, each identified by an IMSI as the key, and include attributes like MSISDN. These models ensure data consistency across all our management interfaces."

---

## Slide 8 - NETCONF Implementation
**Title:** NETCONF Implementation

**Content:**
- Uses ncclient library
- Runs on port 830
- Supports get, edit-config, get-config
- Stores data using YANG models

Sample command:
```
from ncclient import manager
m = manager.connect(host='localhost', port=830, username='admin', password='admin')
config = m.get_config(source="running")
print(config.data_xml)
```

**Speaker Notes:**
"Our NETCONF implementation uses the ncclient Python library and runs on the standard port 830. It supports all the core NETCONF operations including get, edit-config, and get-config. The implementation stores data according to our YANG models, ensuring consistency. As an example, you can connect to the server using ncclient and retrieve the running configuration with just a few lines of code, which returns the data as XML."

---

## Slide 9 - RESTCONF Implementation
**Title:** RESTCONF Implementation

**Content:**
- Built using Flask
- Uses same YANG data structures
- Key endpoints:
  * /restconf/data/subscribers
  * /restconf/data/sessions
  * /restconf/data/qos-profiles
  * /restconf/data/network-functions

RESTCONF = NETCONF + HTTP + JSON

**Speaker Notes:**
"Our RESTCONF implementation is built using Flask and uses the same underlying YANG data structures as our NETCONF implementation. This ensures consistency between both interfaces. We've created key endpoints for accessing subscribers, sessions, QoS profiles, and network functions. RESTCONF essentially brings NETCONF capabilities to the HTTP/JSON world, making it more accessible to web developers while maintaining the same data models."

---

## Slide 10 - SNMP Monitoring
**Title:** SNMP Monitoring

**Content:**
- Uses PySNMP library
- Collects metrics from Open5GS
- Exports to JSON/CSV formats
- Metrics include:
  * Active sessions
  * CPU utilization
  * Memory usage
  * Throughput statistics
  * Packet loss rates

**Speaker Notes:**
"For monitoring capabilities, we implemented SNMP using the PySNMP library. Our SNMP agent collects real metrics from the Open5GS components, including active sessions, CPU and memory utilization, throughput statistics, and packet loss rates. The data can be exported in both JSON and CSV formats for further analysis. This provides comprehensive visibility into the performance and health of our 5G core network."

---

## Slide 11 - Dashboard
**Title:** Dashboard

**Content:**
- Real-time metrics visualization
- Subscriber/session count monitoring
- Performance graphs
- Built with Node.js and Socket.IO
- Integration with Grafana for professional monitoring

**Speaker Notes:**
"Our dashboard provides real-time visualization of all key metrics. It displays subscriber and session counts, performance graphs, and other critical information in an easily digestible format. The dashboard is built with Node.js and Socket.IO for real-time updates, and we've also integrated with Grafana for more professional monitoring capabilities. This gives users both a simple view and advanced analytics options."

---

## Slide 12 - Project Folder Structure
**Title:** Project Folder Structure

**Content:**
```
5g-core-management/
├── open5gs-setup/
├── management-plane/
│   ├── netconf-server/
│   ├── restconf-api/
│   ├── snmp-monitor/
│   └── yang-models/
├── dashboard/
├── docs/
├── tests/
└── start_system.py
```

**Speaker Notes:**
"Let me show you our well-organized project structure. At the top level, we have folders for Open5GS setup, our management plane implementations, dashboard components, documentation, and tests. Within the management plane, we have separate directories for each technology: NETCONF server, RESTCONF API, SNMP monitor, and YANG models. This modular structure makes the project easy to understand, maintain, and extend."

---

## Slide 13 - Demo Flow
**Title:** Demo Flow

**Content:**
### 1. Starting NETCONF server
```
cd management-plane/netconf-server
python netconf_server.py
```

### 2. NETCONF Get-Config Demo
```
python scripts/get_subscribers.py
```

### 3. RESTCONF Demo
```
GET http://localhost:830/restconf/data/subscribers
```

### 4. SNMP Demo
```
snmpwalk -v2c -c public localhost .1.3.6.1.4.1.55555
```

### 5. Dashboard Demo
Show real-time updating graphs

**Speaker Notes:**
"Now let's look at the demo flow for our presentation. First, we start the NETCONF server which also provides our RESTCONF API. Then we can demonstrate NETCONF operations using a simple script to retrieve subscriber information. For RESTCONF, we can make HTTP requests to retrieve the same data in JSON format. For SNMP, we can use standard tools like snmpwalk to query our custom metrics. Finally, we'll show the dashboard with its real-time updating graphs."

---

## Slide 14 - Results
**Title:** Results

**Content:**
✅ Open5GS deployed successfully
✅ NETCONF + RESTCONF interfaces working
✅ SNMP monitoring functioning
✅ Dashboard showing real-time metrics
✅ End-to-end 5G management achieved

**Speaker Notes:**
"I'm happy to report that we've successfully achieved all our project goals. We've successfully deployed Open5GS and have full management capabilities through NETCONF and RESTCONF interfaces. Our SNMP monitoring is fully functional, collecting and exporting metrics as expected. The dashboard displays real-time metrics effectively, and we've achieved complete end-to-end 5G management with all components working together seamlessly."

---

## Slide 15 - Challenges Faced
**Title:** Challenges Faced

**Content:**
- Open5GS configuration issues
- YANG model validation complexities
- NETCONF XML formatting requirements
- SNMP OID management
- Synchronizing NETCONF ↔ RESTCONF states
- Python library compatibility issues

**Speaker Notes:**
"Of course, we faced several challenges during development. Configuring Open5GS properly required significant effort, especially around networking and service dependencies. Validating our YANG models to ensure they were syntactically correct and semantically meaningful was complex. Working with NETCONF's XML formatting requirements was challenging, as was properly managing SNMP OIDs for our custom metrics. Ensuring state consistency between NETCONF and RESTCONF interfaces required careful design. Additionally, we encountered Python library compatibility issues that needed resolution."

---

## Slide 16 - Conclusion
**Title:** Conclusion

**Content:**
- Built a complete 5G Management Plane
- Used real telecom protocols
- Provides actual hands-on environment
- Fully aligned with industry standards
- Demonstrates practical management capabilities

**Speaker Notes:**
"In conclusion, we've successfully built a complete 5G Management Plane that uses real telecom protocols and provides an actual hands-on environment for learning and experimentation. The project is fully aligned with industry standards and demonstrates practical management capabilities that would be found in real telecom networks. This provides educational institutions with an accessible way to teach 5G core management concepts."

---

## Slide 17 - Future Enhancements
**Title:** Future Enhancements

**Content:**
- gNB + UE integration for complete end-to-end testing
- Complete GUI-based provisioning system
- Alarm management system
- TR-069 integration for device management
- Enhanced security (TLS, token authentication)
- Containerization with Docker/Kubernetes

**Speaker Notes:**
"There are several exciting directions for future enhancements. We could integrate actual gNB and UE implementations for complete end-to-end testing. A full GUI-based provisioning system would make the system more accessible. An alarm management system would improve operational capabilities. Integration with TR-069 would enable device management. Enhanced security features like TLS and token authentication would make the system production-ready. Finally, containerization with Docker and Kubernetes would improve deployment flexibility."

---

## Slide 18 - Thank You
**Title:** Thank You / Questions

**Content:**
Questions?

**Speaker Notes:**
"Thank you for your attention. I'm happy to answer any questions you might have about the project, its implementation, or any of the technologies we've discussed."