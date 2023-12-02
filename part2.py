#read test to lines
with open('ref', 'r') as f:
    lines = [x.strip() for x in f.readlines()]
input = "$".join(lines)
input = "#"+input 

atoz =  "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
any = atoz + numbers + "$#"

from NDTM import *
tm = NDTM('qi2', 'qf', '#', 2) 

tm.tapes[0].loadString(input,0)

tm.addTrans('qi2', ("#", '#',), 'qi2', (('#', 'R'),('#','_'),), )
for i in atoz+numbers:
    
    tm.addTrans('qi2', (i, '#',), 'qi3', ((i, '_'),('A','R'),), )
    tm.addTrans('qi3', (i, '#',), 'c1', ((i, '_'),('$','R'),), )

#check one
for i in atoz+numbers:
    if i == "o":
        tm.addTrans('c1', (i, '#',), 'c1o', ((i, 'R'),('#','_'),), )
        continue
    tm.addTrans('c1', (i, '#',), 'c2', ((i, '_'),('#','_'),), )    
for i in atoz+numbers:
    if i == "n":
        tm.addTrans('c1o', (i, '#',), 'c1on', ((i, 'R'),('#','_'),), )
        continue
    tm.addTrans('c1o', (i, '#',), 'c2', ((i, 'L'),('#','_'),), )    
for i in atoz+numbers:
    if i == "e":
        tm.addTrans('c1on', (i, '#',), 'd1on', ((i, 'L'),('#','_'),), )
        continue
    tm.addTrans('c1on', (i, '#',), 'e1on', ((i, 'L'),('#','_'),), )   
tm.addTrans('d1on', ("n", '#',), 'd1o', (("n", 'L'),("#",'_'),), )
tm.addTrans('d1o', ("o", '#',), 'c1', (("1", 'R'),("#",'_'),), ) 
tm.addTrans('e1on', ("n", '#',), 'e1o', (("n", 'L'),("#",'_'),), )
tm.addTrans('e1o', ("o", '#',), 'c2', (("o", '_'),("#",'_'),), )

#check two
for i in atoz+numbers:
    if i == "t":
        tm.addTrans('c2', (i, '#',), 'c2t', ((i, 'R'),('#','_'),), )
        continue
    tm.addTrans('c2', (i, '#',), 'c3', ((i, '_'),('#','_'),), )    
for i in atoz+numbers:
    if i == "w":
        tm.addTrans('c2t', (i, '#',), 'c2tw', ((i, 'R'),('#','_'),), )
        continue
    tm.addTrans('c2t', (i, '#',), 'c3', ((i, 'L'),('#','_'),), )    
for i in atoz+numbers:
    if i == "o":
        tm.addTrans('c2tw', (i, '#',), 'd2tw', ((i, 'L'),('#','_'),), )
        continue
    tm.addTrans('ctw', (i, '#',), 'e2tw', ((i, 'L'),('#','_'),), )  

tm.addTrans('d2tw', ("w", '#',), 'd2t', (("w", 'L'),("#",'_'),), )
tm.addTrans('d2t', ("t", '#',), 'c1', (("2", 'R'),("#",'_'),), ) 
tm.addTrans('e2tw', ("w", '#',), 'e2t', (("w", 'L'),("#",'_'),), )
tm.addTrans('e2t', ("t", '#',), 'c3', (("t", '_'),("#",'_'),), )

#check three
for i in atoz+numbers:
    if i == "t":
        tm.addTrans('c3', (i, '#',), 'c3t', ((i, 'R'),('#','_'),), )
        continue
    tm.addTrans('c3', (i, '#',), 'c4', ((i, '_'),('#','_'),), )
for i in atoz+numbers:
    if i == "h":
        tm.addTrans('c3t', (i, '#',), 'c3th', ((i, 'R'),('#','_'),), )
        continue
    tm.addTrans('c3t', (i, '#',), 'c4', ((i, 'L'),('#','_'),), )
for i in atoz+numbers:
    if i == "r":
        tm.addTrans('c3th', (i, '#',), 'c3thr', ((i, 'R'),('#','_'),), )
        continue
    tm.addTrans('c3th', (i, '#',), 'e3th', ((i, 'L'),('#','_'),), )
for i in atoz+numbers:
    if i == "e":
        tm.addTrans('c3thr', (i, '#',), 'c3thre', ((i, 'R'),('#','_'),), )
        continue
    tm.addTrans('c3thr', (i, '#',), 'e3thr', ((i, 'L'),('#','_'),), )
for i in atoz+numbers:
    if i == "e":
        tm.addTrans('c3thre', (i, '#',), 'd3thre', ((i, 'L'),('#','_'),), )
        continue
    tm.addTrans('c3thre', (i, '#',), 'e3thre', ((i, 'L'),('#','_'),), )

tm.addTrans('d3three', ("e", '#',), 'd3thre', (("e", 'L'),("#",'_'),), )
tm.addTrans('d3thre', ("e", '#',),  'd3thr', (("e", 'L'),("#",'_'),), )
tm.addTrans('d3thr', ("r", '#',),   'd3th', (("r", 'L'),("#",'_'),), )
tm.addTrans('d3th', ("h", '#',),    'd3t', (("h", 'L'),("#",'_'),), )
tm.addTrans('d3t', ("t", '#',), 'c1', (("3", 'R'),("#",'_'),), ) 

tm.addTrans('e3three', ("e", '#',), 'e3thre', (("e", 'L'),("#",'_'),), )
tm.addTrans('e3thre', ("e", '#',), 'e3thr', (("e", 'L'),("#",'_'),), )
tm.addTrans('e3thr', ("r", '#',), 'e3th', (("r", 'L'),("#",'_'),), )
tm.addTrans('e3th', ("h", '#',), 'e3t', (("h", 'L'),("#",'_'),), )
tm.addTrans('e3t', ("t", '#',), 'c4', (("t", '_'),("#",'_'),), )
#check four
for i in atoz+numbers:
    if i == "f":
        tm.addTrans('c4', (i, '#',), 'c4f', ((i, 'R'),('#','_'),), )
        continue
    tm.addTrans('c4', (i, '#',), 'c5', ((i, '_'),('#','_'),), )
for i in atoz+numbers:
    if i == "o":
        tm.addTrans('c4f', (i, '#',), 'c4fo', ((i, 'R'),('#','_'),), )
        continue
    tm.addTrans('c4f', (i, '#',), 'c5', ((i, 'L'),('#','_'),), )
for i in atoz+numbers:
    if i == "u":
        tm.addTrans('c4fo', (i, '#',), 'c4fou', ((i, 'R'),('#','_'),), )
        continue
    tm.addTrans('c4fo', (i, '#',), 'e4fo', ((i, 'L'),('#','_'),), )
for i in atoz+numbers:
    if i == "r":
        tm.addTrans('c4fou', (i, '#',), 'd4fou', ((i, 'L'),('#','_'),), )
        continue
    tm.addTrans('c4fou', (i, '#',), 'e4fou', ((i, 'L'),('#','_'),), )

tm.addTrans('d4four',   ("r", '#',),  'd4fou', (("r", 'L'),("#",'_'),), )
tm.addTrans('d4fou',    ("u", '#',),   'd4fo', (("u", 'L'),("#",'_'),), )
tm.addTrans('d4fo',     ("o", '#',),    'd4f', (("o", 'L'),("#",'_'),), )
tm.addTrans('d4f',      ("f", '#',),     'c1', (("4", 'R'),("#",'_'),), ) 

tm.addTrans('e4four',   ("r", '#',),  'e4fou', (("r", 'L'),("#",'_'),), )
tm.addTrans('e4fou',    ("u", '#',),   'e4fo', (("u", 'L'),("#",'_'),), )
tm.addTrans('e4fo',     ("o", '#',),    'e4f', (("o", 'L'),("#",'_'),), )
tm.addTrans('e4f',      ("f", '#',),     'c5', (("f", '_'),("#",'_'),), )

#check five
for i in atoz+numbers:
    if i == "f":
        tm.addTrans('c5', (i, '#',), 'c5f', ((i, 'R'),('#','_'),), )
        continue
    tm.addTrans('c5', (i, '#',), 'c6', ((i, '_'),('#','_'),), )
for i in atoz+numbers:
    if i == "i":
        tm.addTrans('c5f', (i, '#',), 'c5fi', ((i, 'R'),('#','_'),), )
        continue
    tm.addTrans('c5f', (i, '#',), 'c6', ((i, 'L'),('#','_'),), )
for i in atoz+numbers:
    if i == "v":
        tm.addTrans('c5fi', (i, '#',), 'c5fiv', ((i, 'R'),('#','_'),), )
        continue
    tm.addTrans('c5fi', (i, '#',), 'e5fi', ((i, 'L'),('#','_'),), )
for i in atoz+numbers:
    if i == "e":
        tm.addTrans('c5fiv', (i, '#',), 'd5fiv', ((i, 'L'),('#','_'),), )
        continue
    tm.addTrans('c5fiv', (i, '#',), 'e5fiv', ((i, 'L'),('#','_'),), )

tm.addTrans('d5five',   ("e", '#',),  'd5fiv', (("e", 'L'),("#",'_'),), )
tm.addTrans('d5fiv',    ("v", '#',),  'd5fi', (("v", 'L'),("#",'_'),), )
tm.addTrans('d5fi',     ("i", '#',),  'd5f', (("i", 'L'),("#",'_'),), )
tm.addTrans('d5f',      ("f", '#',),  'c1', (("5", 'R'),("#",'_'),), )

tm.addTrans('e5five',   ("e", '#',),  'e5fiv', (("e", 'L'),("#",'_'),), )
tm.addTrans('e5fiv',    ("v", '#',),  'e5fi', (("v", 'L'),("#",'_'),), )
tm.addTrans('e5fi',     ("i", '#',),  'e5f', (("i", 'L'),("#",'_'),), )
tm.addTrans('e5f',      ("f", '#',),  'c6', (("f", '_'),("#",'_'),), )

#check six
for i in atoz+numbers:
    if i == "s":
        tm.addTrans('c6', (i, '#',), 'c6s', ((i, 'R'),('#','_'),), )
        continue
    tm.addTrans('c6', (i, '#',), 'c7', ((i, '_'),('#','_'),), )
for i in atoz+numbers:
    if i == "i":
        tm.addTrans('c6s', (i, '#',), 'c6si', ((i, 'R'),('#','_'),), )
        continue
    tm.addTrans('c6s', (i, '#',), 'c7', ((i, 'L'),('#','_'),), )
for i in atoz+numbers:
    if i == "x":
        tm.addTrans('c6si', (i, '#',), 'd6si', ((i, 'L'),('#','_'),), )
        continue
    tm.addTrans('c6si', (i, '#',), 'e6si', ((i, 'L'),('#','_'),), )
tm.addTrans('d6six',   ("x", '#',),  'd6si', (("x", 'L'),("#",'_'),), )
tm.addTrans('d6si',    ("i", '#',),  'd6s', (("i", 'L'),("#",'_'),), )
tm.addTrans('d6s',     ("s", '#',),  'c1', (("6", 'R'),("#",'_'),), )

tm.addTrans('e6six',   ("x", '#',),  'e6si', (("x", 'L'),("#",'_'),), )
tm.addTrans('e6si',    ("i", '#',),  'e6s', (("i", 'L'),("#",'_'),), )
tm.addTrans('e6s',     ("s", '#',),  'c7', (("s", '_'),("#",'_'),), )

#check seven
for i in atoz+numbers:
    if i == "s":
        tm.addTrans('c7', (i, '#',), 'c7s', ((i, 'R'),('#','_'),), )
        continue
    tm.addTrans('c7', (i, '#',), 'c8', ((i, '_'),('#','_'),), )
for i in atoz+numbers:
    if i == "e":
        tm.addTrans('c7s', (i, '#',), 'c7se', ((i, 'R'),('#','_'),), )
        continue
    tm.addTrans('c7s', (i, '#',), 'c8', ((i, 'L'),('#','_'),), )
for i in atoz+numbers:
    if i == "v":
        tm.addTrans('c7se', (i, '#',), 'c7sev', ((i, 'R'),('#','_'),), )
        continue
    tm.addTrans('c7se', (i, '#',), 'e7se', ((i, 'L'),('#','_'),), )
for i in atoz+numbers:
    if i == "e":
        tm.addTrans('c7sev', (i, '#',), 'c7seve', ((i, 'R'),('#','_'),), )
        continue
    tm.addTrans('c7sev', (i, '#',), 'e7sev', ((i, 'L'),('#','_'),), )
for i in atoz+numbers:
    if i == "n":
        tm.addTrans('c7seve', (i, '#',), 'd7seve', ((i, 'L'),('#','_'),), )
        continue
    tm.addTrans('c7seve', (i, '#',), 'e7seve', ((i, 'L'),('#','_'),), )
tm.addTrans('d7seven',   ("n", '#',),  'd7seve', (("n", 'L'),("#",'_'),), )
tm.addTrans('d7seve',    ("e", '#',),  'd7sev', (("e", 'L'),("#",'_'),), )
tm.addTrans('d7sev',     ("v", '#',),  'd7se', (("v", 'L'),("#",'_'),), )
tm.addTrans('d7se',      ("e", '#',),  'd7s', (("e", 'L'),("#",'_'),), )
tm.addTrans('d7s',       ("s", '#',),  'c1', (("7", 'R'),("#",'_'),), )

tm.addTrans('e7seven',   ("n", '#',),  'e7seve', (("n", 'L'),("#",'_'),), )
tm.addTrans('e7seve',    ("e", '#',),  'e7sev', (("e", 'L'),("#",'_'),), )
tm.addTrans('e7sev',     ("v", '#',),  'e7se', (("v", 'L'),("#",'_'),), )
tm.addTrans('e7se',      ("e", '#',),  'e7s', (("e", 'L'),("#",'_'),), )
tm.addTrans('e7s',       ("s", '#',),  'c8', (("s", '_'),("#",'_'),), )
#check eight
for i in atoz+numbers:
    if i == "e":
        tm.addTrans('c8', (i, '#',), 'c8e', ((i, 'R'),('#','_'),), )
        continue
    tm.addTrans('c8', (i, '#',), 'c9', ((i, '_'),('#','_'),), )
for i in atoz+numbers:
    if i == "i":
        tm.addTrans('c8e', (i, '#',), 'c8ei', ((i, 'R'),('#','_'),), )
        continue
    tm.addTrans('c8e', (i, '#',), 'c9', ((i, 'L'),('#','_'),), )
for i in atoz+numbers:
    if i == "g":
        tm.addTrans('c8ei', (i, '#',), 'c8eig', ((i, 'R'),('#','_'),), )
        continue
    tm.addTrans('c8ei', (i, '#',), 'e8ei', ((i, 'L'),('#','_'),), )
for i in atoz+numbers:
    if i == "h":
        tm.addTrans('c8eig', (i, '#',), 'c8eigh', ((i, 'R'),('#','_'),), )
        continue
    tm.addTrans('c8eig', (i, '#',), 'e8eig', ((i, 'L'),('#','_'),), )
for i in atoz+numbers:
    if i == "t":
        tm.addTrans('c8eigh', (i, '#',), 'd8eigh', ((i, 'L'),('#','_'),), )
        continue
    tm.addTrans('c8eigh', (i, '#',), 'e8eigh', ((i, 'L'),('#','_'),), )

tm.addTrans('d8eight',   ("t", '#',),  'd8eigh', (("t", 'L'),("#",'_'),), )
tm.addTrans('d8eigh',    ("h", '#',),  'd8eig', (("h", 'L'),("#",'_'),), )
tm.addTrans('d8eig',     ("g", '#',),  'd8ei', (("g", 'L'),("#",'_'),), )
tm.addTrans('d8ei',      ("i", '#',),  'd8e', (("i", 'L'),("#",'_'),), )
tm.addTrans('d8e',       ("e", '#',),  'c1', (("8", 'R'),("#",'_'),), )

tm.addTrans('e8eight',   ("t", '#',),  'e8eigh', (("t", 'L'),("#",'_'),), )
tm.addTrans('e8eigh',    ("h", '#',),  'e8eig', (("h", 'L'),("#",'_'),), )
tm.addTrans('e8eig',     ("g", '#',),  'e8ei', (("g", 'L'),("#",'_'),), )
tm.addTrans('e8ei',      ("i", '#',),  'e8e', (("i", 'L'),("#",'_'),), )
tm.addTrans('e8e',       ("e", '#',),  'c9', (("e", '_'),("#",'_'),), )
#check nine
for i in atoz+numbers:
    if i == "n":
        tm.addTrans('c9', (i, '#',), 'c9n', ((i, 'R'),('#','_'),), )
        continue
    tm.addTrans('c9', (i, '#',), 'c10', ((i, '_'),('#','_'),), )
for i in atoz+numbers:
    if i == "i":
        tm.addTrans('c9n', (i, '#',), 'c9ni', ((i, 'R'),('#','_'),), )
        continue
    tm.addTrans('c9n', (i, '#',), 'c10', ((i, 'L'),('#','_'),), )
for i in atoz+numbers:
    if i == "n":
        tm.addTrans('c9ni', (i, '#',), 'c9nin', ((i, 'R'),('#','_'),), )
        continue
    tm.addTrans('c9ni', (i, '#',), 'e9ni', ((i, 'L'),('#','_'),), )
for i in atoz+numbers:
    if i == "e":
        tm.addTrans('c9nin', (i, '#',), 'd9nin', ((i, 'L'),('#','_'),), )
        continue
    tm.addTrans('c9nin', (i, '#',), 'e9nin', ((i, 'L'),('#','_'),), )

tm.addTrans('d9nine',   ("e", '#',),  'd9nin', (("e", 'L'),("#",'_'),), )
tm.addTrans('d9nin',    ("n", '#',),  'd9ni', (("n", 'L'),("#",'_'),), )
tm.addTrans('d9ni',     ("i", '#',),  'd9n', (("i", 'L'),("#",'_'),), )
tm.addTrans('d9n',      ("n", '#',),  'c1', (("9", 'R'),("#",'_'),), )

tm.addTrans('e9nine',   ("e", '#',),  'e9nin', (("e", 'L'),("#",'_'),), )
tm.addTrans('e9nin',    ("n", '#',),  'e9ni', (("n", 'L'),("#",'_'),), )
tm.addTrans('e9ni',     ("i", '#',),  'e9n', (("i", 'L'),("#",'_'),), )
tm.addTrans('e9n',      ("n", '#',),  'c10', (("n", '_'),("#",'_'),), )
for i in atoz+numbers:
    tm.addTrans('c10', (i, '#',), 'c1', ((i, 'R'),('#','_'),), )

every_special_state = ["c10", "c1","d1","e1", "c1o", "d1o", "e1o","c1on", "d1on", "e1on","c1one", "d1one", "e1one"]
every_special_state+= ["c2","d2","e2", "c2t","d2t","e2t", "c2tw","d2tw","e2tw", "c2two","d2two","e2two" ]
every_special_state+= ["c3","d3","e3", "c3t","d3t","e3t", "c3th","d3th","e3th", "c3thr","d3thr","e3thr", "c3thre","d3thre","e3thre", "c3three","d3three","e3three" ]
every_special_state+= ["c4","d4","e4", "c4f","d4f","e4f", "c4fo","d4fo","e4fo", "c4fou","d4fou","e4fou", "c4four","d4four","e4four" ]
every_special_state+= ["c5","d5","e5", "c5f","d5f","e5f", "c5fi","d5fi","e5fi", "c5fiv","d5fiv","e5fiv", "c5five","d5five","e5five" ]
every_special_state+= ["c6","d6","e6", "c6s","d6s","e6s", "c6si","d6si","e6si", "c6six","d6six","e6six" ]
every_special_state+= ["c7","d7","e7", "c7s","d7s","e7s", "c7se","d7se","e7se", "c7sev","d7sev","e7sev", "c7seve","d7seve","e7seve", "c7seven","d7seven","e7seven" ]
every_special_state+= ["c8","d8","e8", "c8e","d8e","e8e", "c8ei","d8ei","e8ei", "c8eig","d8eig","e8eig", "c8eigh","d8eigh","e8eigh", "c8eight","d8eight","e8eight" ]
every_special_state+= ["c9","d9","e9", "c9n","d9n","e9n", "c9ni","d9ni","e9ni", "c9nin","d9nin","e9nin", "c9nine","d9nine","e9nine" ]

for q in every_special_state:
    tm.addTrans(q, ("$", '#',), 'c1', (("$", 'R'),("#",'_')), )
    tm.addTrans(q, ("#", '#',), 'k1', (("#", 'L'),("#",'_')), )

for i in atoz+numbers+"$":
    tm.addTrans('k1', (i, '#',), 'k1', ((i, 'L'),("#",'_')), )
tm.addTrans('k1', ("#", '#',), 'qi', (("#", 'R'),("#",'_')), )
###


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
tm.run_det(1000000)
print(tm)
answer = tm.tapes[1].symbols
print("".join(answer).replace("#","")[1:])

#print(len(tm.trans.keys()))