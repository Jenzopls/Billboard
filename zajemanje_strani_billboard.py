from datetime import date, timedelta
import re
import orodja as o

vzorec = (
    r'<span class="chart-element__rank__number">(?P<mesto_na_lestvici>\d{1,3})</span>'
    r'\s+'
    r'<span.*</span>'
    r'\s+'
    r'</span>'
    r'\s+'
    r'<span.*>'
    r'\s+'
    r'<span class="chart-element__information__song text--truncate color--primary">(?P<naslov_pesmi>.+)</span>'
    r'\s+'
    r'<span class="chart-element__information__artist text--truncate color--secondary">(?P<ime_izvajalca>.+)</span>'
    r'\s+'
    r'<.+>'
    r'\s+'
    r'<span.*</span>'
    r'\s+'
    r'<span.*</span>'
    r'\s+'
    r'<span class="chart-element__information__delta__text text--peak">(?P<najvišje_mesto>\d{1,3}) Peak Rank</span>'
    r'\s+'
    r'<span class="chart-element__information__delta__text text--week">(?P<tednov_na_lestvici>\d+) Weeks on Chart</span>'
)

def vse_sobote_v_letu(year):
   d = date(year, 1, 1)                    # January 1st
   d += timedelta(days = 5 - d.weekday())  # First Sunday
   while d.year == year:
      yield d
      d += timedelta(days = 7)

#for sobota in vse_sobote_v_letu(2018):
#   url = f'https://www.billboard.com/charts/hot-100/{sobota}'
#   ime_datoteke = f'billboard_{sobota}'
#   o.shrani_spletno_stran(url, ime_datoteke)

pesmi = list()

for sobota in vse_sobote_v_letu(2018):
   datoteka = f'billboard_{sobota}'
   vsebina = o.vsebina_datoteke(datoteka)
   vsebina = vsebina.replace('&#039;','\'')
   vsebina = vsebina.replace('&amp;','&')
   for zadetek in re.finditer(vzorec, vsebina):
      dictzadetek = zadetek.groupdict()
      dictzadetek['mesto_na_lestvici'] = int(dictzadetek['mesto_na_lestvici'])
      dictzadetek['najvišje_mesto'] = int(dictzadetek['najvišje_mesto'])
      dictzadetek['tednov_na_lestvici'] = int(dictzadetek['tednov_na_lestvici'])
      dictzadetek['feat'] = ('Featuring' in dictzadetek['ime_izvajalca'])
      dictzadetek['st_besed'] = dictzadetek['naslov_pesmi'].count(' ') + 1
      if [dictzadetek['naslov_pesmi'],dictzadetek['ime_izvajalca']] not in [[videna['naslov_pesmi'],videna['ime_izvajalca']] for videna in pesmi]:
         videna = dictzadetek
         videna['id'] = len(pesmi)
         videna['tednov'] = 1
         videna['povp_mesto'] = videna['mesto_na_lestvici']
         pesmi.append(videna)
      else:
         for videna in pesmi:
            if [dictzadetek['naslov_pesmi'],dictzadetek['ime_izvajalca']] == [videna['naslov_pesmi'],videna['ime_izvajalca']]:
               videna['tednov_na_lestvici'] = max(videna['tednov_na_lestvici'],dictzadetek['tednov_na_lestvici'])
               videna['najvišje_mesto'] = max(videna['najvišje_mesto'],dictzadetek['najvišje_mesto'])
               videna['povp_mesto'] = (videna['povp_mesto']*videna['tednov'] + dictzadetek['mesto_na_lestvici'])/(videna['tednov'] + 1)
               videna['tednov'] += 1




o.zapisi_csv(pesmi,['id','mesto_na_lestvici','ime_izvajalca','naslov_pesmi','tednov_na_lestvici','najvišje_mesto','tednov','povp_mesto','feat','st_besed'],'videne.csv')
#o.zapisi_json(pesmi,'billboard.json')
#o.zapisi_csv(pesmi,['id','mesto_na_lestvici','naslov_pesmi','ime_izvajalca','najvišje_mesto','tednov_na_lestvici'],'billboard.csv')