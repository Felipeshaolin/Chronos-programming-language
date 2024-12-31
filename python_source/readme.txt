commencé par Felipe Felsner le 18/12/2024 a 10/21 pendant le cours de NSI

####|registers|####

program counter

    register that holds a pointer to the operation
    that will be executed.
    counts up with every operation.(with some exceptions (jumps and gotos))

hold register

    resgister that stores any value, it is used
    as ram to store operations

A$  

    register that can hold any info, can be 
    changed by all intructions that end by 
    "a"

#####|syntax|#####

halt 
(value 0) {one byte} # single-cycle

    a instruction that kills the current task
    it is used by the error messages

add 
[memory or value]: (value 01 and 02) {two bytes}

    adds two values together, it adds the hold 
    register with the value or memory adress given
    and the result goes to the hold register

sub 
[memory or value]: (value 03 and 04) {two bytes}

    subtracts two values together, it subtracts the
    hold register with the value or the memory adress 
    given.

adda 
(value 05) {one bytes} # single-cycle

    adds two values together, it adds the hold 
    register with the value in the a register and
    the result goes to the hold register

suba 
 (value 06) {one bytes} # single-cycle

    subtracts two values together, it subtracts the hold 
    register with the value in the a register and
    the result goes to the hold register

goto 
[memory or value]: (value 07,08 ) {two bytes}

    a instruction that jumps you to a line 
    number it changes the program counter

hold 
[memory or value] (value 09,0A  ) {two bytes}

    a instruction that stores the info given
    in the hold register, all previous info
    stored in the hold register will be 
    erased

holda 
(value 0B ) {one bytes} # single-cycle

    a instruction that stores the info in the
    a register into the hold register, all 
    previous info stored in the hold register
    will be erased

cmt 

    instruction that is not used,
    it can be used to make comments

div 
[memory or value] (value 0C,0D ) {two bytes}

    divides two values, divides the hold 
    register with the value or the memory 
    adress given and the result goes to 
    the hold register

diva 
(value 0E ) {one byte} # single-cycle

    divides two values, divides the hold 
    register with the value in the a register
    and the result goes to the hold register

mult 
[memory or value] (value 0F,10 ) {two bytes}

    multiplies two values, divides the 
    hold register with the value or the
    memory adress given and the result 
    goes to thehold register

multa 
(value 11 ) {one bytes} # single-cycle

    multiplies two values, multiplier the 
    hold register with the value int the 
    a registerhold register

str 
[memory address or value] (value 12,13) {two bytes}

    stores a value in memory from hold register

astr 
[memory address or value] (value 14,15) {two bytes}

    stores the value in memory from the a register

aput
[memory or value] (value 16,17  ) {two bytes}

    a instruction that stores the info given
    in the a register, all previous info
    stored in the a register will be 
    erased

cnde
[memory or value] (value 18,19 ) {two bytes}

    a instruction that compares the hold register
    with the value given and executes the next line 
    if its equal or not

cndb
[memory or value] (value 1A,1B ) {two bytes}

    a instruction that compares the hold register
    with the value given and executes the next line 
    if its bigger or not

cnds
[memory or value] (value 1C,1D ) {two bytes}

    a instruction that compares the hold register
    with the value given and executes the next line 
    if its smaller or not

mark
[memory or value] (value 1E,1F ) {two bytes}

    a litteral mark that doesn no computing but
    is used by jumps to repeat a line

jmpup
[memory or value] (value 20,21 ) {two bytes}

    a instruction that tries to find a mark and 
    pc variable as it, executing it again.
    it searches it mark above its current line.
    if no mark is given an error will accour

jmpdown
[memory or value] (value 22,23 ) {two bytes}

    a instruction that tries to find a mark and 
    pc variable as it, executing it again.
    it searches it mark below its current line.
    if no mark is given an error will accour

in 
(value 24 ) {one byte} # single-cycle

    a instruction that will stop the current 
    and wait a value to be inputed

out
[memory or value] (value 25,26 ) {two bytes}

    a intruction that will output a value as a number

l_out
[memory or value] (value 27,28 ) {two bytes}

    a intruction that will output a value as a letter using ascii

