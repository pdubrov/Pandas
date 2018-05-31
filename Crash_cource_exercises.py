import string


def price_finder(input):
    trans_dict = str.maketrans(string.punctuation, " " * len(string.punctuation))
    return "price" in input.lower().translate(trans_dict).split(" ")


print(price_finder("What is the price?"))
