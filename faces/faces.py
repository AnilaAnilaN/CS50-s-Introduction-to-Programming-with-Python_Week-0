def covert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text


def main():
    userInput = input("Please enter some text including emoticons :) and :( to see the magic  happen: ")
    print(covert(userInput))


main()

