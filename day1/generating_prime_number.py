#Nov 24, 2017 by jimmy shen
# this code is used to generate the prime number

def gen_prime_number(n=10):
    """
    generate a list contain all the prime numbers from 2 to n.
    input n:
    output a list contain all the prime numbers from 2 to n.
    """
    a=range(2,n+1)
    if n<2:
        print "error, the input has to be larger than 2"
    else:
        return [x for x in a if [y for y in range(2,x) if x%y==0 ]==[]]


if __name__ =="__main__":
    n=int(input("pls input a number which is greater than 2 and I will output the list contains all the prime number from 2 to n:"))
    print gen_prime_number(n)
