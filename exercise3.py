correct_num=18
while(True):
    var=int(input("Guess the no."))
    if var==correct_num:
        print("You won")
        break
    else:
        print("Keep guessing")
        continue
