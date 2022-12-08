# Create a dictionary with the key as a vowel in the alphabet and the value as 0. Your dictionary should look like this {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}.

# Do this programmatically (using a dict comprehension or dict method) rather than hard coding the answer!

answer = {char:0 for char in 'aeiou'} # my solution

answer = dict.fromkeys("aeiou", 0) 