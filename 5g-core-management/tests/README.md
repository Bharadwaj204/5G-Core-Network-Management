# Tests

Comprehensive test suite for the 5G Core Management Prototype including unit tests and integration tests for all components.

## Overview

This directory contains a complete test suite for validating the functionality of all components in the 5G Core Management Prototype. The tests cover the management plane components, API endpoints, and integration scenarios.

## Test Structure

### Unit Tests
- [test_netconf_server.py](test_netconf_server.py) - Tests for NETCONF server functionality
- [test_restconf_api.py](test_restconf_api.py) - Tests for RESTCONF API endpoints
- [test_snmp_monitor.py](test_snmp_monitor.py) - Tests for SNMP monitoring components

### Integration Tests
- [test_api_integration.py](test_api_integration.py) - Integration tests for API components
- [test_protocol_compliance.py](test_protocol_compliance.py) - Protocol compliance tests

### Utility Scripts
- [test_utils.py](test_utils.py) - Shared testing utilities and helper functions

## Test Coverage

### NETCONF Server Tests
- Server startup and initialization
- NETCONF hello message handling
- get-config operation
- edit-config operation
- RESTCONF API endpoint validation

### RESTCONF API Tests
- Endpoint accessibility
- HTTP method support (GET, POST, PUT, PATCH, DELETE)
- JSON response validation
- Error handling
- CRUD operations for all resources

### SNMP Monitor Tests
- SNMP agent startup
- MIB structure validation
- Metric exposure
- Polling script functionality
- Data export formats

## Requirements

- Python 3.8 or higher
- All dependencies from management plane components
- pytest (for running tests)

## Installation

```bash
pip install pytest
```

## Running Tests

### Run All Tests
```bash
python -m pytest
```

### Run Specific Test Files
```bash
# Run NETCONF server tests
python test_netconf_server.py

# Run RESTCONF API tests
python test_restconf_api.py

# Run SNMP monitor tests
python test_snmp_monitor.py
```

### Run Tests with Verbose Output
```bash
python -m pytest -v
```

### Run Tests with Coverage Report
```bash
pip install pytest-cov
python -m pytest --cov=.
```

## Test Descriptions

### test_netconf_server.py
Tests the NETCONF server implementation:
- Server initialization and startup
- RESTCONF API endpoint accessibility
- Sample data loading
- Basic CRUD operations via RESTCONF

### test_restconf_api.py
Tests the RESTCONF API implementation:
- All HTTP endpoints
- Response status codes
- JSON data validation
- Resource creation, retrieval, update, and deletion

### test_snmp_monitor.py
Tests the SNMP monitoring components:
- SNMP agent functionality
- MIB structure validation
- Polling script operation
- Data export functionality

## Test Data

All tests use the same sample data that is pre-loaded in the servers:
- 1 AMF (Access and Mobility Management Function)
- 1 SMF (Session Management Function)
- 1 UPF (User Plane Function)
- 1 Subscriber with complete security parameters
- 1 PDU Session
- 1 QoS Profile

## Continuous Integration

The test suite is designed to work with continuous integration systems:
- All tests are independent and can run in parallel
- Tests clean up after themselves
- Clear pass/fail indicators
- Detailed error reporting

## Writing New Tests

### Test Structure
```python
import unittest
import requests

class TestExample(unittest.TestCase):
    def setUp(self):
        # Setup code before each test
        pass
    
    def tearDown(self):
        # Cleanup code after each test
        pass
    
    def test_example_functionality(self):
        # Test implementation
        response = requests.get("http://localhost:8081/restconf/data/network-functions")
        self.assertEqual(response.status_code, 200)
```

### Best Practices
1. Use descriptive test method names
2. Test one thing per test method
3. Include both positive and negative test cases
4. Clean up test data after each test
5. Use assertions to validate expected outcomes
6. Include meaningful error messages

## Test Results

### Expected Results
- All tests should pass with no failures
- No errors should occur during test execution
- Test execution time should be reasonable

### Troubleshooting Test Failures
1. Check that all required services are running
2. Verify network connectivity to test endpoints
3. Confirm all dependencies are installed
4. Check test data initialization
5. Review error messages and stack traces

## Performance Tests

### Load Testing
- Concurrent API requests
- Stress testing of NETCONF operations
- SNMP polling under load

### Response Time Testing
- API response time validation
- NETCONF operation timing
- SNMP query performance

## Security Tests

### Authentication Tests
- API authentication validation
- SNMP community string validation

### Authorization Tests
- Access control for API endpoints
- Resource-level permissions

## Reporting

### Test Reports
- JUnit XML format for CI systems
- HTML reports for detailed analysis
- Coverage reports for code quality

### Test Metrics
- Pass/fail rates
- Execution times
- Coverage percentages
- Failure trends

## Contributing to Tests

To contribute to the test suite:
1. Fork the repository
2. Create a feature branch
3. Add or modify tests
4. Ensure all tests pass
5. Submit a pull request

### Test Development Guidelines
- Follow existing test patterns
- Include both positive and negative cases
- Use meaningful assertions
- Keep tests independent
- Document complex test scenarios