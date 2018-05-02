b = open("bambi.txt", "r");
bambi = b.read();
b.close();
bambi = bambi.split();
for i in bambi:
    i = i.lower();
    
def freq(word):
    f = len(filter(lambda x: x if x == word else None, bambi));
    return f;

def gfreq(words):
    f = sum([freq(w) for w in words]);
    return f;

def mostfreq():
    f = reduce(lambda x, y : x if freq(x) > freq(y) else y, bambi);
    return f;

print freq("the");
print freq("a");
print gfreq(["the","a"])
print mostfreq();

