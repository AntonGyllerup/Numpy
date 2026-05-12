#om man har en matris kan man få enskilda element ur matrisen genom att ta matrisen[a,b] där det är rad b+1 och kolumn b+1
import numpy as np

A = np.array([[1,1,-1],[2,1,1],[4,3,-1]])

print(A[0,2]) #kommer ge -1

#man kan också tilldela elementvis

A[0,2] = 5 #kommer ändra -1 till 5

#de flesta standardfunktioner är elementvisa

np.sin(A) #beräknar sin av varje enskilt element

#vi kan ta ut flera element ur en matris genom att ange start och slutindex

#A[start_row:end_row, start_col:end_col]  slutindex excluderas, detta kallas slicing

#vi kan också avnända steglängd enligt nedan
#A[start_row:end_row:step, start_col:end_col:step]


#om man vill indexera bakåt anväder man None för raderer före första raden, aka
print(A[2:None:-1]) #vi indexerar från rad 2 och bakåt med steg 1 (framåt steg -1) till None, dvs vi nått första raden

print(A[1:None]) #ger rad 1 fram till och med sista rad, man kan också lämna platsen tom, ie print(A[1:])

#om vi vill ta ut raderna från sista till första kan man skriva:
print(A[::-1])