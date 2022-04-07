##
# roulettle_payouts.py
# spins roulette
#
# 11/2/22
import random

#selects random single number
single = random.randint(0,37)
if single == 37:
    print("pay 00")
elif single == 0:
    print("pay 0")
else:
    print("The spin resulted in {}...".format(single))
    print("pay {}".format(single))
    #red vs black
    red_vs_balck = random.randint(1,2)
    if red_vs_balck == 1:
        print("pay red")
    else:
        print("pay black")

    #odd vs even
    #number divided by 2
    odd_even = single%2

    #outputs if the number is even
    if odd_even == 0:
        print("pay even")
    #outputs if the number is odd
    elif odd_even == 1:
        print("pay odd")
        
    #1-18 vs 19-36
    if single < 18:
        print("pay 1-18")
    else:
        print("pay 19-36")
