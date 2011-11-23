from euler4 import palindrome

print sum(i for i in xrange(1000000) if palindrome(str(i)) and palindrome(bin(i)[2:]))
