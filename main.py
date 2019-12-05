from datetime import datetime
import json
import sys

from utils.args_parser import create_parser
from utils.calc_moving_average import MovingAverage
from utils.process_input import check_file_path, get_timestamp_from_string, get_duration_from_string
from utils.read_input_obj import InputSourceFile
from utils.sys_logger import init_sys_logger

logger = init_sys_logger('main_calc_av')


def main():
    parser = create_parser()
    args = parser.parse_args()

    input_file = args.input_file
    window = args.window_size
    logger.info('arguments parsed')
    input_file_is_valid = check_file_path(input_file)
    if not input_file_is_valid:
        sys.exit('Input file is not valid. Please, check')
    logger.info('arguments are valid')
    input_obj = InputSourceFile(input_file)
    first_line_as_dict = json.loads(input_obj.first_line())
    first_date_str = first_line_as_dict.get('timestamp', None)
    if not first_date_str:
        sys.exit('No timestamp in first line. Please, check')
    moving_av = MovingAverage(datetime.strptime(first_date_str, '%Y-%m-%d %H:%M:%S.%f').replace(second=0, microsecond=0)
                              , window)

    with input_obj:
        for line in input_obj:
            line_as_dict = json.loads(line)
            timestamp_str = line_as_dict.get('timestamp', None)
            duration_str = line_as_dict.get('duration', None)
            if not all([timestamp_str, duration_str]):
                logger.info(f'line "{line}" missing some data, ignoring it')
                continue
            timestamp_str_is_valid, timestamp = get_timestamp_from_string(timestamp_str)
            duration_str_is_valid, duration = get_duration_from_string(duration_str)
            if not all([timestamp_str_is_valid, duration_str_is_valid]):
                logger.info(f'line "{line}" has malformed data, ignoring it')
                continue

            moving_av.set_records_count()
            while timestamp != moving_av.last_output_date:
                with open('output.json', 'a') as f:
                    f.write(f'{{"date": {moving_av.last_output_date} , '
                            f'"duration": "{moving_av.get_current_average()}"}} \n')
                moving_av.increase_last_output_date()
                moving_av.check_dates_against_window()

            moving_av.add_duration_value(timestamp, int(duration_str))
            with open('output.json', 'a') as f:
                f.write(f'{{"date": {moving_av.last_output_date} , '
                        f'"duration": "{moving_av.get_current_average()}"}} \n')
            moving_av.increase_last_output_date()


if __name__ == '__main__':
    main()
