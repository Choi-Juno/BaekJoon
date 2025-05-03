shortFormTranslate = {
    "CU": "see you",
    ":-)": "I’m happy",
    ":-(": "I’m unhappy",
    ";-)": "wink",
    ":-P": "stick out my tongue",
    "(~.~)": "sleepy",
    "TA": "totally awesome",
    "CCC": "Canadian Computing Competition",
    "CUZ": "because",
    "TY": "thank-you",
    "YW": "you’re welcome",
    "TTYL": "talk to you later",
}

while True:
    shortForm = input()

    if shortForm == "TTYL":
        print(shortFormTranslate[shortForm])
        break
    elif shortForm in shortFormTranslate.keys():
        print(shortFormTranslate[shortForm])
    else:
        print(shortForm)
