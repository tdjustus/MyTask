from argparse import ArgumentParser
import os
import json

root_path = os.path.dirname(os.path.abspath(__file__)) + os.sep
tasklists_path = root_path + 'tasklists' + os.sep
license_path = root_path + 'LICENSE'
readme_path = root_path + 'README.md'
last_path = root_path + 'last'


def load_list(name):
    if not os.path.exists(tasklists_path + name + '.json'):
        print(f"Task list '{name}' does not exist.")
        exit(1)
    with open(tasklists_path + name + '.json') as f:
        return json.loads(f.read())
    

def save_list(name, tasks):
    with open(tasklists_path + name + '.json', 'w') as f:
        f.write(json.dumps(tasks, indent=4))
    

def get_working_list():
    with open(last_path) as f:
        current_task = f.read().strip()
    if current_task == '':
        print("No task list set. Use --newlist to create a new task list.")
        exit(1)
    if not os.path.exists(tasklists_path + current_task + '.json'):
        print(f"Task list '{current_task}' does not exist.")
        exit(2)
    return current_task


def create_new_list(name):
    if os.path.exists(tasklists_path + name + '.json'):
        print(f"Task list '{name}' already exists.")
        return
    save_list(name, {})
    set_working_list(name)


def set_working_list(name):
    with open(last_path, 'w') as f:
        f.write(name)


def show_all_lists():
    lists = [f[:-5] for f in os.listdir(tasklists_path) if f.endswith('.json')]
    if not lists:
        print("No task lists found.")
        return
    print("Available task lists:")
    for lst in lists:
        print(f"\t{lst}")


def show_current_list():
    current_list = get_working_list()
    tasks = load_list(current_list)
    if not tasks:
        print(f"Task list '{current_list}' is empty.")
        return
    print(f"Current task list '{current_list}':")
    for task_id, task in tasks.items():
        status = 'Complete' if task['done'] else 'Incomplete'
        print(f"\t{task_id}: {task['task']} ({status})")


def delete_list(name):
    if not os.path.exists(tasklists_path + name + '.json'):
        print(f"Task list '{name}' does not exist.")
        return
    os.remove(tasklists_path + name + '.json')
    if os.path.exists(last_path) and open(last_path).read().strip() == name:
        with open(last_path, 'w') as f:
            f.write('')
    print(f"Task list '{name}' deleted.")


def delete_task(task_id):
    tasks = load_list(get_working_list())
    if str(task_id) not in tasks:
        print(f"Task ID '{task_id}' does not exist.")
        return
    del tasks[str(task_id)]
    save_list(get_working_list(), tasks)


def rename_task(task_id):
    tasks = load_list(get_working_list())
    if str(task_id) not in tasks:
        print(f"Task ID '{task_id}' does not exist.")
        return
    old_task_name = tasks[str(task_id)]['task']
    tasks[str(task_id)]['task'] = input('Enter new task name: ')
    save_list(get_working_list(), tasks)
    print(f"Task ID '{old_task_name}' renamed to '{task_id}'.")


def rename_list(name):
    if not os.path.exists(tasklists_path + name + '.json'):
        print(f"Task list '{name}' does not exist.")
        return
    new_name = input("Enter new name for the task list: ")
    if os.path.exists(tasklists_path + new_name + '.json'):
        print(f"Task list '{new_name}' already exists.")
        return
    os.rename(tasklists_path + name + '.json', tasklists_path + new_name + '.json')
    if os.path.exists(last_path) and open(last_path).read().strip() == name:
        with open(last_path, 'w') as f:
            f.write(new_name)
    print(f"Task list '{name}' renamed to '{new_name}'.")


def mark_task_done(task_id):
    tasks = load_list(get_working_list())
    if str(task_id) not in tasks:
        print(f"Task ID '{task_id}' does not exist.")
        return
    tasks[str(task_id)]['done'] = True
    with open(tasklists_path + get_working_list() + '.json', 'w') as f:
        f.write(json.dumps(tasks, indent=4))


def undo_task(task_id):
    tasks = load_list(get_working_list())
    if str(task_id) not in tasks:
        print(f"Task ID '{task_id}' does not exist.")
        return
    tasks[str(task_id)]['done'] = False
    save_list(get_working_list(), tasks)


def add_task(task):
    tasks = load_list(get_working_list())
    task_id = str(len(tasks) + 1)
    tasks[task_id] = {'task': task, 'done': False}
    save_list(get_working_list(), tasks)
    print(f"Task '{task}' added with ID '{task_id}'.")


def main():
    parser = ArgumentParser(description="A simple CLI task manager.")
    parser.add_argument('--license', action='store_true', help='Show license information')
    parser.add_argument('--version', action='store_true', help='Show version information')
    parser.add_argument('--doc', action='store_true', help='Show documentation')
    parser.add_argument('--newlist', type=str, help='Create a new task list')
    parser.add_argument('--setlist', type=str, help='Set the working task list')
    parser.add_argument('--lists', action='store_true', help='Show all task lists')
    parser.add_argument('--show', action='store_true', help='Show the current task list')
    parser.add_argument('--deletelist', type=str, help='Delete a task list')
    parser.add_argument('--delete', type=int, help='Delete a task from your list')
    parser.add_argument('--rename', type=int, help='Edit a task in your list')
    parser.add_argument('--renamelist', type=str, help='Edit the current task list')
    parser.add_argument('--done', type=int, help='Mark a task as done')
    parser.add_argument('--undo', type=int, help='Mark a done task as not done')
    parser.add_argument('--add', type=str, help='Add a new task to your list')

    args = parser.parse_args()

    if args.license:
        with open(license_path) as f:
            print(f.read())
        return
    
    if args.version:
        print('MyTask version 0.0.1')
        return
    
    if args.doc:
        with open(readme_path) as f:
            print(f.read())
        return
    
    if args.newlist:
        create_new_list(args.newlist)
        return
    
    if args.setlist:
        set_working_list(args.setlist)
        return
    
    if args.lists:
        show_all_lists()
        return
    
    if args.show:
        show_current_list()
        return
    
    if args.deletelist:
        delete_list(args.deletelist)
        return
    
    if args.delete:
        delete_task(args.delete)
        return
    
    if args.rename:
        rename_task(args.rename)
        return
    
    if args.renamelist:
        rename_list(args.renamelist)
        return
    
    if args.done:
        mark_task_done(args.done)
        return
    
    if args.undo:
        undo_task(args.undo)
        return
    
    if args.add:
        add_task(args.add)
        return
    
    print("No valid arguments provided. Use --help for more information.")


if __name__ == "__main__":
    main()
