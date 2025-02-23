def convertToSeconds(hours, minutes):
    return f"{hours * 60 * 60 + (minutes * 60)}"


result = convertToSeconds(1, 0)
print(result)