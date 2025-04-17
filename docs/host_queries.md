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

Queries to the controller APIs

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

Get laser status

<a id="host_queries.pyroread"></a>

#### pyroread

```python
def pyroread()
```

Get Pyrometer reading

<a id="host_queries.valvegetstatus"></a>

#### valvegetstatus

```python
def valvegetstatus()
```

Get valve status and return a list with each valve status as an item in the list

<a id="host_queries.pressuresread"></a>

#### pressuresread

```python
def pressuresread()
```

Get guage pressures

<a id="host_queries.xyread"></a>

#### xyread

```python
def xyread()
```

Get X Y Positions

