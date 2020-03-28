def time_conversion(time_seconds):
    """Converts time in seconds to hours, minutes and seconds

    Parameters
    ----------
    time_seconds : int
        Time in seconds

    Returns
    -------
    tuple
        Tuple (hours, minutes, seconds)
    """
    hours, remainder = divmod(time_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return hours, minutes, seconds


def time_format(hours_minutes_seconds_tuple):
    """Formats a tuple with (hours, minutes and seconds) to
    hours:minutes:seconds

    Parameters
    ----------
    hours_minutes_seconds_tuple : tuple
        tuple with (hours, minutes and seconds)

    Returns
    -------
    string
        hours:minutes:seconds
    """
    list_time_parts = [str(part) for part in hours_minutes_seconds_tuple]
    time_string = ':'.join(list_time_parts)
    return time_string


if __name__ == "__main__":
    user_input = input()
    time_tuple = time_conversion(eval(user_input))
    output = time_format(time_tuple)
    print(output)
