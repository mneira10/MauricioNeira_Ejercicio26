import os

inputFile = open("./Pi_2500000.txt",'r')
content = inputFile.read()
inputFile.close()

partitions = [1,10,20,50,100]

def partir(n):
  numChars = (int) (len(content)/n)
  nameDir = 'partition'+str(n)
  if not os.path.exists(nameDir):
      os.makedirs(nameDir)
  for i in range(n):
    writePath = nameDir + '/Pi_' + str(i+1) + '.dat'
    writeFile = open(writePath,'w')
    writeFile.write(content[i*numChars:numChars*(i+1)])
    writeFile.close()

for n in partitions:
    partir(n)


