tasks = []

def task_menu():
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Tasks")
    print("4. Exit")
    
def remove_task():
        if len(tasks) == 0:
            print("NO TASK TO REMOVE")
        elif len(tasks) != 0:
            remove_index = int(input("Which task you want to remove : ")) - 1
            if 0 <= remove_index < len(tasks):
                removed = tasks.pop(remove_index)
                print(f"Your task {removed} is removed succesfully.")
            else:
                print("Invalid Input")
    

while True:
    try:
        task_menu()
        choice = int(input("Enter your choice (1 - 4) : "))
        
        if choice == 1:
            enter_task = input("Enter new Task : ")
            tasks.append(enter_task)
            print(f"Your task {enter_task} saved succesfully.")
            continue
        
        
        elif choice == 2:
            if len(tasks) == 0:
                print("No Task was added.")
            elif len(tasks) != 0:
                print(f"Your tasks are:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
            continue
        
        
        elif choice == 3:
            print(f"Your tasks are:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            remove_task()
            continue
        
            
        elif choice == 4:
            print("Thank you\n GOODBYE!")
        break
    
    
    except ValueError:
        print("Please enter a valid input (1 - 4)")    