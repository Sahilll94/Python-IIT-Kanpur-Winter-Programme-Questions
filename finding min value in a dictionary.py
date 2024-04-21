#Question Description
'''
Get the key of a minimum value from the following dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75 }
Expected output:
Math
'''

#Solution
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'History': 75 
}

min_key = min(sample_dict, key=lambda k: sample_dict[k])
print(min_key)

