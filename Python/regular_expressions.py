import re

patterns = ['term1', 'term2']
phrase = "This the string in which to check patterns term1, Lets match and see!!!"

match = re.search(patterns[0], phrase)
print(match.start(), match.end())

str = "This_will_be_separated by_only underscores"
str_list = re.split('_', str)
print(str_list)

under = re.findall('_', str)
print(under)

def multi_re_find(patterns, phrase):
    for p in patterns:
        print(f"Searching for pattern:{p}")
        print(re.findall(p, phrase), "\n")

test_phrase = 'sdsd..sssddd..sdddsddd...dsdds...dssssss...sddddd'
# (sd*) s followed by zero or more d's
# (sd+) s followed by 1 or more d's
# (sd?) s followed by 0 or 1 time
# (sd{3}) s followed by 3 d's
# (sd{2,3}) s followed by 2 or 3 d's
# (s[sd]+) s followed by (1 or more s's) or (1 or more d's)
test_patterns = ['s[sd]+']
multi_re_find(test_patterns, test_phrase)

test_phrase = 'This is a string! But it has 55 pun 67 ctuation. 12 34 How can we remove it?'
# [^!.?]+ remove 1 or more instance of all special symbols
# [a-z,A-Z]+ includes all uppercase and lowercase letters
# [0-9] includes for numbers
# [\s] for whitespaces
test_patterns = ['[\s]']
multi_re_find(test_patterns, test_phrase)
