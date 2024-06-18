import datetime
import winsound
Timing="7:48 PM"
alTime=str(datetime.datetime.now().strptime(Timing,"%I:%M %p"))
print(alTime)