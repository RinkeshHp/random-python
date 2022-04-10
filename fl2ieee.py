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
    return "".join(bin_int_part)+"."+"".join(bin_frac_part)


if __name__ == "__main__":
    sign = '0'
    value_str = input("Enter Decimal Number: ")
   # set sign bit
    if(value_str[0] == '-'):
        sign = '1'
        value_str = value_str[1:]
    # find binary equivalent
    bin_str = getBin(value_str)
    # find appropriate bias (shifts)
    shifts = 0
    radix_pt_pos, first_1_pos = bin_str.find('.'), bin_str.find('1')
    if(radix_pt_pos > first_1_pos):
        shifts = radix_pt_pos - first_1_pos - 1
    else:
        shifts = radix_pt_pos - first_1_pos
    if(first_1_pos == -1):
        exponent = "00000000"
    else:
        exponent = getBin(str(shifts + 127))[:-2]
    if(len(exponent) < 8):
        exponent = "0"*(8-len(exponent)) + exponent
    mantissa = ((bin_str[:radix_pt_pos] +
                bin_str[radix_pt_pos+1:])[radix_pt_pos-shifts:])[:22]
    if(len(mantissa) < 23):
        mantissa = mantissa + "0"*(23-len(mantissa))
    ieee_32 = sign + '|' + exponent+'|' + mantissa
    print("32-bit IEEE 754: " + ieee_32)
