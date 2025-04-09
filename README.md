# MyTask — A Simple CLI Task Manager

**MyTask** is a straightforward command-line tool written in Python for managing multiple task lists. It uses local JSON files to store tasks, so there's no need for a database or external dependencies.

---

## Features

- Manage multiple task lists
- Add, delete, rename tasks
- Mark tasks as complete/incomplete
- Rename or delete task lists
- View current or all lists
- Minimal, portable, and dependency-free

---

## Getting Started

### Requirements

- Python 3.6+

### Project Structure

```None
project_root/
├── tasklists/           # Contains all task list files (.json)
├── LICENSE              # License information
├── README.md            # This file
├── last                 # Tracks the active task list
├── mytask.sh            # Shell script that runs mytask.py
└── mytask.py            # The main CLI script

```

---

## Usage

Run the script from your terminal:

```bash
python mytask.py [OPTIONS]
```

Or use the mytask.sh script:

```bash
mytask.sh [OPTIONS]
```

---

## Options

| Option | Description |
|--------|-------------|
| `--license` | Show license information |
| `--version` | Show current version |
| `--doc` | Display the README.md content |
| `--newlist NAME` | Create a new task list |
| `--setlist NAME` | Set the current/working task list |
| `--lists` | Show all available task lists |
| `--show` | Show tasks in the current task list |
| `--add NAME` | Add a new task to the current list |
| `--delete ID` | Delete a task by ID |
| `--rename ID` | Rename a task (will prompt for new name) |
| `--renamelist NAME` | Rename a task list (will prompt for new name) |
| `--done ID` | Mark a task as completed |
| `--undo ID` | Mark a task as not completed |
| `--deletelist NAME` | Delete a task list |

---

## Examples

Create a new task list and set it as active:

```bash
python mytask.py --newlist chores
python mytask.py --setlist chores
```

Add tasks:

```bash
python mytask.py --add "Do the laundry"
python mytask.py --add "Take out the trash"
```

Mark task as done:

```bash
python mytask.py --done 1
```

View current list:

```bash
python mytask.py --show
```

Delete a task:

```bash
python mytask.py --delete 2
```

Rename a task:

```bash
python mytask.py --rename 1
# Prompts for new task name
```

Show all lists:

```bash
python mytask.py --lists
```

Delete a list:

```bash
python mytask.py --deletelist chores
```

---

## License

To view the license included with this project:

```bash
python mytask.py --license
```

---

## Version

```bash
python mytask.py --version
```

Current version: **0.0.1**

---

## Known Issues / To-Do

- `--rename` currently relies on `input()` and does not support piping or automation.
- Improve input validation and error handling.
- Consider support for timestamps, tags, or priority fields.

---

## Contributions

Pull requests and suggestions are welcome. Fork it, modify it, and make it your own.
