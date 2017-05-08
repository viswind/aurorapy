# AuroraPy
AuroraPy is a python implementation of Aurora communication protocol for Power-One Aurora inverters.

It implements a **serial Client** and a **TCP Client** for who wants to convert RS485 to Ethernet.

## Manual installation
```
git clone git@code.energievalsabbia.it:ccatterina/aurorapy.git
cd aurorapy
python setup.py install
```

## Usage

```python
from aurorapy.client import AuroraError, AuroraTCPClient # or AuroraSerialClient

client = AuroraTCPClient(ip='192.168.1.34', port=502, address=10)
client.connect()
try:
    print("Inverter serial number: %s" % client.serial_number())
except AuroraError as e:
    print(e.message)
client.close()
```

## Documentation
Documentation is [here](docs/docs.md)

## Available commands

The available commands are:

* 50: State request
* 52: P/N Reading
* 58: Version Reading
* 59: Measure request to the DSP
* 63: Serial Number Reading
* 65: Manufacturing Week and Year
* 67: Flags or switch reading (Only for Aurora Central)
* 68: Cumulated Float Energy Readings (Only for Aurora Central)
* 70: Time/Date reading
* 72: Firmware release reading
* 86: Last Four Alarms
* 101: System Info reading (Only for Aurora Central)
* 200: Junction Box - State Request
* 201: Junction Box - Val Request

Missing commands:

* 78: Cumulated Energy readings (Only for Aurora grid-ties inverters)
* 85: Baud rate setting on serial lines
* 103: Junction Box monitoring status (Only for Aurora Central)
* 105: System P/N Reading (Only for Aurora Central)
* 107: System Serial Number Reading (Only for Aurora Central)
