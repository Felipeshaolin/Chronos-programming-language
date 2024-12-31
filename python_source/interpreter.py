#hi future me [i was here counter][###]
#started 18/12/2024 at 13:33
#this my first try at a intepreter of my own proggraming language

from front_end import *
from back_end import *
import time

start()
#time.sleep(2.5)
file = file_prompt()

debug_mode_check()

start_memory(file[1])
start_registers()
set_instructions()
deciffer_file(file[0])
execute()