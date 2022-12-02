def separator(list):
    try:
        if len(list) == 1:
            print(list[0])
        else:
            for i in range(len(list) - 2):
                print(list[i], end=', ')
            print(list[-2] + ' and ' + list[-1])
    except IndexError:
        print("blablabla")


spam = ['apples', 'bananas', 'tofu', 'cats']
test = ['orange', 'chips', 'dog', 'house', 'auto', 'neige']
word = ['hello']
empty = ''

separator(spam)
separator(test)
separator(word)
separator(empty)