n = [[1,2,3],[4,5,6,7,8,9]]
#function goes here
def myFun(args):
    new = []
    for i in range(len(args)):
        new = new + args[i]
    return new  
		
print myFun(n)
