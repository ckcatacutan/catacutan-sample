def loan_eligibility():
    
    monthly_salary = float(input("Enter your monthly salary: "))
    loan_amount = float(input("Enter the loan amount you are requesting: "))

    salary_threshold = 30000.00
    max_loan_factor = 10 

    if monthly_salary >= salary_threshold:
        maxloanamount = monthly_salary * max_loan_factor
        if loan_amount <= maxloanamount:
            print("Congratulations! You are eligible for the loan.")
            
            months = int(input("In how many months would you like to repay the loan? "))
            
            totalamount = loan_amount * 1.10 
            monthlypment = totalamount / months

            print(f"With a 10% interest rate, the total loan amount is: {totalamount:.2f}")
            print(f"You will need to pay {monthlypment:.2f} per month for {months} months.")
        
        else:
            print(f"Sorry, you are not eligible for the loan because the requested amount exceeds the allowed limit.")
            print(f"Your maximum loan amount can be: {maxloan_amount:.2f}")
    else:
        print(f"Sorry, you are not eligible for the loan due to insufficient salary.")
        print(f"You need a monthly salary of at least {salary_threshold:.2f}.")

loan_eligibility()
