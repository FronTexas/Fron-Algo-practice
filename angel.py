# Python 2
import sys, json

# Read from stdin
locations = json.loads(sys.stdin.read())

stack = [] 

for location in locations: 
	if location["parent_id"] == None: 
		stack.append((location,0))

while len(stack): 
  currentParent,numberOfDash = stack.pop()
  toPrint = ""
  for i in range(0,numberOfDash):
  	toPrint += "-"
  toPrint += currentParent["name"]
  print toPrint

  for location in locations: 
  	if location["parrent_id"] == currentParent["id"]: 
  		stack.append((location,numberofDash+1))
