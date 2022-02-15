correct_num=18
i=0
while(i+1<=9):
    var=int(input("Guess the no."))
    if var==correct_num:
        print("You won")
        break
    elif var<correct_num:
        print("Guess a greater no.")
    else:
        print("Guess a lesser no.")
    i=i+1
if i+1>9:
    print("No. of guesses over")