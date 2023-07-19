import os
from datetime import datetime as dt


def logging_wrapper(logged_action, log_file_path):
    def wrapper_for_function(function):
        def actual_wrapper(*args, **kwargs):
            with open(log_file_path, "a") as f:
                f.write("Action {} executed on {} on {}\n".format(
                    logged_action,
                    log_file_path,
                    dt.now().strftime("%Y-%m-%d %H:%M:%S")))
            return function(*args, **kwargs)
        return actual_wrapper
    return wrapper_for_function


@logging_wrapper("FILE_CREATE", "file_create.txt")
def create_file(path):
    print('creating file {}'.format(path))
    open(path, "w+")


@logging_wrapper("FILE_DELETE", "file_delete.txt")
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)


create_file('dummy_file.txt')
delete_file('dummy_file.txt')
create_file('dummy_file.txt')
delete_file('dummy_file.txt')
