# None

<a id="host_commands"></a>

# host\_commands

Host Commands Module - Hardware Control Interface for PyMS System

This module provides command functions for controlling various hardware components
in the PyMS (Python Mass Spectrometry) system. It handles communication and control
of laboratory equipment including lasers, valves, positioning systems, sensors,
and vacuum pumps.

The module contains functions that send control commands to connected hardware devices,
enabling automated operation of the mass spectrometry system components:

Functions:
- lasercommand(): Controls laser operations and parameters
- lasersetpower(): Sets laser power levels
- valvechange(): Controls valve positions and states
- xymoveto(): Moves XY positioning system to absolute coordinates
- xymove(): Performs relative XY positioning movements
- pyro_rangefinder(): Interfaces with pyrometer/rangefinder sensors
- ion_pump(): Controls ion pump operations

This module works in conjunction with host_queries.py for reading device status
and is part of the larger PyMS automation system for mass spectrometry analysis.

Dependencies:
- Hardware communication libraries for connected devices
- app_control: Application settings and configuration
- logmanager: System logging functionality

Author: Gary Twinn

<a id="host_commands.requests"></a>

## requests

<a id="host_commands.logger"></a>

## logger

<a id="host_commands.settings"></a>

## settings

<a id="host_commands.alarms"></a>

## alarms

<a id="host_commands.lasercommand"></a>

#### lasercommand

```python
def lasercommand(state)
```

Sends a command to control a laser by communicating with the laser host server.

This function constructs a message and sends a POST request to the laser host
server, using the provided state for the laser. The response from the server is
returned in JSON format. The function handles timeouts and other request-related
exceptions, logging issues and incrementing the respective alarm counters.

<a id="host_commands.lasersetpower"></a>

#### lasersetpower

```python
def lasersetpower(power)
```

Sets the power level of the laser by sending a POST request to the laser host endpoint.

This function sends a command to configure the laser device to the specified power level.
It constructs a JSON payload containing the desired power setting, along with the appropriate
headers required for authentication and other configurations. It handles possible exceptions
such as timeouts and request failures, and updates the system settings and alarms accordingly.

<a id="host_commands.valvechange"></a>

#### valvechange

```python
def valvechange(valve, command)
```

Changes the state of a specified valve by sending a command to the valve
control host.

This function sends an HTTP POST request to update the state of a valve. It
handles communication with the external valve control host, processes the
response, and manages errors such as timeouts or other request-related
exceptions.

<a id="host_commands.xymoveto"></a>

#### xymoveto

```python
def xymoveto(axis, location)
```

Send a movement command to the X-Y system to move to a specified location on the given axis.

This function sends a POST request to the XY host API with the desired movement command
and processes the response. It handles exceptions related to timeouts and general HTTP
errors, updating the alarm system accordingly.

<a id="host_commands.xymove"></a>

#### xymove

```python
def xymove(axis, steps)
```

Moves the XY axis of a device by sending a command to a host through an API
request. This function communicates with the XY hardware and updates its
coordinates based on the provided axis and step values. It handles various
network-related exceptions and logs warning or exception messages in case
of issues. It also updates alarm counters as needed.

<a id="host_commands.pyro_rangefinder"></a>

#### pyro\_rangefinder

```python
def pyro_rangefinder(state)
```

Set the state of the Pyrometer Rangefinder by sending a command to the laser host API.

This function sends an HTTP POST request to the laser host API with the specified state,
along with necessary headers and payload. It handles timeout and general exceptions during
the request and logs appropriate warnings or errors.

<a id="host_commands.ion_pump"></a>

#### ion\_pump

```python
def ion_pump(command)
```

Sets the state of an ion pump by sending a command to an external service.

This function communicates with an external service to set the ion pump's
state based on the provided command. The function uses an HTTP POST request
to send the command and handles possible exceptions, logging appropriate
messages, and updating an alarms dictionary in case of failures.

