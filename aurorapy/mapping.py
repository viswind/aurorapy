class Mapping(object):
    GLOBAL_STATES = {
        0: "Sending Parameters",
        1: "Wait Sun/Grid",
        2: "Checking Grid",
        3: "Measuring Riso",
        4: "DcDc Start",
        5: "Inverter Start",
        6: "Run",
        7: "Recovery",
        8: "Pause",
        9: "Ground Fault",
        10: "OTH Fault",
        11: "Address Settings",
        12: "Self Test",
        13: "Self Test Fail",
        14: "Sensor Test + Meas.Riso",
        15: "Leak Fault",
        16: "Waiting for manual reset",
        17: "Internal error E026",
        18: "Internal error E027",
        19: "Internal error E028",
        20: "Internal error E029",
        21: "Internal error E030",
        22: "Sending Wind Table",
        23: "Failed Sending table",
        24: "UTH Fault",
        25: "Remote OFF",
        26: "Interlock Fail",
        27: "Executing autotest",
        30: "Waiting Sun",
        31: "Temperature failure",
        32: "Fan Staucked",
        33: "Int. Com. Fault",
        34: "Slave Insertion",
        35: "DC Switch Open",
        36: "Tras Switch Open",
        37: "MASTER Exclusion",
        38: "Auto Exclusion",
        98: "Erasing Internal EEprom",
        99: "Erasing External EEprom",
        100: "Counting EEprom",
        101: "Freeze"
    }

    DCDC_STATES = {
        0: "DcDc OFF",
        1: "Ramp Start",
        2: "MPPT",
        4: "Input OC",
        5: "Input UV",
        6: "Input OV",
        7: "Input Low",
        8: "No Parameters",
        9: "Bulk OV",
        10: "Communication Error",
        11: "Ramp Fail",
        12: "Internal Error",
        13: "Input Mode Error",
        14: "Ground Fault",
        15: "Inverter Fail",
        16: "DcDc IGBT Sat",
        17: "DcDc ILEAK Fail",
        18: "DcDc Grid Fail",
        19: "DcDc Comm. Error"
    }

    INVERTER_STATES = {
        0: "Stand By",
        1: "Checking Grid",
        2: "Run",
        3: "Bulk OV",
        4: "Out OC",
        5: "IGBT Sat",
        6: "Bulk UV",
        7: "Degauss Error",
        8: "No parameters",
        9: "Bulk low",
        10: "Grid OV",
        11: "Communication Error",
        12: "Degaussing",
        13: "Starting",
        14: "Bulk Cap Fail",
        15: "Leak Fail",
        16: "DcDc Fail",
        17: "Ileak Sensor Fail",
        18: "Selftest: Relay Inverter",
        19: "Selftest: Wait for sensor test",
        20: "Selftest: Test relay DcDc + sensor",
        21: "Selftest: Relay Inverter fail",
        22: "Selftest: Timeout fail",
        23: "Selftest: Relay DcDc fail",
        24: "Selftest 1",
        25: "Waiting selftest start",
        26: "Dc Injection",
        27: "Selftest 2",
        28: "Selftest 3",
        29: "Selftest 4",
        30: "Internal Error",
        31: "Internal Error",
        40: "Forbidden State",
        41: "Input UC",
        42: "Zero Power",
        43: "Grid Not Present",
        44: "Waiting Start",
        45: "MPPT",
        46: "Grid Fail",
        47: "Input OC"
    }

    ALARM_STATES= {
        0: "No alarm",
        1: "Sun Low",
        2: "Input OC",
        3: "Input UV",
        4: "Input OV",
        5: "Sun Low",
        6: "No parameters",
        7: "Bulk OV",
        8: "Comm. Error",
        9: "Output OC",
        10: "IGBT Sat",
        11: "Bulk UV",
        12: "Internal Error",
        13: "Grid Fail",
        14: "Bulk Low",
        15: "Ramp Fail",
        16: "DcDc Fail",
        17: "Wrong Mode",
        18: "Ground Fault",
        19: "Over Temperature",
        20: "Bulk Cap Fail",
        21: "Inverter Fail",
        22: "Start Timeout",
        23: "Ground Fault",
        24: "Degauss error",
        25: "Ileak Sensor Fail",
        26: "DcDc Fail",
        27: "SelfTest Error 1",
        28: "SelfTest Error 2",
        29: "SelfTest Error 3",
        30: "SelfTest Error 4",
        31: "DC Injection Error",
        32: "Grid OV",
        33: "Grid UV",
        34: "Grid OF",
        35: "Grid UF",
        36: "Z Grid Hi",
        37: "Internal Error",
        38: "Riso Low",
        39: "Vref Error",
        40: "Error Meas V",
        41: "Error Meas F",
        42: "Error Meas Z",
        43: "Error Meas Ileak",
        44: "Error Read V",
        45: "Error Read I",
        46: "Table Fail",
        47: "Fan Fail",
        48: "UTH",
        49: "Interlock Fail",
        50: "Remote Off",
        51: "Vout Avg error",
        52: "Battery Low",
        53: "Clk Fail",
        54: "Input UC",
        55: "Zero Power",
        56: "Fan Stucked",
        57: "DC Switch Open",
        58: "Tras Switch Open",
        59: "AC Switch Open",
        60: "Bulk UV",
        61: "AutoExclusion",
        62: "Grid df/dt",
        63: "Den Switch Open",
        64: "JBox Fail"
    }

    VERSION_PARAMETERS = [
        {
            "i": "Aurora 2kW indoor",
            "o": "Aurora 2kW outdoor",
            "I": "Aurora 3.6kW indoor",
            "O": "Aurora 3.0-3.6kW outdoor",
            "5": "Aurora 5kW outdoor",
            "6": "Aurora 6kW outdoor",
            "P": "3-phase interface (3G74)",
            "C": "Aurora 50kW module",
            "4": "Aurora 4.2kW new",
            "3": "Aurora 3.6kW new",
            "2": "Aurora 3.3kW new",
            "1": "Aurora 3.0kW new",
            "D": "Aurora 12.0kW",
            "X": "Aurora 10.0kW",
        },
        {
            "A": "UL1741",
            "E": "VDE0126",
            "S": "DR 1663/2000",
            "I": "ENEL DK 5950",
            "U": "UK G83",
            "K": "AS 4777",
        },
        {
            "N": "Transformerless Version",
            "T": "Transformer Version",
        },
        {
            "W": "Wind Version",
            "N": "PV Version",
        }
    ]

    TRANSMISSION_STATES = {
        0: 'OK',
        51: 'Command is not implemented',
        52: 'Variable does not exist',
        53: 'Variable value is out of range',
        54: 'EEprom not accessible',
        55: 'Not toggled service mode',
        56: 'Can not send the command to internal micro',
        57: 'Command not excecuted',
        58: 'The variable is not avaible, retry'
    }

    STATE_TYPES = {
        'global': 1,
        'inverter': 2,
        'DCDC1': 3,
        'DCDC2': 4,
        'alarm': 5
    }

    TRANSFORMER_TYPES = {
        0: 'no_transformer',
        1: '50kW Transformer',
        2: '100kW Transformer',
        3: '200kW Transformer',
        4: '300kW Transformer',
    }

    JBOX_STATE = [
        "Burnt fuse on Jbox",
        "JBox overtemperature",
        "JBOX overvoltage",
        "Unbalanced string current",
        "Jbox overcurrent",
        "Power off",
        "No Communication",
        "Jbox not calibrated",
    ]
