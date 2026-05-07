# kod koji izvlaci analoge MW iz TNG100-1 iz snap=99 (z=0) 

import illustris_python as il
import pandas as pd
import numpy as np

basePath = "/home/arekysa/Documents/Praksa/AOB_Ana_M_24_25/TNG100-1"
snap = 99
h = 0.6774

# ucitavanje specificnik polja iz kataloga
polja = ['SubhaloMassType', 'SubhaloSFR', 'SubhaloGasMetallicity', 'SubhaloFlag']
subhalos = il.groupcat.loadSubhalos(basePath, snap, fields=polja)

stellar_mass = subhalos['SubhaloMassType'][:, 4] * 1e10 / h
z_gas = subhalos['SubhaloGasMetallicity']
sfr = subhalos['SubhaloSFR']
flag = subhalos['SubhaloFlag']

# definisanje granica za selekciju i filtriranje
mass_min = 10**10.4
mass_max = 10**11.0  

mw_condition = (stellar_mass >= mass_min) & \
               (stellar_mass <= mass_max) & \
               (sfr > 0) & \
               (z_gas > 0) & \
               (flag == 1)

mw_ids = np.where(mw_condition)[0]

# data frame za konverziju u csv
mw_analogs = pd.DataFrame({
    'SubhaloID': mw_ids,
    'StellarMass': stellar_mass[mw_ids],
    'SFR': sfr[mw_ids],
    'GasMetallicity':z_gas[mw_ids]
})

print(f"Pronađeno je {len(mw_ids)} MW analoga.")
output_path = "mw_analogs.csv"
mw_analogs.to_csv(output_path, index=False)

