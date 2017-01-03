import random
def Reels():
    Ret_Val = [0," "," "," "]
    Reel_Spin = random.randrange(1,4,1),random.randrange(1,4,1),random.randrange(1,4,1)
# Reel 1
    if Reel_Spin[0] == 1:
	    Ret_Val[0] += 1
	    Ret_Val[1] = "Banana"
    if Reel_Spin[0] == 2:
	    Ret_Val[0] += 5
	    Ret_Val[1] = "Orange"
    if Reel_Spin[0] == 3:
	    Ret_Val[0] += 20
	    Ret_Val[1] = "Cherry"
# Reel 2
    if Reel_Spin[1] == 1:
	    Ret_Val[0] += 1
	    Ret_Val[2] = "Banana"
    if Reel_Spin[1] == 2:
	    Ret_Val[0] += 5
	    Ret_Val[2] = "Orange"
    if Reel_Spin[1] == 3:
	    Ret_Val[0] += 20
	    Ret_Val[2] = "Cherry"
# Reel 3
    if Reel_Spin[2] == 1:
	    Ret_Val[0] += 1
	    Ret_Val[3] = "Banana"
    if Reel_Spin[2] == 2:
	    Ret_Val[0] += 5
	    Ret_Val[3] = "Orange"
    if Reel_Spin[2] == 3:
	    Ret_Val[0] += 20
	    Ret_Val[3] = "Cherry"
    return Ret_Val
Player_Money = 1000	
Jackpot = 100
Run = True
while Run == True:
    Bet = 0
    if Player_Money < 1:
	    input("Have some more money to gamble with you addict")
	    Player_Money = 1000
	    Jackpot = 100
    Bet_Line = input(" How much are you willing to pay? \n The Jackpot $ " + str(Jackpot) + "\n Current Money $ " + str(Player_Money) + "\n Q = quit \n")
    if Bet_Line == "q" or Bet_Line == "Q":
	    Run = False
	    break
    try:
	    Bet = int(Bet_Line)
    except:
	    print("That doesn't work here")
	    pass
    if Bet > Player_Money:
	    print("You don't have enough money, you addict")
    elif Bet <= Player_Money and Bet != 0:
	    Jackpot += (int(Bet*.15))
	    Player_Money -= Bet
	    Is_Winner = Reels()
	    I_W = Is_Winner[0]
	    Fruits = Is_Winner[1] + " - " + Is_Winner[2] + " - " + Is_Winner[3]
	    if I_W == 3 or I_W == 15 or I_W == 60:
		    print(Fruits + "\n" + "You Won $ " + str(Bet*4) + " !!! \n")
		    Player_Money += (Bet*4)
		    JP1 = random.randrange(1,51,1)
		    JP2 = random.randrange(1,51,1)
		    if  JP1 == JP2:
			    print ("You Won The Jackpot !!!\nHere is your $ " + str(Jackpot) + " prize! \n")
			    Jackpot = 100
		    elif JP1 != JP2:
			    print ("You did not win the Jackpot this time. \nPlease try again ! \n")
	    elif I_W == 7 or I_W == 22 or I_W == 11 or I_W == 30 or I_W == 41 or I_W == 45:
		    print(Fruits + "\n" + "You Won $ " + str(int(Bet*.5)) + ", some chump change. \n")
		    Player_Money += (int(Bet*.5))
	    else:
		    print(Fruits + "\n You really suck at this, don't you.")
