#!/usr/bin/env python
# coding: utf-8

# In[14]:


#The secret auction program
#Receive names and bidding values
#Find the highest bidder!

#initialize the empty secret_bidders dictionary
secret_bidders = {}
#initialize the empty tuple variable for the program loop control
bid_again = ("")

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

print("Welcom to the secret auction program!")
while bid_again not in ("N","n"):

    
    name = input("What is your name? ")

    while True:
        try:
            bid = int(input("What is your bid? $: "))
            break
        except ValueError:
            print("Please input only integer.")

    secret_bidders[name] = bid

    bid_again = ("")
    while bid_again not in("Y", "y", "N", "n"):
        bid_again = input("Is there a next bidder? Y/N: ")

max_bid = 0
max_name = ""
for names in secret_bidders:
    if secret_bidders[names] >= max_bid:
        max_bid = secret_bidders[names]
        max_name = names

print(f"The highest bidder is {max_name} with a bid of ${max_bid}!")


# In[ ]:




