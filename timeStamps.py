def sum_timestamps(timestamps):
    total_seconds = 0

    for timestamp in timestamps:
        minutes, seconds = timestamp.split(',')
        total_seconds += int(minutes) * 60 + int(seconds)

    # Convert the total seconds back to MM, SS format
    final_minutes = total_seconds // 60
    final_seconds = total_seconds % 60

    return f"{final_minutes:02d}, {final_seconds:02d}"



timestamps = ['05, 30', '02, 15', '01, 45']
result = sum_timestamps(timestamps)
print(result)  # Output: 09, 30
