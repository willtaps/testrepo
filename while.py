n = 5
while n > 0 :
    print(n)
    n = n -1
print('All done')

while True:
    line = input('> ')
    if line [0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('Done')

for i in [5,4,3,2,1] :
    print ('Beer ' + str(i))
print("We are out !")

numbers = [5,4,3,2,1] 
for number in numbers :
     print ('Beer ' + str(number))
print("its time to bounce")