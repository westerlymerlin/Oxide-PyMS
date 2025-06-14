# None

<a id="host_commands"></a>

# host\_commands

Commands to the various controller APIs

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

Set laser state (on or off)

<a id="host_commands.lasersetpower"></a>

#### lasersetpower

```python
def lasersetpower(power)
```

Set the laser power

<a id="host_commands.valvechange"></a>

#### valvechange

```python
def valvechange(valve, command)
```

Change a valve state

<a id="host_commands.xymoveto"></a>

#### xymoveto

```python
def xymoveto(axis, location)
```

Move the X-Y stage ***axis*** to a position ***loc***

<a id="host_commands.xymove"></a>

#### xymove

```python
def xymove(axis, steps)
```

Move the **axis** along **steps**

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
def ion_pump(state)
```

Sens a command to the in pump

