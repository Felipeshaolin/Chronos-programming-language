
def halt():
    """this function is responsable of haltinf the program"""

    raise(Exception(f"---halt instruction--- in index {pc_register_pointer}"))

def add_v():
    
    global global_memory

    hold = global_memory[global_memory[hold_register_pointer]] # get the value in the hold register

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[pc_register_pointer]] # get the value 

    global_memory[hold_register_pointer] = hold + value # add ans save them

    global_memory[pc_register_pointer] += 1

def add_a():

    global global_memory

    hold = global_memory[global_memory[hold_register_pointer]] # get the value in the hold register

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[global_memory[pc_register_pointer]]] # get the value 

    global_memory[hold_register_pointer] = hold + value # add ans save them

    global_memory[pc_register_pointer] += 1

def sub_v():

    global global_memory

    hold = global_memory[global_memory[hold_register_pointer]] # get the value in the hold register

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[pc_register_pointer]] # get the value 

    global_memory[hold_register_pointer] = hold - value # substracts ans save them

    global_memory[pc_register_pointer] += 1

def sub_a():

    global global_memory

    hold = global_memory[global_memory[hold_register_pointer]] # get the value in the hold register

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[global_memory[pc_register_pointer]]] # get the value 

    global_memory[hold_register_pointer] = hold - value # subtracts and save them

    global_memory[pc_register_pointer] += 1

def adda():

    global global_memory

    hold = global_memory[global_memory[hold_register_pointer]] # get the value in the hold register

    value = global_memory[a_register_pointer] # get the value 

    global_memory[hold_register_pointer] = hold + value # subtracts and save them

    global_memory[pc_register_pointer] += 1

def suba():

    global global_memory

    hold = global_memory[global_memory[hold_register_pointer]] # get the value in the hold register

    value = global_memory[a_register_pointer] # get the value 

    global_memory[hold_register_pointer] = hold - value # subtracts and save them

    global_memory[pc_register_pointer] += 1

def goto():

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[global_memory[pc_register_pointer]]] 

    global_memory[pc_register_pointer] = value  # change the program counter

    global_memory[pc_register_pointer] += 1

def hold_v():

    global global_memory

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[pc_register_pointer]] # get the value 

    print(f'hold the value of {value}')

    global_memory[hold_register_pointer] = value # change the hold register

    global_memory[pc_register_pointer] += 1

def hold_a():

    global global_memory

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[global_memory[pc_register_pointer]]] # get the value 

    print(f"hold the value in {global_memory[pc_register_pointer]} of {value}")

    global_memory[hold_register_pointer] = value # change the hold register

    global_memory[pc_register_pointer] += 1

def holda():
    global global_memory

    value = global_memory[a_register_pointer] # retrives the value

    global_memory[hold_register_pointer] = value # put it in the hold

    global_memory[pc_register_pointer] +=1

def div_v():
    global global_memory

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[pc_register_pointer]]# gets the value

    hold = global_memory[hold_register_pointer] # gets the hold register value

    global_memory[hold_register_pointer] = int(hold/value) # divides it

    global_memory[pc_register_pointer] +=1

def div_a():
    global global_memory

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[global_memory[pc_register_pointer]]] # gets the value in memory

    hold = global_memory[hold_register_pointer] # get sthe value of the hold register

    global_memory[hold_register_pointer] = int(hold/value) # rounds it up

    global_memory[pc_register_pointer] +=1

def diva():

    global global_memory

    value = global_memory[a_register_pointer] # retrieves the valu eof the a register

    hold = global_memory[hold_register_pointer]

    global_memory[hold_register_pointer] = int(hold/value)

    global_memory[pc_register_pointer] +=1

def mult_v():

    global global_memory

    hold = global_memory[global_memory[hold_register_pointer]] # get the value in the hold register

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[pc_register_pointer]] # get the value 

    global_memory[hold_register_pointer] = hold * value # multiplies ans save them

    global_memory[pc_register_pointer] += 1

def mult_a():
    
    global global_memory

    hold = global_memory[global_memory[hold_register_pointer]] # get the value in the hold register

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[global_memory[pc_register_pointer]]] # get the value 

    global_memory[hold_register_pointer] = hold * value # multiplies ans save them

    global_memory[pc_register_pointer] += 1

def multa():

    global global_memory

    value = global_memory[a_register_pointer] # retrieves the valu eof the a register

    hold = global_memory[hold_register_pointer]

    global_memory[hold_register_pointer] = int(hold/value)

    global_memory[pc_register_pointer] +=1

def stor():
    
    global global_memory

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[pc_register_pointer]] # get the address 

    global_memory[value] = global_memory[hold_register_pointer] # saves it
    
    global_memory[pc_register_pointer] += 1

def stra():
    
    global global_memory

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[pc_register_pointer]] # get the address 

    global_memory[value] = global_memory[a_register_pointer] # saves it
    
    global_memory[pc_register_pointer] += 1

def aput():

    global_memory

    global_memory[pc_register_pointer] += 1

    value = global_memory[global_memory[pc_register_pointer]] # get the value

    print(f"the a register has the value {value} in it")

    global_memory[a_register_pointer] = value # saves it
    
    global_memory[pc_register_pointer] += 1
 

fonction_instruction_list = [halt,add_a,add_v,sub_a,sub_v,adda,suba,goto,hold_a,hold_v,holda,div_a,div_v,diva,mult_a,mult_v,multa,stor,stra,aput]

def execute():

    """this function executes the instructions based on memory"""

    global global_memory

    global pc_register_pointer
    global a_register_pointer
    global hold_register_pointer

    while True:

        fonction_instruction_list[hold_register_pointer]()

    print(global_memory)


def set_instructions():
    """this function finds and attributes all the instruction names in the intructions file"""

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

        print(f"the instruction list is {instruction_list}")
        if len(instruction_list) != len(fonction_instruction_list):

            raise(Exception(f"not the same amount of intructions on configure\ninstruction_list:{len(instruction_list)}\nfonction_instruction_list:{len(fonction_instruction_list)}"))


