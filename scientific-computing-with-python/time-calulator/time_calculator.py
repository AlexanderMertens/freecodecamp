def convert_to_24(time):
    hour = int(time[:2]) % 12
    minute = int(time[3:5])
    if "PM" in time:
        hour += 12
    return hour, minute


def convert_to_12(hours, minutes):
    if hours < 12:
        period = " AM"
        if hours == 0:
            hours = 12
    else:
        period = " PM"
        hours -= 12
    hours, minutes = num_to_string(hours, minutes)
    return ''.join((hours, ':', minutes, period))


def num_to_string(*nums):
    result = []
    for num in nums:
        if num < 10:
            result.append(''.join(('0', str(num))))
        else:
            result.append(str(num))
    return result
