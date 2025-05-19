header = ('Welcome to USSD Banking. Please note  N6.98 network charge will be applied to your account for banking services on this channel')
print(header)
choose = (input('a. Accept \nb. Cancel\n\n'))
correctchoose = {'a'}
if choose == 'a':
    print('you have selected choice', choose)

pick = (input('1. Buy Airtime \n2. Buy Data \n3. Pay Bills \n4. Transfer \n5. Check Balance \n6. Exit\n\n'))
print('you have selected choice', pick)
correctpin = '1111'
currentbalance = 200000

if pick == '1':
    Amount = input('Enter Amount:')
    PhoneNumber = input('Enter your Phone Number or the Phone Number of the Recipient:')
    if len(PhoneNumber) == 11 and PhoneNumber.isdigit():
        print('Recharge of' ,Amount, 'to' , PhoneNumber )
        network = input('1. MTN\n2. Airtel\n3. Glo\n4. Etisalat\n\n')
        if network == '1':
            pin = input('Enter your PIN')
            if pin == correctpin and len(pin) == 4:
                if currentbalance >= int(Amount):
                    print(f'You just bought airtime of {Amount} for {PhoneNumber}')
                else:
                    print('Insufficient Balance') 
            else:
                print('incorrect pin')
        else:
            print('Transfer not possible')
    else:
        print('Incorrect number')  
  

elif pick == '2':
    Data = input('Enter Data Amount:')
    Number = input('Enter your Phone Number or the Phone Number of the Recipient:')
    if len(Number) == 11 and Number.isdigit():
        print(f'Recharge of {Data} to {Number}')
        network = input('1. MTN\n2. Airtel\n3. Glo\n4. Etisalat\n\n')
        if network == '1':
            pin = input('Enter your pin')
            if pin == correctpin and len(pin) == 4:
                if currentbalance >= int(Data):
                    print('you have successfully bought airtime of', Data, 'for', Number)
                else:
                    print('Insufficient Balance')
            else:
                print('incorrect Pin')
    else:
        print('Incorrect number')

elif pick == '3':
    Bill = input('1. IKEDC\n2. DSTV\n3. GOTV\n4. Spectranet\n\n')
    if Bill == '1':
        meternumber = input('please input Meter number')
        if len(meternumber) == 11 and meternumber.isdigit():
            price = input('amount')
            pin = input('Enter your pin')
            if pin == correctpin and len(pin) == 4:
                if currentbalance >= int(price):
                    print('you have successfully bought energy worth', price, 'for', meternumber)
                else:
                    print('Not successful')

elif pick == '4':
    transfer = input('Enter Amount you would like to transfer:')
    AccountNumber = input('Enter your Account Number:')
    if len(AccountNumber) == 10 and AccountNumber.isdigit():
        bank = input ('1. Eco Bank\n2. Zenith Bank\n3. Wema Bank\n4. Input Bank\n\n')
        if bank == '2':
            Click = input('1. Savings\n2. current\n')
            if Click == '1':
                pin = input('Enter your pin')
                if pin == correctpin and len(pin) == 4:
                    if currentbalance >= int(transfer):
                        print('you have successfully transfered a sum of', transfer, 'to Account Number', AccountNumber)
                    else:
                        print('Insufficient Amount')
                else:
                    print('Not successful')

elif pick == '5':
    AccountNumber = input('Enter your Account Number:')
    if len(AccountNumber) == 10 and AccountNumber.isdigit():
        pin = input('Enter your pin')
        if pin == correctpin and len(pin) == 4:
            print('your account balanace is: ' , currentbalance)
        else:
            print('Incorrect Pin')
    else:
        print('Invalid Account Number')
    


elif pick == '6':
    put = ('Thank you for using our service, see you again.')
    print(put)



