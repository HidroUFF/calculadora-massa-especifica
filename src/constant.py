# -*- coding: utf-8 -*-

# ============================================================
#                          CONSTANTES                         
# ============================================================

#Tabela kij
KIJ = [
	[0, 0.00224, 0.1, 0.036, 0.00683, 0.0123, 0.085, 0.0219, 0.0395, 0.03097, 0.05121, 0.044, 0.04701, 0.01427, 0.0392, 0.04, 0.0649, 0.5, 0.03496, 0.023, ],
	[0.00224, 0, 0.1298, 0.05, 0.00126, 0.0041, 0.084, 0.0082, 0.00042, 0.0032, 0.0167, 0.02199, 0.007, -0.00074, 0.0261, 0.02, 0.0344, 0.5, 0.05351, 0.05, ],
	[0.1, 0.1298, 0, -0.02, 0.135, 0.1298, 0.1, 0.125, 0.125, 0.1199, 0.115, 0.1037, 0.1181, 0.09545, 0.0901, 0.0806, 0.0936, -0.5572, 0.0975, 0.0, ],
	[0.036, 0.05, -0.02, 0, 0.08, 0.09, 0.1676, 0.1015, 0.1415, 0.1535, 0.171, 0.1778, 0.1205, 0.21136, 0.1, 0.1597, 0.1932, -2.238, -0.012, 0.0, ],
	[0.00683, 0.00126, 0.135, 0.08, 0, 0.00082, 0.075, 0.00471, 0.00682, 0.00769, 0.00725, 0.00697, 0.0062, -0.01397, 0.0143, 0.02, 0.031, 0.48, 0.07318, 0.03753, ],
	[0.123, 0.0041, 0.1298, 0.09, 0.00082, 0, 0.06, -3e-05, 0.00091, 0.00083, -0.00032, -0.00118, -0.00239, -0.02143, 0.00578, 0.01019, 0.00601, 0.48, 0.09399, 0.1151, ],
	[0.085, 0.084, 0.1, 0.1676, 0.075, 0.06, 0, 0.04972, 0.05915, 0.06596, 0.055, 0.05, 0.0356, -0.00488, 0.05874, 0.009, 0.0081, -0.3896, 0.0, 0.0, ],
	[0.0219, 0.0082, 0.125, 0.1015, 0.00471, -3e-05, 0.04972, 0, -0.00049, -0.00117, -0.00277, -0.00399, -0.00546, -0.02365, 0.0013, 0.016, 0.013, 0.48, 0.11518, 0.0713, ],
	[0.0395, 0.00042, 0.125, 0.1415, 0.00682, 0.00091, 0.05915, -0.00049, 0, -0.00184, -0.0038, -0.0053, -0.00701, -0.02478, -0.003, 0.007, 0.008, 0.48, 0.095, 0.02132, ],
	[0.03097, 0.0032, 0.1199, 0.1535, 0.00769, 0.00083, 0.06596, -0.00117, -0.00184, 0, -0.00292, -0.00463, -0.0065, -0.02394, -0.0072, -0.002, 0.006, 0.48, 0.1587, 0.0866, ],
	[0.05121, 0.0167, 0.115, 0.171, 0.00725, -0.00032, 0.055, -0.00277, -0.0038, -0.00292, 0, -0.00257, -0.00456, -0.02171, -0.00906, 0.003, -0.004, 0.48, 0.156, 0.11463, ],
	[0.044, 0.02199, 0.1037, 0.1778, 0.00697, -0.00118, 0.05, -0.00399, -0.0053, -0.00463, -0.00257, 0, -0.0028, -0.01984, -0.01051, -0.00524, -0.00953, 0.48, 0.20298, 0.11241, ],
	[0.04701, 0.007, 0.1181, 0.1205, 0.0062, -0.00239, 0.0356, -0.00546, -0.00701, -0.0065, -0.00456, -0.0028, 0, -0.01768, 0.01, 0.01, 0.01, 0.48, 0.22529, 0.12404, ],
	[0.01427, -0.00074, 0.09545, 0.21136, -0.01397, -0.02143, -0.00488, -0.02365, -0.02478, -0.02394, -0.02171, -0.01984, -0.01768, 0, -0.03171, -0.00746, -0.02722, 0.48, 0.3305, 0.14388, ],
	[0.0392, 0.0261, 0.0901, 0.1, 0.0143, 0.00578, 0.05874, 0.0013, -0.003, -0.0072, -0.00906, -0.01051, 0.01, -0.03171, 0, 0.02012, 0.003, 0.48, 0.11405, 0.04707, ],
	[0.04, 0.02, 0.0806, 0.1597, 0.02, 0.01019, 0.009, 0.016, 0.007, -0.002, 0.003, -0.00524, 0.01, -0.00746, 0.02012, 0, 0.009, 0.48, 0.09588, 0.03466, ],
	[0.0649, 0.0344, 0.0936, 0.1932, 0.031, 0.00601, 0.0081, 0.013, 0.008, 0.006, -0.004, -0.00953, 0.01, -0.02722, 0.003, 0.009, 0, 0.48, 0.208, 0.06096, ],
	[0.5, 0.5, -0.5572, -2.238, 0.48, 0.48, -0.3896, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0, 0.0, 0.5, ],
	[0.03496, 0.05351, 0.0975, -0.012, 0.07318, 0.09399, 0.0, 0.11518, 0.095, 0.1587, 0.156, 0.20298, 0.22529, 0.3305, 0.11405, 0.09588, 0.208, 0.0, 0, 0.0104, ],
	[0.023, 0.05, 0.0, 0.0, 0.03753, 0.1151, 0.0, 0.0713, 0.02132, 0.0866, 0.11463, 0.11241, 0.12404, 0.14388, 0.04707, 0.03466, 0.06096, 0.5, 0.0104, 0, ],
]

# Listas dos fluidos
# [Massa molar(g/mol), Pressão crítica(KPa), Temperatura crítica (K), Fator acênctrico]
metano = [16.04, 4641, 190.55, 0.0115]
etano = [30.07, 4884, 305, 0.0986]
co2 = [44.01, 7370, 304.13, 0.2389]
n2 = [28.01, 3394, 130, 0.0400]
propano = [44.1, 4257, 369.75, 0.1524]
n_butano = [58.12, 3797, 425, 0.2010]
h2s = [34.08, 9008, 373.65, 0.0810]
n_pentano = [72.15, 3419.72, 469.5, 0.2539]
n_hexano = [86.18, 3072.17, 507.7, 0.3007]
n_heptano = [100.21, 2773.27, 540.0, 0.3498]
n_octano = [114.23, 2530.09, 568.4, 0.4018]
n_nonano = [128.2, 2330.48, 594.4, 0.4455]
n_decano = [170.33, 2135.93, 617.4, 0.4885]
n_pentadecano = [212.42, 1537.10, 706.9, 0.7060]
ciclohexano = [84.16, 4106.70, 553.1, 0.2133]
benzeno = [78.11, 4989.24, 561.9, 0.2150]
tolueno = [92.14, 4154.33, 591.6, 0.2596]
agua_pura = [18.01528, 22413.09, 647.1, 0.3440]
gas_oxigenio = [15.999, 5147.31, 154.6, 0.0190]
argonio = [39.948, 4928.45, 150.6, -0.0040]

ELEMENTOS = [metano, etano, co2, n2, propano, n_butano, h2s, n_pentano, n_hexano, n_heptano, n_octano, 
n_nonano, n_decano, n_pentadecano, ciclohexano, benzeno, tolueno, agua_pura, gas_oxigenio, argonio]

SUBSTANCIAS = ["METANO", "ETANO", "CO2", "N2", "PROPANO", "N-BUTANO", "H2S", "N-PENTANO", "N-HEXANO", "N-HEPTANO", "N-OCTANO", 
"N-NONANO", "N-DECANO", "N-PENTADECANO", "CICLOHEXANO", "BENZENO", "TOLUENO", "ÁGUA PURA", "GÁS OXIGÊNIO", "ARGÔNIO"]
SUBSTANCES = ["METHANE", "ETHANE", "CO2", "N2", "PROPANE", "N-BUTANE", "H2S", "N-PENTANE", "N-HEXANE", "N-HEPTANE", "N-OCTANE", 
"N-NONANE", "N-DECAN", "N-PENTADECAN", "CYCLOHEXANE", "BENZENE", "TOLUENE", "PURE WATER", "OXYGEN GAS", "ARGON"]
SUSTANCIAS = ["METANO", "ETANO", "CO2", "N2", "PROPANO", "N-BUTANO", "H2S", "N-PENTANO", "N-HEXANO", "N-HEPTANO", "N-OCTANO", 
"N-NONANO", "N-DECANO", "N-PENTADECANO", "CICLO-HEXANO", "BENCENO", "TOLUENO", "AGUA PURA", "GAS OXIGENO", "ARGÓN"]

# Número de fluidos cadastrados
NUM_SUBSTANCIAS = 20
