import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it - Done
 -Extract the names and rank numbers and just print them -Done
 -Get the names data into a dict and print it - Done
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  
  #Finding the year
  f = open(filename, 'r+')
  all_text = f.read()
  match = re.search(r'in \d\d\d\d', all_text)
  if match:
	year_raw =  match.group()
  
  year = year_raw[-4:]	
  year = int(year)
  #print "Year:: " + str(year)
  
  f.close()
 
  #Extracting names and rank in a tuple
  f1 = 	open(filename, 'r+')
  all_text = f1.read()
  tuples =() #rank, male, female
  tuples = re.findall(r'right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',all_text)
  f1.close()
   
  
  male_names = {}
  female_names = {}
  for i in range(len(tuples)):
	male_names[tuples[i][1]] = i+1
	female_names[tuples[i][2]] = i+1
  
  final_list = [str(year)]
  #print final_list
    
  for key in male_names:
	final_list.append(key + str(male_names[key]))
   
  for key in female_names:
	final_list.append(key + str(female_names[key]))
	
  final_list = sorted(final_list)
  
  print final_list,
  

def main():
	extract_names('baby1992.html')
	
	
if __name__ == '__main__':
  main()
