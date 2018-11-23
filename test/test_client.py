from __future__ import absolute_import
import unittest

from six import add_move, MovedModule  # noqa: E402

add_move(MovedModule('mock', 'mock', 'unittest.mock'))  # noqa: E221

from six.moves import mock  # noqa: E221

from aurorapy.client import AuroraBaseClient, AuroraError

class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = AuroraBaseClient(1)

    def test_crc(self):
        """ Test the crc calculation.
        """

        buf = bytearray([0x0f, 0x32, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        crc = self.client.crc(buf)
        self.assertEqual(crc, bytearray([0x30, 0xd3]))

        buf = bytearray([0x00, 0x08, 0x03, 0x02, 0x02, 0x10])
        crc = self.client.crc(buf)
        self.assertEqual(crc, bytearray([0xeb, 0x1e]))

    def test_check_transmission_state(self):
        """
        Test transmission state byte control, it should raise an AuroraError
        if the first byte of the response is not equal to 0.
        """
        response = [0, 1, 2, 3, 4]
        self.client.check_transmission_state(response)

        response = [23, 1, 2, 3, 4]
        with self.assertRaises(AuroraError):
            self.client.check_transmission_state(response)
        response = [1, 1, 2, 3, 4]
        with self.assertRaises(AuroraError):
            self.client.check_transmission_state(response)
        response = [10, 1, 2, 3, 4]
        with self.assertRaises(AuroraError):
            self.client.check_transmission_state(response)

    def test_state(self):
        """
        Test state request. (command 50)
        """
        with mock.patch.object(self.client, "send_and_recv", autospec=True) as sar:
            sar.return_value = bytearray(b'\x00\x01\x02\x03\x04\x05\x14\x1a')

            gstate = self.client.state(1)

            sar.assert_called_with(bytearray(b'\x01\x32\x00\x00\x00\x00\x00\x00\x3d\xe3'))
            self.assertEqual(gstate, u'Wait Sun/Grid')

            istate = self.client.state(2, mapped=False)
            self.assertEqual(istate, 2)

            astate = self.client.state(5)
            self.assertEqual(astate, u'Sun Low')

            # Wrong crc
            sar.return_value = bytearray(b'\x00\x01\x02\x04\x04\x05\x08\x82')

            with self.assertRaises(AuroraError):
                self.client.state(3)

            # Wrong transmission state
            sar.return_value = bytearray(b'\x33\x01\x02\x03\x04\x05\xb9\xd1')

            with self.assertRaises(AuroraError):
                self.client.state(3)

    def test_pn(self):
        """
        Test pn request. (command 52)
        """
        with mock.patch.object(self.client, "send_and_recv", autospec=True) as sar:
            sar.return_value = bytearray(b'sample\xe9\xfe')

            pn = self.client.pn()

            sar.assert_called_with(bytearray(b'\x01\x34\x00\x00\x00\x00\x00\x00\xf0\xbb'))
            self.assertEqual(pn, u'sample')

    def test_reset_auto_exclusion(self):
        """
        Test reset auto-exclusion. (command 53)
        """
        with mock.patch.object(self.client, "send_and_recv", autospec=True) as sar:
            sar.return_value = bytearray(b'\x00\x26\x00\x00\x00\x00\x86\xac')

            self.client.reset_auto_exclusion()

            sar.assert_called_with(bytearray(b'\x01\x35\x0a\xc9\x00\x00\x00\x00\x38\x17'))

    def test_version(self):
        """
        Test version request. (command 58)
        """
        with mock.patch.object(self.client, "send_and_recv", autospec=True) as sar:
            sar.return_value = bytearray(b'\x00\x3aCUNW\x9e\x1c')

            version = self.client.version()

            sar.assert_called_with(bytearray(b'\x01\x3a\x00\x00\x00\x00\x00\x00\xd1\x3d'))
            self.assertEqual(version, u'Aurora 50kW module - UK G83 - Transformerless Version - Wind Version')

    def test_measure(self):
        """
        Test measure request. (command 59)
        """
        with mock.patch.object(self.client, "send_and_recv", autospec=True) as sar:
            sar.return_value = bytearray(b'\x00\x00\x43\xde\xc0\x00\x4b\x91')

            voltage = self.client.measure(1)

            sar.assert_called_with(bytearray(b'\x01\x3b\x01\x00\x00\x00\x00\x00\x2f\xa6'))
            self.assertAlmostEqual(voltage, 445.5, 2)

    def test_serial_number(self):
        """
        Test serial number request. (command 63)
        """
        with mock.patch.object(self.client, "send_and_recv", autospec=True) as sar:
            sar.return_value = bytearray(b'123123\x6a\xc5')

            serial = self.client.serial_number()

            sar.assert_called_with(bytearray(b'\x01\x3f\x00\x00\x00\x00\x00\x00\x72\xcd'))
            self.assertEqual(serial, u'123123')

    def test_manufacturing_date(self):
        """
        Test manufacturing date request. (command 65)
        """
        with mock.patch.object(self.client, "send_and_recv", autospec=True) as sar:
            sar.return_value = bytearray(b'\x00\x002315\x95\x22')

            date = self.client.manufacturing_date()

            sar.assert_called_with(bytearray(b'\x01\x41\x00\x00\x00\x00\x00\x00\x1f\x5a'))
            self.assertEqual(date, u'15-W23')

    def test_flags_and_switches(self):
        """
        Test flags and switches request. (command 67)
        """
        with mock.patch.object(self.client, "send_and_recv", autospec=True) as sar:
            sar.return_value = bytearray(b'\x00\x00\x01\x80\x00\x00\xd8\xe7')

            flags_and_switches = self.client.flags_and_switches()

            sar.assert_called_with(bytearray(b'\x01\x43\x00\x00\x00\x00\x00\x00\xa4\x6d'))
            self.assertEqual(flags_and_switches, bytearray(b'\x01\x80\x00\x00'))

    def test_cumulated_float_energy(self):
        """
        Test cumulated float energy request. (command 68)
        """
        with mock.patch.object(self.client, "send_and_recv", autospec=True) as sar:
            sar.return_value = bytearray(b'\x00\x00\x44\x9a\x47\x5c\x50\xfa')

            today_energy = self.client.cumulated_float_energy(1)

            sar.assert_called_with(bytearray(b'\x01\x44\x01\x00\x00\x00\x00\x00\x97\xae'))
            self.assertAlmostEqual(today_energy, 1234.23, 2)

            sar.return_value = bytearray(b'\x00\x00\x46\xea\xc6\x80\x0b\xca')

            last_10_days = self.client.cumulated_float_energy(5, 10)

            sar.assert_called_with(bytearray(b'\x01\x44\x05\x00\x0a\x00\x00\x00\x95\x62'))
            self.assertAlmostEqual(last_10_days, 30051.25, 2)

    def test_cumulated_energy(self):
        """
        Test cumulated energy request. (command 78)
        """
        with mock.patch.object(self.client, "send_and_recv", autospec=True) as sar:
            sar.return_value = bytearray(b'\x00\x00\x01\x02\x03\x04\xc0\x32')

            energy = self.client.cumulated_energy(1)

            sar.assert_called_with(bytearray(b'\x01\x4e\x01\x00\x00\x00\x00\x00\xc0\x47'))
            self.assertEqual(energy, 16909060)

    def test_time_date(self):
        """
        Test time and date request. (command 70)
        """
        with mock.patch.object(self.client, "send_and_recv", autospec=True) as sar:
            sar.return_value = bytearray(b'\x00\x00\x17\xc8\x2f\x00\xac\x0f')

            seconds = self.client.time_date()

            sar.assert_called_with(bytearray(b'\x01\x46\x00\x00\x00\x00\x00\x00\x07\x9d'))
            self.assertEqual(seconds, 398995200)

    def test_firmware(self):
        """
        Test firmware release request. (command 72)
        """
        with mock.patch.object(self.client, "send_and_recv", autospec=True) as sar:
            sar.return_value = bytearray(b'\x00\x001325\x30\x2d')

            firmware = self.client.firmware(1)

            sar.assert_called_with(bytearray(b'\x01\x48\x01\x00\x00\x00\x00\x00\x0d\x1f'))
            self.assertEqual(firmware, u'1.3.2.5')

    def test_alarms(self):
        """
        Test alarms request. (command 86)
        """
        with mock.patch.object(self.client, "send_and_recv", autospec=True) as sar:
            sar.return_value = bytearray(b'\x00\x00\x01\x02\x03\x04\xc0\x32')

            alarms = self.client.alarms()

            sar.assert_called_with(bytearray(b'\x01\x56\x00\x00\x00\x00\x00\x00\xce\x28'))
            self.assertEqual(alarms, [u'Sun Low', u'Input OC', u'Input UV', u'Input OV'])

    def test_sysinfo(self):
        """
        Test system information request. (command 101)
        """
        with mock.patch.object(self.client, "send_and_recv", autospec=True) as sar:
            sar.return_value = bytearray(b'\x00\x00\x02\x00\x00\x00\xf9\xce')

            transformer_type = self.client.sysinfo(1)

            sar.assert_called_with(bytearray(b'\x01\x65\x01\x00\x00\x00\x00\x00\xc1\x52'))
            self.assertEqual(transformer_type, '100kW Transformer')

            sar.return_value = bytearray(b'\x00\x00\x02\x00\x00\x00\xf9\xce')

            modules = self.client.sysinfo(2)

            sar.assert_called_with(bytearray(b'\x01\x65\x02\x00\x00\x00\x00\x00\xbc\x5e'))
            self.assertEqual(modules, 2)

            # Unsupported index
            with self.assertRaises(AuroraError):
                modules = self.client.sysinfo(5)

    def test_junction_box_monitoring_status(self):
        """
        Test junction box monitoring status request. (command 103)
        """
        with mock.patch.object(self.client, "send_and_recv", autospec=True) as sar:
            sar.return_value = bytearray(b'\x00\x01\x01\x01\x02\x00\x1c\x89')

            jbox_connected = self.client.junction_box_monitoring_status()

            sar.assert_called_with(bytearray(b'\x01\x67\x00\x00\x00\x00\x00\x00\x51\x61'))
            self.assertEqual(jbox_connected, bytearray(b'\x02\x00'))

            sar.return_value = bytearray(b'\x00\x00\x01\x01\x02\x00\x58\x82')

            jbox_connected = self.client.junction_box_monitoring_status()

            self.assertEqual(jbox_connected, None)

    def test_junction_box_param(self):
        """
        Test junction box parameter request. (command 201)
        """
        with mock.patch.object(self.client, "send_and_recv", autospec=True) as sar:
            sar.return_value = bytearray(b'\x00\x10\x42\xaa\xcc\xcd\x40\x6e')

            total_current = self.client.junction_box_param(1, 16)

            sar.assert_called_with(bytearray(b'\x01\xc9\x01\x10\x00\x00\x00\x00\x85\xb2'))
            self.assertAlmostEqual(total_current, 85.4, 2)

    def test_junction_box_state(self):
        """
        Test junction box state request. (command 200)
        """
        with mock.patch.object(self.client, "send_and_recv", autospec=True) as sar:
            sar.return_value = bytearray(b'\x00\x00\x00\x00\x00\x00\x8f\xf7')

            state = self.client.junction_box_state(1)

            sar.assert_called_with(bytearray(b'\x01\xc8\x01\x00\x00\x00\x00\x00\x10\x99'))
            self.assertEqual(state, u'OK')

            sar.return_value = bytearray(b'\x00\x04\x00\x00\x00\x00\x9f\xda')

            state = self.client.junction_box_state(1)

            self.assertEqual(state, u'Power off')


if __name__ == '__main__':
    unittest.main()
