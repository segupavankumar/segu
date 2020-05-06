from __init__ import crop_details
graph = input('Do you want to view graph, tell Yes or No\n')
while graph=='yes':
      crop=input('enter the crop name\n')
      crop_details.bargraph(crop)
      graph=input('Again you want to view the graph yes or no\n')
year=input('Do you want to see the details in a particular year, tell Yes or No\n')
while year=='yes':
      year=int(input('enter the year\n'))
      crop_details.yeardetails(year)
      year=input('Again you want to view the yeardetails yes or no\n')

