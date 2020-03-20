num = int(input('enter number here: '))
def dectobin(num):
    if num  >= 1:
        return(bin(num)[2:])
    else:
        return('Number must be greater or equal to 1')

print(dectobin(num))
