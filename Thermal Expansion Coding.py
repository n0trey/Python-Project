print('Hello you!')
print('So we are going to determine thermal expansion.')
print('Do you want me to calculate it? [Y/N}')
YN=input()
if YN == 'Y':
    print('Lets go!')
    print('What is the material made of?')
    material = str(input())
    if material.lower() == 'aluminum':
        α = 25/ 1000000
        float(α)
    else:
        print('What is the material coefficient [α]?')
        α = input()
        float(α)
    print('What kind of thermal expansion; length, area or volume?')
    expansion = str(input())
    while expansion.lower() != 'length' and expansion.lower() != 'area' and expansion.lower() != 'volume':
        print ('Please answer whether you want to find a length, area or volume!')
        expansion = str(input())
    if expansion.lower() == 'length' or expansion.lower() == 'area' or expansion.lower() == 'volume':
        print('Dont forget to use international system of units ok.')
        print('What is the original ' + expansion.lower() + '?')
        X0 = input()
        float(X0)
        print('What about the initial temperature [in degree Celsius]?')
        T0 = input()
        float(T0)
        print('The final temperature?')
        T = input()
        float(T)
        ΔT = ((float(T)) - (float(T0)))
        print('Apparently your ΔT is ' + str(ΔT))
        for i in range(int(T0), int(T), int(ΔT/4)):
            if expansion.lower() == 'length':
                X = float(X0) * (1 + (float(α) * float(i)))
                print('So your ' + expansion.lower() + ' expansion at '+ str(i) + ' degree Celcius is ' + str(X) + ' m.')
                Total = float(X0) + float(X)
                print('And your total ' + expansion.lower() + ' after expansion is ' + str(Total) + ' m.')
            elif expansion.lower() == 'area':
                X = float(X0) * (1 + (float(α) * 2 * float(i)))
                print('So your ' + expansion.lower() + ' expansion at '+ str(i) + ' degree Celcius is ' + str(X) + ' m2.')
                Total = float(X0) + float(X)
                print('And your total ' + expansion.lower() + ' after expansion is ' + str(Total) + ' m2.')
            else:
                X = float(X0) * (1 + (float(α) * 3 * float(i)))
                print('So your ' + expansion.lower() + ' expansion at '+ str(i) + ' degree Celcius is ' + str(X) + ' m3.')
                Total = float(X0) + float(X)
                print('And your total ' + expansion.lower() + ' after expansion is ' + str(Total) + ' m3.')
        print('Thank you for using our service! Have a lovely day (^•w•^)ﾉ~ ')
else :
    print('Alright then. See you later!(^•w•^)ﾉ~ ')
