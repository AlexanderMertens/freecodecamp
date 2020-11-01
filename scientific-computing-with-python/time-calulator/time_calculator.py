DAYS_OF_WEEK = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
WEEK_IN_DAY = 7
HOUR_IN_MIN = 60
DAY_IN_HOUR = 24


def add_time(start, duration, day_of_week=False):
    hours, minutes = convert_to_24(start)

    add_hour, add_minute = map(int, duration.split(':'))
    minutes += add_minute
    hours, minutes = hours + (minutes // HOUR_IN_MIN) + add_hour, minutes % HOUR_IN_MIN
    days, hours = hours // DAY_IN_HOUR, hours % DAY_IN_HOUR

    new_time = convert_to_12(hours, minutes)

    if day_of_week:
        index = (DAYS_OF_WEEK.index(day_of_week.lower()) + days) % WEEK_IN_DAY
        day_of_week = f', {DAYS_OF_WEEK[index].capitalize()}'
    else:
        day_of_week = ''

    if days == 0:
        message_days = ''
    elif days == 1:
        message_days = " (next day)"
    else:
        message_days = f" ({days} days later)"
    return ''.join((new_time, day_of_week, message_days))


def convert_to_24(time):
    hour, minute = map(int, time[:-2].split(':'))
    if "PM" in time:
        if hour != 12:
            hour += 12
    else:
        if hour == 12:
            hour = 0
    return hour, minute


def convert_to_12(hours, minutes):
    if hours < 12:
        period = " AM"
        if hours == 0:
            hours = 12
    else:
        period = " PM"
        if hours != 12:
            hours -= 12
    hours = str(hours)
    minutes = add_zero(minutes)
    return ''.join((hours, ':', minutes, period))


def add_zero(num):
    if num < 10:
        return ''.join(('0', str(num)))
    else:
        return str(num)
