![UBMATF](https://img.shields.io/badge/MASS--UBMATF-Astrostatistics_2026-blue)

# Galaktička nastanjivost i procena broja terestrijalnih planeta u analozima Mlečnog puta

## Opis projekta

Ovaj projekat istražuje **galaktičku nastanjivost** populacije analoga Mlečnog puta iz kosmološke simulacije [IllustrisTNG (TNG100)](https://www.tng-project.org/) na crvenom pomaku z = 0.

Centralno pitanje: da li galaksije koje su hemijski "van ravnoteže" — čija zvezdana metaličnost značajno prevazilazi gasnu — imaju veći ili manji potencijal za nastanjivost od onih u ravnoteži?

Koristimo proxy za broj terestrijalnih planeta po [Dayal et al. (2015)](https://doi.org/10.1088/2041-8205/810/1/L2):

$$\frac{N_p}{N_{p,\rm MW}} = \left(\frac{M_\ast}{M_{\ast,\rm MW}}\right)^2 \left(\frac{Z_{\rm G}}{Z_{\rm MW}}\right)^\alpha \frac{\rm SFR_{\rm MW}}{\rm SFR}$$

**Glavni nalaz:** Galaksije van hemijske ravnoteže dominiraju na visokom kraju distribucije nastanjivosti (~40× veća medijana od galaksija u ravnoteži), ali imaju **manji budući potencijal** za formiranje novih planeta — suštinski *kompromis nastanjivosti* koji opisuju Mitrašinović et al. (2026).

## Struktura repozitorijuma

```
├── projekat_notebook.ipynb   # Glavni notebook — pokreće se od početka do kraja
├── download_data.py          # Skripta za preuzimanje mw_analogs.csv
├── mw_analogs.csv            # Podaci (MW analozi iz TNG100, ~uzorak)
├── requirements.txt          # Python paketi
└── README.md
```

## Pokretanje

### Brzo pokretanje (sa CSV podacima)

```bash
# 1. Kloniranje repozitorijuma
git clone https://github.com/arekysa/Galakticka-nastanjivost-i-procena-broja-terestrijalnih-planeta-u-analozima-Mlecnog-puta.git
cd Galakticka-nastanjivost-i-procena-broja-terestrijalnih-planeta-u-analozima-Mlecnog-puta

# 2. Instalacija paketa
pip install -r requirements.txt

# 3. Otvoriti projekat_notebook.ipynb i pokrenuti Kernel → Restart & Run All
```

### Sa originalnim TNG100 podacima

Ako imate pristup TNG100 simulaciji (dostupna na https://www.tng-project.org/data/):

```bash
export TNG100_PATH=/putanja/do/TNG100-1
```

Notebook automatski detektuje ovu env varijablu i učitava podatke direktno.

### Preuzimanje podataka

```bash
python download_data.py
```

Ova skripta preuzima `mw_analogs.csv` — podskup TNG100 galaksija koji odgovara opsegu masa Mlečnog puta (10^10.4 – 10^11.0 M☉).

## Podaci

Podaci su generisani iz [IllustrisTNG TNG100-1](https://www.tng-project.org/) simulacije (javno dostupna). Fajl `mw_analogs.csv` sadrži filtrirani podskup subhalo kataloga (snap=99, z=0) sa sledećim kolonama:

| Kolona | Opis | Jedinica |
|--------|------|---------|
| SubhaloID | TNG100 identifikator | — |
| StellarMass | Zvezdana masa | M☉ |
| GasMass | Masa gasa | M☉ |
| SFR | Stopa formiranja zvezda | M☉/yr |
| GasMetallicity | Gasna metaličnost (Z_G) | — |
| StarMetallicity | Zvezdana metaličnost (Z_*) | — |

## Zavisnosti

Videti `requirements.txt`. Ključni paketi: `numpy`, `pandas`, `matplotlib`, `scipy`, `illustris_python`.
