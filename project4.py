'''
Purpose: This program creates a plot from three text files:
income, expenses, and savings goals, and also calculates if a 
specified savings goal was met or not. 
Authors: Sofia and Genevieve
Date: Dec 12th 2023
CS112
'''

import matplotlib.pyplot as plt

def text_to_list(inputlist): 
    '''
    This function takes a text file with a row of data and converts it to a list
    Input: text file
    Output: list
    '''
    list_from_text = []
    for line in inputlist:
        line = float(line)
        list_from_text.append(line)
    return list_from_text

def create_plot(income,expenses,savings_goals):
    '''
    This function opens three text files (income, costs, and savings goals)
    and plots them together on a graph.
    Inputs: income, expenses, and savings goal as a text file
    Output: graph plotting the data from all three files
    '''
    months = 12 # Hardcoding 12 months for one year
    
    # Plotting
    fig, ax1 = plt.subplots()

    # Plotting income and expenses on the first y-axis
    ax1.plot(range(1, months + 1), text_to_list(income), label='Income', color='b')
    ax1.plot(range(1, months + 1), text_to_list(expenses), label='Expenses', color='r')
    ax1.plot(range(1, months + 1), text_to_list(savings_goals), label='Savings Goals', color = 'g')
    ax1.set_xlabel('Months')
    ax1.set_ylabel('Amount ($)', color='b')

    # Adding labels and title
    plt.title('Income, Expenses, and Savings Goals Over 12 Months')
    
    # Display the plot
    plt.show()
    
    return

def goal_met(income,expenses,savings_goals):
    '''
    This function determines whether or not a savings goal is met 
    by calculating if the amount saved is greater than the set savings goal.
    Input: text file of income and savings goals
    Output: A message stating if a savings goal was met or not
    '''
    # open income text file
    income = text_to_list(income)
    # open savings text file
    savings_goals = (text_to_list(savings_goals))

    # Check if savings goals are met each month
    for month in range(1, len(income) + 1):
        saved = income[month - 1] - expenses[month - 1]
        goal = savings_goals[month - 1]
        if saved >= goal:
            result = "Congrats!! You achieved your savings goal!"
        else:
            result = "You're getting there! Don't spend too much!"
        print(f"For Month {month}: {result}!")
    return

def main():
    income = open('income.txt','r')
    expenses = open('expenses.txt','r')
    savings_goals = open('savings.txt','r')
    income = text_to_list(income)
    expenses = text_to_list(expenses)
    savings_goals = text_to_list(savings_goals)
    create_plot(income, expenses, savings_goals)
    goal_met(income, expenses, savings_goals)
    
main()