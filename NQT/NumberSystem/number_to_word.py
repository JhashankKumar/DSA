# 1234 -> one thousand two hundred thirty four

def number_to_words(n):
    if n == 0:
        return "zero"

    def one(num):
        switcher = {
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine"
        }
        return switcher.get(num)

    def two_less_20(num):
        switcher = {
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen"
        }
        return switcher.get(num)

    def ten(num):
        switcher = {
            2: "twenty",
            3: "thirty",
            4: "forty",
            5: "fifty",
            6: "sixty",
            7: "seventy",
            8: "eighty",
            9: "ninety"
        }
        return switcher.get(num)

    def two(num):
        if num == 0:
            return ""
        elif num < 10:
            return one(num)
        elif num < 20:
            return two_less_20(num)
        else:
            tenner = num // 10
            rest = num % 10
            return ten(tenner) + ("-" + one(rest) if rest != 0 else "")

    def three(num):
        hundred = num // 100
        rest = num % 100
        if hundred and rest:
            return one(hundred) + " hundred and " + two(rest)
        elif not hundred and rest:
            return two(rest)
        elif hundred and not rest:
            return one(hundred) + " hundred"

    billion = n // 1000000000
    million = (n - billion * 1000000000) // 1000000
    thousand = (n - billion * 1000000000 - million * 1000000) // 1000
    remainder = n % 1000