def uncomment_xml(file, key_word):
    """This function will uncomment the code part in file that is with the given key_word"""

    f = open(file, "r+")

    new_text = ""
    while True:
        line = f.readline()
        if not line:
            break
        if line.count(key_word) > 0:
            print('%s found in the code, about to uncomment...' % key_word)
            new_text += line.replace("!-- ", "").replace("--", "")
        else:
            new_text += line
    f.close()
    f = open(file, "w+")
    f.write(new_text)
    print("Successfully uncommented!")
    f.close()


def edit_xml(file, key_word, phrase_to_replace):
    """This function will replace the code part in file by phrase_to_replace after searching by given key_word"""

    f = open(file, "r+")

    phrase = ""
    while True:
        line = f.readline()
        if not line:
            break
        if line.count(key_word) > 0:
            print('%s found in the code, about to change with given phrase...' % key_word)
            phrase += phrase_to_replace
        else:
            phrase += line
    f.close()
    f = open(file, "w+")
    f.write(phrase)
    print("Successfully replaced with given phrase!")
    f.close()
