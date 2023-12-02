#read test to lines
with open('ref', 'r') as f:
    lines = [x.strip() for x in f.readlines()]
input = "$".join(lines)

atoz =  "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
any = atoz + numbers + "$#"

from NDTM import *
tm = NDTM('qi2', 'qf', '#', 2) 

tm.tapes[0].loadString(input,0)

for i in atoz+numbers:
    tm.addTrans('qi2', (i, '#',), 'qi3', ((i, '_'),('A','R'),), )
    tm.addTrans('qi3', (i, '#',), 'qi', ((i, '_'),('$','R'),), )
for i in atoz:
        #skip letters
        tm.addTrans('qi', (i, '#',), 'qi', ((i, 'R'),('#','_'),), )
        tm.addTrans('q2', (i, '#',), 'q2', ((i, 'R'),('#','_'),), )



        
for i in numbers:
        tm.addTrans('qi', (i, '#',), 'q1', ((i, '_'),(i,'R'),), )
        tm.addTrans('q1', (i, '#',), 'q2', ((i, 'R'),(i,'R'),), )
        #q2 now read letters
        tm.addTrans('q2', (i, '#',), 'q3', ((i, '_'),('#','L'),), )
        for j in numbers:
            tm.addTrans('q3', (i, j,), 'q2', ((i, 'R'),(i,'R'),), )
            tm.addTrans('q4', (i, j,), 'q2', ((i, 'R'),(i,'_'),), )
        tm.addTrans('q2', ("#", i,), 'qi', (("#", 'R'),(i,'_'),), )


tm.addTrans('qi', ("$", '#',), 'qi', (("$", 'R'),("$",'R')), )
tm.addTrans('q2', ("$", '#',), 'qi', (("$", 'R'),("$",'R')), )

tm.addTrans('q2', ("#", '#',), 'q9', (("A", 'R'),("#",'_')), )
tm.addTrans('q9', ("#", '#',), 'q10', (("0", 'R'),("#",'_')), )
tm.addTrans('q10', ("#", '#',), 'a1', (("0", 'L'),("#",'_')), )
#first step done now in q10
#go left until you find a number
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
#go final
tm.addTrans('a11', ("A", "#",), 'qf', (("#", '_'),("#",'_')), )
tm.run_det(100000)
print(tm)
answer = tm.tapes[1].symbols
print(int("".join(answer)))

#print(tm.trans.keys())