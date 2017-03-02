T = input('Enter the number of test cases')

digits = { 0: ' - \n| |\n|_|',
           1: ' | \n | \n | ',
           2: ' - \n _|\n|_ ',
           3: ' - \n _|\n _|',
           4: '| |\n|_|\n  |',
           5: ' - \n|_ \n _|',
           6: ' - \n|_ \n|_|',
           7: ' - \n  |\n  |',
           8: ' - \n|_|\n|_|',
           9: ' - \n|_|\n _|'

        }
input_list = []
while(T!=0):
    input_list.append(input('Enter the number'))
    T -=1
for x in input_list: 
    l = []

    line1 = ''
    line2 = ''
    line3 = ''
    
    for elm in str(x):
        l.append(elm)

    for elm in l:
        digital_integer = digits[int(elm)]
        digital_list = digital_integer.split('\n')
        line1 = line1 + ' ' + digital_list[0]
        line2 = line2 + ' ' + digital_list[1]
        line3 = line3 + ' ' + digital_list[2]

    print(line1)
    print(line2)
    print(line3)
    print('\n')
