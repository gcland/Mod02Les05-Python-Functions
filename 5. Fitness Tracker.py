import math
def tracker():
    i=0
    activities = [] 
    duration = []
    

    while i<3:
    
        activities.append(input("\n Enter an activity to track: "))

        duration.append(input("\n Enter in the duraction of the activity (in minutes): "))

        i+=1
        print(activities, duration)
    
    def calories(): 
        for i in range(0, len(duration)):
            duration[i] = int(duration[i])
        burned = sum(duration)*4 #4 is defined number of carloies burned per minute.
        print("\n Total calories burned:", burned)

    def summary():
        for i in range (len(activities)):
            print("\n Activity", str(i+1)+":", activities[i]+". Duration:", duration[i],"minutes. Calories burned:", int(duration[i])*4)
        calories()
    print("TODAY'S ACTIVITY REPORT:")       
    summary()

tracker()