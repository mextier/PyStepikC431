def get_int(start_message, error_message, end_message):
    print(start_message)
    while True:
        try:
            i = int(input())
            print(end_message)
            return(i)
        except ValueError as e:
            print(error_message)

get_int("start","error","end")
