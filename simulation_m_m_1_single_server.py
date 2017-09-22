arrival_time = [3,10,13,15,20,21,22,23,24]
service_time = [4,3,4,3,4,3,4,3,4]
service_start_time = []
departure_time = []

for i in range(len(arrival_time)):
	if i == 0:
		service_start_time.append(arrival_time[i])
		departure_time.append(arrival_time[i]+service_time[i])
	else:
		if arrival_time[i]>=departure_time[i-1]:
			service_start_time.append(arrival_time[i])
			departure_time.append(arrival_time[i]+service_time[i])
		else:
			service_start_time.append(departure_time[i-1])
			departure_time.append(service_start_time[-1]+service_time[i])
	
print 'service_start_time = ',service_start_time,'\ndeparture_time =     ',departure_time
print 'arrival_time =       ',arrival_time,'\nservice_time =       ',service_time
