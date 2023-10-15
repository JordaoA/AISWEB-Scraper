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
"""
{
    'letters': 
        {
         'ADC': ['ADC SBMT'], 
         'PDC': ['PDC SBMT'], 
         'VAC': ['RWY 12/30']
        }, 
    'meta_taf': 
        {
         'METAR': '151400Z 10006KT 9999 BKN019 21/17 Q1023=', 
         'TAF': '150800Z 1512/1524 09005KT 9999 BKN015 TX23/1516Z TN18/1524Z BECMG 1513/1515 16010KT BKN025 BECMG 1519/1521 BKN015 PROB30 1522/1524 6000 BKN012 RMK PGN='
        }, 
    'sun_times': 
        {
         'sunrise': '08:33', 
         'sunset': '21:11'
        }
}
"""
