# the not_blank function will reiterate itself until the user has input something other than an empty string


def not_blank(question):
    while True:
        answer = input(question).strip()
        if len(answer) != 0:
            return answer
        else:
            print("error, enter something")


# main program running to test all values in the test plan

for i in range(3):
    not_blank("enter your name")
