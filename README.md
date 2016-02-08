# taskTrack
A command-line tool inspired by Wunderlist, with added customizations.

## Features
- Valid commands:
  - "add task [, day]/[monthAbbr dateNum]": add a new task to the list
  - "exit"/"quit": exit the shell
  - "help": show this message
  - "rm/rem(ove)/del(ete)/did desc": removes a task matching desc
  - "show": display all tasks
    - Defaults to chronological order
  - "set setting value": update setting to value (True/False)
- Customizable shell settings:
  - showOnStart/showOnAdd/showOnRem
 
### Future Changes
- Allow multiple todo lists
- Allow wider range of date input formats
