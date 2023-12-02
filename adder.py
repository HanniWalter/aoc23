#just to try some stuff
with open('ref', 'r') as f:
    lines = [x.strip() for x in f.readlines()]
input = "$".join(lines)

atoz =  "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
any = atoz + numbers + "$#"

from NDTM import *
tm = NDTM('a1', 'af', '#', 2) 

tm.tapes[0].loadString("f3tA00",4)
tm.tapes[1].loadString("A$32$92$91",9)


#first step done now in q10
#go left until you find a number
for number in numbers:
    tm.addTrans('a1', (number, '#',), 'a1', ((number, '_'),("#",'L')), )
    tm.addTrans('a1', (number, 'Y',), 'a1', ((number, '_'),("Y",'L')), )

#add first number
for top in numbers:
    for bottom in numbers:
        sum = int(top) + int(bottom)
        sum2 = str(sum%10)

        if int(top) + int(bottom) > 9:            
            tm.addTrans('a1', (top, bottom,), 'a3', ((sum2 , 'R'),("#",'L')), )
            #q11 carry needed
        else:
            tm.addTrans('a1', (top, bottom,), 'a2', ((sum2 , 'R'),("#",'L')), )
#add second number no carry
for top in numbers:
    for bottom in numbers:
        sum = int(top) + int(bottom)
        sum2 = str(sum%10)
        if int(top) + int(bottom) <10:            
            tm.addTrans('a2', (top, bottom,), 'a4', ((sum2 , '_'),("#",'L')), )
            #q11 carry needed
        else:
            tm.addTrans('a2', (top, bottom,), 'a5', ((sum2, 'R'),("#",'L')), )
#add second number with carry
for top in numbers:
    for bottom in numbers:
        sum = int(top) + int(bottom) + 1
        sum2 = str(sum%10)
        if int(top) + int(bottom) +1<10:            
            tm.addTrans('a3', (top, bottom,), 'a4', ((sum2 , '_'),("#",'L')), )
            #q11 no carry needed
        else:
            tm.addTrans('a3', (top, bottom,), 'a5', ((sum2, 'R'),("#",'L')), )
#if carry is needed add the carry
for top in numbers+"#":
    if top == "#":
        n = "0"
    else:
        n = top
    sum = int(n) + 1
    if sum == 10:
        tm.addTrans('a5', (top, "$",), 'a5', (("0", 'R'),("$",'_')), )
    else:
        tm.addTrans('a5', (top, "$",), 'a4', ((str(sum), '_'),("$",'_')), )
#go left until you find A
for top in numbers:
    tm.addTrans('a4', (top, "$",), 'a4', ((top, 'L'),("$",'_')), )
#restart
tm.addTrans('a4', ("A", "$",), 'a1', (("A", 'R'),("#",'L')), )
#when A go in next step
for top in numbers:
    tm.addTrans('a1', (top, "A",), 'a10', ((top, 'R'),("A",'_')), )
#go right to last number
for top in numbers:
    tm.addTrans('a10', (top, "A",), 'a10', ((top, 'R'),("A",'_')), )
#go one left
tm.addTrans('a10', ("#", "A",), 'a11', (("#", 'L'),("A",'R')), )
#reverse
for top in numbers:
    tm.addTrans('a11', (top, "#",), 'a11', ((top, 'L'),(top,'R')), )

#for top in numbers:
#    tm.addTrans('a1', (top, "A",), 'a6', ((top, 'R'),("A",'R')), )
    

#for top in numbers:
#    for bottom in numbers:
#        tm.addTrans('q11', (top, bottom,), 'q11', ((top, '_'),(bottom,'L')), )
#        tm.addTrans('q12', (top, bottom,), 'q12', ((top, '_'),(bottom,'L')), )
#    tm.addTrans('q11', (top, "$",), 'q11a', ((top, '_'),("$",'L')), )
#    tm.addTrans('q12', (top, "$",), 'q12a', ((top, '_'),("$",'L')), )
#    #go left until you find a number
#    tm.addTrans('q11a', (top, "Y",), 'q11a', ((top, '_'),("Y",'L')), )
#    tm.addTrans('q12a', (top, "Y",), 'q12a', ((top, '_'),("Y",'L')), )
#for top in numbers:
#    for bottom in numbers:
#        sum = int(top) + int(bottom)
#        sum2 = str(sum%10)
#        if int(top) + int(bottom) <10:            
#            tm.addTrans('q11a', (top, bottom,), 'q11b', ((sum2 , 'R'),("Y",'L')), )
#            tm.addTrans('q12a', (top, bottom,), 'q12b', ((sum2 , 'R'),("Y",'L')), )
#            #q11 carry needed
#        else:
#            tm.addTrans('q12a', (top, bottom,), 'q11b', ((sum2, 'R'),("Y",'L')), )
# go right until you find a #
#for top in numbers+"#":
#    for bottom in numbers+"Y$":
#        tm.addTrans('q11b', (top, bottom,), 'q11b', ((top, '_'),(bottom,'R')), )
#        tm.addTrans('q12b', (top, bottom,), 'q12b', ((top, '_'),(bottom,'R')), )
#write carry 
#tm.addTrans('q11b', ("#", "#",), 'q13', (("1", '_'),("#",'_')), )
#tm.addTrans('q12b', ("#", "#",), 'q13', (("0", '_'),("#",'_')), )
#go left until you find a number
#for top in numbers:
#    for bottom in "Y#":
#        tm.addTrans('q13', (top, bottom,), 'q13', ((top, '_'),(bottom,'L')), )
#    for bottom in numbers:
#        tm.addTrans('q13', (top, bottom,), 'q10', ((top, '_'),(bottom,'_')), )
#for top in numbers:
#    tm.addTrans('q13', (top, "$",), 'q20', ((top, '_'),("$",'_')), )
#    tm.addTrans('q20', (top, "$",), 'q21', (("#",'L'),("$", '_'),), )
#    tm.addTrans('q21', (top, "$",), 'q22', ((top, bottom),("Y",'L')), )
    #go left until you find a $
#    for bottom in "Y":
#        tm.addTrans('q22', (top, bottom,), 'q22', ((top, bottom),("Y",'L')), )
#    tm.addTrans('q22', (top, "$"), 'q23', ((top, "_"),("$",'R')), )
#copy upper band
#for top in numbers:
#    tm.addTrans('q23', (top, "Y",), 'q23', (("#", "L"),(top,'R')), )
#go one right
#tm.addTrans('q23', ("A", "Y",), 'q24', (("A", "R"),("Y",'_')), )
#go right until you find a # and delete
#tm.addTrans('q24', ("#", "Y",), 'q24', (("#", "_"),("#",'R')), )
#go left until you find a number
#tm.addTrans('q24', ("#", "#",), 'q25', (("#", "_"),("#",'L')), )
#write 0 as carry
#tm.addTrans('q25', ("#", "#",), 'q10', (("0", "_"),("#",'_')), )

#when P write carry or not
#tm.addTrans('q12b', ("P", "#",), 'q26', (("P", "_"),("#",'_')), )
     
#tm.addTrans('qi', ("#", '#',), 'qf', (("$", 'S'),("$",'S')), )
tm.run_det(100)
print(tm)
print(tm.state)
#print(tm.trans.keys())