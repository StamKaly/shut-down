import os, time, sys



def Main():
    while True:
        time_type = input('What type of time do you want to use?\n"h" for hours\n"m" for minutes\n"s" for seconds\n')
        if time_type == "h" or time_type == "m" or time_type == "s":
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
        else:
            print("Please try again!\n\n")


if __name__ == '__main__':
    Main()
