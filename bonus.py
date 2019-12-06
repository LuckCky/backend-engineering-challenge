import json
import sys

import pandas as pd

from utils.read_input_obj import InputSourceFile
from utils.sys_logger import init_sys_logger

logger = init_sys_logger('bonus')


def main():
    user_input = input('Please provide size of X axis as integer: ')
    try:
        chart_len = int(user_input)
    except ValueError:
        logger.warning('Provided value is not an integer, please try again')
        sys.exit('Exiting')

    input_obj = InputSourceFile('output.json')
    data_frame_dict = {'date': [], 'av_duration': []}
    with input_obj:
        lines_counter = 0
        for line in input_obj:
            if lines_counter == chart_len:
                break
            line_as_dict = json.loads(line)
            timestamp = line_as_dict.get('date', 0)
            av_duration = line_as_dict.get('average_delivery_time', 0)
            data_frame_dict['date'].append(timestamp)
            data_frame_dict['av_duration'].append(av_duration)
            lines_counter += 1

    df = pd.DataFrame(data_frame_dict)
    sum_df = df.groupby('date').sum()
    pie = sum_df.plot(kind='line', figsize=(6, 6), legend=True, use_index=True, subplots=True, colormap='Pastel1')

    fig = pie[0].get_figure()
    fig.savefig('./bonus.png')


if __name__ == '__main__':
    main()
