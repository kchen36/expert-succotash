bambi = open("bambi.txt", "r");
bambi = bambi.read();
bambi = bambi.split();
print bambi;

len(filter(lambda x : x if x = "the", bambi))

