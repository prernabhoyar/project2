def task():
    tasks = []#empty list
    print("---WELCOME TO THE TASK MANAGEMENT SYSTEM---")
    
    total_task= int(input("Total number of tasks you want to add="))
    for i in range(1,total_task+1):
        task_name= input(f"Enter task {i} = ")
        tasks.append(task_name)
    print(f"Total tasks are: {tasks}")
        
    while True:
        choice=int(input("Enter\n1.ADD\n2.UPDATE\n3.DELETE\n4.VIEW\n5.EXIT"))
        if choice==1:
            add=input("Enter the task you want to add")
            tasks.append(add)
            print(f"task{add} added successfully....")
        elif choice==2:
            updated_val=input("Enter the name of task you want to update: ")
            if updated_val in tasks:
                up=input("Enter the new task: ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"The updated task is {up}")        
        elif choice==3:
            del_val=input("Enter the value you want to delete")
            if del_val in tasks:
                ind= tasks.index(del_val)
                del tasks[ind]
                print(f"The task{ind} is deleted.....")
        elif choice==4:
            print(f"The tasks are: {tasks}")
        elif choice==5:
            print("Closing the program.....")
            break      
        else:
            print("Invalid input")
task()