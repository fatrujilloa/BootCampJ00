import  sys, string

def text_analyzer(*args):
    if len(args) == 0:
        T = input('What is the text to analyze?: ')
    elif len(args) > 1:
        print ("Too many arguments")
        return
    else:
        T = args[0]
    l, u, s, p = 0, 0, 0, 0
    for i in range(0, len(T)):
        if T[i] in string.ascii_lowercase:
            l = l + 1
        elif T[i] in string.ascii_uppercase:
            u = u + 1
        elif T[i] in string.whitespace:
            s = s + 1
        elif T[i] in string.punctuation:
            p = p + 1
    print ("The text contains", len(T), "characters:\n\n", "- ", u, "upper letters\n\n",
        "- ", l, "lower letters\n\n", "- ", p, "punctuation marks\n\n", "- ", s, "spaces")