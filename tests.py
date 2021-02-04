# Jhonatan Becerra
# Random Testing

import random

# holds the different card brands
brandName = ["VISA", "MASTERCARD", "AMEX", "RANDOM"]

# holds the length of the number for a brand
brandLen = [16, 16, 15]

# createCreditNumber generates and returns a credit card number based
# on two parameters. brandIndex, and valid
# brandIndex is an int representing the desired brand in the brand array
# valid is an integer, representing true and false ie. 1=true 0=false


def createCreditNumber(brandindex, validlen, validchk):
    # get a prefix number for the brand
    ccnum = getprefix(brandName[brandindex])

    # generate the credit card number
    # based on the prefix
    for i in range(len(ccnum), brandLen[brandindex]):
        ccnum += str(random.randint(0, 9))

    # if a number without a valid length is desired
    if validlen == 0:
        # generate a random number (100 values) to
        # determine if we want the number to be
        # longer or shorter than the standard
        rl = random.randint(1, 100)

        if rl % 2 == 0:
            # remove last number
            ccnum = ccnum[:-1]
        else:
            # add a random number
            ccnum += str(random.randint(0,9))

    # regardless of whether or not we want a valid credit card
    # number, we must check if the number is valid
    valid = checkvalidity(ccnum)

    # if we want a number with a valid checksum
    if validchk == 1:
        # the number is already valid
        if valid == 1:
            return ccnum
        else:
            # if the checksum isn't valid
            return makevalidchk(ccnum)
    else:
        # we don't want a number with a valid checksum
        # but the checksum is valid, so make it invalid
        if valid == 1:
            return makeinvalidchk(ccnum)
        else:
            # number is already not valid
            return ccnum

def makeinvalidchk(ccnum):
    # get the checksum digit
    lastInt = int(ccnum[len(ccnum)-1])

    randNum = lastInt

    # generate a random number other than the current checksum digit
    while randNum == lastInt:
        randNum = random.randint(0,9)

    # replace the checksum digit
    ccnum = ccnum[:-1]
    ccnum += str(randNum)

    return ccnum

# makevalidchk creates a valid checksum digit
# it takes a single parameter, ccnum, which is a
# string representing a credit card number
def makevalidchk(ccnum):
    # get the sum of even digits
    evenSum = getevensum(ccnum)

    # get the sum of odd digits
    oddSum = getoddsum(ccnum)

    # while the sum of even and odd digits isn't divisible by 10
    while (evenSum + oddSum) % 10 != 0:
        # remove the checksum digit
        ccnum = ccnum[:-1]

        # create a new checksum digit
        ccnum = ccnum + str(random.randint(0, 9))

        # calculate the even sum with the new checksum digit
        evenSum = getevensum(ccnum)
    return ccnum

# getPrefix returns a prefix for a given brand
# the single parameter, manuf, is the brand name
def getprefix(manuf):
    if manuf == "VISA":
        return "4"
    elif manuf == "MASTERCARD":
        # randomly select among the two prefix ranges
        sp = random.randint(1, 100)

        # first set (prefix 51 -55)
        if sp % 2 == 0:
            return str(random.randint(51, 55))
        # second set (prefix 2221 - 2720)
        else:
            return str(random.randint(2221, 2720))
    else:
        # AMEX
        # select among the two prefixes
        sp = random.randint(1, 100)
        if sp % 2 == 0:
            return "34"
        else:
            return "37"

# getevensum returns the sum of the even digits in a string
# ccnum is a string representing a credit card number
def getevensum(ccnum):
    evenSum = 0

    # add every even digit
    for j in range(len(ccnum) - 1, 0, -2):
        evenSum = evenSum + int(ccnum[j])
    return evenSum

# get oddsum returns the sum of all odd digit number
# ccnum is a string representing a credit card number
def getoddsum(ccnum):
    oddSum = 0

    # add every odd digit
    for i in range(len(ccnum) - 2, -1, -2):
        # multiply every digit by 2
        num = 2 * int(ccnum[i])

        # if the number is greater than 9, add all digits
        if num > 9:
            num = 1 + (num - 1) % 9
        oddSum = oddSum + num
    return oddSum

# checkvalidity check if a credit card has a valid checksum
# ccnum is a string representing a credit card number
# 1 is returned if the string is valid, 0 otherwise
def checkvalidity(ccnum):
    # get even sum
    evenSum = getevensum(ccnum)

    # get odd sum
    oddSum = getoddsum(ccnum)

    # if sum is divisible by 10
    if (oddSum + evenSum) % 10 == 0:
        # valid
        return 1
    else:
        # invalid
        return 0


if __name__ == '__main__':
    nfb = random.randint(0,2)
    nfl = random.randint(0,1)
    nfc = random.randint(0,1)

    num = createCreditNumber(nfb, nfl, nfc)
    print("number = {} length = {}".format(num, len(num)))
    # print(makevalidchk("2720993047019419"))