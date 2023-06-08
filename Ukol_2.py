import pandas
from scipy import stats

#INFLACE
data_inflace = pandas.read_csv('data.csv')

print(data_inflace.head())

#Test normality obou skupin
#H0: Procento lidí, kteří považují inflaci a růst životních nákladů za jeden ze svých nejzávažnějších problémů, má normální rozdělení.
#H1: Procento lidí, kteří považují inflaci a růst životních nákladů za jeden ze svých nejzávažnějších problémů, nemá normální rozdělení.

tn_1 = stats.shapiro(data_inflace["98"])
tn_2 = stats.shapiro(data_inflace["97"])
print(tn_1)
print(tn_2)
#Jelikož je p-hodnota větší než hladina významnosti 0.05, nezamítáme nulovou hypotézu. Data v obou letech mají normální rozdělení a lze použít parametrický test (párový t-test).

#Párový t-test
#H0: Procento lidí, kteří považují inflaci a růst životních nákladů za jeden ze svých nejzávažnějších problémů, je stejné v obou obdobích. 
#H1: Procento lidí, kteří považují inflaci a růst životních nákladů za jeden ze svých nejzávažnějších problémů, se v obou obdobích liší.
res = stats.ttest_rel(data_inflace["97"], data_inflace["98"])
print(res)
#p-hodnota je menší než hladina významnosti 0.05. Nulová hypotéza se zamítá. Procento lidí, kteří považují inflaci a růst životních nákladů za jeden ze svých nejzávažnějších problémů, se změnilo.


#Důvěra ve stát a v EU
data_eu = pandas.read_csv('data.csv')

print(data_eu.head())

#Omezeni pouze pro státy EU (možná nejdřív načíst země eu a pak k nim přidat hodnocení lidí)
#data_eu = pandas.merge(data_stat_eu, countries, on=['Country'], how = 'outer')
#print(data_eu)

#Test normality obou skupin
#H0: Procento lidí, kteří věří své vládě, má normální rozdělení.
#H1: Procento lidí, kteří věří své vládě, nemá normální rozdělení.

#H0: Procento lidí, kteří věří EU, má normální rozdělení.
#H1: Procento lidí, kteří věří EU, nemá normální rozdělení.

tn_1 = stats.shapiro(data_eu["National Government Trust"])
tn_2 = stats.shapiro(data_eu["EU Trust"])
print(tn_1)
print(tn_2)
#Jelikož je p-hodnota větší než hladina významnosti 0.05, nezamítáme nulovou hypotézu. Důvěřa lidí ve vládu i v EU mají normální rozdělení a lze použít parametrický test.


#Pearsonův korelační koeficient
#H0: Důvěra lidí ve vládu a EU není statisticky závislá. 
#H1: Důvěra lidí ve vládu a EU je statisticky závislá. 

res = stats.pearsonr(data_eu["National Government Trust"], data_eu["EU Trust"])
print(res)
#p-hodnota je menší než hladina významnosti 0.05. Nulová hypotéza se zamítá. Důvěra lidí ve vládu a v EU je statisticky závislá.