import requests
from bs4 import BeautifulSoup

class AiswebData():
    
    def __init__(self, icao_code, user_agent='Chrome/100.0.1234.56'):
        user_agent = user_agent
        header = {'user-agent':user_agent}
        response = requests.get(f"https://aisweb.decea.mil.br/?i=aerodromos&codigo={icao_code}", headers=header)
        raw_text = response.text
        self.soup = BeautifulSoup(raw_text, 'html.parser')


    def __get_sun_times(self):
        sun_times = self.soup.findAll('h4', {'class':'mt-0'})
        times = {'sunrise':sun_times[0].contents[1].text,'sunset':sun_times[1].contents[1].text}

        return times


    def __get_meta_taf(self):
        soup_obj = self.soup.findAll('div', {'class':'col-lg-4 order-sm-12'})
        metar_taf = soup_obj[0].find_all(['h5','p'])

        metar_id = None
        for id_values in range(len(metar_taf)):
            if metar_taf[id_values].contents[0].text == 'METAR':
                metar_id = id_values 
                break

        list_slice = metar_taf[metar_id:]

        metar = list_slice[1].text if len(list_slice[1]) > 0 else None
        taf = list_slice[3].text if len(list_slice[3]) > 0 else None

        values = {'METAR':metar,'TAF':taf}

        return values


    def __get_letters(self):
        soup_obj = self.soup.findAll('div', {'class':'col-lg-4 order-sm-12'})
        letters = soup_obj[0].find_all('h4', {'class':'heading-primary'})
        n_letters = int(letters[1].text[8:-1])

        letter_codes = ['AOC','PATC','ENRC','ARC','ATC','SID','STAR','IAC','VAC','ADC','AGMC','PDC','WAC','CNAV','CINAV','CAP','CIAP']
        key_letter = None
        if n_letters > 0:
            letters = soup_obj[0].find_all(['a','h4'])

            init_index = None
            for i in range(len(letters)):
                if letters[i].text in letter_codes:
                    init_index = i
                    break
            
            end_index = None
            for i in range(len(letters)-1,-1,-1):
                if letters[-1].text[:19] == 'Rotas Preferenciais':
                    end_index = i
                    break

            letters = letters[init_index:end_index]
            
            key_letter = {}
            init = 0
            neo_init = None
            for i in range(len(letters)):
                if letters[i].text in letter_codes:
                    neo_init = i
                    key_letter[letters[init].text] = [letter.text for letter in letters[init+1:neo_init]]
                    init = neo_init
            
            key_letter[letters[neo_init].text] = [letter.text for letter in letters[neo_init+1:]]

        return key_letter


    def scrap_data(self):
        error_msg = self.soup.findAll('h1', {'style':'color:red'})

        if len(error_msg) == 0:
            letters = self.__get_letters()
            sun_times = self.__get_sun_times()
            meta_taf = self.__get_meta_taf()

            return {'letters':letters, 
                    'sun_times':sun_times, 
                    'meta_taf':meta_taf}
        else:
            
            return {'error': 'icao code not found'}
        