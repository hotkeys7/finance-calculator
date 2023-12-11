import math

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

# these lists to catch spelling mistakes/different inputs a user might make, could be expanded
i = ["investment", "invest", "Investment", "INVESTMENT", "INVVESTMENT", "i"]
b = ["bond", "Bond", "BOND", "b", "BOOOND", "bOOND", "BoNd", "Bonding", "Bz", "Bn"]
s = ["simple", "Simple", "s", "si", "sim", "simp", "simpl", "SI", "SIM", "SiM", "SIMPLE"]
c = ["compound", "Compound", "COnpound", "Confond", "CoMpoUnd", "COMPOUND", "c"]

# function for investing, cleans up the later operation 
# .replace() to catch user inputs that could alter the calculation
# I have assumed the currency as £
def invest():
    deposit = int(input("How much money are you depositing in £? ").replace("£", ""))
    per = int(input("What is the interest rate as a percentage? ").replace("%", ""))
    r = per/100
    years = int(input("How many years do you intend to invest? ").replace("years", ""))
    interest = input("Do you want 'simple' or 'compound'? ")
    if interest in s:
        A = deposit * (1 + (r*years))
        print(f"You will make £{int(A)} after {years} years")
    elif interest in c:
        A_c = deposit * math.pow((1 + r), years)
        print(A_c)
    else: 
        print("Please try again")
        invest()

# function for calculating bonds
def bond():
    value = int(input("What is the value of your house in £?").replace("£", ""))
    per = int(input("What is the interest rate?").replace("%", ""))
    i = ((per/100) / 12)
    month = int(input("How many months do you plan to pay the bond?").replace("months", ""))
    repayment = (i * value) / (1 - (1 + i)**(-month))
    print(f"You will have to pay £{int(repayment)} each month :o")         

# This function to start the process, that guides the user to either the invest() function 
# or the bond() function 
def start():
    decide = input("Enter either 'investment' or 'bond' from the menu above to proceed. (i/b) ")

    if decide in i:
        invest()
        
    elif decide in b:
        bond()

    else:
        print("Sorry, we didn't catch that. Please enter again ")
        start()


start()