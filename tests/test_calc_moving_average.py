from datetime import datetime, timedelta
import unittest

from utils.calc_moving_average import MovingAverage


class TestMovingAverage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.window_size = 5
        cls.timestamp = datetime.now().replace(second=0, microsecond=0)
        cls.moving_av = MovingAverage(cls.timestamp, cls.window_size)

    def test_set_records_count_none(self):
        self.moving_av.set_records_count()
        self.assertEqual(self.moving_av.records_count, 0)

    def test_set_records_count_one(self):
        self.moving_av.data_dict = {self.timestamp: 0}
        self.moving_av.set_records_count()
        self.assertEqual(self.moving_av.records_count, 1)
        self.moving_av.data_dict.pop(self.timestamp)
        self.moving_av.records_count = 0

    def test_get_current_average_zero_count(self):
        self.moving_av.records_count = 0
        self.moving_av.durations_sum = 0
        av_zero_count = self.moving_av.get_current_average()
        self.assertEqual(av_zero_count, 0)

    def test_get_current_average_non_zero_count(self):
        self.moving_av.records_count = 5
        self.moving_av.durations_sum = 10
        av_non_zero_count = self.moving_av.get_current_average()
        self.assertEqual(av_non_zero_count, 2)

    def test_increase_last_output_date(self):
        new_date = self.timestamp + timedelta(minutes=2)
        self.moving_av.increase_last_output_date()
        self.moving_av.increase_last_output_date()
        self.assertEqual(new_date, self.moving_av.last_output_date)

    def test_add_duration_value(self):
        self.moving_av.add_duration_value(self.timestamp, 10)
        self.assertEqual(self.moving_av.data_dict, {self.timestamp: 10})
        self.assertEqual(self.moving_av.durations_sum, 10)
        self.moving_av.data_dict.pop(self.timestamp)

    def test_check_dates_against_window_empty_data(self):
        self.moving_av.check_dates_against_window()
        self.assertEqual(self.moving_av.data_dict, {})

    def test_check_dates_against_window_non_empty_data(self):
        self.moving_av.add_duration_value(self.timestamp - timedelta(minutes=self.window_size), 10)
        # self.moving_av.last_output_date = self.timestamp
        self.moving_av.check_dates_against_window()
        self.assertEqual(self.moving_av.data_dict, {})
        self.assertEqual(self.moving_av.durations_sum, 0)

    def test_set_new_duration_sum_empty_data_dict(self):
        self.moving_av.set_new_durations_sum()
        self.assertEqual(self.moving_av.durations_sum, 0)

    def test_set_new_duration_sum_non_empty_data_dict(self):
        self.moving_av.add_duration_value(self.timestamp, 10)
        self.moving_av.set_new_durations_sum()
        self.assertEqual(self.moving_av.data_dict, {self.timestamp: 10})
        self.assertEqual(self.moving_av.records_count, 1)
