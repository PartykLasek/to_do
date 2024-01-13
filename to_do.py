class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added.')

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" removed.')
        else:
            print(f'Task "{task}" not found.')

    def display_tasks(self):
        if not self.tasks:
            print('No tasks in the to-do list.')
        else:
            print('To-Do List:')
            for i, task in enumerate(self.tasks, start=1):
                print(f'{i}. {task}')


def main():
    todo_list = ToDoList()

    while True:
        print('\nOptions:')
        print('1. Add task')
        print('2. Remove task')
        print('3. Display tasks')
        print('4. Exit')

        choice = input('Enter your choice (1-4): ')

        if choice == '1':
            task = input('Enter the task: ')
            todo_list.add_task(task)
        elif choice == '2':
            task = input('Enter the task to remove: ')
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            print('Exiting the program. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 4.')


if __name__ == '__main__':
    main()
