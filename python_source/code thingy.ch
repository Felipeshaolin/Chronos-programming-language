
cmt this calculates x^y

hold 3
cmt put the value of x here
cmt !3
str 49
cmt !5
cmt the number on the bottom is stored in 49

hold 2
cmt put the value of y here
cmt !7
str 50
cmt !9
cmt the exponent is stored in 50

hold 1
cmt ! 11
str 51
cmt ! 13

hold #50
cmt !15

cnde 0
cmt !17
goto 52
cmt !19
cmt if it hasnt hit 0

hold #51
cmt !21

mult #49
cmt !23
cmt multiply by itself

str 51
cmt !25
cmt the result goes to 51

hold #50
cmt !27
sub 1
cmt !29
str 50
cmt !31
cmt decrements the exponent

mark 69

goto 15
cmt !33
