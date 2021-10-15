# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# Our is_two defines a single parameter, x that is an integer, and will return Boolean value
def is_two(x):
    # Check to see if passed argument is equal to the integer 2. If so the function will return True.
    if x == 2:
        return True
    # Otherwise the function will return False.
    else:
        return False
'''
Walkthrough 
1. When we pass the integer '2' into the function is_two, the IF condition will evaluate to 'True' and the function will RETURN the Boolean 'True', then terminate.

    --> print(is_two(2))

2. When we pass the integer '3' into the 'is_two' function, the IF condition is not met. The code within the IF conditional is skipped and the code in the 
ELSE conditional runs. The only thing to run is the RETURN statement. Which, in this case, the function will RETURN the Boolean FALSE.

    --> print(is_two(3))
'''



# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# The 'is_vowel' function is created and it is set to receive one string arguement. 
def is_vowel(vowel):
    # The IF condition is set to check if the 'vowel' argument is equal to a lower case or upper case vowel. If it is a vowel(upper or lower) the function will return the Boolean TRUE and terminate.
    if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u' or vowel == 'A' or vowel == 'E' or vowel == 'I' or vowel == 'O' or vowel == 'U':
        return True
    # This ELSE condition runs if the IF condition is not met and the function will return a Boolean FALSE and terminate.
    else:
        return False
'''
Walkthrough
1. When we pass the string argument, 'E', into the 'is_vowel' function the IF condition is met and the function will RETURN the Boolean TRUE and the function will
terminate.

    --> print(is_vowel('E'))

2. When we pass the string argument, 'b', into the 'is_vowel' function the IF condition is not met, the code within the IF conditional is skipped, and the ELSE 
condition evaluates and the function RETURNS the Boolean False

    --> print(is_vowel('b'))

3. This function RETURNS the Boolean False for anything that is not an uppercase or lowercase vowel.

    --> print(is_vowel(3))
    --> print(is_vowel('bReNT'))
'''

# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# The 'is_consonant' function is created and has one parameter called 'letter' which will take in a string argument.
def is_consonant(letter):
    # The IF condition is set to check if the 'letter' argument is equal to a lower case or upper case vowel. If it is a vowel(upper or lower) the function will 
    # return the Boolean FALSE and terminate.
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U' or len(letter) > 1:
        return False
    # The ELSE condition runs if the argument passed to the function is not a vowel.
    else:
        return True
'''
Walkthrough
1. When 'c' is passed into the function the function RETURNS the Boolean True and then terminates.

    --> print(is_consonant('c'))

2. When 'a' is passed into the function the function RETURNS the Boolean True and then terminates.

    --> print(is_consonant('i'))

3. If any multi-lettered string is passed into the function the function will RETURN the Boolean True which can cause confusion 
since the function's name is 'is_consonant'. In order to fix this I could add an 'OR len(letter) > 1' to the IF conditional.

    --> print(is_consonant('La Panederia'))
    --> print(is_consonant('even this?'))
'''
    


# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# The 'capitalize_word' function is created and the 'word' paramater will receive a string argument.
def capitalize_word(word):
    # The 'splitstring' variable is created and the string method 'split()' converts 'word' into a list and stores that list into the 'splitstring' variable.
    splitstring = word.split()
    # The IF condition checks if the first letter in 'word' is an upper case or lower case vowel. If it is a vowel, the function will RETURN the 'word' and 
    # terminate.
    if word[0] in ['a','e','i','o','u','A','E','I','O','U']:
        return word
    # If the first letter is a consonant, the function will RETURN the 'word' with the first letter capitalized, using the .capitalize() string method.
    else:
        return word.capitalize()
'''
Walkthrough
1. When the string 'meliodas' is passed into the function, the function will RETURN the 'Meliodas'. If you use the print() function 'Meliodas' will be
printed to the scree.

    --> print(capitalize_word('meliodas'))

2. When the string 'asparagus' is passed into the function, the function will RETURN 'asparagus' just as it was entered. When the string '1234' is passed
into the function the function will RETURN '1234' since '1' is the capitalized form of '1' (If that can make any sense. This statement can make sense to
people with a pretty cool imagination.)

    --> print(capitalize_word('asparagus'))
    --> print(capitalizze_word('1234'))

3. When the integer 1234 is passed into the function, the function will return an error message because the string method .split() can only work on strings
and not integers. 

    --> print(capitalize_word(1234))
'''


# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# Create a function called 'calculate_tip() which takes in the parameters 'tip' and 'bill_total'.
def calculate_tip(tip, bill_total):
    # Create the variable 'amount_to_tip' and set it equal to the argument passed into 'tip' multiplied by the argument passed into 'bill_total', then return the variable 'amount_to_tip'.
    amount_to_tip = tip * bill_total
    return amount_to_tip
'''
Walkthrough
1. When the arguments '.20' and '8' are passed into the 'calculate_tip' function, the function will multiply the two numbers together and RETURN the result:

    --> print(calculate_tip(.20, 8))

2. This function will also receive two integers and return the two numbers multiplied together:

    --> print(calculate_tip(3,20))
    --> print(calculate_tip(20,3))

3. If you pass in an integer and a string, the function will return the string the integer amount of times:

    --> print(calculate_tip('How much to tip?', 8))

4. And if you pass two strings into the function, it should return an error because the multiplication operation cannot be used with two strings:

    --> print(calculate_tip('brent', 'schriver'))
'''


# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# Create a function called 'apply_discount' that takes two parameters 'original_price' and 'discount_percentage'.
def apply_discount(original_price, discount_percentage):
    # Create a variable called 'new_price' and have it store the result of the mathematical operation of taking the argument passed into 'original_price' and 
    # multiplying it by the value of 1 minus the argument passed into discount_percentage and returns that value.
    new_price = original_price * (1 - discount_percentage)
    return new_price
'''
Walkthrough
1. When the arguments '100' and '80' are passed into 'original_price' and 'discount_percentage', respectively, the function will return

    --> print(apply_discount(100, 80))
'''



# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
def handle_commas(string_with_commas):
    no_commas = int(string_with_commas.replace(',',''))
  
    return no_commas



# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(number_grade):
    while True:
        grade = input('Please input the student\'s grade: ')
        if int(grade) <= 59:
            print('Student grade: F')
        elif int(grade) <= 66:
            print('Student grade: D')
        elif int(grade) <= 79:
            print('Student grade: C')
        elif int(grade) <= 87:
            print('Student grade: B')
        else:
            print('Student grade: A')
        more = input('Would you like to input another grade? (Y/N)')
        if more.lower() == 'n':
            break

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
def remove_vowels(anyword): 
    new_word = ''
    for letter in anyword:   
        if is_vowel(letter) == True:
            new_word = new_word.replace(letter, '')
        elif is_vowel(letter) == False:
            new_word = new_word + letter
    return new_word

vowel = ['a','e','i','o','u','A','E','I','O','U']

'''10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
anything that is not a valid python identifier should be removed
leading and trailing whitespace should be removed
everything should be lowercase
spaces should be replaced with underscores
for example:
Name will become name
First Name will become first_name
% Completed will become completed '''

def normalize_name(string):
    for char in string:
        if (char.isalnum() == False
            and char != ' '):
            string = string.replace(char,'')
    string = string.lower().strip()
    string = string.replace(' ', '_')
    return string


# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.

def cumulative_sum(array):
    curr_position_in_array = 0
    cumulative_sum = 0
    length_of_array = len(array)
    cumulative_sum_list = []
    while curr_position_in_array < length_of_array:
        for n in array:
            cumulative_sum_list.append(cumulative_sum + n)
            cumulative_sum += n
            curr_position_in_array += 1
    return cumulative_sum_list
    

def string_cheese_to_processed_cheese(money_string):
    string_cheese = money_string.strip('$').replace(',','')
    processed_cheese = float(string_cheese)
    return processed_cheese




