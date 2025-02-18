#define scores as array
scores = []
#define array for percentages
pctscore = []

#define function for reading array
def readScores():
  print("Reading Scores...")

  #open scores.txt file
  myScores = open("scores.txt","r")

  #loop through file adding the data each loop into the scores array
  for x in myScores:
    #add the data to the array
    scores.append(int(x))

  #close file to not take resources
  myScores.close()
  #new line for readability
  print(scores,"\n")


#define function for getting percentages and placing them into array
def percentage():
  print("Calculating Percentages...")
  
  #debug
  #print(scores)


  #loop through array calculating percentage
  for x in scores:
    pct = x/60 * 100
    pctscore.append(pct)
    #debug
    #print(x/60 * 100)

  #print percentage array
  print(pctscore)
  #create new line for readability
  print("\n")
    

#function to get average score and percentage
def avg():
  print("Calculating Average...")
  #defining total
  total = 0

  #adding all the scores together
  for x in scores:
    total += x

  #define variable for average score and percentage
  averageScore = total/len(scores)
  averagePercentage = averageScore/60*100
  #print averages
  print("Average Score: ", averageScore)
  print("Average Percentage: ", averagePercentage,"\n")

def median():
  print("Calculating Median...")
  #sort arrays
  scores.sort()
  pctscore.sort()
  #debug
  #print(scores)
  
  #find middle point
  midpoint = int(len(scores)/2)
  
  #print the median number
  print("Median Score: ", scores[midpoint])
  
  #print median percentage
  print("Median Percentage", pctscore[midpoint])
  








#call functions
readScores()

percentage()

avg()

median()