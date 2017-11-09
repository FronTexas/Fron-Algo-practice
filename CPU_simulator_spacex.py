cpu = [0] * 43
MAX = (2**32) 


def getPosFromLoc(loc):
    the_number = loc[1:]
    return int(the_number)
    

def MOV(args):
	loc1 = args[0]
	loc2 = args[1]
	if('R' == loc1[0]):
		_loc1 = getPosFromLoc(loc1)
		_loc2 = getPosFromLoc(loc2)
		cpu[_loc2] = cpu[_loc1]
		return 
	_loc2 = getPosFromLoc(loc2)
	cpu[_loc2] = int(loc1)

def ADD(args):
	loc1 = args[0]
	loc2 = args[1]
	_loc1 = getPosFromLoc(loc1)
	_loc2 = getPosFromLoc(loc2)
	cpu[_loc1] = (int(cpu[_loc1]) + int(cpu[_loc2])) % MAX

def DEC(args):
	_loc = getPosFromLoc(args[0])
	if(cpu[_loc] == 0):
		cpu[_loc] = MAX - 1
		return 
	cpu[_loc] -= 1 

def INC(args):
	_loc = getPosFromLoc(args[0])
	if(cpu[_loc] == MAX - 1):
		cpu[_loc] = 0
		return 
	cpu[_loc] += 1 

def INV(args):
	_loc = getPosFromLoc(args[0])
	cpu[_loc] = ~cpu[_loc]
    
def cpuEmulator(subroutine):
	func_dict = {
		"MOV" : MOV,
		"ADD" : ADD,
		"DEC" : DEC,
		"INC" : INC,
		"INV" : INV,
	}
	i = 0
	while(i < len(subroutine)):
		routine = subroutine[i].split(' ')
		func_name = routine[0]

		if func_name == "NOP":
			i+=1
			continue

		params = routine[1].split(',')

		if func_name == "JMP":
			i = int(params[0]) - 1
			continue

		if func_name == "JZ":
			if cpu[0] == 0:
				i = int(params[0]) - 1
				continue
			i+= 1 
			continue

		func_dict[func_name](params)
		i+=1 
	return str(cpu[-1])
