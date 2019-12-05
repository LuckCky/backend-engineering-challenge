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
        # self.last_output_date = None
        # self.set_last_output_date()
        logger.info('moving average object is initialised')

    # def set_last_output_date(self):
    #     self.last_output_date = datetime.strptime(self.last_output_date_str, '%Y-%m-%d %H:%M:%S.%f')
    #     logger.info(f'new last output date is set to {self.last_output_date}')

    def set_records_count(self):
        self.records_count = len(self.data_dict)
        logger.info(f'records count is increased and now is {self.records_count}')

    def get_current_average(self) -> float:
        logger.info(f'returning new moving average value for durations sum of {self.durations_sum} '
                    f'and records count of {self.records_count}')
        try:
            return self.durations_sum/self.records_count
        except ZeroDivisionError:
            return 0

    def increase_last_output_date(self):
        self.last_output_date = self.last_output_date + timedelta(minutes=1)
        logger.info(f'last output date is increased and now is {self.last_output_date}')

    def add_duration_value(self, timestamp: datetime, duration_int: int):
        self.data_dict[timestamp] = duration_int
        self.set_new_durations_sum()
        logger.info('new timestamp and duration were added to data dict')

    def check_dates_against_window(self):
        if self.data_dict:
            first_timestamp = list(self.data_dict.keys())[0]
            if first_timestamp <= self.last_output_date - timedelta(minutes=self.window_size):
                self.data_dict.pop(first_timestamp)
                self.set_new_durations_sum()
        logger.info(self.data_dict)

    def set_new_durations_sum(self):
        self.durations_sum = sum(self.data_dict.values())
        self.set_records_count()
        logger.info(f'new durations sum is set to {self.durations_sum}')
