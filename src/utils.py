def print_letters(letters):
    if letters:
        print('Cartas:')
        for letter in letters:
            print(f'  Cartas {letter}:')
            print_letter_list(letters[letter])
    else:
        print('Aeródromo não apresenta Cartas.')

def print_letter_list(letter_list):
    for letter in letter_list:
        print(f'   {letter}')

def print_meta_taf(meta_taf):
    if not meta_taf['METAR']:
        print('Aeródromo não apresenta Valores META.')
    if not meta_taf['TAF']:
        print('Aeródromo não apresenta Valores TAF.')
    else:
        print('Valores META TAF:')
        print(f"   META: {meta_taf['METAR']}")
        print(f"   TAF: {meta_taf['TAF']}")

def print_sun_times(sun_times):
    if sun_times:
        print('Horários de Sol:')
        print(f"  Nascer do Sol: {sun_times['sunrise']}")
        print(f"  Pôr do Sol: {sun_times['sunset']}")
    else:
        print('Horarios de sol indisponível.')