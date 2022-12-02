"""
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1



Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
 

Constraints:
1 <= numRows <= 30
"""



def generate(numRows):
    result = [[1]]
    
    if numRows == 1:
        return result
    
    for i in range(1, numRows):
        tmp_result = list()
        
        for a,b in zip((result[i-1]+[0]), ([0]+result[i-1])):
            tmp_result.append(a+b)
        
        result.append(tmp_result)
    
    return result



if __name__ == '__main__':
    for numRows in [5, 1, 3]:
        pt = generate(numRows)
        print(f'numRows={numRows}\tPT={pt}')
