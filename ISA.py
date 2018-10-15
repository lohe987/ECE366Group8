#ISA design

def disassembler(I,Nlines):
    print(ECE 366 Group 8 Disassembler")
	print("----------------")
	#print the instructions
	
	
#def assembler(I,Nlines):
#def simulator(I,Nsteps,debug_mode,Memory):
def main():
    instr_file = open("Project21MIPS_horridattempt","r")
	#data_file = open(data file ,"r") we need a file for the data set
	#Nsteps = 3  #How many cycles to run before output
	Nlines = 0   #How may instrs total in input.txt
    Instructions[] #all instructions will be stored here
	print( " ECE 366 Group 8")
	#print( " 1 = simulator")
	#print( " 2 = disassembler")
	print( " 3 = assembler")
	
	mode= int(input( "Please enter the mode of Program: "))
	print( "Mode selected: ",end=" ")
	if(mode== 1):
	    print("Simulator")
	elif(mode== 2):
	    print("disassembler")
		#disassembler(Instructions,Nlines)
	elif:
	    print("assembler")
	    #assemble(Instructions, Nlines)
	else:
        print("Error. Unrecognized mode. Exiting")
        exit()
		
    for line in instr_file: # Reading in the instructions
	    if (line == "/n" or line[0] == '#'):  #empty lines, comments ignored
		line = line.replace("\n"," ")
		Instructions.append(line)             #Copy all instruction into a list
		Nline+=1
	#for line in data_file: # Read in data memoryview
	#    if(line== "\n" or line[0] =='#'):
	#        continue
	#    Memory.append(int(line,2))
	
	if (mode == 1): #Check whether to use disassembler of assembler or simulator
	#    simulator(Instructions,Nsteps,debug_mode,Memory)
	elif(mode == 2):
	    disassembler(Instructions,Nlines)
	else
	    assembler(Instructions,Nlines)
		
		
    instr_file.close()
	#data_file.close()
	