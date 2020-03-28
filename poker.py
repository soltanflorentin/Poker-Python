import itertools
import random
import unicodedata
import time

def bet_choice():
    return 10

def random_cards(nr):
    cards=[]
    for i in range(nr):
        y=random.choice(deck)
        cards.append(y)
        deck.remove(y)
    return cards

def cards_add(x,z):
    y = 0
    for i in x:
        i = int(i)
        z[i-1] = new_cards[y]
        y += 1
    return z

def doubble_win(x):
    z = ["♣", "♥", "♠", "♦"]
    while True:
        z1 = random.choice(z)
        z2 = z1
        if z1 == "♣" or z1 == "♠":
            z1 = "b"
        else:
            z1 = "r"
        while True:
            user = input("Red or Black?? R/B ?")
            if user == "r" or user == "R" or user == "b" or user == "B":
                break
            else:
                print("Please enter R or B, try again!")
                continue
        if user == z1:
            x *= 2
            print("You win: {}".format(x), z2)
            time.sleep(1)
            while True:
                ask = input("Would you like to try doubble it again? Y/N?")
                if ask == "y" or ask == "Y":
                    break
                elif ask == "n" or ask == "N":
                    return x
                else:
                    print("Upss, enter y or n, try again!")
                    continue
        else:
            print("You lost!!! ",z2)
            time.sleep(2)
            x = 0
            return x

def sort_cards(x):
   nr = []
   suits = []
   for i in x:
      nr.append(i[0] + i[1])
      if i[:2].isdigit():
         suits.append(i[3:])
      else:
         suits.append(i[2:])
   return nr,suits

def checkConsecutive(l):
    return sorted(l) == list(range(min(l), max(l) + 1))

def careu(a):
   for i in a:
      if a.count(i) == 4:
         return True

def three_kinds(a):
   for i in a:
      if a.count(i) == 3:
         return True

def two_pairs(a):
   c = 0
   b = 0
   for i in a:
       if b == 2:
           return True
       if a.count(i) == 2:
           if i == c:
               continue
           c = i
           #a.remove(i)
           b += 1
   return False

def one_pair(a):
    for i in a:
        if a.count(i) == 2:
            if i >= 12 or i == 1:
                return True
    return False


def if_win(nr,suits):

    if sorted(nr) == [1,10,12,13,14] and (suits.count("clubs") or suits.count("hearts") or suits.count("spades") or suits.count("diamonds")) == 5:
        print("ROYAL FLUSH !!!!!!")
        return bet*500
    elif (checkConsecutive(nr) or sorted(nr) == [7,8,9,10,12] or sorted(nr) == [8,9,10,12,13] or sorted(nr) == [9,10,12,13,14]) and (suits.count("clubs") or suits.count("hearts") or suits.count("spades") or suits.count("diamonds")) == 5:
        print("STRAIGHT FLUSH!!!!")
        return bet*300
    elif careu(nr):
        print("4 OF A KIND!!!!")
        return bet*100
    elif (suits.count("clubs") or suits.count("hearts") or suits.count("spades") or suits.count("diamonds")) == 5:
        print("FLUSH!!!")
        return bet*20
    elif checkConsecutive(nr) or sorted(nr) == [7,8,9,10,12] or sorted(nr) == [8,9,10,12,13] or sorted(nr) == [9,10,12,13,14]:
        print("STRAIGHT!!!")
        return bet*15
    elif three_kinds(nr):
        print("3 of a kind !!")
        return bet*10
    elif two_pairs(nr):
        print("2 pairs!!")
        return bet*5
    elif one_pair(nr):
        print("One big pair!!")
        return bet*2
    else:
        return 0


credit = 100
miza = 0
castig = 0
while True:
    numere = ["1","2","3","4","5","6","7","8","9","10","12","13","14"]
    culori=["♣","♥","♠","♦"]
    credit += castig
    if credit <= 0:
        print("No more credit !!!")
        break
    deck=[]
    for i in culori:
        for y in numere:
            deck.append(y+" "+i)

    random.shuffle(deck)
    bet = bet_choice()
    credit -= bet
    print("\n")
    print("CREDIT: {}".format(credit))
    print("BET: {}".format(bet))

    first_5_cards = random_cards(5)
    print(*first_5_cards,sep="    ")
    print(" 1  ","    2  ","   3  ","   4   ","   5 ",)

    hold_cards_input = input("Which cards you want to change? 1 2 3 4 5 ?")
    new_cards = random_cards(len(hold_cards_input))

    final_cards = cards_add(hold_cards_input, first_5_cards)
    print(*final_cards,sep="    ")

    b = sort_cards(final_cards)
    nr_str, suits_str = b[0], b[1]
    nr_int = []
    for i in nr_str:
        nr_int.append(int(i))

    castig = if_win(nr_int,suits_str)

    if castig > 0:
        print("You win: {}".format(castig))
        while True:
                ask = input("Would you like to try doubble it? Y/N?")
                if ask == "y" or ask == "Y":
                    doubble = doubble_win(castig)
                    castig = doubble
                    break
                elif ask == "n" or ask == "N":
                    break
                else:
                    print("Upss, enter y or n, try again!")
    else:
        castig = 0
        print("You lost!")
        time.sleep(2)
