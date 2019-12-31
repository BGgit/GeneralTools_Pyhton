

# PYTHON CHEAT SHEET STARTED: 12/29/2019

#1.GENERATE FUNCTION TO SUM OVER A LIST OF LISTS. 
## 1.START

listsample = [[1,2,3,4,5],[1,2,5,4,6,7],[7,8,9,5,6]]

# METHOD 1 - NOT IN A FUNCTION
result = list(map(sum,listsample))
print(result)
# Desired_output= [15,25,35]


# METHOD 2
def sumr(ls):
    return [sum(subls) for subls in ls]
print("output", sumr(listsample))
# Desired_output= [15,25,35]
## 1.END 	