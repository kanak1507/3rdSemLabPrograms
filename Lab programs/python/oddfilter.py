number = [1,2,3,4,5,6,7,8,9,10,15,178,43,55,90]
def odd(num):
    return num%2 != 0
odd_num = list(filter(odd,number))
print("ORIGINAL LIST:", number)
print("ODD NUMBERS: ", odd_num)