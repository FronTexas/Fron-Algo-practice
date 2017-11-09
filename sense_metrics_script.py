import socket, json
from dateutil import parser
import matplotlib.pylab as plt
import dateutil.parser

metricId = "theta_y"
unitId = "deg"
apiCode = '5935EC447DB27AD70693603A'
sensorId = '/dev/385236/node/demo/310886/device/demo1/sensor'

def buildSocket(socket_id,apiCode):
    host = "app.sensemetrics.com"
    port = 4200 

    # Open a new socket connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # Send the authentication request
    handshake = json.dumps({
	    "jsonrpc": "2.0",
	    "method": "authenticate",
	    "params": {
	        "code" : apiCode
	    },
	    "id": socket_id
	})
    s.send(handshake.encode())
    return s


def retreiveSensorsOutput(socket_id,socket,sensorId,metricId,unitId):
    sensors_output = {}

	# Create a set of parameters for data retrieval
    retrievalParams = {
	    "sensor": sensorId,
	    "metric": metricId,
	    "unit": unitId,
	};

	# Retrieve data from server
    json_to_send = json.dumps({
	    "jsonrpc": "2.0",
	    "method": "getData",
	    "id": socket_id,
	    "params": retrievalParams
	}).encode()
    socket.send(json_to_send)

	# Handle incoming observations asynchronously
    while True:
	    # Decode response
	    response = json.loads(decodeOneJsonFrame(socket))

	    if "data" in response['result']: 
	        # Store the incoming observations
	        data = response["result"]["data"]
	        for date in data:
	            sensors_output[date] = data[date];

	    # Close the socket when all observations are received
	    if "requestStatus" in response["result"] and response["result"]["requestStatus"] == "finished":
	        socket.close()
	        break
    return sensors_output

def buildPlot(data):
	lists = sorted(data.items()) # sorted by key, return a list of tuples

	x, y = zip(*lists) # unpack a list of pairs into two tuples

	x = [dateutil.parser.parse(e) for e in x]

	plt.plot(x, y)
	plt.show()

# Gets one JSON frame from the TCP stream
# Extremely slow and not reliable, shown for example only
def decodeOneJsonFrame(socket):
    frame = ""
    count = 0
    while True:
        byte = socket.recv(1).decode("utf-8") 
        if byte == "{":
            count = count + 1
        elif byte == "}":
            count = count - 1
        frame = frame + byte
        if count == 0:
            return frame;

socket_id = 0
socket = buildSocket(socket_id , apiCode)
socket_id += 1
sensors_output = retreiveSensorsOutput(socket_id,socket,sensorId,metricId,unitId)
plot = buildPlot(sensors_output)
