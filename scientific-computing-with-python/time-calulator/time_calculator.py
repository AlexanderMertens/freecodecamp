def convert_to24(time):
    hour = int(time[:2]) % 12
    minute = int(time[3:5])
    if "PM" in time:
        hour += 12
    return hour, minute
