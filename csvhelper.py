import csv

# This function reads a CSV and converts it into an array
# @arg file: path to the file to be read
# @arg converter: function called to convert from string to data type, defaults to int
def read(file, converter=int):
  # Define the array we will be returning
  returnArray = []

  # Open the file in a variable called csvfile
  with open(file, newline='') as csvfile:
    # Read the file we opened, storing each line of the file in an iterator(array)
    csvreader = csv.reader(csvfile, delimiter=',')
    
    for row in csvreader:   # Iterate through each line
      for item in row:      # Iterate through each item in the row
        if item:            # If the item exists, i.e. not an empty string: ''
          # Append the item to our return array, but first we convert it to the type we want
          returnArray.append( converter(item) )

  # Return the array we just built
  return returnArray