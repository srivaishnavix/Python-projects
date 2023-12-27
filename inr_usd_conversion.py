def main():
    print("This program converts INR to USD")
    print()

    inr = eval(input("Enter amount in INR: "))

    usd = convert_to_usd(inr)

    print("That is" , usd , "US dollars. ")

convert_to_usd = lambda inr: inr * 0.012

main()