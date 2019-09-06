#Converts grams into ounces or vice versa 
def convert_gram(gram):
    ounce = gram / 28.35
    print("Grams:", gram, "\n" + "Ounces:", ounce)

def convert_ounce(ounce):
    gram = ounce * 28.35
    print("Ounces:", ounce, "\n" + "Grams:", gram)

gramounce = input("Input g to convert from grams, o to convert from ounces. ").lower()
while True:
    if gramounce == "g" or gramounce == "o":
        break
    else:
        gramounce = input("input was not g or o.")

if gramounce == "g":
    while True:
        try:
            gram = int(input("Input number of grams: "))
            convert_gram(gram)
            break
        except ValueError:
            print("Not an int.")
        continue
elif gramounce == "o": 
    while True:
        try:
            ounce = int(input("Input number of ounces: "))
            convert_ounce(ounce)
            break
        except ValueError:
            print("Not an int.")
        continue
