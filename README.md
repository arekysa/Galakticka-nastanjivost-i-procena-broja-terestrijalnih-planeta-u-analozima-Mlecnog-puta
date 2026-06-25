![UBMATF](https://img.shields.io/badge/UBMATF-Astrostatistics_2026-blue)

# Galaktička nastanjivost i procena broja terestrijalnih planeta u analozima Mlečnog puta

## Opis projekta

Ovaj projekat istražuje galaktičku nastanjivost populacije analoga Mlečnog puta iz kosmološke simulacije [IllustrisTNG (TNG100)](https://www.tng-project.org/) na crvenom pomaku z = 0.

Centralno pitanje kojim se bavimo jeste da li galaksije koje su hemijski "van ravnoteže", odnosno one čija zvezdana metaličnost značajno prevazilazi gasnu, imaju veći ili manji potencijal za nastanjivost od onih sistema koji se nalaze u hemijskoj ravnoteži.

Za procenu i modelovanje koristimo proxy za broj terestrijalnih planeta prema utvrđenom radu [Dayal et al. (2015)](https://doi.org/10.1088/2041-8205/810/1/L2):

$$\frac{N_p}{N_{p,\rm MW}} = \left(\frac{M_\ast}{M_{\ast,\rm MW}}\right)^2 \left(\frac{Z_{\rm G}}{Z_{\rm MW}}\right)^\alpha \frac{\rm SFR_{\rm MW}}{\rm SFR}$$

Glavni nalaz: Galaksije van hemijske ravnoteže dominantno se nalaze na visokom kraju distribucije nastanjivosti (sa oko ~9× većom medijanom u odnosu na galaksije u ravnoteži). Međutim, ove galaksije istovremeno pokazuju manji budući potencijal za formiranje novih terestrijalnih planeta. Ovaj fenomen predstavlja svojevrsni kompromis nastanjivosti (engl. habitability trade-off) koji detaljno opisuju Mitrašinović et al. (2026).

## Struktura repozitorijuma
```
├── projekat_notebook.ipynb   # Glavni Jupyter notebook — pokreće se od početka do kraja
├── requirements.txt          # Spisak potrebnih Python paketa za pokretanje koda
├── .gitignore                # Fajl koji definiše šta Git ignoriše (sirovi TNG podaci, venv)
├── README.md                 # Dokumentacija projekta (ovaj fajl)
└── data/
    └── mw_analogs.csv        # Pre-procesirani uzorak podataka (1703 MW analoga izvučenih iz TNG100-1)
```
## Uputstvo za pokretanje

Notebook je u potpunosti automatizovan. Prilikom pokretanja nisu potrebne nikakve ručne intervencije, unošenje putanja niti preuzimanje dodatnih paketa unutar samih ćelija.

### Korak 1: Kloniranje repozitorijuma
Otvorite Vaš terminal i klonirajte projekat sledećom komandom:
git clone https://github.com/arekysa/Galakticka-nastanjivost-i-procena-broja-terestrijalnih-planeta-u-analozima-Mlecnog-puta.git
cd Galakticka-nastanjivost-i-procena-broja-terestrijalnih-planeta-u-analozima-Mlecnog-puta

### Korak 2: Instalacija potrebnih paketa
Instalirajte sve zavisnosti navedene u konfiguracionom fajlu unutar Vašeg radnog okruženja:
pip install -r requirements.txt

### Korak 3: Pokretanje Jupyter Notebook-a
Pokrenite Jupyter okruženje, otvorite fajl projekat_notebook.ipynb i izvršite komandu:
Kernel → Restart & Run All

*Napomena za ocenjivanje:* Unutar notebook-a implementirana je automatska provera postojanja sirovih simulacionih podataka na putanji data/TNG100-1. Ukoliko ti podaci nisu lokalno dostupni (što je podrazumevano na računaru ispitivača), kod bez prekida i grešaka prebacuje fokus na učitavanje pre-procesiranog uzorka iz fajla data/mw_analogs.csv. Time je omogućena trenutna reprodukcija svih grafikona, statističkih testova i rezultata.

## Podaci

Uzorak podataka u priloženom CSV fajlu generisan je filtriranjem i obradom javno dostupnog [IllustrisTNG TNG100-1](https://www.tng-project.org/) subhalo kataloga (snapshot=99, crveni pomak z=0). Selekcija je izvršena tako da zadovolji opseg zvezdanih masa Mlečnog puta (10^10.4 - 10^11.0 M☉).

Fajl data/mw_analogs.csv sadrži sledeće atribute za svaku od 1703 selektovane galaksije:

| Kolona | Opis atributa | Jedinica |
|---|---|---|
| SubhaloID | Jedinstveni identifikator subhaloa unutar TNG100 simulacije | — |
| StellarMass | Ukupna zvezdana masa galaksije | M☉ |
| GasMass | Ukupna masa gasne komponente unutar galaksije | M☉ |
| SFR | Trenutna brzina formiranja zvezda (Star Formation Rate) | M☉/yr |
| GasMetallicity | Metaličnost gasne komponente (Z_G) | — |
| StarMetallicity | Metaličnost zvezdane komponente (Z_*) | — |

## Opciono: Preuzimanje sirovih podataka i konfiguracija okruženja

Ukoliko želite da ponovite celokupan proces ekstrakcije podataka direktno iz originalne IllustrisTNG simulacije umesto korišćenja pre-procesiranog CSV fajla, ispratite sledeće korake:

### 1. Preuzimanje Group kataloga i Offset fajlova
Potrebno je preuzeti grupni katalog i offset fajl za Snapshot 99 (crveni pomak z = 0). Otvorite terminal na željenoj lokaciji na vašem lokalnom skladištu i izvršite sledeće komande:

mkdir TNG100-1
cd TNG100-1

mkdir groups_099
cd groups_099
wget -nd -nc -nv -e robots=off -l 1 -r -A hdf5 --content-disposition --header="API-Key: f6ea08cec6fc426a55cc2b97da9af398" "http://www.tng-project.org/api/TNG100-1/files/groupcat-99/?format=api" 

wget -O checksums.txt -nv --header="API-Key: f6ea08cec6fc426a55cc2b97da9af398" http://www.tng-project.org/api/TNG100-1/checksums/groupcat-99/
sha256sum -c checksums.txt

mkdir ../offsets
cd ../offsets
wget --header="API-Key: f6ea08cec6fc426a55cc2b97da9af398" https://www.tng-project.org/api/TNG100-1/files/offsets.99.hdf5

### 2. Preuzimanje i modifikacija zvaničnog illustris_python paketa
Da bi struktura direktorijuma bila ispoštovana i fajlovi ispravno prepoznati, potrebno je ručno prepraviti jednu liniju koda u paketu pre instalacije.

Klonirajte paket sa zvaničnog repozitorijuma:
git clone https://github.com/illustristng/illustris_python.git

Otvorite fajl "illustris_python/illustris_python/groupcat.py" i pronađite liniju 24 u kojoj piše:
offsetPath = basePath + '/../postprocessing/offsets/offsets_%03d.hdf5' % snapNum

Zamenite je sa:
offsetPath = basePath + '/offsets/offsets_%03d.hdf5' % snapNum

Nakon sačuvane izmene, pozicionirajte se u osnovni direktorijum (gde ste uradili git clone) i instalirajte izmenjeni paket komandom:
pip install illustris_python/

*Važna napomena:* Ukoliko koristite Anaconda okruženje ili radite unutar JupyterLab-a, uverite se da ovu instalaciju izvršavate unutar terminala tog aktivnog okruženja. U prvoj ćeliji notebook-a promenljivu BASE_PATH postavite kao apsolutnu putanju do vašeg kreiranog TNG100-1 foldera.

## Zavisnosti i automatsko testiranje

Projekat se oslanja na standardne naučne biblioteke za analizu podataka (numpy, pandas, scipy) i vizuelizaciju (matplotlib). 

U skladu sa praksama kursa, provera izvršavanja i validacija stila koda na repozitorijumu vrši se pokretanjem sledećih komandi:

# Provera izvršavanja kompletnog notebook-a od prve do poslednje ćelije
pytest --nbmake --nbmake-timeout=60 projekat_notebook.ipynb

# Statička analiza i provera stila koda unutar ćelija notebook-a
nbqa pylint projekat_notebook.ipynb
