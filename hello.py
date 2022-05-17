# smallest = None
#print ('Before')
#for value in [1, 14, 66, 21, 2, 4, 23, 22] :
#    if smallest is None:
#        smallest = value
#    if value < smallest:
#        smallest = value
#    print (smallest, value)

iValue = 0
fValue = 0.0
count = 0
total = 0
avg = 0

while True :
    iValue = input('Please input a number ',)
    if iValue == 'done':
        break
    try :
        fValue = float(iValue)
    except :
        print('Not a number')
        continue

count = count + 1
total = total + fValue
avg = total / count
print('Total is', total)
print('Count is', count)
print('Average is', avg)
