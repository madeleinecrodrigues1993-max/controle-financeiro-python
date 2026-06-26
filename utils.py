def ler_float(mensagem):
   
    while True:
       
        try:
       
            valor = float(input(mensagem))
            return valor
        
        except ValueError:
            print("\nValor inválido. Por favor, digite um número válido.\n")
            
def mostrar_cabecalho(titulo):

    print("=" * 40)
    print(titulo.center(40))
    print("=" * 40)