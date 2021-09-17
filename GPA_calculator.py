#!/usr/bin/env python
# coding: utf-8

# # Python GPA Calculator

# In[2]:


class GpaCalculator():
    '''Declare the variables'''
    count = 0
    '''use for to loop '''
    hrs   = 0
    numberofsubject =0
    totalhours = 0
    totalPoints = 0.0
    gpa = 0.0
    '''Prompt the user for the number of subject taking'''
    numberofsubject = int(input("Enter number of  subject "))

    for count in range(count, numberofsubject):
        '''This is to keep track of the number of classes (Optional)'''
        print("For Subjact # ", count+1)

        '''Prompt user for number of number of credit hours per class'''
        hrs = int(input("Enter the credit hrs "))

        '''Prompt user to enter the letter grade'''
        grade = input("Enter the letter grade ")

        '''Use if statement to check the grade and increment points and total hours'''

        if grade == 'A' or grade == 'a':
            totalPoints = totalPoints + (hrs * 4)
            totalhours = totalhours + hrs
        elif grade == 'B' or grade == 'b':
            totalPoints += (hrs * 3.0)
            totalhours += hrs
        elif grade == 'C' or grade == 'c':
            totalPoints += (hrs * 2.0)
            totalhours += hrs
        elif grade == 'D' or grade == 'd':
            totalPoints += (hrs * 1.0)
            totalhours += hrs
            '''If not A,B, C, D then it must be F. You can write validation to check in other lettes'''
        else:
            totalPoints += (hrs * 0.0)
            totalhours += hrs
    '''Calculate GPA based on the total points and total hours'''
    gpa = totalPoints / totalhours
    print("Your GPA is :", gpa)

def main():
    gpa = GpaCalculator()

if __name__ == '__main__':main()


# 
