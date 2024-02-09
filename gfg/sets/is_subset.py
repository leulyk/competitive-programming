# https://www.geeksforgeeks.org/problems/array-subset-of-another-array2317/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

def isSubset( a1, a2, n, m):
    num_frequency = {}
    
    for num in a1:
        if num_frequency.get(num):
            num_frequency[num] += 1
        else:
            num_frequency[num] = 1
            
    for num in a2:
        if not num_frequency.get(num) or num_frequency[num] == 0:
            return "No"
        else:
            num_frequency[num] -= 1
    
    return "Yes"

#{ 
 # Driver Code Starts
#Initial Template for Python 3
def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

