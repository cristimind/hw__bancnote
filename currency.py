amount = int(input ( 'Suma de bani : '))

bancnote_20 = amount // 20
bancnote_5  = (amount - bancnote_20 * 20 ) // 5
bancnote_1  = amount  % 5

print ( "20 X " , bancnote_20 , ' 5 X ' , bancnote_5 , " 1  X " , bancnote_1 )