# None

<a id="host_queries"></a>

# host\_queries

Host Queries Module - Network communication interface for hardware devices

This module provides query functions for communicating with various hardware
components in the PyMS mass spectrometry system over TCP/IP connections.
The module handles network requests and responses for:

- Laser system status monitoring and pyrometer temperature readings
- Valve position and status queries
- Pressure gauge readings from multiple sensors
- XY stage position monitoring

All functions implement error handling with timeout management and logging
to ensure robust communication with remote hardware controllers.

Functions:
    lasergetstatus(): Query laser system operational status
    pyroread(): Read pyrometer temperature measurements
    valvegetstatus(): Check valve positions and states
    pressuresread(): Retrieve pressure readings from gauges
    xyread(): Get current XY stage coordinates

Author: Gary Twinn

<a id="host_queries.requests"></a>

## requests

<a id="host_queries.settings"></a>

## settings

<a id="host_queries.alarms"></a>

## alarms

<a id="host_queries.logger"></a>

## logger

<a id="host_queries.check_float"></a>

#### check\_float

```python
def check_float(value_string)
```

Converts the given string to a float. If the conversion fails due to a
`ValueError`, it will return a NaN (Not a Number) value instead.

<a id="host_queries.convert_pfeiffer_mt200"></a>

#### convert\_pfeiffer\_mt200

```python
def convert_pfeiffer_mt200(value)
```

Converts the pressure value read from a Pfeiffer MT200 device into a
scientifically usable format.

This function processes the pressure value encoded as a string by the
Pfeiffer MT200 device by separating it into its mantissa and exponent parts,
and computing the actual pressure in terms of scientific notation.

A string containing the pressure reading, where the first 4 characters
represent the mantissa as an 4 sf integer value and the remaining characters
represent the exponent offset from -20.

<a id="host_queries.lasergetstatus"></a>

#### lasergetstatus

```python
def lasergetstatus()
```

Fetches the current status of the laser system by sending a request to the configured
laserhost. The response includes details about the laser's keyswitch and door
interlock statuses. Updates the laserhost's alarm counters based on the response or
any exceptions encountered during the execution.

<a id="host_queries.pyroread"></a>

#### pyroread

```python
def pyroread()
```

Communicates with a pyrometer through a laser host to retrieve temperature data, process it according to the
calibration settings, and handle potential exceptions during the operation.

Temperature data retrieved from the pyrometer is recalibrated using a slope and intercept defined in the
settings. The function interacts with a remote API using an HTTP POST request and expects a JSON response
containing temperature metrics. Exception handling is included to manage timeouts and general API request
issues, ensuring that the function can return fallback data to maintain operational stability.

<a id="host_queries.valvegetstatus"></a>

#### valvegetstatus

```python
def valvegetstatus()
```

Fetches the status of valves from the specified API endpoint. The function sends a
POST request with specific headers and payload to retrieve the status of up to
16 valves. Each valve's status is represented as an integer in a list
(1 for open and 0 for closed). Handles timeouts and general request exceptions
gracefully, updating corresponding alarm states upon errors.

<a id="host_queries.pressuresread"></a>

#### pressuresread

```python
def pressuresread()
```

Reads pressure information from the pump host and updates the pressure data in the
application settings. The function sends a POST request to the pump host API, receives
the pressure data for different pumps, and processes it. In case of a timeout or
request exception, it logs the issue and increments the alarm counter for the pump
host while returning a default response to indicate an exception.

<a id="host_queries.xyread"></a>

#### xyread

```python
def xyread()
```

Fetch the current status of the X-Y controller by sending a status query to the designated host.

This function communicates with an external X-Y controller service to retrieve information
about the status of the controller by submitting an API request. The function handles
exceptions related to request timeouts and general network errors during the operation.
In case of exceptions, the function increments the `xyhost` alarm counter and returns
a default response indicating an exception.

