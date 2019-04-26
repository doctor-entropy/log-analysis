def convert_datetime_to_string(date_time):

    month_string = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }

    return '{} {}, {}'.format(date_time.day,
                              month_string[date_time.month], date_time.year)
