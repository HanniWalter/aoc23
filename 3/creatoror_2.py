
from automata import Automata
from automata import state_number_encoder



def create_pattern(input, patternfilename, refAutomata):
    outputlines = []
    with open(input, 'r') as f:
        lines = f.readlines()

    outputlines.append("x= " + str(len(lines[0]))+ ", y= " + str(len(lines)) + ", rule = " + refAutomata.name)

    pattern = ""
    for line in lines:
        line = line.strip()
        for char in line:
            if char in "0123456789":
                char = char+"_d"
            if char not in refAutomata.state_number:
                print("ERROR: "+ char +" not in states")
                exit()
            charnumber = refAutomata.state_number[char]
            charchar = state_number_encoder(charnumber)
            pattern+=charchar
        pattern+="$"
    pattern = pattern[:-1] + "!"
    outputlines.append(pattern)


    #write to file:
    with open("Rules/aoc3/" + patternfilename + ".rle", 'w') as f:
        for line in outputlines:
            f.write(line + '\n')

def main():
    rulename = "aoc3_2"

    A = Automata(rulename)
    A.add_state(".", [50,50,50], pic = None)    
    A.add_state("0", [0,30,0], pic = "0")
    A.add_state("1", [0,50,0], pic = "1")
    A.add_state("2", [0,70,0], pic = "2")
    A.add_state("3", [0,90,0], pic = "3")
    A.add_state("4", [0,110,0], pic = "4")
    A.add_state("5", [0,130,0], pic = "5")
    A.add_state("6", [0,150,0], pic = "6")
    A.add_state("7", [0,170,0], pic = "7")
    A.add_state("8", [0,190,0], pic = "8")
    A.add_state("9", [0,210,0], pic = "9")

    A.add_state("0_d", [30,30,0], pic = "0")
    A.add_state("1_d", [50,50,0], pic = "1")
    A.add_state("2_d", [70,70,0], pic = "2")
    A.add_state("3_d", [90,90,0], pic = "3")
    A.add_state("4_d", [110,110,0], pic = "4")
    A.add_state("5_d", [130,130,0], pic = "5")
    A.add_state("6_d", [150,150,0], pic = "6")
    A.add_state("7_d", [170,170,0], pic = "7")
    A.add_state("8_d", [190,190,0], pic = "8")
    A.add_state("9_d", [210,210,0], pic = "9")

    A.add_state("0_c", [0, 30, 30], pic="0")
    A.add_state("1_c", [0, 30, 30], pic="1")
    A.add_state("2_c", [0, 30, 30], pic="2")
    A.add_state("3_c", [0, 30, 30], pic="3")
    A.add_state("4_c", [0, 30, 30], pic="4")
    A.add_state("5_c", [0, 30, 30], pic="5")
    A.add_state("6_c", [0, 30, 30], pic="6")
    A.add_state("7_c", [0, 30, 30], pic="7")
    A.add_state("8_c", [0, 30, 30], pic="8")
    A.add_state("9_c", [0, 30, 30], pic="9")

    A.add_state("0_b", [0, 30, 30], pic="0")
    A.add_state("1_b", [0, 30, 30], pic="1")
    A.add_state("2_b", [0, 30, 30], pic="2")
    A.add_state("3_b", [0, 30, 30], pic="3")
    A.add_state("4_b", [0, 30, 30], pic="4")
    A.add_state("5_b", [0, 30, 30], pic="5")
    A.add_state("6_b", [0, 30, 30], pic="6")
    A.add_state("7_b", [0, 30, 30], pic="7")
    A.add_state("8_b", [0, 30, 30], pic="8")
    A.add_state("9_b", [0, 30, 30], pic="9")
    A.add_state("._b", [255,255,255], pic=".")
    c_num = [str(x)+"_c" for x in range(0,10)]
    d_num = [str(x)+"_d" for x in range(0,10)]
    b = [str(x)+"_b" for x in range(0,10) ] + ["._b"]

    A.add_var("c_num", c_num)
    A.add_var("c_num_2", c_num)
    A.add_var("d_num", d_num)
    A.add_var("b", b)
    
    A.add_state("*", [255,0,0], pic = "*")
    A.add_state("#", [255,0,0], pic = "#")
    A.add_state("+", [255,0,0], pic = "+")
    A.add_state("$", [255,0,0], pic = "$")
    A.add_state("@", [255,0,0], pic = "*")
    A.add_state("=", [255,0,0], pic = "*")
    A.add_state("%", [255,0,0], pic = "*")
    A.add_state("&", [255,0,0], pic = "*")
    A.add_state("/", [255,0,0], pic = "*")
    A.add_state("-", [255,0,0], pic = "*")

    A.add_state("dead_num", [255,0,255], pic=".")
    A.add_state("dead_symbol", [255,0,255], pic=".")

    #transform when only one number
    A.add_var("empty_1", ["."])
    A.just_transform("*", "dead_symbol")


    A.just_transform("dead_symbol", ".")
    A.just_transform("dead_num", ".")
    A.add_var("plainnumber", ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    A.add_var("fieldvalue_start", ["*", "#", "+", "$", "@","=","%","&","/","-", ".", "0_d", "1_d", "2_d", "3_d", "4_d", "5_d", "6_d", "7_d", "8_d", "9_d"])
    A.add_var("fieldvalue", ["*", "#", "+", "$", "@","=","%","&","/","-", ".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    A.add_state("boundary1", [30,30,30], pic=".")
    A.add_state("boundary2", [70,70,70], pic=".")
    A.add_state("wire", [160,160,20], pic=".")
    A.add_state("temp1", [255,255,255], pic=".")
    A.add_state("temp2", [255,255,255], pic=".")
    A.add_state("temp3", [255,255,255], pic=".")
    A.add_state("temp2_2", [255,255,255], pic=".")
    
    for x in range(0,10):
        d_num = str(x)+"_d"
        c_num = str(x)+"_c"
        
        A.tranform_when_neighbour(d_num, c_num, "dead_symbol")   
        A.transform_when_E(d_num, c_num, "c_num")
        A.transform_when_W(d_num, c_num, "c_num")

    A.transform_when_W("EMPTY", "temp1", "fieldvalue_start")
    A.transform_when_W("EMPTY", "temp2", "temp1")
    A.transform_when_W("EMPTY", "temp2_2", "temp2")
    A.tranform_when_neighbour("EMPTY", "boundary1", "fieldvalue_start")
    A.tranform_when_neighbour("EMPTY", "boundary1", "temp1")
    A.tranform_when_neighbour("EMPTY", "boundary1", "temp2")
    A.tranform_when_neighbour("EMPTY", "boundary1", "temp2_2")
    A.tranform_when_neighbour("EMPTY", "wire", "boundary1")
    A.tranform_when_neighbour("EMPTY", "boundary2", "wire")


    A.add_state("phase1", [0,0,50], pic=".")
    A.transform_when_N_W("wire", "phase1", "wire", "wire")
    
    
    A.add_state("phase2", [0,0,50], pic=".")
    A.just_transform("phase1", "phase2")
    A.add_state("electron", [255,190,30], pic=".")
    A.add_state("electron_tail", [255,190,30], pic=".")
    A.transform_when_S("wire", "electron","phase1")
    A.transform_when_close_neighbour("wire", "electron", "electron")
    A.just_transform("electron", "electron_tail")
    A.just_transform("electron_tail", "wire")

    A.transform_when_N_S("boundary1", "temp3", "temp1", "electron")
    A.just_transform("temp3", "boundary1")

    A.transform_when_S("temp1", ".", "temp3")
    A.transform_when_S("temp1", ".", ".")

    A.transform_when_W("temp2", ".", ".")
    A.transform_when_W("temp2_2", "0_c", ".")

    A.add_state("phase2_a", [0,255,255], pic=".")
    A.add_state("phase2_b", [0,255,255], pic=".")
    
    A.add_state("Y", [255,255,255] ,pic=".")
    A.add_state("._Y", [255,255,255] ,pic=".")
    A.tranform_when_neighbour("boundary1", "Y", "phase2_a")
    A.just_transform("Y", "boundary1")
    A.tranform_when_neighbour("0_c", "0_b","Y")
    for x in range(0,10):
        b_num = str(x)+"_b"
        c_num = str(x)+"_c"
        d_num = str(x)+"_d"
        e_num = str(x)+"_e"
        num = str(x)

        A.transform_when_S(c_num,b_num,"b")
        A.transform_when_S(d_num,"._b","b")
        A.transform_when_E(c_num,b_num,"b")
        A.transform_when_E(d_num,"._b","b")
        A.just_transform(b_num,num)

    A.transform_when_S(".","._b","b")
    A.transform_when_E(".","._b","b")
    A.just_transform("._b",".")
    




          
    A.add_state("phase3" , [0,0,90], pic=".")
    A.transform_when_W("phase2", "phase2_a", "electron")
    A.just_transform("phase2_a", "phase2_b")

    A.transform_when_S("wire", "electron", "phase2_a")
    A.transform_when_W("phase2_b", "phase3", "electron")
    
    # horizontal add
    #positrons and markers

    A.add_state("phase4" , [0,0,90], pic=".")
    A.add_state("positron" , [0,0,255], pic=".")
    A.add_state("positron2" , [0,0,255], pic=".")
    A.transform_when_S("wire", "positron","phase3")
    A.transform_when_S("wire", "positron","positron")
    A.just_transform("positron", "electron_tail")
    A.just_transform("phase3", "phase4")

    A.add_state("marker_start_add" , [255,0,0], pic=".")
    A.transform_when_E_W("boundary1","marker_start_add", "positron", "fieldvalue")

    #here make the signal take n^2 time to get over the top


    #here do the adding stuff
    A.just_transform("marker_start_add", "boundary1")

    willadd = [str(x) + "_willadd" for x in range(0,10)]


    A.add_state("._willadd" , [255,255,255], pic=".")
    A.transform_when_W("._willadd", ".", "plainnumber")
    A.transform_when_W("._willadd", ".", ".")
    A.add_state("last_digit", [255,0,0], pic=".")
    for x in range(0,10):
        plain = str(x)
        special = plain + "_willadd"
        A.add_state(special, [255,255,255], pic=plain)        
    
    A.add_var("willadd", willadd)
    A.add_state
    for x in range(0,10):
        plain = str(x)
        special = plain + "_willadd"

        A.just_transform(special, plain)
        A.transform_when_E(plain, special, "marker_start_add")
        A.transform_when_E(plain, special, "willadd")    
        A.transform_when_E(".", "._willadd", "willadd")    
    A.transform_when_E_W(".", "._willadd", "._willadd", ".")
    #test
    #A.transform_when_E_W(".", "._willadd", "._willadd", "plainnumber")
    
    for x in range(0,10):
        plain = str(x)
        special = plain + "_willadd"
        dotcarry = "._carry_" + plain
        special = "._carry_" + plain + "_kill"

        A.add_state(dotcarry, [255,255,255], pic=".")
        A.add_state(special, [255,0,0], pic=".")
        A.just_transform(special, dotcarry)
        A.transform_when_E(dotcarry, ".", ".")
        A.transform_when_E_W(".", special, "._willadd", plain)
        #this is the one that needs to be fixed
        A.transform_when_E_W(plain, ".", special, "plainnumber")
        A.transform_when_E_W(plain, "last_digit", special, ".")
        A.transform_when_E_W(plain, "last_digit", special, "boundary1")
        
        A.transform_when_W(".", dotcarry, dotcarry)

    dotcarry = ["._carry_" + str(x) for x in range(0,10)]
    A.add_var("dotcarry", dotcarry)
    A.transform_when_E("dotcarry", "plainnumber", "plainnumber")
    A.transform_when_W("plainnumber", "dotcarry", "dotcarry")

    for x in range(0,10):
        yellow_num = str(x) + "_yellow"
        red_num = str(x) + "_red"
        orange_num = str(x) + "_orange"
        A.add_state(yellow_num, [255,255,0], pic=str(x))
        A.add_state(red_num, [255,0,0], pic=str(x))
        A.add_state(orange_num, [255,100,0], pic=str(x))
    A.add_state("1_blue", [0,0,255], pic="1")
    A.add_state("0_blue", [0,0,100], pic="0")
    yellow_num = [str(x) + "_yellow" for x in range(0,10)]
    red_num = [str(x) + "_red" for x in range(0,10)]
    orange_num = [str(x) + "_orange" for x in range(0,10)]
    A.add_var("yellow_num", yellow_num)
    A.add_var("red_num", red_num)
    A.add_var("orange_num", orange_num)

    
    for x in range(0,10):
        plain = str(x)
        for y in range (0, 10):
            dotcarry = "._carry_" + str(y)

            sum = str((y + x) % 10) 
            needs_carry = (y + x) >= 10
            if needs_carry:
                A.transform_when_E_W(dotcarry, sum+"_red", "boundary1", plain)
                A.transform_when_E_W(dotcarry, sum+"_red", "orange_num", plain)
            else:
                A.transform_when_E_W(dotcarry, sum+"_yellow", "orange_num", plain)
                A.transform_when_E_W(dotcarry, sum+"_yellow", "boundary1", plain)
        A.just_transform(plain+"_red", plain+"_yellow")        
        A.just_transform(plain+"_yellow", plain+"_orange")       
        #plain_1 = str(x+1)
        A.transform_when_E(plain,"1_blue","red_num")
        for y in range (0,2):
            blue = str(y) + "_blue"
            sum = str((y + x) % 10)
            needs_carry = (y + x) >= 10
            A.transform_when_W(blue, sum, plain)
            if needs_carry:
                A.transform_when_E(plain, "1_blue", blue)
            else:
                A.transform_when_E(plain, "0_blue", blue)

        A.transform_when_E(plain,"1_blue","red_num")

    
    A.transform_when_E("plainnumber", "0_blue", "yellow_num")

        # here add blues right
#    for x in range(0,10):
#        plain = str(x)
#        for y in range (0, 2):
#            blue = str(y) + "_blue"
#            sum = str((y + x) % 10)
#            needs_carry = (y + x) >= 10
#            A.transform_when_W(blue, sum, plain)
#            if needs_carry:
#                A.transform_when_E(plain, "1_blue", blue)
#            else:
#                A.transform_when_E(plain, "0_blue", blue)
    
    A.transform_when_E(".", "._willadd", "0_blue")
    A.transform_when_E(".", "._willadd", "1_blue")
    A.transform_when_W("0_blue", "0", ".")
    A.transform_when_W("1_blue", "1", ".")

    A.add_state("._heal", [0,255,255], pic=".")
    A.just_transform("._heal", ".")
    for x in range(0,10):
        heal = str(x) + "_heal"
        A.add_state(heal, [0,255,255], pic=str(x))

    heal = [str(x) + "_heal" for x in range(0,10)]
    A.add_var("heal_num", heal)
    A.transform_when_E_W(".", "._heal", "._willadd", "last_digit")
    #test
    A.transform_when_W("._willadd", "._heal","last_digit")
    A.transform_when_E("last_digit", ".", "._heal")
    A.transform_when_E("last_digit", ".", "heal_num")
    
    A.transform_when_W(".", "._heal", "._heal")
    A.transform_when_W(".", "._heal", "heal_num")


    for x in range(0,10):
        A.just_transform(str(x)+"_heal", str(x))
        plain = str(x)
        heal = str(x) + "_heal"
        orange = str(x) + "_orange"
        A.just_transform(heal, plain)
        A.transform_when_W(plain, heal, "._heal")
        A.transform_when_W(plain, heal, "heal_num")
        A.transform_when_W(orange, heal, "._heal")
        A.transform_when_W(orange, heal, "heal_num")
    A.transform_when_W("boundary1", "marker_start_add", "._heal")
    A.transform_when_W("boundary1", "marker_start_add", "heal_num")

    # fill with "0"
    A.add_state("add_0", [0,255,255], pic="0")
    A.transform_when_E_W(".", "add_0", "._willadd", "boundary1")
    A.just_transform("add_0", "0")
    A.transform_when_W(".", "add_0", "add_0")



    # signal for h add
    A.add_state("phase5" , [0,0,120], pic=".")
    A.add_state("phase5_A" , [0,0,120], pic=".")
    A.add_state("phase6" , [0,0,120], pic=".")
    A.add_state("phase6_A" , [0,0,120], pic=".")
    A.add_state("phase7" , [0,0,200], pic=".")
    A.add_state("myon_A", [255,0,0], pic=".")
    A.add_state("myon_B", [255,0,0], pic=".")
    A.add_state("myon_C", [255,0,0], pic=".")
    A.add_state("positron_2", [0,0,255], pic=".")

    A.transform_when_E("wire", "electron", "positron")   
    A.transform_when_W("phase4", "phase5", "electron")
    A.just_transform("phase5", "phase5_A")
    A.just_transform("phase5_A", "phase6")
    A.transform_when_S("wire", "electron", "phase5_A")
    A.transform_when_E("wire", "myon_A", "phase5_A")
    A.transform_when_W("myon_A", "myon_B", "electron")
    A.just_transform("myon_B", "myon_C")
    A.just_transform("myon_C", "electron")
    A.transform_when_W("phase6", "phase6_A", "electron")
    A.just_transform("phase6_A", "phase6")
    A.transform_when_S("wire", "electron", "phase6_A")

    A.transform_when_N_W("myon_A", "positron_2", "electron", "boundary2")
    A.transform_when_W("wire","positron_2", "positron_2")
    A.just_transform("positron_2", "wire")
    A.transform_when_W("phase6", "phase7", "positron_2")


    A.transform_when_E("wire", "myon_A", "myon_C")
    

    #V add
    #clock for V add
    A.add_state("positron_3_A" , [0,0,255], pic=".")
    A.add_state("positron_3_B" , [0,0,255], pic=".")
    A.add_state("positron_4", [0,0,150], pic=".")
    A.add_state("phase8" , [0,0,120], pic=".")
    A.add_state("phase9" , [0,0,120], pic=".")
    A.add_state("phase10" , [0,0,120], pic=".")
    A.add_state("phase11" , [0,0,120], pic=".")
    A.add_state("phase12" , [0,0,120], pic=".")
    A.transform_when_S("wire", "positron_3_A", "phase7")
    A.transform_when_S("wire", "positron_3_A", "positron_3_A")
    A.transform_when_N("positron_3_A", "positron_3_B", "boundary2")
    A.just_transform("positron_3_A", "wire")
    A.just_transform("phase7", "phase8")
    A.just_transform("phase8", "phase9")
    A.just_transform("phase9", "phase10")
    A.just_transform("phase10", "phase11")
    A.just_transform("phase11", "phase12")
    A.just_transform("phase12", "phase8")
    A.transform_when_S("wire", "positron_4", "phase8")
    A.transform_when_N("positron_4", "positron_3_B", "positron_3_B")
    A.transform_when_S("wire", "positron_4", "positron_4")
    A.just_transform("positron_4", "wire")
    A.transform_when_S("positron_3_B", "wire", "positron_3_B")
    A.add_state("X", [255,0,0], pic=".")
    A.add_state("X_2", [255,255,0], pic=".")
    A.add_state("X_3", [255,255,0], pic=".")
    A.add_state("X_4", [255,255,0], pic=".")
    A.transform_when_E("boundary1", "X", "positron_3_B")
    A.just_transform("X", "X_2")
    A.just_transform("X_2", "X_3")
    A.just_transform("X_3", "X_4")
    A.just_transform("X_4", "boundary1")
    
    for x in range(0,10):
        plain = str(x)
        Add = str(x) + "_Add"
        no_carry = str(x) + "_no_carry"
        carry = str(x) + "_carry"
        A.add_state(Add, [0,0,255], pic=plain)
        A.add_state(no_carry, [0,0,255], pic=plain)
        A.add_state(carry, [0,0,255], pic=plain)

    add = [str(x) + "_Add" for x in range(0,10)]
    no_carry = [str(x) + "_no_carry" for x in range(0,10)]
    carry = [str(x) + "_carry" for x in range(0,10)]
    A.add_var("add", add)
    A.add_var("no_carry", no_carry)
    A.add_var("carry", carry)
    for x in range(0,10):
        plain = str(x)
        add = str(x) + "_Add"
        no_carry = str(x) + "_no_carry"
        carry = str(x) + "_carry"

        #A.transform_when_N_E(plain, plain, "boundary1", "X")
        A.transform_when_N_E(plain, add, "plainnumber", "X")

        for y in range(0,10):
            top = str(y)
            sum = str((y + x) % 10)
            sum_1 = str((y + x + 1) % 10)
            needs_carry = (y + x) >= 10
            needs_carry_1 = (y + x + 1) >= 10
            if needs_carry:
                result = sum + "_carry"
                A.transform_when_N_E(add, result, top, "no_carry")
                A.transform_when_N_E(add, result, top, "X_2")
            else:
                result = sum + "_no_carry"
                A.transform_when_N_E(add, result, top, "no_carry")
                A.transform_when_N_E(add, result, top, "X_2")
            if needs_carry_1:
                result = sum_1 + "_carry"
                A.transform_when_N_E(add, result, top, "carry")
            else:
                result = sum_1 + "_no_carry"
                A.transform_when_N_E(add, result, top, "carry")
        A.just_transform(carry, plain)
        A.just_transform(no_carry, plain)
        A.transform_when_E(plain, add, "add")


    
    #finish

    A.create_rule("Rules/" +rulename+".rule")
    A.print_states()
    input = "Rules/aoc3/test_input.txt"
    patternfilename = "aoc3_test"
    create_pattern(input, patternfilename,A)

if __name__ == '__main__':
    main()