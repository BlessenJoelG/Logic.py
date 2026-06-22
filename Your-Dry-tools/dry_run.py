text =  "nlaebolko"
freq,c = {},0
if (text.count("b")>=1 and text.count("a")>=1 and text.count("l")>=2 and text.count("o")>=2 and text.count("n")>=1):
    for x in text:
        if x not in freq:
            freq[x] = 1
        else:
            freq[x] += 1
    while(freq["b"]>=1 and freq["a"]>=1 and freq["l"]>=2 and freq["o"]>=2 and freq["n"]>=1):
        freq["b"]-=1
        freq["a"]-=1
        freq["l"]-=2
        freq["o"]-=2
        freq["n"]-=1
        c += 1
print(freq,c)