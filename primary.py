while True:
    print("Choose an option [a]Main Path and [b] User Provided Path: ")
    choice =str(input("Your Choice: "))
    if choice == 'a':
        import main
        break
        
    elif choice == 'b':
        import call
        break
    else:
        print ("Invalid input......!")