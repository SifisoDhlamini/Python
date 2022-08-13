def main():
    sentence = input()
    print(convert(sentence))


def convert(sentence):
    return sentence.replace(':)', '🙂').replace(':(', '🙁')


main()