#Q1
def perfect_number_harmony_checker(n):
    """
    Determines if a number is a perfect number.

    A perfect number is a positive integer that is equal to the sum of its
    proper divisors (the positive divisors excluding the number itself).

    Parameters:
    - n (int): The number to check.

    Returns:
    - (True, [divisors sorted]) if n is a perfect number.
    - False if n is not a perfect number.
    - "input invalid" if n is not an integer or is less than or equal to 0.

    Examples:
    >>> perfect_number_harmony_checker(28)
    (True, [1, 2, 4, 7, 14])
    >>> perfect_number_harmony_checker(12)
    False
    >>> perfect_number_harmony_checker(-5)
    'input invalid'
    """
    import math
    lfac,s,l1,l2=[],0,[],[]
    if isinstance(n,int):
        if n>1:
            sq=int(math.sqrt(n)+1)
            lfac=[(i,int(n/i)) for i in range(1,sq) if n%i==0]
            for i in lfac:
                s+=sum(i)
                l1.append(i[0])
                l2.append(i[1])
            l2.reverse()
            lfac=l1+l2
            lfac.pop()
            if s-n==n:
                return (True,lfac)
            else:
                return False
        elif n==1:
            return False
        else:
            return 'input invalid'
    else:
        return 'input invalid'
#Q2
def collatz_chaotic_path_generator(n):
    """
    Generates a Collatz sequence for a given positive integer n.

    The Collatz sequence is defined as follows:
    - If n is even, the next number is n / 2.
    - If n is odd, the next number is 3 * n + 1.
    The sequence stops when it reaches 1.

    Parameters:
    - n (int): The starting integer.

    Returns:
    - list: The Collatz sequence.
    - "input invalid" if n is not a positive integer.

    Tricky Details:
    - If n > 10^6, cap the sequence at 1000 steps and append "truncated".
    - Detect and handle potential loops by tracking previously seen numbers.

    Examples:
    >>> collatz_chaotic_path_generator(6)
    [6, 3, 10, 5, 16, 8, 4, 2, 1]
    >>> collatz_chaotic_path_generator(0)
    'input invalid'
    """
    l=[]
    if isinstance(n,int): 
        if n<=0:
            return 'input invalid'
        elif n<=10**6:
            while n!=1:
                if n%2==0:
                    l.append(n)
                    n=int(n/2)
                else:
                    l.append(n)
                    n=3*n+1
            l.append(1)
            return l
        else:
            k=0
            for i in range(999):
                if n!=1:
                    if n%2==0:
                        l.append(n)
                        n=int(n/2)
                    else:
                        l.append(n)
                        n=3*n+1
                else:
                    break
                k+=1
            if k<=999:
                l.append(1)
                return l
            else:
                l.extend([1,'truncated'])
                return l
    else:
        return 'input invalid'
#Q3
def prime_code_breaker(n):
    """
    Determines if an integer n > 1 is a prime or composite number.

    Parameters:
    - n (int): The integer to check.

    Returns:
    - ('prime', next_prime) if n is prime, where next_prime is the next prime number after n.
    - 'composite' if n is a composite number.
    - 'neither' if n is 1.
    - "input invalid" if n is not an integer or is negative.

    Tricky Details:
    - For n up to 10^12, use an efficient primality test (e.g., trial division with 6k +/- 1 optimization).

    Examples:
    >>> prime_code_breaker(13)
    ('prime', 17)
    >>> prime_code_breaker(15)
    'composite'
    >>> prime_code_breaker(1)
    'neither'
    """
    import math
    if isinstance(n,int):
        if n>1:
            if n<=10**12:
                a=True
                for i in range(2,n//2+1):
                    if n%i==0:
                        a=False
                        break
                if a==True:
                    k=n+1
                    b=False
                    while True:
                        if any(k%i==0 for i in range(2,k-1)):
                            pass
                        else:
                            b=True
                            break
                        k+=1
                    if b==True:
                        return('prime',k)
                else:
                    return 'composite'
        elif n==1:
            return 'neither'
        else:
            return 'input invalid'
    else:
        return 'input invalid'
#Q4
import time
import bisect
import matplotlib.pyplot as plt
import numpy as np
def analyze_search_performance():
    """
    Analyzes and compares the performance of linear and binary search algorithms.

    This program performs two main tasks:
    1.  Measures and compares the execution times of linear and binary search for specific targets
        within a large sorted list (1 to 100,000). It calculates and prints the speedup factor.
    2.  Compares the worst-case performance of both algorithms across various list sizes (10 to 1,000,000)
        and plots the results on a logarithmic scale. The plot is saved as 'search_performance.png'.

    The program uses the `time` module for precise timing, the `bisect` module for an efficient
    binary search implementation, and `matplotlib.pyplot` for generating the performance plot.

    Parameters:
    - None

    Returns:
    - None

    Example:
    >>> analyze_search_performance()
    (This will print search times and save a plot, so no direct return value is shown.)
    """
    def linear_search(x,l):
        for i in l:
            if x==i:
                return True
        return False
    l=list(range(1,100001))
    ltimespeed,btimespeed,diff=[],[],[]
    for i in [97654,10**5,12345,31415]:
        stime=time.perf_counter()
        linear_search(i,l)
        sttime=time.perf_counter()
        comp=sttime-stime
        ltimespeed.append(comp)
        stime=time.perf_counter()
        bisect.bisect_left(l,i)
        sttime=time.perf_counter()
        btimespeed.append(comp/(sttime-stime))
    print("Speed-up factor of binary search over linear search is:",sum(btimespeed)/4)
    ltime,btime=[],[]
    testcases=list(range(10,100,1))+list(range(100,1000,10))+list(range(1000,10**4,100))+list(range(10**4,10**5,1000))+list(range(10**5,10**6,10**4))
    for i in testcases:
        start=time.perf_counter()
        linear_search(i,list(range(1,i+1)))
        stop=time.perf_counter()
        ltime.append(stop-start)
        start=time.perf_counter()
        bisect.bisect_left(list(range(1,i+1)),i)
        stop=time.perf_counter()
        btime.append(stop-start)
    plt.xlabel('Problem_Size')
    plt.xscale('log')
    plt.ylabel('Time in seconds(s)')
    plt.yscale('log')
    x=np.array(testcases)
    lt=np.array(ltime)
    bt=np.array(btime)
    plt.plot(x,lt,'r')
    plt.plot(x,bt,'b')
    plt.legend(['Linear Search','Binary Search'])
    plt.savefig('search_performance.png')
#Q5
def lpalgten(l):
    """
    Given a list of integers representing inscription codes, use a list comprehension to return a sorted list (in
    descending order) of unique codes that are both palindromic and greater than 10.
    • Tricky Details:
    – The input list may contain mixed data types; skip any non-integer values.
    – If there are fewer than three valid codes, return an empty list.
    – If the input is not a list, return "input invalid".

    Sample Input and Output
    Input: [121, 101, 23, 444, "a", 11, 202]
    Output: [444, 202, 121, 101]
    Input: [5, 10, 55]
    Output: []
    Input: 123
    Output: "input invalid"
    """
    if type(l)==list:
        ret=[i for i in l if str(i)==str(i)[::-1] and isinstance(i,int) and i>10]
        if len(ret)<3:
            return []
        else:
            ret.sort(reverse=True)
            return ret
    else:
        return 'input invalid'

'''#Q6
def enigfreqmap(str1):
    """
    Given an enigma text string, create a dictionary that maps characters to their frequencies. Only include
    characters that appear an odd number of times.
    • Tricky Details:
    – The output dictionary should be sorted by frequency in ascending order. For ties in frequency,
    sort by the character’s ASCII value.
    – Ignore spaces and punctuation (isalnum() can be helpful here).
    – If no characters have an odd frequency, return an empty dictionary.
    – If the input is not a string, return "input invalid".
    Sample Input and Output
    Input: "Hello World! This is an enigma."
    Output: {‘s’: 3, ‘o’: 3, ‘n’: 3, ‘d’: 1, ‘H’: 1, ‘W’: 1, ‘T’: 1, ‘h’: 1, ‘a’: 1, ‘e’: 1}
    Input: "programming"
    Output: {}
    Input: 123
    Output: "input invalid"
    """
    if type(str1)==str:
        lstr,dstr=[],{}
        for i in str1:
            if i.isalnum() and str1.count(i)%2!=0:
                lstr.update([i,ord(i),str1.count(i)])
        for i in range(1,len(lstr)):
            for j in range(1,i+1):
                if lstr[j-1][2]>lstr[j][2]:
                    lstr[j],lstr[j-1]=lstr[j-1],lstr[j]
                elif lstr[j-1][2]==lstr[j][2]:
                    if lstr[j-1][1]>lstr[j][1]:
                        lstr[j],lstr[j-1]=lstr[j-1],lstr[j]
                    else:
                        lstr[j-1],lstr[j]=lstr[j],lstr[j-1]
        lstr.reverse()
        y=set(lstr)
        print(lstr)
    else:
        return 'input invalid'
str1=eval(input("Enter a string: "))
print(enigfreqmap(str1))'''
