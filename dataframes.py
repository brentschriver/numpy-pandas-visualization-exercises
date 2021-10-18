from pydataset import data

mpg = data('mpg')

import pandas as pd
import numpy as np

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

# Each column in a Pandas Dataframe is a Pandas Series. You must keep this in mind when working with the values within the Series.
# This line of code will print to the terminal the data type of the 'name' Series within the 'df' Dataframe.
print(type(df.name))

# 1. Copy the code from the lesson to create a dataframe full of student grades.
#   a. Create a column named 'passing_english' that indicates whether each student has a passing grade in English.
df['passing_english'] = df.english > 70
print(df)


#   b. Sort the english grades by the passing_english column. How are duplicates handled?
#print(df.sort_values('passing_english'))
# In the case of duplicates, it seems as if it'll sort by numerical values from left to right.


#   c. Sort the english grades first by passing_english and then by student name. All the students that are failing english should 
# be first, and within the students that are failing english they should be ordered alphabetically. The same should be true for the 
# students passing english. (Hint: you can pass a list to the .sort_values method)
sorted_by_passing_then_name = df.sort_values(['passing_english', 'name'])
print(sorted_by_passing_then_name)


#   d. Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.
sorted_by_passing_then_grade = df.sort_values(['passing_english', 'english'])
print(sorted_by_passing_then_grade)

