def emoji_converter:
    words = message.split(' ')
    emoji = {":)": "🙂", "sad": "☹"}
    output = ""
    for word in words:
        output += emoji.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))