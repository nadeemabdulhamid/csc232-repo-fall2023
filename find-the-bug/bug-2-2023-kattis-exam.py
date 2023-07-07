# FIND THE BUG
# https://open.kattis.com/problems/exam

# Hint: You might have to 

def main():
    k = int(input())

    myAns = input()
    frAns = input()
    n = len(myAns)
    p = 0  # number of matching

    for i in range(n):
        if (myAns[i] == frAns[i]): p += 1
    
    print(min(k, p) + (n-k))

main()


'''
Input:
3
FTFFF
TFTTT

Output:
2


Input:
6
TTFTFFTFTF
TTTTFFTTTT

Output:
9


'''