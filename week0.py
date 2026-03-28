# week 0 problem 1
# create a function that returns a list of (vitamins,injections) tuples for each attribute that they need.
# Complete problem statement in README.mds


# your input type should be a list,
# output should also be a list containing tuples
# Example:
# input: [250, 0, 250, 0, 0, 0]
# expected output: [(25,0),(0,0),(25,0),(0,0),(0,0),(0,0)]
# input: [500, 1, 2, 3, 4, 5]
#expected output: "No medicine given"
# HINT: using % operator to find remainder may be helpful
def dose(needs):
    #YOUR SOLUTION STARTS HERE
    
    import math


    # hp = int(input("please input the HP"))
    # attack = int(input("Please input the Attack"))
    # defense = int(input("please input the defense"))
    # special_attack = int(input("please input the special attack"))
    # special_defence = int(input("please input the special defence"))
    # speed = int(input("please input the speed"))

    # sum = hp+attack+defense+special_defence+speed
    
    hp = needs[0]
    attack = needs[1]
    defense = needs[2]
    special_attack = needs[3]
    special_defence = needs[4]
    speed = needs[5]

    needs = [int(hp), int(attack), int(defense), int(special_attack), int(special_defence), int(speed)]
    vitamins = int(10)
    injections = int(1)
    decision = []


    if sum(needs) <= 500:
        for i in needs:
            while i <= 250:
                vit_doze = int((math.ceil(i/10) * 10)/vitamins)
                inj_doze = (vit_doze*vitamins)-(i*injections)
                total_doze = (vit_doze, inj_doze)
                print("Total doze for each is: ", total_doze)
                decision.append(total_doze)
                break
    else:
        print("no medicine given")

    print("The given needs is: ", needs)
    return print("Here is the outcome: ", decision)

example1 = [223,12,126,0,37,12]    
result = dose(example1)
    #YOUR SOLUTION ENDS HERE

