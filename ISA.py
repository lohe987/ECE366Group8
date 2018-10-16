#ISA design

def disassembler(M,Nlines):
    print("ECE 366 Group 8 Disassembler")
    print("----------------")
	#print the instructions
	
    print(" Nlines in loop: ", Nlines)
    for i in range(Nlines):
        print("in loop")
        fetch =M[i]
        print(fetch)
        if(fetch[1:4] == "000"):
            #if(fetch[8] =="1") : #load imm
            Rx = int(fetch[4:5])
           #imm= int(fech[5:8],2)
            print("loadi R" + str(Rx) )#+",(R" + str(imm))
	
	
#def assembler(I,Nlines):
#def simulator(I,Nsteps,debug_mode,Memory):
def main():
    instr_file = open("P1_Instruction.txt","r")
    data_file = open("P1_Machine.txt" ,"r") #we need a file for the data set
    #Nsteps = 3  #How many cycles to run before output
    #global Nlines
    Nlines = 0   #How may instrs total in input.txt
    Instructions = [] #all instructions will be stored here
    Memory = []
    print( " ECE 366 Group 8")
	#print( " 1 = simulator")
    print( " 2 = disassembler")
    #print( " 3 = assembler")
	
    mode= int(input( "Please enter the mode of Program: "))
    print( "Mode selected: ",end=" ")
    #if(mode== 1):
        #print("Simulator")
    #elif(mode== 2):
       # print( "disassembler")
        #disassembler(Instructions,Nlines)
    #elif(mode== 3):
       # print( "assembler")
	    #assemble(Instructions, Nlines)
    
		
    for line in instr_file: # Reading in the instructions
        if (line == "/n" or line[0] == '#'):  #empty lines, comments ignored
            line = line.replace("\n"," ")
            Instructions.append(line)             #Copy all instruction into a list
        #Nline+=1
		
    for line in data_file: # Read in data memoryview
        if(line== "\n" or line[0] =='#'):
	        continue
	        Memory.append(int(line,2))
            Nlines+=1
    if(mode == 1): #Check whether to use disassembler of assembler or simulator
        #simulator(Instructions,Nsteps,debug_mode,Memory)
        print("assembler")
    elif(mode== 2):
        disassembler(Memory,Nlines)
        print("disassembler is being done")
    elif(mode== 3):
        #assembler(Instructions,Nlines)
        print("assembler is being done")
    else:
        print("Error. Unrecognized mode. Exiting")
        exit()
		
		
    #instr_file.close()
    data_file.close()
	
if __name__ == "__main__":
    main()
	