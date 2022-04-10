# function to display 8 bit registers A, Q, M


def displayRegisters(a, q, m):
    print("["+"{0:^15}".format("A")+"]\t" + "["+"{0:^15}".format("Q")+"]\t"+"[" +
          "{0:^15}".format("M")+"]\t"+"\n"+"["+"|".join(a)+"]\t"+"["+"|".join(q)+"]\t"+"["+"|".join(m)+"]\t")

# function to left shift registers by 1 bit


def shiftLeft(reg):
    a = reg[1:]
    a.append("0")
    # print("aq"+str(reg)+"lsl"+str(a))
    return a

# function to calculate 2's complement


def complement(x):
    a = []
    invert = False
    for i in reversed(x):
        if(i == "0" and invert == False):
            a.append("0")
        elif(i == "1" and invert == False):
            invert = True
            a.append("1")
        elif(i == "1"):
            a.append("0")
        else:
            a.append("1")
    a.reverse()
    return a

# function to perform binary subtraction


def add(a, m):
    # add
    sum = ["0", "0", "0", "0", "0", "0", "0", "0"]
    carry = 0
    for i in range(7, -1, -1):
        if(a[i] == "0" and m[i] == "0" and carry == 0):
            sum[i] = "0"
            carry = 0
        elif(a[i] == "0" and m[i] == "0" and carry == 1):
            sum[i] = "1"
            carry = 0
        elif(a[i] == "0" and m[i] == "1" and carry == 0):
            sum[i] = "1"
            carry = 0
        elif(a[i] == "0" and m[i] == "1" and carry == 1):
            sum[i] = "0"
            carry = 1
        elif(a[i] == "1" and m[i] == "0" and carry == 0):
            sum[i] = "1"
            carry = 0
        elif(a[i] == "1" and m[i] == "0" and carry == 1):
            sum[i] = "0"
            carry = 1
        elif(a[i] == "1" and m[i] == "1" and carry == 0):
            sum[i] = "0"
            carry = 1
        elif(a[i] == "1" and m[i] == "1" and carry == 1):
            sum[i] = "1"
            carry = 1

    return sum


def getBin(value_str):
    parts = value_str.split('.')
    frac_part = 0.0
    int_part = int(parts[0])
    bin_int_part = []
    bin_frac_part = []
    # max number of bits in fractional part
    precision_controller = 100

    if (len(parts) == 2):
        frac_part = float('0.' + parts[1])
    else:
        bin_frac_part.append('0')

    if(int_part == 0):
        bin_int_part.append('0')

    # convert integer part to binary
    if(int_part != 0):
        while(int_part != 0):
            bin_int_part.append(str(int_part % 2))
            int_part = int(int_part / 2)
        bin_int_part.reverse()

    # convert fractional part to binary
    if(len(parts) == 2):
        while(precision_controller != 0 and frac_part != 0):
            bin_frac_part.append(str(int(frac_part*2)))
            if(frac_part*2 >= 1):
                frac_part = frac_part * 2 - 1
            else:
                frac_part = frac_part * 2
            precision_controller = precision_controller - 1
    return bin_int_part


def getDec(bin):
    dec = 0
    n = len(bin)
    for i in range(0, n):
        dec = dec + (2**i)*int((bin[n-i-1]))
    return dec


if __name__ == "__main__":
    sign = 0
    dividend = input("Enter Dividend: ")
    divisor = input("Enter Divisor: ")
    signDividend = 0
    signDivisor = 0
   # set sign bit
    if(dividend[0] == '-'):
        signDividend = 1
        dividend = dividend[1:]
    if(divisor[0] == '-'):
        signDivisor = 1
        divisor = divisor[1:]
    sign = (signDividend+signDivisor) % 2
    # find binary equivalents
    dividend = getBin(dividend)
    if(len(dividend) < 8):
        dividend.reverse()
        for i in range(0, 8-len(dividend)):
            dividend.append("0")
        dividend.reverse()
    divisor = getBin(divisor)
    if(len(divisor) < 8):
        divisor.reverse()
        for i in range(0, 8-len(divisor)):
            divisor.append("0")
        divisor.reverse()
    # initialise division registers
    a = ["0", "0", "0", "0", "0", "0", "0", "0"]
    m = divisor
    q = dividend
    displayRegisters(a, q, m)
    for i in range(8):
        aq = a+q
        temp = shiftLeft(aq)
        # print(temp)
        a = temp[:8]
        q = temp[8:]
        # print(a, q)
        a = add(a, (complement(m)))
        # check if a<0
        if(a[0] == "1"):
            # set q0 = 0 and a = a + m
            q[-1] = "0"
            a = add(a, m)
        else:
            # set q0 = 1
            q[-1] = "1"
        displayRegisters(a, q, m)
    if(sign == 1):
        print("-"+str(getDec(q))+"R-"+str(getDec(a)))
    else:
        print(str(getDec(q))+"R"+str(getDec(a)))
