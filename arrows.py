import arrow

time = '2020-11-09 18:35:00'
#print(arrow.get(time).to('US/Pacific'))

time=arrow.get(time).replace(tzinfo='US/Pacific')
print(time)
print(arrow.get(time).to('America/New_York'))

