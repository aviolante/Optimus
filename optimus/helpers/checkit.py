## Helpers to check if an object belong to some kind

from pyspark.sql import DataFrame
import os


def is_function(obj):
    """
    Check if a param is a function
    :param obj: object to check for
    :return:
    """
    return hasattr(obj, '__call__')


def is_list(value):
    """
    Check if an object is a list
    :param value:
    :return:
    """
    return isinstance(value, list)


@staticmethod
def is_list_of_str_or_int(value):
    """
    Check if an object is a string or an integer
    :param value:
    :return:
    """
    return bool(value) and isinstance(value, list) and all(isinstance(elem, (int, str)) for elem in value)


def is_list_of_str_or_num(value):
    """
    Check if an object is string, integer or float
    :param value:
    :return:
    """
    return bool(value) and isinstance(value, list) and all(isinstance(elem, (str, int, float)) for elem in value)


def is_list_of_dataframes(value):
    """
    Check if an object is a Spark DataFrame
    :param value:
    :return:
    """
    return bool(value) and isinstance(value, list) and all(isinstance(elem, DataFrame) for elem in value)


def is_filepath(file_path):
    """
    Check if a valid filepath
    :param file_path:
    :return:
    """
    # the file is there
    if os.path.exists(file_path):
        return True
    # the file does not exists but write privileges are given
    elif os.access(os.path.dirname(file_path), os.W_OK):
        return True
    # can not write there
    else:
        return False


def is_ip(address):
    """
    Check is a valid ip
    :param address:
    :return:
    """
    parts = address.split(".")
    if len(parts) != 4:
        return False
    for item in parts:
        if not 0 <= int(item) <= 255:
            return False
    return True


def is_list_of_strings(value):
    """
    Check that all elements in a list are strings
    :param value:
    :return:
    """
    return bool(value) and isinstance(value, list) and all(isinstance(elem, str) for elem in value)


def is_list_of_numeric(value):
    """
    Check that all elements in a list are int or float
    :param value:
    :return:
    """
    return bool(value) and isinstance(value, list) and all(isinstance(elem, (int, float)) for elem in value)


def is_list_of_tuples(value):
    """
    Check that all elements in a list are tuples
    :param value:
    :return:
    """
    return bool(value) and isinstance(value, list) and all(isinstance(elem, tuple) for elem in value)


def is_one_element(value):
    """
    Check that a var is a single element
    :param value:
    :return:
    """
    return isinstance(value, (str, int, float, bool))


def is_str_or_int(value):
    """
    Check that a var is a single element
    :param value:
    :return:
    """
    return isinstance(value, (str, int))


def is_numeric(value):
    """
    Check that a var is a single element
    :param value:
    :return:
    """
    return isinstance(value, (int, float))


def is_str(value):
    """
    Check if an object is a string
    :param value:
    :return:
    """
    return isinstance(value, str)


def is_int(value):
    """
    Check if an object is an integer
    :param value:
    :return:
    """
    return isinstance(value, int)


def is_data_type(value, data_type):
    """
    Check if a value can be casted to a specific
    :param value: value to be checked

    :return:
    """
    data_type = "string"

    if isinstance(value, int):  # Check if value is integer
        data_type = "int"
    elif isinstance(value, float):
        data_type = "float"
    elif isinstance(value, bool):
        data_type = "boolean"
    # if string we try to parse it to int, float or bool
    elif isinstance(value, str):
        print("str")
        if str_to_int(value):
            data_type = "int"

        elif str_to_float(value):
            data_type = "float"

        elif str_to_boolean(value):
            data_type = "boolean"
    else:
        data_type = "null"

    if data_type == data_type:
        return True
    else:
        return False


def is_dataframe(value):
    """
    Check if an object is a Spark DataFrame
    :param value:
    :return:
    """
    return isinstance(value, DataFrame)


def str_to_int(value):
    """
    Check if a str can be converted to int
    :param value:
    :return:
    """
    try:
        int(value)
        return True

    except ValueError:
        pass


def str_to_float(value):
    """
    Check if a str can be converted to float
    :param value:
    :return:
    """
    try:
        int(value)
        return True

    except ValueError:
        pass


def str_to_boolean(value):
    """
    Check if a str can be converted to boolean
    :param value:
    :return:
    """
    value = value.lower()
    if value == "true" or value == "false":
        return True
