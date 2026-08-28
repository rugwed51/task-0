import numpy as np #importing numpy module
hrsStudied = np.array([4.8,3.5,6.7,4.6,2.9])    #creating arrays
attendance = np.array([75,85,65,98,49])
prevScore =np.array([58,60,39,78,58])
finalScore = np.array([70,91,58,87,76])
print("hrsStudied: Shape- "+str(hrsStudied.shape)+"\t Data Type- "+str(hrsStudied.dtype) )  #printing shape and data type of array
print("attendance: Shape- "+str(attendance.shape)+"\t Data Type- "+str(attendance.dtype) )
print("prevScore: Shape- "+str(prevScore.shape)+"\t Data Type- "+str(prevScore.dtype) )
print("finalScore: Shape- "+str(finalScore.shape)+"\t Data Type- "+str(finalScore.dtype) )
mean = (np.sum(finalScore))/(np.size(finalScore))   #calculating mean,maxm,minm,std deviation
maximum=np.max(finalScore)
minimum=np.min(finalScore)
stdev=np.std(finalScore)
print("Mean: "+str(mean)+"\nMaximum: "+str(maximum)+"\nMinimum: "+str(minimum)+"\nStandard Deviation: "+str(stdev))
finalScore+=5       #adding bonus marks
booleanArr = finalScore>=75     #creating boolean array
print(booleanArr)
trueOnes = finalScore[finalScore>=75]   #printing only true scores
print(trueOnes)