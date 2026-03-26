string = input()
words = [x for x in string.split(" ")]
while True:
    try:
        words.remove('')
    except ValueError:
        print(len(words))
        break