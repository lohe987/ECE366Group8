#ISA design

def disassembler(M,Nlines):
    print("ECE 366 Group 8 Disassembler")
    print("----------------")
	#print the instructions
    Rx = 0
    Ry = 0
    imm = 0
    print(" Nlines in loop: ", Nlines)
    for i in range(Nlines):
        #print("in loop")
        #print("i is: ", i)
        fetch =M[i]
        print("M[",i,"]:",M[i])# prints out all the values stored from P1_machine.txt
        
        #Edit P1_machine.txt and save to test out if what your adding is correct
        #use fetch[x:y]  to read in the values stored in M[] ymax = 8  
        #then you can use a == to compare to a value in " "
        #if you notice fetch[0:4] reads  the place marked with "x" : xxxx0000
        # another example fetch[4:6] reads the place marked with "x" :0000xx00
        #the first if statement was a test but its also use as an example
        #the else statement at the end is to check errors for any combinations
        #we are not using.
        
        if(fetch[0:4] == "0000"): # reads in parity bit and 3 digits after
            Rx = int(fetch[4:6],2) #uses 5th and 6th value and changes it to dec
            imm= int(fetch[6:8],2)  #uses 7th and 8th value and changes it to dec
            print("loadi R" + str(Rx) +",(R" + str(imm) + ")")
            
            
        elif(fetch[0:4] == "0001"):#template for instruction
            print("another instruction")
            #Rx = int(fetch[x:y],2) #uses xth to yth value and changes it to dec
            #Ry = int(fetch[x:y],2) #uses xth to yth value and changes it to dec
            #imm = int(fetch[x:y],2) #uses xth to yth value and changes it to dec
            #print("instruction" + str(Rx) + str(Ry) + str(imm))
            
            #remove # as needed depending on what instructions your using
            #change x and y for what ever digits you accessing
            #remove or add to print statement as needed to get desired outcome.
            
        elif(fetch[0:4] == "0010"): #template for instruction
            print("another one")
            #Rx = int(fetch[x:y],2) #uses xth to yth value and changes it to dec
            #Ry = int(fetch[x:y],2) #uses xth to yth value and changes it to dec
            #imm = int(fetch[x:y],2) #uses xth to yth value and changes it to dec
            #print("instruction" + str(Rx) + str(Ry) + str(imm))
        else:
            print("Instruction set not supported")
	
	
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
    
		
    #for line in instr_file: # Reading in the instructions
    #    if (line == "/n" or line[0] == '#'):  #empty lines, comments ignored
    #       line = line.replace("\n"," ")
    #        Instructions.append(line)             #Copy all instruction into a list
        #Nline+=1
		
    for line in data_file: # Read in data memoryview
        if(line== "\n" or line[0] =='#'):
	        continue
            
        #Memory.append(int(line,2))
        Memory.append(line)
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
	