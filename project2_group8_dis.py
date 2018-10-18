#ISA design for AVS

def disassembler(M,Nlines):
    print("ECE 366 Group 8 Disassembler")
    print("----------------")
	#print the instructions
    Rx = 0
    Ry= 0
    imm = 0
    for i in range(Nlines):

        fetch =M[i]
        print("Machine code: " + M[i])
        if(fetch[0:4] == "0011"): # load imm
            imm= int(fetch[4:8],2)  
            print("loadi "+ str(imm))

        elif(fetch[0:4] == "1000"):#store Rx, Ry 
            Rx= int(fetch[4:6],2)
            Ry= int(fetch[6:8],2)
            print("store R" + str(Rx)+ ", R" + str(Ry))
            
        elif(fetch[0:6] == "000100"):#srl Rx 
            Rx= int(fetch[6:8],2)
            print("srl R" + str(Rx))
            
        elif(fetch[0:4] == "0100"):#addi Rx, imm 
            Rx= int(fetch[4:6],2)
            imm= int(fetch[6:8],2)
            print("addi R" + str(Rx)+ ", " + str(imm))
            
        elif(fetch[0:6] == "010110"):#subi Rx 
            Ry= int(fetch[6:8],2)
            print("subi R" + str(Ry))
            
        elif(fetch[0:6] == "111011"):#bne Rx 
            print("bne R" + str(Rx))
            
        elif(fetch[0:6] == "110001"):#slt Rx 
            Rx= int(fetch[6:8],2)
            print("slt R" + str(Rx))
            
        elif(fetch[0:5] == "00100"):#BezDec imm 
            imm= int(fetch[5:8],2)
            print("bezDec " + str(imm))
            
        elif(fetch[0:4] == "0111"):#xori Rx, imm
            Rx= int(fetch[4:6],2)
            imm= int(fetch[6:8],2)
            print("xori R" + str(Rx)+ ", R" + str(imm))
            
        elif(fetch[0:4] == "0111"):#andi Rx, imm
            Rx= int(fetch[4:6],2)
            imm= int(fetch[6:8],2)
            print("andi" + str(Rx)+ "," + str(imm))
            
        elif(fetch[0:4] == "1010"):#jump 'branch'(imm)
            imm= int(fetch[4:8],2)
            print("jump " + str(imm))
            
        elif(fetch[0:4] == "1001"):#add RX, Ry
            Rx= int(fetch[4:6],2)
            Ry= int(fetch[6:8],2)
            print("add R" + str(Rx)+ ", R" + str(Ry))
            
        elif(fetch[0:4] == "1101"):#sub Rx, Ry
            Rx= int(fetch[4:6],2)
            Ry= int(fetch[6:8],2)
            print("sub R" + str(Rx)+ ", R" + str(Ry))
            
        elif(fetch[0:8] == "10110110"):#subln R4

            print("subln $R4")
            
        elif(fetch[0:8] == "11110000"):#bne R4
            print("bne $R4" )   
            
        elif(fetch[0:8] == "01010101"):# jump ' first branch'
            print("jump 'first branch' ")
            
        elif(fetch[0:8] == "00000000"):#halt 
            Rx= int(fetch[4:6],2)
            Ry= int(fetch[6:8],2)
            print("halt")
            
        elif(fetch[0:6]=="101110"): #load Rx
            Rx= int(fetch[6:8],2)
            print("load R" + str(Rx))
            
        elif(fetch[0:6]=="000001"): #blt4 Rx
            Rx= int(fetch[6:8],2)
            print("blt4 R" + str(Rx))
          
        elif(fetch[0:6] == "110000"): #beq4 Rx
            Rx = int(fetch[6:8],2)
            print("beq R" + str(Rx))
            
        elif(fetch[0:6] == "111110"): #andi5 imm
            imm= int(fetch[6:8],2)
            print("and5i R" + str(imm))
            
        elif(fetch[0:6] == "101111"): #srl5 imm
            imm=int(fetch[6:8]) 
            print("srl5 " + str(imm))
         
        elif(fetch[0:4] == "0110"): #xor Rx, Ry
            Rx =int(fetch[4:6],2)
            Ry =int(fetch[6:8],2)
            print("xor R" + str(Rx) + ",R" + str(Ry))
            
        else:
            print("Instruction set not supported")
        print("----------------")
	
	
#def assembler(I,Nlines):
#def simulator(I,Nsteps,debug_mode,Memory):
def main():
    instr_file = open("P1_Instruction.txt","r")
    data_file = open("project2_group8_p1_bin.txt" ,"r")
    data_file2 = open("project2_group8_p2_bin.txt", "r")
    #we need a file for the data set
    #Nsteps = 3  #How many cycles to run before output
    Nlines = 0   #How may instrs total in input.txt
    Instructions = [] #all instructions will be stored here
    Memory = []
    print( " ECE 366 Group 8")
	#print( " 1 = simulator")
    print( " 2 = disassembler")
    #print( " 3 = assembler")
	
    mode= int(input( "Please enter the mode of Program: "))
    print( "Mode selected: ",end=" ")
    modedis= int(input( "Please enter the which program 1 or 2:  "))
    print( "Mode selected: ", end=" ")
    
    #if(mode== 1):
        #print("Simulator")
    #elif(mode== 2):
       # print( "disassembler")
        #disassembler(Instructions,Nlines)
    #elif(mode== 3):
       # print( "assembler")
	    #assemble(Instructions, Nlines)
    
		
    #for line in instr_file: # Reading in the instructions
    #    if (line == "/n" or line[0] == '#'):  #empty lines, comments ignored
    #       line = line.replace("\n"," ")
    #        Instructions.append(line)             #Copy all instruction into a list
        #Nline+=1
		
    #for line in data_file: # Read in data P1_Machine.txt
     #   if(line== "\n" or line[0] =='#'):
	 #      continue
      #  Memory.append(line)
        #Nlines+=1
    if(mode == 1): #Check whether to use disassembler of assembler or simulator
        #simulator(Instructions,Nsteps,debug_mode,Memory)
        print("assembler")
    elif(mode== 2):
        if (modedis == 1):
            for line in data_file: # Read in data P1_Machine.txt
                if(line== "\n" or line[0] =='#'):
                    continue
                Memory.append(line)
                Nlines+=1
        elif(modedis == 2):
            for line in data_file2: # Read in data P1_Machine.txt
                if(line== "\n" or line[0] =='#'):
                    continue
                Memory.append(line)
                Nlines+=1
        else:
            print("That is not one of the options")
            
        disassembler(Memory,Nlines)
        print("disassembler is being done")
    elif(mode== 3):
        #assembler(Instructions,Nlines)
        print("assembler is being done")
    else:
        print("Error. Unrecognized mode. Exiting")
        exit()
		
    #instr_file.close()
    data_file2.close()
    data_file.close()
	
if __name__ == "__main__":
    main()
	