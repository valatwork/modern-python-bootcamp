import re
text = "Last night Mrs. Daisy and Mr. white murdered Ms. Chow"

pattern = re.compile(r'(Mr.|Mrs.|Ms.) ([a-z])[a-z]+', re.I)
result = pattern.sub("\g<1> \g<2>", text)
print(result)

'''
Define a function called censor  that accepts a single string. 
Rather than censoring any real profanity, we're going to censor any words that start with "frack".  
This includes "fracking", "fracker", "frack", etc.  Replace the entire word with the string "CENSORED".  
Your regex should be case insensitive. For example:

censor("Frack you")                #"CENSORED you"
censor("I hope you fracking die")  #"I hope you CENSORED die"
censor("you fracking Frack")       #"You CENSORED CENSORED"
'''

import re
 
def censor(input):
    pattern = re.compile(r'\bfrack\w*\b', re.IGNORECASE)
    return pattern.sub("CENSORED", input)
