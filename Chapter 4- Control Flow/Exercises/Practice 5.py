#Write a Python program that uses the elif statement to determine the season based on the
#month provided as input.

# Get user input for the month
month = input("Enter any month : ")

# Convert input to lowercase for case-insensitive comparison
month = month.lower()

# Determine the season based on the month
if month in ["december", "january", "february"]:
    season = "Winter"
elif month in ["march", "april", "may"]:
    season = "Spring"
elif month in ["june", "july", "august"]:
    season = "Summer"
elif month in ["september", "october", "november"]:
    season = "Autumn"
else:
    season = "Unknown"

# Display the result
if season != "Unknown":
    print(f"The season in {month.capitalize()} is {season}.")
else:
    print(f"Sorry, the month '{month.capitalize()}' is not valid or recognized.")
