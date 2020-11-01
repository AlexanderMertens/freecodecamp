def convert_to_24(time):
    hour = int(time[:2]) % 12
    minute = int(time[3:5])
    if "PM" in time:
        hour += 12
    return hour, minute


def convert_to_12(hours, minutes):
    if hours < 12:
        period = " AM"
    else:
        period = " PM"
    return ''.join((str(hours % 12), ':', str(minutes), period))
