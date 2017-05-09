# List of avaible commands and how to use it:

## 50) State Request.

State request is implemented by state(self, state_type) method where the state_type is an integer that represents the type of state that you want to retrieve.

```python
    alarm_state = client.state(5)
```

**Available states types**:
* 1 = Global State
* 2 = Inverter State
* 3 = DCDC State Channel 1
* 4 = DCDC State Channel 2
* 5 = Alarm State


## 52) P/N Reading

P/N Reading request is implemented by **pn(self)** method.

```python
product_number = client.pn()
```

P/N is an ASCII coded string of 6 characters.

## 58) Version Reading

Version Reading Request is implemented by **version(self)** method.

```python
version = client.version()
```

Version format:

* ''Type - Grid Standard - Trafo/Non Trafo - Wind/PV''

## 59) Measure request to the DSP

Measure request is implemented by **measure(self, index, global_measure=False)** method.

```python
grid_voltage = client.measure(1, global_measure=True)

inverter_temperature = client.measure(21)
```

global_measure must be set to True for the Global measurement. (Only master can require global measurements)

Measures marked with '\*' can be required as global.

N.B. Not all measurements are available for all type of inverters.

### Table of measure's codes

| Code  | Measure                         | Notes                                   |
|-------|---------------------------------|-----------------------------------------|
| 1     | Grid Voltage\*                  | For three-phases systems is the mean    |
| 2     | Grid Current\*                  | For three-phases systems is the mean    |
| 3     | Grid Power\*                    | For three-phases systems is the mean    |
| 4     | Frequency                       | For three-phases systems is the mean    |
| 5     | Vbulk                           | For Inverter with more Bulk is the sum  |
| 6     | Ileak (Dc/Dc)                   |                                         |
| 7     | Ileak (Inverter)                |                                         |
| 8     | Pin1\*                          | Pin for single channel module           |
| 9     | Pin2                            |                                         |
| 21    | Inverter Temperature            |                                         |
| 22    | Booster Temperature             |                                         |
| 23    | Input 1 Voltage                 | Input Voltage for single channel module |
| 24    | - - -                           |                                         |
| 25    | Input 1 Current\*               | Input Current for single channel module |
| 26    | Input 2 Voltage                 |                                         |
| 27    | Input 2 Current                 |                                         |
| 28    | Grid Voltage (Dc/Dc)            |                                         |
| 29    | Grid Frequency (Dc/Dc)          |                                         |
| 30    | Isolation Resistance (Riso)     |                                         |
| 31    | Vbulk (Dc/Dc)                   |                                         |
| 32    | Average Grid Voltage (VgridAvg) |                                         |
| 33    | VbulkMid                        |                                         |
| 34    | Power Peak                      |                                         |
| 35    | Power Peak Today                |                                         |
| 36    | Grid Voltage neutral            |                                         |
| 37    | Wind Generator Frequency        |                                         |
| 38    | Grid Voltage neutral-phase      |                                         |
| 39    | Grid Current phase r            |                                         |
| 40    | Grid Current phase s            |                                         |
| 41    | Grid Current phase t            |                                         |
| 42    | Frequency phase r               |                                         |
| 43    | Frequency phase s               |                                         |
| 44    | Frequency phase t               |                                         |
| 45    | Vbulk +                         |                                         |
| 46    | Vbulk -                         |                                         |
| 47    | Supervisor Temperature          |                                         |
| 48    | Alim. Temperature               |                                         |
| 49    | Heat Sink Temperature           |                                         |
| 50    | Temperature 1                   |                                         |
| 51    | Temperature 2                   |                                         |
| 52    | Temperature 3                   |                                         |
| 53    | Fan 1 Speed                     |                                         |
| 54    | Fan 2 Speed                     |                                         |
| 55    | Fan 3 Speed                     |                                         |
| 56    | Fan 4 Speed                     |                                         |
| 57    | Fan 5 Speed                     |                                         |
| 58    | Power Saturation limit (Der.)   |                                         |
| 59    | Riferimento Anello Bulk         |                                         |
| 60    | Vpanel micro                    |                                         |
| 61    | Grid Voltage phase r            |                                         |
| 62    | Grid Voltage phase s            |                                         |
| 63    | Grid Voltage phase t            |                                         |


## 63) Serial Number request

Serial number request is implemented by **serial_number(self)** method.

```python
serial_number = client.serial_number()

```

Serial Number is an ASCII coded string of 6 characters.

## 65) Manufacturing Week and Year request

Manufacturing Week and Year request is implemented by **manufacturing_date(self)** method.

```python
manufacturing_date = client.manufacturing_date()
```

It returns a python a date string with "%Y-W%W" format.

## 67) Flags or switch reading request

Flags or switch reading request is implemented by **flags_and_switches(self)** method.

```python
flags_and_switches = client.flags_and_switches()
```

It returns a bytearray of 4 bytes those represent the state of the flag1, flag2, switch1 and switch2 respectively.

## 68) Cumulated energy request

Cumulated energy request is implemented by **cumulated_energy(self, period, ndays=None, global_measure=False)** method.

```python
daily_energy = client.cumulated_energy(period=1)

week_energy = client.cumulated_energy(period=2)

last_200_days_energy = client.cumulated_energy(period=5, ndays=200)

year_energy_global = client.cumulated_energy(period=4, global_measure=True)
```

### Avaiable periods:
* 1 = Current day
* 2 = Current week
* 3 = Current Month
* 4 = Current Year
* 5 = Last NDays days. (Need to set ndays parameter, maximum 366)
* 6 = Total
* 7 = Partial

### Global
Setting global_measure parameter to True returns the global energy otherwise it returns the module energy. (Available for all periods)

## 70) Time/Date reading request

Time/Date reading request is implemented by **time_date(self)** method.

```python
seconds_since_january_2000 = client.time_date()
```

Returns the number of past seconds since midnight of January 1, 2000. [int]

## 72) Firmware release reading request

Firmware release reading request is implemeted by **firmware(self, mrelease)** method.

```python
firmware_micro_release_C = client.firmware(3)
```

Returns an ASCII coded string with this format: 'Char1.Char2.Char3.Char4'.

### mrelease
mrelease is the microcontroller release number. (1=A,2=B,...)

For aurora grid-tied inverters mrelease must be set to 0.

## 86) Last four alarms request

Last four alarms request is implemented by **alarms(self)** method.

```python
last_four_alamrs = client.alarms()
```

Returns a list of last 4 alarm descriptions.

## 101) System info reading request (Only for Aurora Central)

System info reading request is implemented by **sysinfo(self, index)** method.

```python
transformer_type = client.sysinfo(1)

modules_number = client.sysinfo(2)
```

Returns the info requested.

### Available index:

* 1 = Transformer Type
* 2 = 50kW modules number

## 200) Junction Box State request

JBox state request is implemented by **junction_box_state(self, junction_box)** method.
```python
jbox_1_state = client.junction_box_state(1)
```

### junction_box
junction_box represents the id of the junction box.

## 201) Junction Box Values request

JBox value request is implemented by **junction_box_param(self, junction_box, parameter)** method.
```python
jbox_1_voltage = client.junction_box_param(1, 11)
```

### junction_box
**junction_box** represents the id of the junction box.

### parameter
**parameter** represents the number of parameter to read.

### Available parameters:

| Num   | Parameter                       | Unit |
|-------|---------------------------------|------|
| 0     | Current String 0                | A    |
| 1     | Current String 1                | A    |
| 2     | Current String 2                | A    |
| 3     | Current String 3                | A    |
| 4     | Current String 4                | A    |
| 5     | Current String 5                | A    |
| 6     | Current String 6                | A    |
| 7     | Current String 7                | A    |
| 8     | Current String 8                | A    |
| 9     | Current String 9                | A    |
| 10    | Internal Temperature            | °C   |
| 11    | Global Parallel Voltage         | V    |
| 12    | Analog input 1                  | -    |
| 13    | Analog input 2                  | -    |
| 14    | Analog input 3                  | -    |
| 15    | Analog Input 4                  | -    |
| 16    | Global string current           | A    |
