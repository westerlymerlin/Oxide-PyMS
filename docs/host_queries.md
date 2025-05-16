# Contents for: host_queries

* [host\_queries](#host_queries)
  * [requests](#host_queries.requests)
  * [settings](#host_queries.settings)
  * [alarms](#host_queries.alarms)
  * [logger](#host_queries.logger)
  * [lasergetstatus](#host_queries.lasergetstatus)
  * [pyroread](#host_queries.pyroread)
  * [valvegetstatus](#host_queries.valvegetstatus)
  * [pressuresread](#host_queries.pressuresread)
  * [xyread](#host_queries.xyread)

<a id="host_queries"></a>

# host\_queries

Queries to the various controller APIs

<a id="host_queries.requests"></a>

## requests

<a id="host_queries.settings"></a>

## settings

<a id="host_queries.alarms"></a>

## alarms

<a id="host_queries.logger"></a>

## logger

<a id="host_queries.lasergetstatus"></a>

#### lasergetstatus

```python
def lasergetstatus()
```

Fetches the current status of the laser system by sending a request to the configured
laserhost. The response includes details about the laser's keyswitch and door
interlock statuses. Updates the laserhost's alarm counters based on the response or
any exceptions encountered during the execution.

:raises requests.Timeout: If the request exceeds the configured timeout duration.
:raises requests.RequestException: If any other network-related exception occurs.
:return: A dictionary containing the status of the laser system. If an error occurs,
    returns a dictionary with 'laser' key set to 'exception'.
:rtype: dict

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

