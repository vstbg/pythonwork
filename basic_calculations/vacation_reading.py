# Read user input
pages = int(input())
pages_for_one_hour = int(input())
total_days = int(input())

# Logics
total_time_needed = pages / pages_for_one_hour
pages_a_day = total_time_needed / total_days

# Print output
print(int(pages_a_day))
