def is_valid_event(event):
	invalid_domains = ['gmail.com','googlemail.com','atlassian.com']
	recipient_email = event['recipient_email']
	domain = recipient_email[recipient_email.index('@') + 1:]
	return len(recipient_email) < 40 and domain not in invalid_domains

def count_num_of_valid_events(events):
	valid_event_counter = 0
	for event in events: 
		if is_valid_event(event):
			valid_event_counter += 1 
	return valid_event_counter

def find_min_and_max_value(data):
	min_value = 2**32
	max_value = -1
	for key in data: 
		value = data[key]
		min_value = min(min_value,value)
		max_value = max(max_value,value)
	return min_value,max_value

def normalize(data):
	minimum,maximum = find_min_and_max_value(data)
	for key in data:
		value = data[key]
		data[key] = round(float(value - minimum) / float(maximum-minimum),2)

def populateHistogram(histogramData,events):
	for event in events: 
		if not is_valid_event(event): continue 
		histogramData[event['hour']] += 1

def buildHistogram(events):
	if len(events) < 5 or count_num_of_valid_events(events) < 5: return None
	
	histogramData = {hour:0 for hour in range(0,24)}
	populateHistogram(histogramData,events)
	normalize(histogramData)
	return histogramData

# ------------------------------------------------------------------------

def is_same(expected,actual):
	if not expected and not actual: return True

	if (expected and not actual) or (not expected and actual): return False

	for key in expected:
		if expected[key] != actual[key]: 
			return False 
	return True

def test(input,expected,actual):
	if not is_same(expected,actual): 
		print ('*** FAILED ***')
		print ('input = ' + str(input))
		print ('expected = ' + str(expected))
		print ('actual = ' + str(actual))
	else:
		print ('PASSED!')


expected = {hour:0 for hour in range(0,24)}
expected[1] = 1 
expected[2] = 1 
expected[3] = 0.5
events = [{'hour':1,'recipient_email':'fahran.kamili@utexas.edu'},{'hour':1,'recipient_email':'forfron@trurecruit.com'},{'hour':2,'recipient_email':'some@company.com'},{'hour':2,'recipient_email':'valid@email.com'},{'hour':3,'recipient_email':'valid@email.com'}]
test(events,expected,buildHistogram(events))


events = [{'hour':1,'recipient_email':'fahran.kamili@utexas.edu'},{'hour':1,'recipient_email':'forfron@gmail.com'},{'hour':2,'recipient_email':'valid@email.com'},{'hour':2,'recipient_email':'valid@email.com'},{'hour':3,'recipient_email':'valid@email.com'}]
test(events,None,buildHistogram(events))

expected[1] = 0.5 
expected[2] = 1 
expected[3] = 1
events = [{'hour':1,'recipient_email':'fahran.kamili@utexas.edu'},{'hour':1,'recipient_email':'forfron@gmail.com'},{'hour':2,'recipient_email':'valid@email.com'},{'hour':2,'recipient_email':'valid@email.com'},{'hour':3,'recipient_email':'valid@email.com'},{'hour':3,'recipient_email':'valid@email.com'}]
test(events,expected,buildHistogram(events))



