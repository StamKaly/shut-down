import os, time, sys



def Main():
    while True:
        time_type = input('What type of time do you want to use?\n"h" for hours\n"m" for minutes\n"s" for seconds\n"hm" for Hours:Minutes (eg: 3:43)\n')
        if time_type == "h" or time_type == "m" or time_type == "s" or time_type == "hm":
            while True:
                if time_type == "h":
                    try:
                        hours = int(input("In how many hours do you want your computer to shut down?\n"))
                        shut = hours * 3600
                        print("Please don't close this window!\n")
                        time.sleep(shut)
                        print("Shutting down...\nIf you've changed your mind you have 7 seconds to close this window before it shuts your computer down")
                        time.sleep(7)
                        os.system('shutdown -s')
                        sys.exit(0)
                    except ValueError:
                        print("Please input a number of hours!")
                if time_type == "m":
                    try:
                        minutes = int(input("In how many minutes do you want your computer to shut down?\n"))
                        shut = minutes * 60
                        print("Please don't close this window!")
                        time.sleep(shut)
                        print("Shutting down...\nIf you've changed your mind you have 7 seconds to close this window before it shuts your computer down")
                        time.sleep(7)
                        os.system('shutdown -s')
                        sys.exit(0)
                    except ValueError:
                        print("Please input a number of minutes!")
                if time_type == "s":
                    try:
                        seconds = int(input("In how many seconds do you want your computer to shut down?\n"))
                        print("Please don't close this window!")
                        time.sleep(seconds)
                        print("Shutting down...\nIf you've changed your mind you have 7 seconds to close this window before it shuts your computer down")
                        time.sleep(7)
                        os.system('shutdown -s')
                        sys.exit(0)
                    except ValueError:
                        print("Please enter a number of seconds!")
                if time_type == "hm":
                    timen = input("In how many Hours:Minutes do you want your computer to shut down?\n")
                    if len(timen) <= 5 and timen.count(':') == 1:
                        hours, minutes = timen.split(':')
                        try:
                            hours = int(hours)
                            minutes = int(minutes)
                            if hours <= 23 and minutes <= 59:
                                if minutes != 0:
                                    shutm = minutes * 60
                                else:
                                    shutm = 0
                                if hours != 0:
                                    shuth = hours * 3600
                                else:
                                    shuth = 0
                                shut = shutm + shuth
                                print("Please don't close this window!\n")
                                time.sleep(shut)
                                print("Shutting down...\nIf you've changed your mind you have 7 seconds to close this window before it shuts your computer down")
                                time.sleep(7)
                                os.system('shutdown -s')
                                sys.exit(0)
                            else:
                                print("Maximum is 23:59")
                        except ValueError:
                            print("Please make sure you input actual time!")
                    else:
                        print("Please make sure you input actual time!")
                        

        else:
            print("Please try again!\n\n")


if __name__ == '__main__':
    Main()
