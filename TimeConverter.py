Hours = int(input("Enter the hour : "))
Min = int(input("Enter the minutes : "))
# 24 Hour to 12 Hour
if Hours > 12 :
    TweleveHour = Hours - 12 
    print (TweleveHour,":",Min,"PM")
    # 12 Hour to 24 Hour
elif Hours <12 : 
    State = str(input("ENTER AM OR PM : "))
    if State == 'PM':
        TwentyFourHour = Hours + 12
        print(TwentyFourHour,Min)
    elif State == 'AM':
        if Hours > 9 :
            print (Hours,Min)
        elif Hours < 10 :
            print("0",Hours,Min)
