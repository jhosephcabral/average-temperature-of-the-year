meses = ['January','February','March','April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

temp = []
 
tempmedia = 0
acimaMedia = {}

for i in range(len(meses)):
 	temp.append(float(input('Temperature corresponding to each month of the year: ' + meses[i] + ':'  )))
tempmedia += temp[i]

media = tempmedia/len(meses)

for i in range(len(meses)):
 	if(temp[i] > media):
 		acimaMedia.update({meses[i] : temp[i]})


print('Average temperatures in the year: ' + str(media))
print('Months that had above average temperatures: ' + str(acimaMedia))


