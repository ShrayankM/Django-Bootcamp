#Varibles
a = 3
b = 3.4
str = "string varible"

#Special string format printing style
print(f"a = {a} and b = {b} are integer varibles and str = \"{str}\" is string" + "\n" + "on newLine")

#Slicing
mystr = "abcdefghijklmnopqrstuvwxyz"
print(mystr[2:6])                    #prints from index (2 to 5) cdef
print(mystr[:6])                     #prints from index (0 to 5) abcdef
print(mystr[6:])                     #prints from index (6 to end) ghijklmnopqrstuvwxyz
print(mystr[::2])                    #prints everything (0 to end) with space 1
print(mystr[::-1])                   #prints everything in reverse (can also specify start and end)
print(mystr[::-2])                   #prints everything in reverse with space 2

mystr = "Separated on the spaces"
str_arr = mystr.split(' ')
print(type(str_arr))

#Lists ( indexing and slicing of list is same as strings )
#Lists can be modified
emptyList = list()
myL = ['string', 23, True, 45.5, "stringTwo", [1, 2, 3, 4, 5]]
print(len(myL))
myL[-1] = ['newList', 2, 3, 4]                                 #modifies element of list
myL.append(44)                                                 #append any item to end of list
print(myL)
print(myL.pop(), myL)                                          #pop can take index of element to pop
print(myL.pop(2), myL)

LOne = [1, 2, 3, 4]
LTwo = [5, 6, 7]
LOne.extend(LTwo)                                              #merging two lists together
print(LOne)

myL = [34, 45, 12, 6, 7, 78]
myL.sort()
print(myL)

myL.reverse()
print(myL)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

fcol = [row[0] for row in matrix]
print(fcol)


#Dictionaries
emptyDict = dict()
my_dict = {'k1':'vOne', 'k2' : 'vTwo', 'k3' : 'vThree'}
print(my_dict['k3'])
my_dict['k4'] = 'vFour'
print(my_dict)

for (k, v) in my_dict:
    print(k + " " + v)

#Tuples, Sets
#Tuples are immutable
emptyTuples = tuple()
my_t = (1, 2, 3, 4, 5, 6)
print(type(my_t))
print(my_t)
print(my_t[0])

my_t = ('str', 45, 3,4, True, 'strTwo')
print(my_t)
# gives error my_t[0] = 100

#sets cannot be indexed
emptySets = set()
myS = {1, 2, 3, 4, 4, 4, 5, 5, 5}
print(myS)


#For Loops
print("FOR LOOPS")
for i in range(0, 10, 2):
    print(i)

n = [1, 2, 3, 4, 5]
n = [x * 2 for x in n]
print(n)

print("\nFunctions")
#Functions
def add(a = 5, b = 3):
    ''' adds 2 integers and returns them '''
    return a + b
print(add(5, 4))

#Lambda expressions
myL = list(range(0, 20))
def even_bool(n):
    return n%2 == 0

myF = (myL, lambda x: x%2 == 0)
print(list(myF))


myL = [1, 2, 3, 4]
myL.pop(0)
print(myL)
