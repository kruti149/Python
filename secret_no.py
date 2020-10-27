secret_number = 777
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

bol = True
while bol == True:
    inputvalue = int(input("Enter an integer  "))
    if(inputvalue == secret_number):
        print("Well done, muggle! You are free now.")
        bol == False
        break
    else:
        print("Ha ha! You're stuck in my loop!")
        # bol == True
        continue