# Billboardova lestvica "vročih hitov"
...Skupni imenovalci in ostali faktorji zvočnih izdelkov pop kulture dva tisoč osemnajstega leta gospodovega...

Ah, kdo ne mara vsako jutro, ko se njegov radijski sprejemnik poveže z eno od lokalnih komercialnih
radijskih postaj, slišati enega od desetih "vročih hitov", ki mu potem še cel dan ali dva odzvanjajo
v ušesih. Zakaj poslušamo, kar poslušamo? Kaj naredi komad popularen? Je Keith Richards res nesmrten? 
Ker me navedena vprašanja že nekaj časa ropajo dragocenega spanca, bom v kratki raziskavi
poskušal nanje odgovoriti.
Vse potrebne podatke:
- ime izvajalca, 
- naslov pesmi, 
- število tednov na lestvici, 
- najvišje mesto pesmi na lestvici 

bom izkopal s strani https://www.billboard.com/charts/hot-100, prek katere želim izvedeti naslednje:

- Je število črk oz. besed v naslovu pesmi odvisno od nje popularnosti?
- Ali število izvajalcev pesmi vpliva na njen uspeh?
- Ali so pesmi, ki so dosegle visoka mesta, dalj časa na lestvici?

V analizo bom vključil vseh 100 najbolj priljubljenih pesmi vsakega tedna preteklega leta,
sodeč po billboardu. Upajmo, da kaj uspe. 

# Zbrani podatki
V datoteki billboard_csv je zbranih vseh nekaj tisoč vročih hitov prejšnjega leta. Poleg naslova pesmi in imena izvajalca je razvidno tudi povprečno mesto, ki ga je pesem dosegla, najvišje doseženo mesto in število tednov, ki ga je pesem že preživela na lestvici. Tej datoteki dela družbo tudi json datoteka z istimi podatki. Če ne drugega zato, ker zgleda precej lepo.
Podatke sem si nekega hladnega novembrskega jutra priskrbel z "zajemanje_strani_billboard", v pomoč pa so mi prišla tudi "orodja.py", katera sem s pridom uporabil. Samo za okus sem priložil še primer html datoteke s katere sem razbiral vzorce. Zaenkrat je to od mene vse, do takrat pa... 


...bomo videli.
