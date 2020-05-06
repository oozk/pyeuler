#!/usr/bin/env python3

###
# Problem 17
# https://projecteuler.net/problem=17
# ###
# Solution: O(n) time | O(n) space
###

def problem_17(n):
    return sum(len(num2words(x).replace(' ', '')) for x in range(1, n +1))

def num2words(n):
    e3, e2, e1, e0 = '', '', '', ''
    numbers = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
                 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
                11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
                15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
                19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
                50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
                90: 'Ninety', 100: 'Hundred', 1000: 'Thousand', 0: 'Zero'}

    if 10000 > n >= 1000:
        e3 = numbers[int(str(n)[:1])] + ' ' + numbers[1000]


    if 1000 > n >= 100:
        e2 = numbers[int(str(n)[:1])] + ' ' + numbers[100]

    if 1000 > n:
        if 10 <= n % 100 <= 19:
            e1 = numbers[int(str(n)[-2:])]
        if 100 > n % 100 > 19:
            e1 = numbers[n % 100 - n % 100 %10]
            if n%10 > 0:
                e1 += numbers[n%10].lower()
        if 1 <= n % 100 <= 9:
            if n%10 > 0:
                e1 = numbers[n%10].lower()

    if e1 != '' and e2 != '':
        e0 = e2 + ' and ' + e1
    elif e1 != '' and e2 == '':
        e0 = e1
    else:
        e0 = e2
    return e3 + ' ' + e0

print(problem_17(1000))
