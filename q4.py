import numpy as np
hrsStudied = np.array([4.8, 3.5, 6.7, 4.6, 2.9])    #creating arrays
attendance = np.array([75, 85, 65, 98, 49])
prevScore = np.array([58, 60, 39, 78, 58])
finalScore = np.array([70, 91, 58, 87, 76])
print(f"hrsStudied: Shape- {hrsStudied.shape}\t Data Type- {hrsStudied.dtype}")  #printing shape and data type of array
print(f"attendance: Shape- {attendance.shape}\t Data Type- {attendance.dtype}")
print(f"prevScore: Shape- {prevScore.shape}\t Data Type- {prevScore.dtype}")
print(f"finalScore: Shape- {finalScore.shape}\t Data Type- {finalScore.dtype}")
mean = (np.sum(finalScore)) / (np.size(finalScore))   #calculating mean,maxm,minm,std deviation
maximum= np.max(finalScore)
minimum= np.min(finalScore)
stdev= np.std(finalScore)
print(f"Mean: {mean}\nMaximum: {maximum}\nMinimum: {minimum}\nStandard Deviation: {stdev}")
finalScore+=5       #adding bonus marks
booleanArr = finalScore>=75     #creating boolean array
print(booleanArr)
trueOnes = finalScore[finalScore>=75]   #printing only true scores
print(trueOnes)