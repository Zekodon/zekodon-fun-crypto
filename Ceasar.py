import os

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def enc():
	plaintext = input("Enter message: ")
	key = int(input("Enter offset (1-26): "))
	cipher = ''
	for c in plaintext:
		if c in alphabet:
			cipher += alphabet[(alphabet.index(c)+key)%(len(alphabet))]

	print('Your translated message is: ' + cipher)

def dnc():
	plaintext = input("Enter message: ")
	key = -26
	cipher = ''
	while key < 27:
		cipher = ''
		for c in plaintext:
			if c in a:
				cipher += alphabet[(alphabet.index(c)+key)%(len(alphabet))]
		
		print(str(key) + " |-> " + cipher)
		key+=1

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def TitleBar():
        print("  _____   _____   ______  ______   ______   ______")
        print(" |       |_____| |______ |______  |______| |_____/")
        print(" |_____  |     | |______  ______| |      | |    \_\n\n")
                                                
                                                

def getusrChoice():   
	# Let users know what they can do.
	TitleBar()
	print("[E]ncrypt text as Caesar cipher.")
	print("[D]ecrypt a Caesar cipher.")
	print("[A]bout this Program.")
	print("[Q]uit.")
	return input("\nWhat would you like to do? " )

####################
### MAIN PROGRAM ###
####################
choice = ''
cls()
while choice != 'Q':    
    choice = getusrChoice()
    # Respond to the user's choice.
    
    if choice == 'E':
    	enc()
    elif choice == 'D':
    	dnc()
    elif choice == 'A':
        print("\nThis is Ceasar cipher/solver tool. Developed by @Zekodon and @KobyKotiv. Follow us on twitter.")
    elif choice == 'Q':
        print("\nGoodbye.")
    else:
        print("\nError! Try again!\n")
