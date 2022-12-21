import unittest
from unittest.mock import Mock
import odometer


class TestOdometer(unittest.TestCase):
    def test_alert_normal(self):
        odometer.speed = Mock()
        odometer.speed.return_value = 70
        self.assertFalse(odometer.alert())

    def test_alert_over_speed(self):
        odometer.speed = Mock()
        odometer.speed.return_value = 110
        self.assertTrue(odometer.alert())

    def test_alert_under_speed(self):
        odometer.speed = Mock()
        odometer.speed.return_value = 59
        self.assertTrue(odometer.alert())


if __name__ == '__main__':
    unittest.main()
