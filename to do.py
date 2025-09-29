l=[]
def todolist():
    user =int(input('Select you option\n1. add\n2. remove\n3. Show\n4. quit \nEnter here : '))
    while True:
        if user == 1:
            ask= input("Enter the task : ")
            l.append(ask)
            print('task added succesfully')
            again1=input('If you want to do more operation type "yes" if you want to exit than type "no" \n Enter here : ').lower()
            if again1 == 'yes':
                todolist()
            else:
               print('Thank for using to-do list')
        elif user == 2:
            remove=input('Enter the task to be remove : ')
            if remove.isalpha():
                l.remove(remove)
            else:
                print('Task not found in list')
            print('task removed succesfully')
            again2=input('If you want to do more operation type "yes" if you want to exit than type "no" \n Enter here : ').lower()
            if again2 == 'yes':
                todolist()
            else:
               print('Thank for using to-do list') 
        elif user == 3:
            for i,j in enumerate(l):
                print(i,j)
            
            again3=input('If you want to do more operation type "yes" if you want to exit than type "no" \n Enter here : ').lower()
            if again3 == 'yes':
                todolist()
            else:
               print('Thank for using to-do list')
            
        elif user == 4:
            print('thank you for using')
            break
        else:
            print('enter the valid option')

todolist()