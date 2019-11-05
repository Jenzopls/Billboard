import re

re.DOTALL

with open('Top 100 Songs _ Billboard Hot 100 Chart _ Billboard.html') as f:
    vsebina = f.read()
    
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
    r'<span class="chart-element__information__delta__text text--week">(?P<tednov_na_lestici>\d+) Weeks on Chart</span>'
)

with open('billboard_work','a', encoding='utf-8') as b:
    for zadetek in re.finditer(vzorec,vsebina):
        b.write(str(zadetek.groupdict()))
        b.write('\n')