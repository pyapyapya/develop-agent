web_prompts = \
"""
[Request]: Please develop a website that displays hello world
You have python in shell.

Process
--------
-  If not installed flask package, install flask and use it.
-  [Request] using flask package, develop a website that displays hello world
-  Add flask code using 'echo' command to /home/taehyeon/develop-agent/develop-agent/page.py
-  Execute server when connect to http://localhost:8001, then user can see "hello world"
--------

let's step by step

"""




q2_prompts = \
"""
[Request]: Please develop a webpage that allows me to move a box with my mouse.

Prerequisites
--------
1. You have python in shell.
2. You have flask, tkinter package in python. if not, install it.
--------

Process
--------
-  [Request] using flask, tkinter package, develop a webpage that allows me to move a box with my mouse.
-  Add flask, tkinter code using 'echo' command add to /home/taehyeon/develop-agent/develop-agent/page.py
-  Execute server when connect to http://localhost:8001, then user can see a website that allows me to move a box with my mouse.
--------

let's step by step

"""