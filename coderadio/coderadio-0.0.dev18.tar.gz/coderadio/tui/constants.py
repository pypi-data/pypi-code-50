DISPLAY_BUFFER = "display_buffer"
LISTVIEW_BUFFER = "listview_buffer"
PROMPT_BUFFER = "prompt_buffer"
POPUP_BUFFER = "popup_buffer"

# https://stackoverflow.com/questions/21503865/how-to-denote-that-a-command-line-argument-is-optional-when-printing-usage
HELP_TEXT = """

coderadio
---------

Press `Ctrl + Up` or `Ctrl + Down` to move the focus.
Press `UP` or `Down` to navigate between stations
To exit press `Ctrl + q` or type `exit` in the prompt and press enter.
To close this window, press F1 or change focus.


Command List
------------

Player commands
---------------

play <id>
stop
pause

Record commands
---------------
rec start <id> # TODO
rec stop <id> # TODO
rec list_all # TODO
Search commands
---------------

list bycodec <codec>
list bycountry <country>
list byid <id>
list bylanguage <language>
list byname <name>
list bystate <state>
list bytag <tag>
list byuuid <uuid>
list tags
search <options> # TODO

Help commands
--------------

help 
help <command> # TODO
"""

