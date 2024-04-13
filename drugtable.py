global table # ID, Price, Amount, Name
global money
from bs4 import BeautifulSoup
with open('saves/save.xml', 'r') as f:
    save = f.read()

Bs_save = BeautifulSoup(save, "xml")

# Find the meth tag
meth = Bs_save.find('meth')
cocaine = Bs_save.find('cocaine')
heroin = Bs_save.find('heroin')
marijuana = Bs_save.find('marijuana')
opium = Bs_save.find('opium')
money = 100
savetable = [
    [0, 10, 0, 'Meth'],
    [1, 20, 0, 'Cocaine'],
    [2, 30, 0, 'Heroin'],
    [3, 40, 0, 'Marijuana'],
    [4, 50, 0, 'Opium'],
]
loadtable = [
    [0, meth['price'], 0, 'Meth'],
    [1, cocaine['price'], 0, 'Cocaine'],
    [2, heroin['price'], 0, 'Heroin'],
    [3, marijuana['price'], 0, 'Marijuana'],
    [4, opium['price'], 0, 'Opium'],
]
