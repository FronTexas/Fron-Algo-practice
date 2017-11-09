def flattenDictionaryHelper(runningKey,dictionary,toReturn):
  for key in dictionary: 
    nextRunningKey = runningKey + "." + key if len(runningKey) > 0 else key
    if type(dictionary[key]) is dict:
      flattenDictionaryHelper(nextRunningKey,dictionary[key],toReturn)
    else: 
      toReturn[nextRunningKey] = dictionary[key]
      

def flatten_dictionary(dictionary):
  toReturn ={}
  flattenDictionaryHelper("",dictionary,toReturn)
  return toReturn

dictionary = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : "1"
                }
            }
        }
# dictionary = {"a":{"b":{"c":{"d":{"e":{"f":{"":"pramp"}}}}}}}
# dictionary =  {"":{"a":"1"},"b":"3"}

print flatten_dictionary({"Key1":"1","Key2":{"a":"2","b":"3","c":{"d":"3","e":"1"}}})