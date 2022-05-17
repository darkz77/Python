# hour = input('Please input your hour of work ',)
# try:
#     hour = float(hour)
# except:
#     print('Please input a number in hour')
#     quit()
# rate = input('Please input your rate ',)
# try:
#     rate = float(rate)
# except:
#     print('Please input a number in rate')
#     quit()
#
# pay = hour * rate
# if pay > 40:
#     pay = hour * rate *1.5
#     print('Your pay is ', pay)
# else:
#     print('Your pay is ', pay)

score = input('Please enter your score ',)
try:
    score = float(score)
except:
    print('Please input a number')
    quit()

if score >= 0.0 and score <= 1.0:
    if score >= 0.9:
        print('You got an A')
    elif score >= 0.8:
        print('You got a B')
    elif score >= 0.7:
        print('You got a C')
    elif score >= 0.6:
        print('You got a D')
    elif score < 0.6:
        print('You got a F')

else:
    print('Please input a number from range 0.0 to 1.0')
