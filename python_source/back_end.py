
debug_mode = False
discreet_mode = False
global_memory = None

hold_register_pointer = None
pc_register_pointer = None
a_register_pointer = None

def debug_mode_check():

    global discreet_mode,debug_mode

    """this function checks if the user wants to use another type of execution"""

    print("chose your mode (type h for help)") # main message

    while True: # a loop that assures that you cant  make a wrong choise

        choise = input("") 

        if choise.lower() == 'h':

            print("commands:")
            print("h  - help (you already knew that).")
            print("")
            print("db - for debug mode, all instructions will")
            print("     print a message about what they did, ")
            print("     and memory will be printed before and")
            print("     after execution.")
            print("")
            print("d  - a more discreet way to run code,     ")
            print("     nothing will be printed except by    ")
            print("     \'start of execution\' and \'end of  ")
            print("     execution\' and print commmands.     ") # blablabla
            print("")
            print("n  - normal execution.")
        
        if choise.lower() == "db":
            print('debug mode: on')
            debug_mode = True
            break

        if choise.lower() == "d":
            print('discreet mode: on')
            discreet_mode = True
            break

        if choise.lower() == "n":
            print("normal execution")
            break



def start_memory(size):

    """this function starts the list with the memory in it"""

    global global_memory

    if size < 30:# prevents that the memory is at least 30 bytes long for the registers and code (error prown)

        size += 30

    global_memory = [0 for i in range(size)] # creates the list

    if debug_mode or not discreet_mode:
        print(f"the size of memory is {len(global_memory)} Bytes")


def start_registers():

    """this set the pointer to memory of each register"""

    global global_memory
    global hold_register_pointer
    global pc_register_pointer
    global a_register_pointer

    if debug_mode or not discreet_mode:

        print("starting registers")

    a_register_pointer = 0
    hold_register_pointer = 1 # this code is useles but i love it's uselessness
    pc_register_pointer = 2

    global_memory[pc_register_pointer] = 3

    if debug_mode or not discreet_mode:

        print("registers set")

def deciffer_file(file):

    global global_memory,instruction_list

    """this function is responsable of putting instructions in the memory"""

    #this function is complex and 100% pure spaghetti

    with open(file,'r') as file_to_deciffer: 

        info = file_to_deciffer.read() # read the file

        counter = 0 # var to get track of where we are in the file

        word = "" # var that stores "words"

        memory_pointer = 3 # var that indicates the current memory plcement of next "byte" is

        ignore = False # var used to ignore the addition fo letter in "word"
        comentaire = False # var used to flag a comment in code

        instruction = True # var that flags instructions if tey have already been detected
        single_cycle = False # var that flags single instructions like halt, aadd, asub, etc (that dont have a value)
        instruction_type = 0 # var that stores the instrction type wich is theyre value

        value = False # var flags if there is a value after a instruction
        adress = False # a var the flag if there is an adresses after a instruction
        after_value = 0 # a var that stores the value after a instruction

        while True: # main loop

            if counter >= len(info): # if counter is bigger that the file size it stops
                break

            letter = info[counter] # pick a letter from the file

            if word in instruction_list and instruction: # if the "word" is in the instrucion list and instructions is true

                if instruction_list.index(word) in (0,5,6,11,14,17): #if it's a single cycle instruction 
                                                                     # that's why its necessary to change this while writing your won single cycle instrucion
                    single_cycle = True

                instruction_type = instruction_list.index(word) # the type is the index of the word

                instruction = False # flag that the instruciton's been treated

                word = "" # blank the word var

            if word == "cmt": # if word is cmt (comment)

                comentaire = True 

            if letter == "#" and not instruction: #if "#" is present and the instruction has been treated

                ignore = True # we ignore this character
                Value = False # its not a value
                adress = True # it is an adress

            elif not instruction and not adress and letter != ' ': # if the instruction hasben treated it is not an adress and the letter is not equal to nothing

                value = True # it is a value

            if letter == '\n' : # end of line

                ignore = True # whe dont count this character

                if not single_cycle and not comentaire: # if it is not a comment or single cycle

                    # we continue on

                    if debug_mode:# all print check first if debug mode is active

                        if value: # if value is True

                            print(f'{instruction_list[instruction_type]}_v',end="") # v stands for value
                            instruction_type += 1

                        else: # if NOT value

                            print(f'{instruction_list[instruction_type]}_a',end="") # a stands for adress
                        
                    if word != "": # if the word in not nothing
                           
                        if debug_mode:

                            after_value = int(word) # translate the value from str to int
                            print(f" with a value of {after_value}")

#                       ilustration:                       
#                       o - indexed adress y - value after the instruction
#                       x - instruction                                    ...|o|0|0|...
                        global_memory[memory_pointer] = instruction_type # ...|x|0|0|...
                        memory_pointer += 1                              # ...|x|o|0|...
                        global_memory[memory_pointer] = after_value      # ...|x|y|0|...
                        memory_pointer += 1                              # ...|x|y|o|...

                    elif debug_mode: # if it is a blank line

                        print("\n no number detected: check for errors in code or this message just means you used an blank lines somewhere")


                else: # if it is a commennt or a single cycle instruction

                    if not comentaire: # if its a syngle cycle instruction

                        if debug_mode:
                            print(f'single cycle {instruction_list[instruction_type]} instruction')

#                       ilustration:                       
#                       o - indexed adress 
#                       x - instruction                                                         ...|o|0|...
                        global_memory[memory_pointer] = instruction_type                       #...|x|0|...
                        memory_pointer += 1                                                    #...|x|o|...

                    elif debug_mode: # if it is a comment

                        print(f'comment')
            
                comentaire = False
                instruction = True
                single_cycle = False
                instruction_type = 0

                value = False
                adress = False
                after_value = 0

                word = ""

            counter += 1
            if not ignore:
                word += letter
            else:
                ignore = False
        
        if debug_mode:
            print(global_memory)

        if debug_mode or not discreet_mode:
            print("memory written")

 
def halt():

    """this function is responsable of haltinf the program"""

    if debug_mode:
        print(global_memory)
    if discreet_mode:
        print("end of execution")
        quit()

    raise(Exception(f"---halt instruction--- in index {global_memory[pc_register_pointer]}"))

def add_v():
    
    global global_memory

    hold = global_memory[hold_register_pointer] # get the value in the hold register

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[pc_register_pointer]] # get the value

    if debug_mode:

        print(f"operation add_v {hold} + {value} = {hold + value}") 

    global_memory[hold_register_pointer] = hold + value # add ans save them

    global_memory[pc_register_pointer] += 1

def add_a():

    global global_memory

    hold = global_memory[hold_register_pointer] # get the value in the hold register

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[global_memory[pc_register_pointer]]] # get the value 

    if debug_mode:
        print(f"operation add_a {hold} + {value} = {hold + value}")

    global_memory[hold_register_pointer] = hold + value # add ans save them

    global_memory[pc_register_pointer] += 1

def sub_v():

    global global_memory

    hold = global_memory[hold_register_pointer] # get the value in the hold register

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[pc_register_pointer]] # get the value 

    if debug_mode:
        print(f"operation sub_v {hold} - {value} = {hold - value}")

    global_memory[hold_register_pointer] = hold - value # substracts ans save them

    global_memory[pc_register_pointer] += 1

def sub_a():

    global global_memory

    hold = global_memory[hold_register_pointer] # get the value in the hold register

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[global_memory[pc_register_pointer]]] # get the value 

    if debug_mode:
        print(f"operation sub_a {hold} - {value} = {hold - value}")

    global_memory[hold_register_pointer] = hold - value # subtracts and save them

    global_memory[pc_register_pointer] += 1

def adda():

    global global_memory

    hold = global_memory[hold_register_pointer] # get the value in the hold register

    value = global_memory[a_register_pointer] # get the value

    if debug_mode:
        print(f"operation aadd {hold} - {value} = {hold + value}")

    global_memory[hold_register_pointer] = hold + value # subtracts and save them

    global_memory[pc_register_pointer] += 1

def suba():

    global global_memory

    hold = global_memory[hold_register_pointer] # get the value in the hold register

    value = global_memory[a_register_pointer] # get the value 

    if debug_mode:
        print(f"operation asub {hold} - {value} = {hold - value}")

    global_memory[hold_register_pointer] = hold - value # subtracts and save them

    global_memory[pc_register_pointer] += 1

def goto_a():

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[global_memory[pc_register_pointer]]] 

    if debug_mode:
        print(f"operation goto_a of index{value}")

    global_memory[pc_register_pointer] = value  # change the program counter

def goto_v():

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[pc_register_pointer]]

    if debug_mode:
        print(f"operation goto_v of index {value}")

    global_memory[pc_register_pointer] = value  # change the program counter

    print(global_memory[global_memory[pc_register_pointer]])
    
def hold_v():

    global global_memory

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[pc_register_pointer]] # get the value 

    if debug_mode:
        print(f"operation hold_v of value {value}")

    global_memory[hold_register_pointer] = value # change the hold register

    global_memory[pc_register_pointer] += 1

def hold_a():

    global global_memory

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[global_memory[pc_register_pointer]]] # get the value 

    if debug_mode:
        print(f"operation hold_a of value {value}")

    global_memory[hold_register_pointer] = value # change the hold register

    global_memory[pc_register_pointer] += 1


def holda():
    
    global global_memory

    value = global_memory[a_register_pointer] # retrives the value

    global_memory[hold_register_pointer] = value # put it in the hold

    if debug_mode:
        print(f"operation ahold of value {value}")

    global_memory[pc_register_pointer] +=1

def div_v():
    global global_memory

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[pc_register_pointer]]# gets the value

    hold = global_memory[hold_register_pointer] # gets the hold register value

    if debug_mode:
        print(f"operation div_v {hold} / {value} = {int(hold / value)}")

    global_memory[hold_register_pointer] = int(hold/value) # divides it

    global_memory[pc_register_pointer] +=1

def div_a():
    global global_memory

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[global_memory[pc_register_pointer]]] # gets the value in memory

    hold = global_memory[hold_register_pointer] # get sthe value of the hold register

    if debug_mode:
        print(f"operation div_a {hold} / {value} = {int(hold / value)}")

    global_memory[hold_register_pointer] = int(hold/value) # rounds it up

    global_memory[pc_register_pointer] +=1

def diva():

    global global_memory

    value = global_memory[a_register_pointer] # retrieves the value of the a register

    hold = global_memory[hold_register_pointer]

    if debug_mode:
        print(f"operation adiv {hold} / {value} = {int(hold / value)}")

    global_memory[hold_register_pointer] = int(hold/value)

    global_memory[pc_register_pointer] +=1

def mult_v():

    global global_memory

    hold = global_memory[hold_register_pointer] # get the value in the hold register

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[pc_register_pointer]] # get the value

    if debug_mode:
        print(f"operation mult_v {hold} * {value} = {hold * value}") 

    global_memory[hold_register_pointer] = hold * value # multiplies ans save them

    global_memory[pc_register_pointer] += 1

def mult_a():
    
    global global_memory


    hold = global_memory[hold_register_pointer] # get the value in the hold register

    global_memory[pc_register_pointer] += 1

    value = global_memory[ global_memory[ global_memory[pc_register_pointer]] ] # get the value 

    if debug_mode:
        print(f"operation mult_a {hold} * {value} = {hold * value}") 

    global_memory[hold_register_pointer] = hold * value # multiplies ans save them

    global_memory[pc_register_pointer] += 1

def multa():

    global global_memory

    value = global_memory[a_register_pointer] # retrieves the valu eof the a register

    hold = global_memory[hold_register_pointer]
    
    if debug_mode:
        print(f"operation mult_a {hold} * {value} = {hold * value}") 

    global_memory[hold_register_pointer] = hold * value

    global_memory[pc_register_pointer] += 1

def stor_v():
    
    global global_memory

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[pc_register_pointer]] # get the address 

    global_memory[value] = global_memory[hold_register_pointer] # saves it

    if debug_mode:
        print(f"operation stor_v storing {global_memory[hold_register_pointer]} in {value}")
    
    global_memory[pc_register_pointer] += 1

def stor_a():
    
    global global_memory

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[global_memory[pc_register_pointer]]] # get the address 

    if debug_mode:
        print(f"operation stor_a storing {global_memory[hold_register_pointer]} in {value}")

    global_memory[value] = global_memory[hold_register_pointer] # saves it
    
    global_memory[pc_register_pointer] += 1

def stra_v():
    
    global global_memory

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[pc_register_pointer]] # get the address 

    if debug_mode:
        print(f"operation astor_v storing {global_memory[a_register_pointer]} in {value}")

    global_memory[value] = global_memory[a_register_pointer] # saves it
    
    global_memory[pc_register_pointer] += 1


def stra_a():
    
    global global_memory

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[global_memory[pc_register_pointer]]] # get the address 

    if debug_mode:
        print(f"operation astor_a storing {global_memory[a_register_pointer]} in {value}")

    global_memory[value] = global_memory[a_register_pointer] # saves it
    
    global_memory[pc_register_pointer] += 1

def aput_v():

    global global_memory

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[pc_register_pointer]] # get the value

    if debug_mode:
        print(f"operation aput_v storing {value}")

    global_memory[a_register_pointer] = value # saves it
    
    global_memory[pc_register_pointer] += 1

def aput_a():

    global global_memory

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[global_memory[pc_register_pointer]]] # get the value

    if debug_mode:
        print(f"operation aput_v storing {value}")

    global_memory[a_register_pointer] = value # saves it
    
    global_memory[pc_register_pointer] += 1


def cnde_v():
    
    global global_memory

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[pc_register_pointer]]

    hold = global_memory[hold_register_pointer]

    if debug_mode:

        print(f"operation cnde_v between {value} and {hold} wich is ", end="")

    if value == hold :

        if debug_mode:
            print("true")

        global_memory[pc_register_pointer] += 1

    else:

        if debug_mode:
            print('false')

        global_memory[pc_register_pointer] += 3


def cnde_a():
    
    global global_memory

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[global_memory[pc_register_pointer]]]

    hold = global_memory[hold_register_pointer]

    if debug_mode:

        print(f"operation cnde_a  between {value} and {hold}")

    if value == hold :

        if debug_mode:
            print("true")

        global_memory[pc_register_pointer] += 1

    else:

        if debug_mode:
                print('false')

        global_memory[pc_register_pointer] += 3


def cndb_v():
    
    global global_memory

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[pc_register_pointer]]

    hold = global_memory[hold_register_pointer]

    if debug_mode:

        print(f"operation cndb_v  between {value} and {hold}")

    if value < hold :

        if debug_mode:
            print("true")

        global_memory[pc_register_pointer] += 1

    else:

        if debug_mode:
            print('false')

        global_memory[pc_register_pointer] += 3


def cndb_a():
    
    global global_memory

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[global_memory[pc_register_pointer]]]

    hold = global_memory[hold_register_pointer]

    if debug_mode:

        print(f"operation cndb_a between {value} and {hold}")

    if value < hold :

        if debug_mode:
            print("true")

        global_memory[pc_register_pointer] += 1

    else:

        if debug_mode:
            print('false')

        global_memory[pc_register_pointer] += 3

    
def cnds_v():
    
    global global_memory

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[pc_register_pointer]]

    hold = global_memory[hold_register_pointer]

    if debug_mode:

        print(f"operation cnds_v between {value} and {hold}")

    if value > hold :

        if debug_mode:
            print("true")

        global_memory[pc_register_pointer] += 1

    else:

        if debug_mode:
            print('false')

        global_memory[pc_register_pointer] += 3


def cnds_a():
    
    global global_memory

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[global_memory[pc_register_pointer]]]

    hold = global_memory[hold_register_pointer]

    if debug_mode:

        print(f"operation cnds_a between {value} and {hold}")

    if value > hold :

        if debug_mode:
            print("true")

        global_memory[pc_register_pointer] += 1

    else:

        if debug_mode:
            print('false')

        global_memory[pc_register_pointer] += 3

def mark_a():

    if debug_mode:
        print("mark")

    global_memory[pc_register_pointer] += 2


def mark_v():

    if debug_mode:
        print("mark")

    global_memory[pc_register_pointer] += 2

def jmpup_a():

    global global_memory

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[global_memory[pc_register_pointer]]]

    if debug_mode:

        print(f"operation jmpup_a searching for mark of value {value}")
    
    while True:

        if global_memory[global_memory[pc_register_pointer]] == value :

            if global_memory[global_memory[pc_register_pointer]-1] == 31 or global_memory[global_memory[pc_register_pointer]-1] == 32:
        
                global_memory[pc_register_pointer] -= 1

                if debug_mode:
                    print(f"mark found")

                break

        global_memory[pc_register_pointer] -= 1

def jmpup_v():

    global global_memory

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[pc_register_pointer]]

    if debug_mode:

        print(f"operation jmpup_v searching for mark of value {value}")
    
    while True:

        if global_memory[global_memory[pc_register_pointer]] == value :

            if global_memory[global_memory[pc_register_pointer]-1] == 31 or global_memory[global_memory[pc_register_pointer]-1] == 32:
        
                global_memory[pc_register_pointer] -= 1

                if debug_mode:
                    print(f"mark found")

                break

        global_memory[pc_register_pointer] -= 1
 
fonction_instruction_list = [halt,add_a,add_v,sub_a,sub_v,adda,suba,goto_a,goto_v,hold_a,hold_v,holda,div_a,div_v,diva,mult_a,mult_v,multa,stor_a,stor_v,stra_a,stra_v,aput_a,aput_v,cnde_a,cnde_v,cndb_a,cndb_v,cnds_a,cnds_v,mark_a,mark_v,jmpup_a,jmpup_v]


def jmpdown_a():

    global global_memory

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[global_memory[pc_register_pointer]]]

    if debug_mode:

        print(f"operation jmpdown_a searching for mark of value {value}")
    
    while True:

        if global_memory[global_memory[pc_register_pointer]] == value :

            if global_memory[global_memory[pc_register_pointer]-1] == 31 or global_memory[global_memory[pc_register_pointer]-1] == 32:
        
                global_memory[pc_register_pointer] += 1

                if debug_mode:
                    print(f"mark found")

                break

        global_memory[pc_register_pointer] += 1

def jmpdown_v():

    global global_memory

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[pc_register_pointer]]

    if debug_mode:

        print(f"operation jmpdown_v searching for mark of value {value}")
    
    while True:

        if global_memory[global_memory[pc_register_pointer]] == value :

            if global_memory[global_memory[pc_register_pointer]-1] == 31 or global_memory[global_memory[pc_register_pointer]-1] == 32:
        
                global_memory[pc_register_pointer] += 1

                if debug_mode:
                    print(f"mark found")

                break

        global_memory[pc_register_pointer] += 1

 
fonction_instruction_list = [halt,add_a,add_v,sub_a,sub_v,adda,suba,goto_a,goto_v,hold_a,hold_v,holda,div_a,div_v,diva,mult_a,mult_v,multa,stor_a,stor_v,stra_a,stra_v,aput_a,aput_v,cnde_a,cnde_v,cndb_a,cndb_v,cnds_a,cnds_v,mark_a,mark_v,jmpup_a,jmpup_v,jmpdown_a,jmpdown_v]


def execute():

    """this function executes the instructions based on memory"""

    global global_memory

    if discreet_mode:

        print("start of execution")

    while True:

        if debug_mode:
            print(global_memory[ global_memory[pc_register_pointer] ])
            print(fonction_instruction_list[global_memory[ global_memory[pc_register_pointer]] ])

        fonction_instruction_list[global_memory[ global_memory[pc_register_pointer] ]]()


def set_instructions():
    """this function finds and attributes all the instruction names in the intructions file"""

    if debug_mode or not discreet_mode:
        print("starting intruction list")

    global instruction_list

    instruction_list =  []

    with open('configure.txt','r') as file:

        instructions = file.read()

        word = ""

        for i in instructions:

            if i == "\n":

                instruction_list.append(word) # reads each word in the file to put it in the list
                word = ''

            else:   
                word += i

        if debug_mode or not discreet_mode:
            print(f"the instruction list is {instruction_list}")

        if len(instruction_list) != len(fonction_instruction_list):

            raise(Exception(f"not the same amount of intructions on configure\ninstruction_list:{len(instruction_list)}\nfonction_instruction_list:{len(fonction_instruction_list)}"))


           













