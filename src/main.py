import requests
from utils import (print_letters, print_meta_taf, print_sun_times)

# TODO - Criar menu para uso no terminal.
# TODO - Criar lógica para funcionamento no caso de valores nullos.
print("""
Entre com código ICAO para receber informações como:

  -- Cartas.
  -- TAF e METAR.
  -- Horários de Nascer do sol e Por do sol.

Para finalizar a execução, insira "sair" no prompt.
""")
end = False
while not end:
    
    icao_code = input('Entrada: ')
    print()
    if icao_code == 'ajuda':
        print("""
            Para receber informações entre com codigo ICAO.
            Para finalizar a execução, insira "sair" no prompt.
              """)
    
    elif icao_code == 'sair':
        end = True
    
    else:
        x = requests.get(f'http://localhost:5000/scrap-data/{icao_code}')
        
        if x.status_code == 200:
            response = x.json()
            letters = response['letters']
            meta_taf = response['meta_taf']
            sun_times = response['sun_times']

            print_letters(letters)
            print()
            print_meta_taf(meta_taf)
            print()
            print_sun_times(sun_times)
            print()
            
        else:
            print('Codigo ICAO não existe.\n')
