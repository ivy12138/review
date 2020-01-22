data=[]
with open('reviews.txt','r')as f:
    for line in f:
        data.append(line)
print(len(data))
print(data[0])
print('------------')
print(data[1])
sum_len=0
for d in data:
    sum_len=sum_len+len(d)
print('the average length is',sum_len/len(data))
