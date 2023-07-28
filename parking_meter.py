'''
[180, 5000, 10, 600]	["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]	[14600, 34400, 5000]
[120, 0, 60, 591]	["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]	[0, 591]
[1, 461, 1, 10]	["00:00 1234 IN"]	[14841]

'''


def solution(fees, records):
    def timify(string):
        hour, minute = list(map(int,string.split(':')))
        
        '''
        is map object iterable? maybe not
        '''
        return hour * 60 + minute
    park_car_now = {}
    overall_time = {}
    for i in records:
        time, license_plate, status = i.split()
        print(time,license_plate,status)
        
        if status == 'IN':
            park_car_now[license_plate] = timify(time)
            print(park_car_now)
            pass
        else:
            overall_time[license_plate] = overall_time.get(license_plate, 0) + timify(time) - park_car_now.pop(license_plate)
            print(park_car_now)
        
    for i in park_car_now:
        overall_time[i] = overall_time.get(i,0) + (1439 - park_car_now[i])
    
    answer = [i for i in sorted(list(overall_time.keys()))] 
    print(overall_time)
    for i in range(len(answer)):
        added_time1 = overall_time[answer[i]] - fees[0]
        added_time2 = (added_time1 // fees[2]) if added_time1 % fees[2] == 0 else added_time1 // fees[2] + 1
        print(added_time2)  
        answer[i] = added_time2 * fees[-1] * (added_time1 > 0) + fees[1]
        
    return answer
a = [180, 5000, 10, 600]
b = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

# print( solution(a, b) )

a = [1, 461, 1, 10]	
b = ["00:00 1234 IN"]
print( solution(a, b) )
