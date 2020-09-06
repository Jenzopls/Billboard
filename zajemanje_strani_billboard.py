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
    r'<span class="chart-element__information__song text--truncate color--primary">(?P<naslov>.+)</span>'
    r'\s+'
    r'<span class="chart-element__information__artist text--truncate color--secondary">(?P<izvajalec>.+)</span>'
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


for sobota in vse_sobote_v_letu(2018):
   url = f'https://www.billboard.com/charts/hot-100/{sobota}'
   ime_datoteke = f'billboard_{sobota}'
   o.shrani_spletno_stran(url, ime_datoteke)


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
      if [dictzadetek['naslov'],dictzadetek['izvajalec']] not in [[videna['naslov'],videna['izvajalec']] for videna in pesmi]:
         videna = dictzadetek
         videna['id'] = len(pesmi)
         videna['tednov'] = 1
         videna['povp_mesto'] = videna['mesto_na_lestvici']
         videna['feat'] = ('Featuring' in videna['izvajalec']) or (',' in videna['izvajalec']) or ('&' in videna['izvajalec'])
         pesmi.append(videna)
      else:
         for videna in pesmi:
            if [dictzadetek['naslov'],dictzadetek['izvajalec']] == [videna['naslov'],videna['izvajalec']]:
               videna['tednov_na_lestvici'] = max(videna['tednov_na_lestvici'],dictzadetek['tednov_na_lestvici'])
               videna['najvišje_mesto'] = min(videna['najvišje_mesto'],dictzadetek['najvišje_mesto'])
               videna['povp_mesto'] = (videna['povp_mesto']*videna['tednov'] + dictzadetek['mesto_na_lestvici'])/(videna['tednov'] + 1)
               videna['tednov'] += 1


o.zapisi_csv(pesmi,['id','mesto_na_lestvici','izvajalec','naslov','tednov_na_lestvici','najvišje_mesto','tednov','povp_mesto','feat'],'billboard.csv')
o.zapisi_json(pesmi,'billboard.json')