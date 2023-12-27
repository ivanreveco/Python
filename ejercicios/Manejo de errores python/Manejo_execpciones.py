resultado = None
a=10
b=0


#ZerodivisionError
try:    
    resultado=a/b
except Exception as e: #expect ZeroDivisionError
    print(f'nose puede dividir en 0   {e}')
    print('continuamos con el proceso')
