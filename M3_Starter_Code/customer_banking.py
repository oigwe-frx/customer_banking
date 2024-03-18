# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("Enter the savings account balance: "))
    savings_interest = float(input("Enter the savings account interest rate: "))
    savings_maturity = int(input("Enter the number of months for the savings account: "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    formatted_interest_earned = "{:.2f}".format(interest_earned)
    print(f"The interest earned on the savings account is ${formatted_interest_earned}.")
    
    formatted_updated_savings_balance = "{:.2f}".format(updated_savings_balance)
    print(f"The updated savings account balance is ${formatted_updated_savings_balance}.")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("Enter the CD account balance: "))
    cd_interest = float(input("Enter the CD account interest rate: "))
    cd_maturity = int(input("Enter the number of months for the CD account: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_cd_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    formatted_cd_interest_earned = "{:.2f}".format(interest_cd_earned)
    print(f"The interest earned on the CD account is ${formatted_cd_interest_earned}.")

    formatted_updated_cd_balance = "{:.2f}".format(updated_cd_balance)
    print(f"The updated CD account balance is ${formatted_updated_cd_balance}.")

if __name__ == "__main__":
    # Call the main function.
    main()
