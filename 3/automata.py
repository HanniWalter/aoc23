import itertools

def state_number_encoder(num):
    if num == 0:
        return "."
    # when num is in 1..24 return A..X
    if num < 25:
        return chr(ord('A') + num - 1)
    if num < 255:
        firstletter = chr(ord('p') + (num-1)//24 - 1)
        secondletter = chr(ord('A') + (num-1)%24)
        return firstletter + secondletter
    else:
        print("ERROR: state number too high")
    exit()

picNone = """
.......
.......
.......
.......
.......
.......
.......
"""
pic1 = """
.....A.
.....A.
.....A.
.....A.
.....A.
.....A.
.....A.
"""
pic2 = """
.AAAAA.
.....A.
.....A.
.AAAAA.
.A.....
.A.....
.AAAAA.
"""
pic3 = """
.AAAAA.
.....A.
.....A.
.AAAAA.
.....A.
.....A.
.AAAAA.
"""
pic4 = """
.A...A.
.A...A.
.A...A.
.AAAAA.
.....A.
.....A.
.....A.
"""
pic5 = """
.AAAAA.
.A.....
.A.....
.AAAAA.
.....A.
.....A.
.AAAAA.
"""
pic6 = """
.AAAAA.
.A.....
.A.....
.AAAAA.
.A...A.
.A...A.
.AAAAA.
"""
pic7 = """
.AAAAA.
.....A.
.....A.
.....A.
.....A.
.....A.
.....A.
"""
pic8 = """
.AAAAA.
.A...A.
.A...A.
.AAAAA.
.A...A.
.A...A.
.AAAAA.
"""
pic9 = """
.AAAAA.
.A...A.
.A...A.
.AAAAA.
.....A.
.....A.
.AAAAA.
"""
pic0 = """
.AAAAA.
.A...A.
.A...A.
.A...A.
.A...A.
.A...A.
.AAAAA.
"""
picStar = """
.......
.A...A.
..A.A..
...A...
..A.A..
.A...A.
.......
"""

picPlus = """
.......
...A...
...A...
.AAAAA.
...A...
...A...
.......
"""

picHash = """
.......
.A.A.A.
AAAAAAA
.A.A.A.
AAAAAAA
.A.A.A.
.......
"""

picDollar = """
...AAA.
..A....
.AAAAA.
...A...
.AAAAA.
....A..
.AAA...
"""



picture = {
    "0": pic0,
    "1": pic1,
    "2": pic2,
    "3": pic3,
    "4": pic4,
    "5": pic5,
    "6": pic6,
    "7": pic7,
    "8": pic8,
    "9": pic9,
    "*": picStar,
    "+": picPlus,
    "#": picHash,
    "$": picDollar,
    ".": picNone
}

def colorcode(r ,g ,b):
    colorcode = "#"
    r1 = hex(r)[2:].upper()
    if len(r1) == 1:
        r1 = "0" + r1
    g1 = hex(g)[2:].upper()
    if len(g1) == 1:
        g1 = "0" + g1
    b1 = hex(b)[2:].upper()
    if len(b1) == 1:
        b1 = "0" + b1
    colorcode += r1 + g1 + b1
    return colorcode

class Automata():
    def __init__(self, name):
        self.name = name
        self.states = []
        self.state_color = {}
        self.state_number = {}
        self.state_pic = {}
        self.transitions = []
        self.var = {}
        self.all_colors = []
        self.colors_char = {}
        self.colors_char_from_state1 = {}
        self.colors_char_from_state2 = {}
        self.add_state("EMPTY")
    
    def print_states(self):
        for i, state in enumerate(self.states):
            print(str(i) + " " + state)

    def add_state(self, state, color = [0,0,0], color2 = [0,0,0], pic = None):
        if pic == None:
            self.state_pic[state] = "."
        else:
            self.state_pic[state] = pic
        self.states.append(state)
        self.state_number[state] = len(self.states)-1
        self.state_color[self.state_number[state]] = color
        #255 255 255 to FF FF FF
        cc = self.add_color(color[0], color[1], color[2])
        i = 0
        for color in self.all_colors:
            if color == cc:
                break
            i+=1

            self.colors_char_from_state1[state] = self.colors_char[cc]

        cc = self.add_color(color2[0], color2[1], color2[2])
        i = 0
        for color in self.all_colors:
            if color == cc:
                break
            i+=1
        self.colors_char_from_state2[state] = self.colors_char[cc]
    
    def add_color(self, r, g, b):
        cc = colorcode(r,g,b)
        if cc not in self.all_colors:
            next_char = state_number_encoder(len(self.all_colors))
            self.colors_char[cc] = next_char
            self.all_colors.append(cc)
        return cc

    def add_var(self, var, values):
        self.var[var] = [self.state_number[value] for value in values]

    def just_transform(self, state1, state2):
        if state1 in self.states:
            state1 = self.state_number[state1]
        if state2 in self.states:
            state2 = self.state_number[state2]
            
        self.transitions.append([state1, "any0", "any1", "any2", "any3", "any4", "any5", "any6", "any7", state2])

    def tranform_when_neighbour(self, state1, state2, neighbour):
        if state1 in self.states:
            state1 = self.state_number[state1]
        if state2 in self.states:
            state2 = self.state_number[state2]
        if neighbour in self.states:
            neighbour = self.state_number[neighbour]
        
        self.transitions.append([state1, "any0", "any1", "any2", "any3", "any4", "any5", "any6", neighbour, state2])
        self.transitions.append([state1, "any0", "any1", "any2", "any3", "any4", "any5", neighbour, "any7", state2])
        self.transitions.append([state1, "any0", "any1", "any2", "any3", "any4", neighbour, "any6", "any7", state2])
        self.transitions.append([state1, "any0", "any1", "any2", "any3", neighbour, "any5", "any6", "any7", state2])
        self.transitions.append([state1, "any0", "any1", "any2", neighbour, "any4", "any5", "any6", "any7", state2])
        self.transitions.append([state1, "any0", "any1", neighbour, "any3", "any4", "any5", "any6", "any7", state2])
        self.transitions.append([state1, "any0", neighbour, "any2", "any3", "any4", "any5", "any6", "any7", state2])
        self.transitions.append([state1, neighbour, "any1", "any2", "any3", "any4", "any5", "any6", "any7", state2])

    def transform_when_close_neighbour(self, state1, state2, neighbour):
        if state1 in self.states:
            state1 = self.state_number[state1]
        if state2 in self.states:
            state2 = self.state_number[state2]
        if neighbour in self.states:
            neighbour = self.state_number[neighbour]
        
        self.transitions.append([state1, "any0", "any1", "any2", "any3", "any4", "any5", neighbour, "any7", state2])
        self.transitions.append([state1, "any0", "any1", "any2", "any3", neighbour, "any5", "any6", "any7", state2])
        self.transitions.append([state1, "any0", "any1", neighbour, "any3", "any4", "any5", "any6", "any7", state2])
        self.transitions.append([state1, neighbour, "any1", "any2", "any3", "any4", "any5", "any6", "any7", state2])

    def transform_when_E_W(self, state1, state2, E, W):
        if state1 in self.states:
            state1 = self.state_number[state1]
        if state2 in self.states:
            state2 = self.state_number[state2]
        if E in self.states:
            E = self.state_number[E]
        if W in self.states:
            W = self.state_number[W]
        
        self.transitions.append([state1, "any0", "any1", E, "any3", "any4", "any5", W, "any7", state2])

    def transform_when_N_S(self, state1, state2, N, S):
        if state1 in self.states:
            state1 = self.state_number[state1]
        if state2 in self.states:
            state2 = self.state_number[state2]
        if N in self.states:
            N = self.state_number[N]
        if S in self.states:
            S = self.state_number[S]
        
        self.transitions.append([state1, N, "any1", "any2", "any3", S, "any5", "any6", "any7", state2])
        
    def transform_when_N_E(self, state1, state2, N, E):
        if state1 in self.states:
            state1 = self.state_number[state1]
        if state2 in self.states:
            state2 = self.state_number[state2]
        if N in self.states:
            N = self.state_number[N]
        if E in self.states:
            E = self.state_number[E]
        
        self.transitions.append([state1, N, "any1", E, "any3", "any4", "any5", "any6", "any7", state2])

    def transform_when_N_W(self, state1, state2, N, W):
        if state1 in self.states:
            state1 = self.state_number[state1]
        if state2 in self.states:
            state2 = self.state_number[state2]
        if N in self.states:
            N = self.state_number[N]
        if W in self.states:
            W = self.state_number[W]        
        self.transitions.append([state1, N, "any1", "any2", "any3", "any4", "any5", W, "any7", state2])

    def transform_when_S_E(self, state1, state2, S, E):
        if state1 in self.states:
            state1 = self.state_number[state1]
        if state2 in self.states:
            state2 = self.state_number[state2]
        if S in self.states:
            S = self.state_number[S]
        if E in self.states:
            E = self.state_number[E]
        
        self.transitions.append([state1, "any0", "any1", E, "any3", S, "any5", "any6", "any7", state2])

    def transform_when_S_W(self, state1, state2, S, W):
        if state1 in self.states:
            state1 = self.state_number[state1]
        if state2 in self.states:
            state2 = self.state_number[state2]
        if S in self.states:
            S = self.state_number[S]
        if W in self.states:
            W = self.state_number[W]
        
        self.transitions.append([state1, "any0", "any1", "any2", "any3", S, "any5", W, "any7", state2])
 
    def transform_when_N(self, state1, state2, N):
        if state1 in self.states:
            state1 = self.state_number[state1]
        if state2 in self.states:
            state2 = self.state_number[state2]
        if N in self.states:
            N = self.state_number[N]
        
        self.transitions.append([state1, N, "any1", "any2", "any3", "any4", "any5", "any6", "any7", state2])
    
    def transform_when_E(self, state1, state2, E):
        if state1 in self.states:
            state1 = self.state_number[state1]
        if state2 in self.states:
            state2 = self.state_number[state2]
        if E in self.states:
            E = self.state_number[E]
        
        self.transitions.append([state1, "any0", "any1", E, "any3", "any4", "any5", "any6", "any7", state2])

    
    def transform_when_S(self, state1, state2, S):
        if state1 in self.states:
            state1 = self.state_number[state1]
        if state2 in self.states:
            state2 = self.state_number[state2]
        if S in self.states:
            S = self.state_number[S]
        
        self.transitions.append([state1, "any0", "any1", "any2", "any3", S, "any5", "any6", "any7", state2])

    def transform_when_W(self, state1, state2, W):
        if state1 in self.states:
            state1 = self.state_number[state1]
        if state2 in self.states:
            state2 = self.state_number[state2]
        if W in self.states:
            W = self.state_number[W]
        
        self.transitions.append([state1, "any0", "any1", "any2", "any3", "any4", "any5", W, "any7", state2])

    def create_rule(self, rulefilename):
        for i in range(10):
            self.var["any"+str(i)] = [i for i in range(len(self.states))]

        lines = []
        lines.append("@RULE " + self.name)
        lines.append("@TABLE")
        lines.append("n_states:" + str(len(self.states)))
        lines.append("neighborhood:Moore")
        lines.append("symmetries:none")
        for var in self.var:
            lines.append("var "+ var + "={" + ",".join([str(x) for x in self.var[var] ]) +"}")
        for transition in self.transitions:
            lines.append(",".join([str(x) for x in transition]))

#        for rule in self.rules:
#            lines.append(str(rule[0]) + "," + str(rule[1]) + "," + str(rule[2]) + "," + str(rule[3]) + "," + str(rule[4]) + "," + str(rule[5]) + "," + str(rule[6]) + "," + str(rule[7]) + "," + str(rule[8]) + "," + str(rule[9]))
        

        #Pictures:
        lines.append("@COLORS")
        for i in range(len(self.states)):
            r = str(self.state_color[i][0])
            g = str(self.state_color[i][1])
            b = str(self.state_color[i][2])

            lines.append(str(i) + " " + r + " " + g + " " + b)
        
        #lines.append("@ICONS")
        #lines.append("XPM")
        #lines.append("/* width height num_colors chars_per_pixel */")
        #lines.append('"'+str(7) + " " + str(7*len(self.states)- 7) + " " + str(len(self.all_colors)) + " 1" +'"')
        #lines.append("/* colors */")
        #for color in self.all_colors:
        #    lines.append('"'+self.colors_char[color] + " c " +  color+'"')
        #for i, state in enumerate(self.states):
        #    if i == 0:
        #        continue
        #    
        #    lines.append("/* icon for state " + str(self.state_number[state]) + " */")
        #    pic = picture[self.state_pic[state]].strip()

        #    pic = pic.replace(".", "$")
        #    pic = pic.replace("A", self.colors_char_from_state2[state])
        #    pic = pic.replace("$", self.colors_char_from_state1[state])
        #    for line in pic.split("\n"):
        #        lines.append('"'+line+'"')

        
        #write to file:
        with open(rulefilename, 'w') as f:
            for line in lines:
                f.write(line + '\n')