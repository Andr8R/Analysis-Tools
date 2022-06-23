import os
import logging

def check_output_path(output_path: str) -> str:
    if not os.path.exists(output_path):
        if not os.path.splitext(output_path)[1]:
            _out_dir = output_path
        else:
            _out_dir = os.path.dirname(output_path) 
        os.makedirs(_out_dir, exist_ok=True)


def set_logging(filename='logs_new.log', rank=-1):
    logging.basicConfig(filename=filename, filemode='w',
                        level=logging.INFO if rank in [-1, 0] else logging.DEBUG)
