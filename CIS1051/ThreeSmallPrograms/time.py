#HOURS MINUTES SECONDS
#REFRENCED 2.15 FROM TEXTBOOK

seconds = int(input("Enter a number of seconds "))
hours = seconds // 3600
remainingsecs = seconds % 3600
minutes =  remainingsecs // 60
finalsecs = remainingsecs  % 60
print("Hours: ", hours, "Minutes: ", minutes, "Seconds: ", finalsecs)
