tasks = []

print("hello, welcome to task tracker, do u want to add/update/delete/see your tasks?")

while True:
    choice = input("add/update/delete/see or quit: ")

    if choice == "add":
        new_task = input("add a new task: ")
        tasks.append(new_task)
        print("task added.")

    elif choice == "see":
        number = 1
        for task in tasks:
            print(number, task)
            number = number + 1

    elif choice == "update":
        print(tasks)
        task_no = int(input("enter task.no of task that needs to be updated: "))
        updated_task = input("enter the new task: ")
        official_task_no = task_no - 1
        tasks.pop(official_task_no)
        tasks.append(updated_task)
        print(tasks)
    
    elif choice == "delete":
        if not tasks:
            print("no tasks saved.")
        else:
            delete_task = int(input("which task do u want to delete?: "))
            task_deleted = delete_task - 1
            tasks.pop(task_deleted)
            print(tasks)

    elif choice == "quit":
        break
        
    

        