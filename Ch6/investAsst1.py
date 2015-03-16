# Investment + Interest Script - Functions
def invest(amount, rate, time):
    investVal = amount
    for n in range(1,time+1):
        investVal = investVal + (investVal * rate)
        print("year {0}: ${1}".format(n, investVal))
    return 

def main():
    uinputAmount = input("enter principal amount:")
    uinputRate = input("enter annual rate of return:")
    uinputTime = input("enter time to maturation:")
    print("principal amount:", uinputAmount)
    print("annual rate of return:", uinputRate)
    invest(float(uinputAmount),float(uinputRate),int(uinputTime))
    
main()
