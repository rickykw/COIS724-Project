import glob
import time
import datetime
from geopy.distance import vincenty


data = glob.glob('Data/002/Trajectory/*.*')

days = [list(open(d, "r")) for d in data]
days = [d[6:] for d in days]
total_stay_points = 0 # stay points for this user
for i in range(len(days)):

    prev_second = 0
    curr_second = 0

    total_seconds = 0

    start_lat = 0
    start_long = 0
    
    curr_lat = 0
    curr_long = 0

    total_distance = 0
    
    

    for j in range(len(days[i])):
        days[i][j] = days[i][j].strip('\r\n').split(',')
        x = days[i][j][-1]
        x = time.strptime(x,'%H:%M:%S')
        curr_second = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()

        curr_lat = days[i][j][0]
        curr_long = days[i][j][1]
        
        if j == 0: 
            prev_second = curr_second
            start_lat = curr_lat
            start_long = curr_long
            
        total_seconds += int(curr_second) - int(prev_second)
        
        prev_second = curr_second

        curr_pos = (curr_lat, curr_long)
        start_pos = (start_lat, start_long)

        total_distance = vincenty(start_pos, curr_pos).meters

        if total_seconds  >= 1200 and total_distance <= 200:
            print "stay point"
            print "the time is %s %s" % (str((total_seconds) / 60.),  "hours" if ((total_seconds) / 60.) > 60 else "minutes")  
            print "the distance is %s metres" % total_distance
            start_lat = curr_lat
            start_long = curr_long
            total_stay_points += 1
            total_seconds = 0
        elif total_seconds >= 1200 and total_distance > 200:
            total_seconds = 0
            start_lat = curr_lat
            start_long = curr_long
            
            
    print "There are %s stay points for this date" % str(total_stay_points)
    
     # remove this break if you want to run all the dates for the user
