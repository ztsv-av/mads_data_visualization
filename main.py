# NASA Exoplanet Archive
# https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PS

# pl_name, hostname, sy_snum, sy_pnum, sy_mnum, disc_year, discoverymethod, pl_orbper, pl_orbpererr1, pl_orbpererr2, pl_rade, pl_radeerr1, pl_radeerr2, pl_masse, pl_masseerr1, pl_masseerr2, pl_dens, pl_denserr1, pl_denserr2, pl_orbeccen, pl_orbeccenerr1, pl_orbeccenerr2, pl_insol, pl_insolerr1, pl_insolerr2, pl_eqt, pl_eqterr1, pl_eqterr2, pl_orbincl, pl_orbinclerr1, pl_orbinclerr2, st_teff, st_tefferr1, st_tefferr2, st_rad, st_raderr1, st_raderr2, st_mass, st_masserr1, st_masserr2, st_met, st_meterr1, st_meterr2, st_lum, st_lumerr1, st_lumerr2, st_logg, st_loggerr1, stlogger2, st_age, st_ageerr1, st_ageerr2, st_dens, st_denserr1, st_denserr2, sy_dist, sy_disterr1, sy_disterr2

# Solar System Planets
# https://dataherb.github.io/flora/planets_in_solar_system/

import pandas as pd

EXOPLANETS_PATH = 'data/exoplanets.csv'
EXOPLANETS_HEADER = 290
SOLARPLANETS_URL = 'https://raw.githubusercontent.com/InterImm/dataset-planets-in-solar-system/master/dataset/planets_in_solar_system.csv'

descriptions = pd.read_csv(EXOPLANETS_PATH, nrows=EXOPLANETS_HEADER - 1)[2:-1].iloc[:, 0].tolist()
descriptions_clear = [description.split(':')[1].strip() for description in descriptions]

columns_considered = [
    'pl_name', 'hostname', 'discoverymethod', 'pl_controv_flag', 'sy_snum', 'sy_pnum', 'sy_mnum',
    'pl_orbper', 'pl_orbpererr1', 'pl_orbpererr2', 'pl_rade', 'pl_radeerr1', 'pl_radeerr2',
    'pl_masse', 'pl_masseerr1', 'pl_masseerr2', 'pl_dens', 'pl_denserr1', 'pl_denserr2',
    'pl_orbeccen', 'pl_orbeccenerr1', 'pl_orbeccenerr2', 'pl_insol', 'pl_insolerr1', 'pl_insolerr2',
    'pl_eqt', 'pl_eqterr1', 'pl_eqterr2', 'pl_orbincl', 'pl_orbinclerr1', 'pl_orbinclerr2',
    'st_teff', 'st_tefferr1', 'st_tefferr2', 'st_rad', 'st_raderr1', 'st_raderr2',
    'st_mass', 'st_masserr1', 'st_masserr2', 'st_lum', 'st_lumerr1', 'st_lumerr2', 
    'st_logg', 'st_loggerr1', 'st_loggerr2', 'st_age', 'st_ageerr1', 'st_ageerr2', 
    'st_dens', 'st_denserr1', 'st_denserr2', 'sy_dist', 'sy_disterr1', 'sy_disterr2'
]

columns_clear = []
for column in columns_considered:
    for idx, description in enumerate(descriptions):
        if column in description:
            if 'st_radv' in description:
                continue
            description_clear = description.split(':')[1].strip()
            if 'Limit' in description_clear or description_clear in columns_clear:
                continue
            columns_clear.append(description_clear)

exoplanets = pd.read_csv(EXOPLANETS_PATH, header=EXOPLANETS_HEADER, usecols=columns_considered, index_col=None)
# exoplanets.columns = columns_clear

columns_group = ['Planet Name', 'Host Name']
exoplanets_grouped = exoplanets.groupby(columns_group).mean()
exoplanetzzs_grouped = exoplanets_grouped.reset_index()

solarplanets = pd.read_csv(SOLARPLANETS_URL)

# TODO: make a moving graph of how fast planets go around their star, including earth
