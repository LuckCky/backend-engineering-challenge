from datetime import datetime, timedelta
from typing import Dict, Optional

from utils.sys_logger import init_sys_logger

logger = init_sys_logger(__name__)


class MovingAverage:
    records_count: int
    last_output_date_str: str
    last_output_date: Optional[datetime]
    durations_sum: int
    data_dict: Dict
    window_size: int

    def __init__(self, last_output_date: datetime, window_size: int):
        self.records_count = 0
        self.last_output_date = last_output_date
        self.durations_sum = 0
        self.data_dict = {}
        self.window_size = window_size
        logger.info('moving average object is initialised')

    def set_records_count(self):
        """
        Sets new records count for moving average
        Returns: None

        """
        self.records_count = len(self.data_dict)

    def get_current_average(self) -> float:
        """
        Calculates current average
        Returns: current average value

        """
        try:
            return self.durations_sum/self.records_count
        except ZeroDivisionError:
            return 0

    def increase_last_output_date(self):
        """
        Adds one minute to last date saved in output file
        Returns: None

        """
        self.last_output_date = self.last_output_date + timedelta(minutes=1)

    def add_duration_value(self, timestamp: datetime, duration_int: int):
        """
        Adds record to dict containing values for calculating average at given moment
        Args:
            timestamp: timestamp from input file
            duration_int: duration for given timestamp

        Returns: None

        """
        self.data_dict[timestamp] = duration_int
        self.set_new_durations_sum()

    def check_dates_against_window(self):
        """
        Checks if first value in dict of values needed to calculate average is not older that window size
        Returns: None

        """
        if self.data_dict:
            first_timestamp = list(self.data_dict.keys())[0]
            if first_timestamp <= self.last_output_date - timedelta(minutes=self.window_size):
                self.data_dict.pop(first_timestamp)
                self.set_new_durations_sum()

    def set_new_durations_sum(self):
        """
        Calculates new sum of all durations
        Returns: None

        """
        self.durations_sum = sum(self.data_dict.values())
        self.set_records_count()
