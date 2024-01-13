A basic To-Do list application in Python.

## Overview

This project is a simple command-line application for managing a to-do list. It allows users to add tasks, remove tasks, and display the current list of tasks.

## Features

- Add tasks to the to-do list.
- Remove tasks from the to-do list.
- Display the current tasks in the to-do list.

## Getting Started

1. Make sure you have Python installed on your system.
2. Clone the repository:

    ```bash
    git clone https://github.com/your-username/todo-app.git
    cd todo-app
    ```

3. Run the application:

    ```bash
    python todo_app.py
    ```

4. Follow the on-screen instructions to interact with the To-Do app.

## Usage

1. Choose an option by entering the corresponding number.
2. For adding tasks, enter the task description.
3. For removing tasks, enter the task description to remove.
4. To display the current tasks, choose the display option.

## Example

```plaintext
Options:
1. Add task
2. Remove task
3. Display tasks
4. Exit

Enter your choice (1-4): 1
Enter the task: Buy groceries
Task "Buy groceries" added.

Options:
1. Add task
2. Remove task
3. Display tasks
4. Exit

Enter your choice (1-4): 3
To-Do List:
1. Buy groceries

Options:
1. Add task
2. Remove task
3. Display tasks
4. Exit

Enter your choice (1-4): 2
Enter the task to remove: Buy groceries
Task "Buy groceries" removed.

Options:
1. Add task
2. Remove task
3. Display tasks
4. Exit

Enter your choice (1-4): 4
Exiting the program. Goodbye!
