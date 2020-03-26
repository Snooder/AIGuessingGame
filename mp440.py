

'''
GCD algorithm
'''
def gcd(a, b):
	if(a%b==0):
		return b
	else:
		gcd(b,a%b)
	return -1

'''
Rectangles on a rubik's cube
'''
def rubiks(n):
	count=0
	i=1
	while i <= n:
		count+=i
		i+=1
	return ((count*count)*6)
'''
Guessing a number
'''
def guess_unlimited(n, is_this_it):
    # The code here is only for illustrating how is_this_it() may be used  
	x=0
	for x in range(1,n+1):
		if is_this_it(x) == True:
			return x
        
'''
Guessing a number where you can only make two guesses that are larger
'''
def guess_limited(n, is_this_smaller):
    lower_bound = 1
    guess = (-1+(1-4*1*-2*n)**0.5)/2
    if (guess).is_integer() == False:
        guess = int(guess)+1
    else:
        guess = int(guess)
    increment = guess

    while lower_bound <= n:
        if is_this_smaller(guess) == False:
            for x in range (lower_bound, guess):
                if is_this_smaller(x) == False:
                    return x
            return guess
        else:
            lower_bound = guess+1
            guess += increment-1
            increment -= 1
            if guess > n:
                guess = n

    if lower_bound > n:
            return "Error. The number you have to guess for Problem 4 is out of range."		
'''
Guessing a number, bonus problem
'''
def guess_limited_plus(n, is_this_smaller):
    return guess_limited_plus_helper(1, n, is_this_smaller)
 
def guess_limited_plus_helper(lower, upper, is_this_smaller):
    if lower == upper:
        return lower
    elif upper-lower == 1:
        if is_this_smaller(lower) == False:
            return lower
        return upper
 
    mid = (lower + upper)/2
    if is_this_smaller(mid) == False:
        return guess_limited_plus_helper(lower, mid, is_this_smaller)
    else:
        return guess_limited_plus_helper(mid+1, upper, is_this_smaller)
        

