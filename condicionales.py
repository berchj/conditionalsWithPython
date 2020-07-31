
cryptoCurrency1 = input('Enter the name of the first cryptocurrency: ')
cryptoCurrencyVal1 = float(input('Enter the value of ' + str(cryptoCurrency1) + ': '))
cryptoCurrency2 = input('Enter the name of the second cryptocurrency: ')
cryptoCurrencyVal2 = float(input('Enter the value of ' + str(cryptoCurrency2) + ': '))
cryptoCurrency3 = input('Enter the name of the third cryptocurrency: ')
cryptoCurrencyVal3 = float(input('Enter the value of ' + str(cryptoCurrency3) + ': '))
if (cryptoCurrencyVal1 > cryptoCurrencyVal2 and cryptoCurrencyVal1 > cryptoCurrencyVal3) :
    print(str(cryptoCurrency1) + ' : ' + str(cryptoCurrencyVal1))
    if(cryptoCurrency2 > cryptoCurrency3):
        print(str(cryptoCurrency2) + ' : ' + str(cryptoCurrencyVal2))
        print(str(cryptoCurrency3) + ' : ' + str(cryptoCurrencyVal3))
    else:
        print(str(cryptoCurrency3) + ' : ' + str(cryptoCurrencyVal3))
        print(str(cryptoCurrency2) + ' : ' + str(cryptoCurrencyVal2))
elif(cryptoCurrencyVal2 > cryptoCurrencyVal1 and cryptoCurrencyVal2 > cryptoCurrencyVal3):
    print(str(cryptoCurrency2) + ' : ' + str(cryptoCurrencyVal2))
    if(cryptoCurrencyVal1 > cryptoCurrencyVal3 ):
        print(str(cryptoCurrency1) + ' : ' + str(cryptoCurrencyVal1))
        print(str(cryptoCurrency3) + ' : ' + str(cryptoCurrencyVal3))
    else:
        print(str(cryptoCurrency3) + ' : ' + str(cryptoCurrencyVal3))
        print(str(cryptoCurrency1) + ' : ' + str(cryptoCurrencyVal1))
elif(cryptoCurrencyVal3 > cryptoCurrencyVal1 and cryptoCurrencyVal3 > cryptoCurrencyVal2 ):
    print(str(cryptoCurrency3) + ' : ' + str(cryptoCurrencyVal3))
    if(cryptoCurrencyVal2 > cryptoCurrencyVal1):
        print(str(cryptoCurrency2) + ' : ' + str(cryptoCurrencyVal2))
        print(str(cryptoCurrency1) + ' : ' + str(cryptoCurrencyVal1))
    else:
        print(str(cryptoCurrency1) + ' : ' + str(cryptoCurrencyVal1))
        print(str(cryptoCurrency2) + ' : ' + str(cryptoCurrencyVal2))
print('Thank you a lot for test this code.')
