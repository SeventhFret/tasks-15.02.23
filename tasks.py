from os import system

users = [
    {
        "name": "Holly",
        "type": "Student",
        "password": "hunter",
        "modules": [
            {
                "title": "Computer basics",
                "completed": True
            },
            {
                "title": "Python basics",
                "completed": False
            }
        ]
    },
    {
        "name": "Peter",
        "type": "Student",
        "password": "pan",
        "modules": [
            {
                "title": "Computer basics",
                "completed": False
            }
        ]
    },
    {
        "name": "Luke",
        "type": "Student",
        "password": "skywalker",
        "modules": [
            {
                "title": "Computer basics",
                "completed": True
            }
        ]
    },
    {
        "name": "Janis",
        "type": "Teacher",
        "password": "joplin"
    }
]

modules = [
    {
        "name": "Computer basics"
    },
    {
        "name": "Python basics",
        "requirement": "Computer basics"
    },
    {
        "name": "Django",
        "requirement": "Python basics"
    }
]

# TASK 1
def show_registration(username: str, password: str, modulename: str, users_storage=users):
    for user in users:
        if user['name'] == username and user['password'] == password:
            if user['type'] == 'Student':
                for module in user['modules']:
                    if module['title'] == modulename:
                        print(f'You are registered to the module {modulename}')
                        return user                
                pass
            else:
                print('You are the teacher')
                return None
    print(f'You did not register to the module {modulename}')
    return False


# TASK 2
def has_completed_module(username: str, password: str, modulename: str, users_storage=users):
    result = show_registration(username, password, modulename)
    if result:
        for module in result['modules']:
            if module['title'] == modulename and module['completed']:
                print(f'You have competed module {modulename}')
                return True
            else:
                print(f'You did not compete module {modulename}')
                return False

# TASK 3
def is_student(name: str, password: str, users=users):
    return [True if name == user['name'] and password == user['password'] and user['type'] == 'Student' else False for user in users]

def may_enroll(username: str, password: str, modulename: str, modules=modules):
    if show_registration(username, password, modulename) == False:
        if is_student(username, password):
            for module in modules:
                if 'requirement' not in list(module.keys()):
                    return True
                elif has_completed_module(username, password, module['requirement']):
                    return True
        else:
            for module in modules:
                if 'requirement' not in list(module.keys()):
                    return True
                else:
                    return False
    elif show_registration(username, password, modulename) == None:
        return False
        #     # return [True for module in modules if "requirement" not in module.keys()]


while True:
    system('clear')
    print('''What you want to do?
[1] - Task 1
[2] - Task 2
[3] - Task 3
[x] - Exit
''')
    choice = input()
    print()
    if choice == '1':
        username = input("What is your username? ")
        password = input(f"Type the password for username {username}: ")
        modulename = input("What module do you want to check? ")
        show_registration(username, password, modulename)
    elif choice == '2':
        username = input("What is your username? ")
        password = input(f"Type the password for username {username}: ")
        modulename = input("What module do you want to check? ")
        show_registration(username, password, modulename)
        has_completed_module(username, password, modulename)
    elif choice == '3':
        username = input("What is your username? ")
        password = input(f"Type the password for username {username}: ")
        modulename = input("What module do you want to check? ")
        if may_enroll(username, password, modulename):
            print(f"You may register to the module {modulename}.")
        else:
            print(f"You may not register to the module {modulename}.")
    if choice != 'x':
        print()
        input('Press Enter to continue...')
        continue
    else:
        print("Alright, see you!")
        break