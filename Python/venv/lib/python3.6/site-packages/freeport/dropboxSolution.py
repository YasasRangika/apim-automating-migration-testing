def  wordpattern( pattern,  input):

    rwords = []
    iptopattern = input[:]
    uniqueWords = list(set(pattern))
    loopNumber = 0

    while(input):
        loopNumber += 1
        if loopNumber > len(uniqueWords):
            return 0

        sample = input[:]

        wordList = []
        for i in range(len(sample)/2):
            word = sample[:i+1]
            if word in sample[i+1:]:

                wordList.append(word)
        bword = wordList[-1]
        rwords.append(bword)
        if len(rwords) > len(uniqueWords):
            return 0


        input = input.replace(bword, '')
        iptopattern = iptopattern.replace(bword, uniqueWords[len(rwords)-1])


    if iptopattern == pattern:
        return 1
    else:
        return 0


ip = "reddedlyred"
pattern = 'aba'
result = wordpattern(pattern, ip)
print(result)