# Write a function called combine_words  which accepts a single string called word and any number of additional key word arguments.  
# If a prefix is provided, return the prefix followed by the word.  If a suffix is provided, return the word followed by the suffix.  
# If neither is provided, just return the word.  It might sound confusing, but the examples should make this a lot clearer!

# combine_words("child")  #'child'

# combine_words("child", prefix="man")  #'manchild'

# combine_words("child", suffix="ish")  #'childish'

# combine_words("work", suffix="er")  #'worker'

# combine_words("work", prefix="home")  #'homework'

def combine_words(**kwargs):
      if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word