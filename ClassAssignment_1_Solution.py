#Q1
def even_odd(n):
    """
    Checks whether a number is even or odd.

    Parameters:
    - n: int, integer-like string, or other  (e.g., 4, "7", etc.)

    Returns:
    - "even" if n is an integer and even
    - "odd" if n is an integer and odd
    - "input invalid" for any other type of input

    Examples:
    >>> even_odd(6)
    'even'
    >>> even_odd(7)
    'odd'
    >>> even_odd("abc")
    'input invalid'
    """
    if type(n).__name__=="int":
        if n%2==0:
            return "even"
        elif n%2==1:
            return "odd"
        else:
            return "input invalid"
    elif type(n).__name__=="str":
        if n.isdigit():
            return even_odd(int(n))
        elif n.startswith("-") and n[1:len(n)].isdigit():
            return even_odd(int(n))
        else:
            return "input invalid"
    else:
        return "input invalid"
#Q2
def course_name_formatter(course):
    """
    Extract and return the first and last words from the given course string.

    Parameters:
    - course: a string representing the course title.

    Returns:
    - "<first> <last>" if the course has at least two words.
    - "input invalid" otherwise

    Examples:
    >>> course_name_formatter("Programming Structures")
    'Programming Structures'
    >>> course_name_formatter("Data Structures and Algorithms")
    'Data Algorithms'
    >>> course_name_formatter("Python")
    'input invalid'
    """
    if type(course).__name__=="str" and len(course.split())>=2:
        y=course.split()
        return  y[0]+" "+y[len(y)-1]
    else:
        return "input invalid"
#Q3
def digit_sum(n):
    """
    Compute the sum of all digits in the given integer n.

    Parameters:
    - n: an integer (positive or negative), or integer-like string

    Returns:
    - Sum of digits as int
    - "input invalid" for invalid input

    Examples:
    >>> digit_sum(12345)
    15
    >>> digit_sum(-502)
    7
    >>> digit_sum("abc")
    'input invalid'
    """
    if type(n).__name__=="int":
        c=0
        x=abs(n)
        while x!=0:
            c+=abs(x)%10
            x=x//10
        return c
    elif type(n).__name__=="str":
        if n.isdigit():
            return digit_sum(int(n))
        elif n.startswith("-") and n[1:len(n)].isdigit():
            return digit_sum(int(n))
        else:
            return "input invalid"
    else:
        return "input invalid"
#Q4
def library_fine(overdue_days):
    """
    Compute the total library fine based on overdue days.

    Parameters:
    - overdue_days: an integer >= 0, or integer-like string

    Returns:
    - Fine as int
    - "input invalid" for invalid input

    Fine Rules:
    - ₹1/day for first 5 days
    - ₹2/day for next 5 days
    - ₹5/day beyond 10 days

    Examples:
    >>> library_fine(3)
    3              # 3 days * ₹1
    >>> library_fine(7)
    9              # 5*₹1 + 2*₹2 = 5 + 4 = 9
    >>> library_fine(12)
    25             # 5*₹1 + 5*₹2 + 2*₹5 = 5 + 10 + 10 = 25
    >>> library_fine("ten")
    'input invalid'
    """
    n=overdue_days
    if type(n).__name__=="int":
        if n==0:
            return 0
        elif 5>=n>0:
            return n*1
        elif 10>=n>5:
            return 5+(n-5)*2
        elif n>10:
            return 15+(n-10)*5
        else:
            return "input invalid"
    elif type(n).__name__=="str":
        if n.isdigit():
            if int(n)>=0:
                return library_fine(int(n))
            else:
                return "input invalid"
        else:
            return "input invalid"
    else:
        return "input invalid"
#Q5
def encode_morse(text):
    """
    Takes a given text as input and converts it into morse code

    Parameters:
    - text: Takes a text as input and converts it into morse code

    Returns:
    - Morse code if the given input is an str
    - "input invalid" for any type of input given
    """
    lmcode={"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":"--","X":"-..-","Y":"-.--","Z":"--..","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.","0":"-----"}
    mcode=""
    if type(text).__name__=="str":
        for i in text:
            for j in lmcode:
                if i.upper()==j:
                    mcode+=lmcode[j]+" "
        return mcode
    else:
        return "input invalid"
def decode_morse(morse_code):
    """
    Takes a given morse code as input and converts it into text

    Parameters:
    - text: Takes a string as input and converts it into morse code

    Returns:
    - text if the given input is morse code
    - "input invalid" for any type of input given
    """
    lmcoderev={".-":"A","-...":"B","-.-.":"C","-..":"D",".":"E","..-.":"F","--.":"G","....":"H","..":"I",".---":"J","-.-":"K",".-..":"L","--":"M","-.":"N","---":"O",".--.":"P","--.-":"Q",".-.":"R","...":"S","-":"T","..-":"U","...-":"V",".--":"W","-..-":"X","-.--":"Y","--..":"Z",".----":"1","..---":"2","...--":"3","....-":"4",".....":"5","-....":"6","--...":"7","---..":"8","----.":"9","-----":"0"}
    try:
        y=morse_code.split()
        txt=[]
        for i in y:
            for j in lmcoderev:
                if i==j:
                    txt+=[lmcoderev[j]]
        x="".join(txt)
        return x
    except:
        return "input invalid"
