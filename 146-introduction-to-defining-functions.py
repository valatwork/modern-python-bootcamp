# OBJECTIVES
# Describe what a function is and how they are useful
# Explain exactly what the return keyword does and some of the side effects when using it
# Add parameters to functions to output different data
# Define and diagram how scope works in a function
# Add keyword arguments to functions


# What is a Function?

# A process for executing a task
# It can accept input and return an output
# Useful for executing similar procedures over and over

# Why Use Functions?

# Stay DRY - Don't Repeat Yourself! (WET - write everything twice)
# Clean up and prevent code duplication
# "Abstract away" code for other users
#    Imagine if you had to rewrite the "print()" function for every program you wrote

# functions are procedures for executing code. They accept inputs and return outputs when the return keyword is used
# To create inputs, we make parameters which can have default values, we call those default parameters
# variables defined inside of functions are scoped to that function - watch out for that!

# When invoking a function we can pass in keyword arguments in any order, we'll see this more later!

# Be careful to not return too early in your conditional logic and refactor when you can to remove unnecessary conditional logic. 
# Make sure you don't return in a loop too early as well!