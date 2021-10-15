import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from function_exercises import string_cheese_to_processed_cheese 

print(string_cheese_to_processed_cheese('$12,423,234.83'))

def count_vowels(string):
    vowel_count = 0
    for letter in string:
        if "a" in letter or "e" in letter or "i" in letter or "o" in letter or "u" in letter:
            vowel_count += 1
    return vowel_count


fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

#print(fruits.size)
#print(fruits.index)
#print(fruits.values)
#print(fruits.dtype)
#print(fruits.head())
#print(fruits.tail(2))
#print(fruits.sample(2))
#print(fruits.describe())
#print(fruits.unique())
#print(fruits.value_counts())
#print(fruits.value_counts().head(1))
#print(fruits.value_counts().nsmallest(n = 1, keep = 'all'))

# Exercises Part II
# 1. Capitalize all the string values in fruits.
#print(fruits.str.capitalize())


# 2. Count the letter "a" in all the string values.
#print(fruits.str.count('a'))


# 3. Output the number of vowels in each and every string value.
#print(fruits.apply(count_vowels))


# 4. Write the code to get the longest string value from fruits.
#print(max(fruits.str.len()))


# 5. Write the code to get the string values with 5 or more letters in the name.
#print(fruits[fruits.str.len() > 5])


# 6. Use the .apply method with a lambda function to find the fruit(s) containing the letter "o" two or more times.
#print(fruits[fruits.apply(lambda fruit: fruit.count('o') >= 2)])


# 7. Write the code to get only the string values containing the substring "berry".
#print(fruits[fruits.str.contains('berry')])


# 8. Write the code to get only the string values containing the substring "apple".
#rint(fruits[fruits.apply(lambda fruit: 'apple' in fruit)])


# 9. Which string value contains the most vowels?
#print(fruits[fruits.apply(count_vowels).idxmax()])


letters = list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy')
series_version_of_letters = pd.Series(letters)

# 1. Which letter occurs the most frequently in the letters series?
#print(series_version_of_letters.value_counts().head(1))


# 2. Which letter occurs the least frequently?
#print(series_version_of_letters.value_counts().tail(1))


# 3. How many vowels are in the series?
vowels = list('aeiou')
boolean_series = series_version_of_letters.isin(vowels)
series_of_vowels = series_version_of_letters[boolean_series]
print(series_of_vowels.sum())


# 4. How many consonants are in the series?
boolean_series = series_version_of_letters.isin(vowels)
series_of_consonants = series_version_of_letters[~boolean_series]
print(series_of_consonants.value_counts())

# 5. Create a series that has all of the same letters but uppercase.
#print(series_version_of_letters.str.upper())

# 6. Create a bar plot of the frequencies of the 6 most commonly occuring letters.
series_version_of_letters.value_counts().head(5).plot.bar()
#plt.show()

list_of_numbers = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
series_version_of_list_of_numbers = pd.Series(list_of_numbers)


# 1. What is the data type of the number Series?
#print(type(series_version_of_list_of_numbers))

# 2. How many elements are in the number Series?
# 200

# 3. Perform the necessary manipulations by accessing Series attributes and methods to convert the number Seies to a numeric data type.
convert_to_numeric_type = series_version_of_list_of_numbers.apply(string_cheese_to_processed_cheese)
#print(convert_to_numeric_type.dtype)

# 4. Run the code to discover the maximum value from the Series.
#print(convert_to_numeric_type.nlargest(n=1))

# 5. Run the code to discover the minimum value from the Series.
#print(convert_to_numeric_type.nsmallest(n=1))

# 6. What is the range of the values in the Series?
# The range is from 278.60 to 4789988.17

# 7. Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.
bins_for_numeric_values = pd.cut(convert_to_numeric_type, 4).value_counts()
#print(bins_for_numeric_values)

# 8. Plot the binned data in a meaningful way. Be sure to include a title and axis labels.
bins_for_numeric_values.plot.bar()
#plt.title('Frequency of Income')
#plt.show()


list_of_exam_scores = [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]
series_version_of_list_of_exam_scores = pd.Series(list_of_exam_scores).sort_values()
print(series_version_of_list_of_exam_scores)
# 1. How many elements are in the exam_scores Series?
# There are 20 elements in the exam_scores Series.

# 2. Run the code to discover the minimum, the maximum, the mean, and the median scores for the exam_scores Series.
print(series_version_of_list_of_exam_scores.mean())
print(series_version_of_list_of_exam_scores.min())
print(series_version_of_list_of_exam_scores.max())
print(series_version_of_list_of_exam_scores.median())

# 3. Plot the Series in a meaningful way and make sure your chart has a title and axis lables.
#pd.cut(series_version_of_list_of_exam_scores, 4).value_counts(sort = False).plot.bar()
#plt.show()

pd.cut(series_version_of_list_of_exam_scores, 4).value_counts(sort = False).plot.bar()
#plt.show()

# 4. Write the code necessary to implement a curve for your exam_grades Series and save this as curved_grades. 
# Add the necessary points to the highest grade to make it 100, and add the same number of points to every other 
# score in the Series as well.
curved_grades = series_version_of_list_of_exam_scores + 4
print(curved_grades.value_counts())

# 5. Use a method to convert each of the numeric values in the curved_grades Series into a categorical value of 
# letter grades. For example, 86 should be a 'B' and 95 should be an 'A'. Save this as a Series named letter_grades.

#numbers_series.apply(lambda n: 'even' if n % 2 == 0 else 'odd')

curved_grades.apply(lambda n: 'A' if n >= 95 else ('B' if n >= 85 else ('C' if n >= 75 else ('D' if n >= 65 else 'F')))).value_counts().sort_index().plot.bar()
#plt.show()




