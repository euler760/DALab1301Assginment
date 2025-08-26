#Q1
def validate_password(password):
    """
    Validate a password based on the following rules:
    - Minimum 8 characters.
    - At least one uppercase letter.
    - At least one digit.

    Parameters:
    - password (str): The password to validate.

    Returns:
    - bool: True if password is strong, False otherwise.
    - "input invalid" if the input is not a string.

    Example:
    >>> validate_password("Hello123")
    True
    >>> validate_password(12345678)
    'input invalid'
    """
    if type(password)==str:
        x=len(password)
        Ucoun,dcoun=0,0
        if x>=8:
            for i in password:
                if i.isupper():
                    Ucoun+=1
                if i.isdigit():
                    dcoun+=1
            if Ucoun>=1 and dcoun>=1:
                return True
            else:
                return False
        else:
            return False
    else:
        return "input invalid"
#Q2
def mask_email(email):
    """
    Mask an email ID for privacy based on the following rules:
    - Show only the first 2 letters of the username.
    - Replace the rest of the username with '*' characters.
    - Keep the domain name unchanged.

    Parameters:
    - email (str): The email address to mask.

    Returns:
    - str: The masked email address.
    - "input invalid" if the input is not a valid email string.

    Example:
    >>> mask_email("john.doe@gmail.com")
    'jo*****@gmail.com'
    >>> mask_email(123)
    'input invalid'
    """
    if type(email)==str:
        if '@' not in email:
            return 'input invalid'
        else:
            y=email.index('@')
            x=list(email)
            for i in range(2,y):
                x[i]="*"
            return ''.join(x)
    else:
        return "input invalid"
#Q3
def atm_withdrawal(withdraw_amount, account_balance):
    """
    Simulate an ATM withdrawal with the following rules:

    Rules:    
    - Minimum withdrawal is ₹100, maximum is ₹10,000.
    - Withdrawal amount must be a multiple of ₹100.
    - Users must have enough balance to withdraw.
    - Bank charges ₹5 for each withdrawal.

    Parameters:
    - withdraw_amount (int or integer-like string): Amount the user wants to withdraw.
    - account_balance (int or integer-like string): Current account balance.

    Returns:
    - float: Updated account balance after withdrawal and ₹5 charge if transaction is valid.
    - str: Error message: "Rules not met" if even one of the rules are not met.
    - "input invalid" if inputs are not valid integers or are negative.

    Notes:
    - Deduct ₹5 only if withdrawal is successful.
    - If withdrawal is unsuccessful, balance should remain unchanged.

    Examples:
    >>> atm_withdrawal(500, 2000)
    1495.0
    >>> atm_withdrawal("five hundred", 2000)
    'input invalid'
    >>> atm_withdrawal(103, 2000)
    "Rules not met" 
    """
    if isinstance(withdraw_amount,str):
        if withdraw_amount.isdigit()==False:
            return 'input invalid'
    intwithdraw=int(withdraw_amount)
    if isinstance(account_balance,str):
        if account_balance.isdigit()==False:
            return 'input invalid'
    intaccount=int(account_balance)
    if 0<=intaccount<105 or intwithdraw>(intaccount-5) or intwithdraw<100 or intwithdraw>10000 or intwithdraw%100!=0:
        if intwithdraw<0 or intaccount<0:
            return 'input invalid'
        else:
            return "Rules not met"
    else:
        return 1.0*(intaccount-intwithdraw-5)
#Q4
def calculate_ticket_price(ages):
    """
    Calculate the total price for cinema tickets:
    - ₹150 per ticket for children under 12 years.
    - ₹200 per ticket for senior citizens (age 60+).
    - ₹250 per ticket for others.
    - If more than 5 tickets are booked in one transaction: 10% discount.

    Parameters:
    - ages (list of int): Ages of all people in the group.

    Returns:
    - float: Total amount to be paid after discounts.
    - "input invalid" if ages is not a list of valid non-negative integers.

    Example:
    >>> calculate_ticket_price([10, 30, 65, 40, 8, 12])
    1080.0
    >>> calculate_ticket_price("10, 30")
    'input invalid'
    """
    if type(ages)==list:
        fare=0
        if len(ages)>=5 and all(j>=0 for j in ages) and all(type(j)==int for j in ages):
            for i in ages:
                if i<12:
                    fare+=150
                elif i>=60:
                    fare+=200
                else:
                    fare+=250
            return fare*0.9
        elif len(ages)<5 and all(j>=0 for j in ages) and all(type(j)==int for j in ages):
            for i in ages:
                if i<12:
                    fare+=150
                elif i>=60:
                    fare+=200
                else:
                    fare+=250
            return fare*1.0
        else:
            return "input invalid"
    else:
        return "input invalid"
#Q5
def first_non_repeating_char(s):
    """
    Return the first non-repeating character in the given string.

    Parameters:
    - s (str): The input string.

    Returns:
    - str: The first character that occurs exactly once in the string.
    - "" (empty string) if every character repeats or input string is empty.
    - "input invalid" if the input is not a string.

    Requirements:
    - Treat characters case-sensitively ('a' and 'A' are considered different).
    - Do NOT print anything; only return the result.
    - Add comments inside your function specifying:
        # Time Complexity: ...
        # Space Complexity: ...

    Examples:
    >>> first_non_repeating_char("leetcode")
    'l'
    >>> first_non_repeating_char("aabbcc")
    ''
    >>> first_non_repeating_char(1234)
    'input invalid'
    """
    #Time complexity: This code will have to initially iterate through a string of length n, creating a dictionaries where the keys are the individual characters (non-repetitive, i.e., if any character is repetitive or not, it will be recorded only once) of the string. So, already the complexity is proportional to n. After this, it will iterate the dictionary in search of the first character which is non-repetitive (that is character count=1) and the list of keys to print that specific character (if it exists). Usage of two loops squares the complexity, making it proportional to n^2
    #Space complexity: This code's space complexity is n (as the length of the string determines it), with the length of the string input, being n.
    if type(s)==str:
        d={}
        a=False
        x=0
        for i in s:
            if i!="'":
                d[i]=s.count(i)
        y=list(d)
        c=0
        for i in d:
            if d[i]==1:
                a=True
                x=y.index(i)
                c+=1
                if c==2:
                    break
        if a==True:
            return y[x]
        else:
            return ''
    else:
        return "input invalid"
print(first_non_repeating_char(eval(input("Enter a string: "))))
