def main():
    print("This program converts USD to INR")
    print()

    usd = eval(input("Enter amount in USD: "))

    inr = convert_to_inr(usd)

    print("That is" , inr , " Indian rupees.")

convert_to_inr = lambda usd: usd * 83.27 

main()