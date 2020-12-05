arr = [1,2,3,4,5]
evn=[]
odd=[]
for i in range(len(arr)):
    if i%2==0:
        evn.append(arr[i])
    else:
        odd.append(arr[i])

print(evn,odd)

wave_arr=[]
max_odd=len(odd)
max_eve=len(evn)
od_in=0
ev_in=0
count=0
for i in range(len(arr)):
    if i==0 or count==0:
        if(od_in<max_odd):
            wave_arr.append(odd[od_in])
            od_in=od_in+1
    count=1  
    if count==1:
        if(ev_in<max_eve):
            wave_arr.append(evn[ev_in])
            ev_in=ev_in+1
    count=0
print(wave_arr)

