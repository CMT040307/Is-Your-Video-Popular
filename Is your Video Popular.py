def master():
    likes = int(input("How many likes has the video got?"))
    gained_subs = int(input("How many subscribers/followers have you gained because of the video?"))
    if likes >= 100 and gained_subs >= 1:
        print("The Video is popular")
    else:
        print("Not popular yet sorry")

    restart = input("Do you want to restart? y/n")
    if restart.lower() == "y":
        master()
    else:
        exit()

master()