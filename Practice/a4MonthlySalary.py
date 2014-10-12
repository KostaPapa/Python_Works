def calculate_the_total_monthly_salary ():
    ''' This function will calculate the total monthly salary by adding the monthly salary and bonus. '''

    first_and_last_name = str (raw_input ( "Please, enter your first and last name: " ))    
    employer_id = str (raw_input ("Please, enter your identification number? "))
    monthly_salary = 5.123
    monthly_bonus = float (raw_input ( "Please, enter the monthly bonus: "))       # Will get the bonus amount and store it to the memory.
    
    total_salary = monthly_salary + monthly_bonus

    print "\nYour total salary for this month is: ", total_salary
    
    print "Have a nice day!"
    

calculate_the_total_monthly_salary()
