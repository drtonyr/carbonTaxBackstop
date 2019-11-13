#!/usr/bin/python3

# ./carbonTaxBackstop.py && git commit -m auto docs/* ; git push

config='''
## you might want to play with this block
exclItem = ['4.1.1', '4.1.2']          # excluded items
inclItem = ['13.3', '13.4.2', '14.6']  # included items
nyear = 10        # the number of years taken to get to Net Carbon Zero
nEquality = 1     #  decile with no net impact
nEqualityZero = 6 #  decile with no net impact when no decarbonisation fund
ctaxLo = 200      # the low  illustrative Carbon Tax rate in £/tCO2e
ctaxHi = 500      # the high illustrative Carbon Tax rate in £/tCO2e
thresholdPC = 50  # the percentage increase over nyear considered small (30% works for £400/t, 40% at £500/t, 60% at £800/t)
cacheImg = True   # set to False to recalculate images even if already present

## you probably don't want to play with this block
path = r'docs/basicCarbonTaxUK.xls' # name of cached spreadsheet 
ndec = 10      # number of decile divisions
nChange = ndec # number of decile to illustrate expenditure change
npoly = 1      # polynomial order
'''
exec(config)

import os
import re
import sys
import math
import time
import pandas as pd # ubuntu: apt install python3-pandas python3-xlrd
import subprocess
import matplotlib.pyplot as plt
import numpy as np
import numpy.polynomial.polynomial as nppp

# disk cache a URL - fetch if it doesn't already exist
def cacheURL(url, path):
  if not os.path.exists(path):
    from urllib.request import Request, urlopen

    urlp = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}))
    with open(path, 'wb') as fdata:
      fdata.write(urlp.read())
    urlp.close()

# fetch the spreadsheet if we don't already have it
cacheURL('https://www.ons.gov.uk/file?uri=/peoplepopulationandcommunity/personalandhouseholdfinances/expenditure/datasets/detailedhouseholdexpenditurebyequivaliseddisposableincomedecilegroupoecdmodifiedscaleuktable31e/financialyearending2018/table31efinal201718.xls', path)

df = pd.read_excel(path).transpose()

# avoid zeros - if zero assume uniform on [0.0,0.1] and use mean
# a lower value can also be justified, but it makes little difference
minData =  0.05
weeksInYear = 365.24 / 7
def toYear(rows):
  raw = [float(x) if not isinstance(x, str) else 0.0 for x in rows]
  return [minData * weeksInYear if x == 0.0 else x * weeksInYear for x in raw]

# open the docs/README.md and write a new version
fREADME = open(os.path.join('docs', 'README.md'), 'w')
fREADME.write('''# A Carbon Tax Backstop to Guarantee Carbon Neutrality
<p align="center">
Tony Robinson<br>
Version: 1.0.%s<br>
First release: 23 September 2019<br>
This release: %s<br>
</p>
''' % (subprocess.check_output(['sha512sum', sys.argv[0]], universal_newlines=True)[0:8], time.strftime("%d %B %Y", time.localtime(os.path.getmtime(sys.argv[0])))))

fREADME.write('''
## Abstract

This work models the impact of a [Carbon Tax](https://en.wikipedia.org/wiki/Carbon_tax) on UK household spending and tax raised.  It is widely accepted that we must achieve [Carbon Neutrality](https://en.wikipedia.org/wiki/Carbon_neutrality) as soon as is practical and a carbon tax is regarded as the main economic tool to achieve this.

This work assumes that a significant carbon tax will be implemented and that the revenues raised can be used to reduce [CO2e](https://en.wikipedia.org/wiki/Carbon_dioxide_equivalent) emissions such that we achieve carbon neutrality.  Analysis of household spending from the UK gives a reasonable approximation of CO2e emissions by item expenditure.  Analysis of income elasticity by item gives an expectation of the change in spending at a given rate of carbon tax.  In order not to disadvantage the lowest income households a universal household income is included so that there is no net change to ''')

if nEquality == 1:
  fREADME.write('the first decile.')
else:
  fREADME.write('decile %d (with lower deciles gaining and higher deciles contributing).' % nEquality)

fREADME.write('''  Details of the expected changes are provided.

This analysis is modelled as a [Backstop](https://www.collinsdictionary.com/dictionary/english/backstop), that is a system that will come into effect if no other arrangement is made.  By committing to this 'worst case' scenario a country can guarantee that it will become carbon neutral whilst not having to specify every detail.  The adoptation of a backstop provides the economic pressure to find better ways to decarbonise and so achieve zero carbon with only modest expected changes in household expenditure.

This report is generated from python source code which is [freely available](https://github.com/drtonyr/carbonTaxBackstop).

## Motivation

The necessity to eliminate our [CO2e](https://en.wikipedia.org/wiki/Carbon_dioxide_equivalent) emissions is now [well establised](https://climate.nasa.gov/evidence).  A [Carbon Tax](https://en.wikipedia.org/wiki/Carbon_tax) offers a means to rectify the emissions problem.

Broadly speaking, the spectrum of climate change policy ranges between:

* Aspirational:  These polices will have a clear target but are not backed up by a detailed implementation.  They carry an execution risk because they may not be practical and aspirations may change.
* Implementational:  These have a detailed implementation, typically involving many interdependent parts which sum to the desired target.  They carry an execution risk as inevitably some parts will work out and some won't - the Danish saying "Prediction is very difficult, especially about the future." is pertinent as there are many things we can't model exactly.

It is important to achieve carbon neutrality for all policies.  Accordingly, this analysis is modelled as a [backstop](https://www.collinsdictionary.com/dictionary/english/backstop), that is a system that will come into effect if no other arrangement is made.  Many better arrangements are possible than the crude ones modelled here, and this report makes no apology for that.  The purpose of this work is not to detail the best climate change policy, it's to provide a means to guarantee the desired outcome, better means can and will be implmented so the changes required will be less than those modelled here.

A carbon tax backstop is valuable to all policies and all political parties.  It provides the ability to commit to carbon neutrality which is now of key importance to the UK electorate ([Climate crisis affects how majority will vote in UK election](https://www.theguardian.com/environment/2019/oct/30/climate-crisis-affects-how-majority-will-vote-in-uk-election-poll)).

## Methodology

This report considers the effect of a carbon tax on household consumption, both directly in terms of the amount consumed of various categories and indirectly in terms of the embedded carbon in the consumed goods and services.

Production of goods and services is highly driven by economic considerations, efficiency is well defined, a company or process that isn't as efficient as competitors will have to adapt or cease.  It is therefore expected that a carbon tax will be highly productive in driving rapid change.

Household spending is only weakly driven by economics, there is no clear definition of efficiency or what is to be optimised and behaviours change slowly.  Nevertheless, it is total household spending that drives the economy and households that vote for parliament that implement climate change policies.

This report looks a the effect of carbon tax on household spending.  It is not assumed that households will make complex economic decisions, it is assumed that the companies and processes that supply households will adapt to economic circumstances.

### Household Expenditure

The [Office for National Statistics (ONS)](https://www.ons.gov.uk/) collects and publishes a wide variety of data for the UK, specifically [Detailed household expenditure by equivalised disposable income decile group: Table 3.1E](https://www.ons.gov.uk/peoplepopulationandcommunity/personalandhouseholdfinances/expenditure/datasets/detailedhouseholdexpenditurebyequivaliseddisposableincomedecilegroupoecdmodifiedscaleuktable31e).   This breaks household expenditure down into about 140 [COICOP](https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Classification_of_individual_consumption_by_purpose_(COICOP)) categories, and further breaks down all categories into deciles of total household spending.
''')

table = {}
notable = {}

class TabItem:
  def __init__(self, name, data, parent):
    self.name   = name
    self.data   = data
    self.mean   = np.mean(data)
    self.isLeaf = True
    self.parent = parent
    self.elasticity = None

for col in df.columns:
  for offset, regex in ((0, r'\d+(\.\d+)?'), (1, r'\d+\.\d+\.\d+')):

    # find label and ensure all labels are strings
    label = df[col][offset]
    if isinstance(label, float):
      label = str(label)

    # pick out those lines that have data for table
    if isinstance(label, str) and re.fullmatch(regex, label):

      name = df[col][offset + 1]
      data = toYear(df[col][4:4+ndec])
      # fix instances of line wrap in 4.3 5.1 5.6 9.3 9.4.1 9.4.3 9.4.5 10.2
      if math.isnan(data[0]):
        name += ' ' + df[col + 1][offset + 1]
        data = toYear(df[col + 1][4:4+ndec])
      name = re.sub(r'  +', r' ', name) # one item has two spaces
      name = re.sub(r'\d+$', r'', name) # two items have footnotes
        
      if label in exclItem or (re.match('1[34]', label) and label not in inclItem):
        notable[label] = name
        continue

      parent = re.sub(r'\.\d+$', r'', label)
      if parent != label:
        if parent in table:
          table[parent].isLeaf = False
        table[label] = TabItem(name, data, parent)
      else:
        table[label] = TabItem(name, data, None)

leaves = [x for x in table if table[x].isLeaf]

fREADME.write('''
This work adjusts COICOP categories for a few items.  Some items have been excluded as they don't form part of the total calculation:

|    | Excluded item description |
|:---|:--------------------------|
''')

for item in exclItem:
  fREADME.write('| %s | %s |\n' % (item, notable[item]))

fREADME.write('''

Some non-COICOP items in the ONS data were included as they constituted significant discretionary spending:

|    | Included item description |
|:---|:--------------------------|
''')

for item in inclItem:
  fREADME.write('| %s | %s |\n' % (item, table[item].name))

fREADME.write('''

The weekly expenditures provided have been scaled to annual expenditures.  Throughout this work all values are per annum (e.g. £ and CO2e).

### Calculation Of Carbon Footprint

Various sources are used to estimate the mass of CO2e emitted per pound spent (kgCOe2/£).  In the case of fuel the emissions are known and current household prices were used.  Other sources were researched and are documented in the code.  Hierarchical inheritance is used so that if a value is not know it is assumed to be the same as it's parent.  As can be seen later, only a few items dominate the household CO2e emissions and so it is felt that the approximations used are appropriate.
''')
                               
total = [0.0] * ndec
for leaf in leaves:
  total = [sum(x) for x in zip(total, table[leaf].data)]

for leaf in leaves:
  item = table[leaf]
  ## linear code
  linearPoly = nppp.Polynomial.fit(total, item.data, npoly)
  # plt.plot(total, item.data, 'o', t, poly(t), '-')

  ## log linear code
  logLinPoly = nppp.Polynomial.fit(total, [math.log(x) for x in item.data], npoly)
  # plt.plot(total, item.data, 'o', [math.exp(x) for x in t], poly(t), '-')

  ## log log code
  logLogPoly = nppp.Polynomial.fit([math.log(x) for x in total], [math.log(x) for x in item.data], npoly)

  coef = linearPoly.convert().coef
  if len(coef) > 1:
    table[leaf].elasticity = coef[1]
  else:
    table[leaf].elasticity  = 0.0

  # generate elasticity images if required
  img = os.path.join('docs', leaf + '.png')
  if not cacheImg or not os.path.exists(img):
    tmin = 0.5 * total[0] # could be from 0 to total[0]
    t = np.linspace(tmin, total[-1], 200)
    plt.figure(figsize=(10,4))
    plt.plot(total, item.data, 'o', t, linearPoly(t), '-', t, np.exp(logLinPoly(t)), ':', t, np.exp(logLogPoly(np.log(t))), '--')
    plt.title(leaf + ': ' + item.name)
    if tmin < total[0]:
      plt.xlim(0)
      plt.ylim(0, 1.15 * max(item.data))
    plt.xlabel('Household expeniture (£ per year)')
    plt.ylabel('Item expenditure (£ per year)')
    plt.legend(['Data', 'Linear', 'Exponential', 'Monomial'], loc='lower right')
    plt.savefig(img)
    plt.close()

# put in some rough numbers for kgCO2e per £ - exact numbers don't matter as they are all very similar and small except fuel
kgCO2epp = {
  '1.1':    0.72,     # from carbonfootprint.com for a vegetarian - meat is overwritten below
  '1.2':    0.72,     # as 1.1
  '1.1.5':  18/10,    # beef is about £10/kg, mince half this, steak more. foodemissions.com says 18 kgCO2e/kg
  '1.1.6':  5.7/5,    # pork is £3/kg to £7/kg at Tesco - use £5/kg.  foodemissions.com says 5.7 kgCO2e/kg
  '1.1.7':  25/11,    # lamb is £8/kg to £14/kg at Tesco - use £11/kg.  foodemissions.com says 25 kgCO2e/kg
  '1.1.7':  3.5/3.7,  # factory chicken is £2/kg to £5/kg at Tesco - use £2.5/kg.  foodemissions.com says 3.7 kgCO2e/kg
  '1.1.9':  5.4/14,   # cod and salmon about £14/kg at Tesco.  foodemissions.com says 5.4 kgCO2e/kg for cod and salmon
  '1.1.10': 1.3,      # other meats - rough average of meats above
  '2.1.2':  1.2/8,    # tesco is £8 bottle bordeaux. https://www.theguardian.com/lifeandstyle/2008/sep/07/foodanddrink12 says 1.2kg per bottle bordeaux
  '3.1':    0.33,     # from carbonfootprint.com for 'Clothes, textiles and shoes'
  '3.2':    0.33,     # from carbonfootprint.com for 'Clothes, textiles and shoes'
  '4.4.1':  0.3072/0.1325, # 100% renewable electicity costs 13.25p/kWh and converts at 0.3072 kgCO2e/kWh
  '4.4.2':  0.184/0.0287,  # "100% green" (sic) natural gas costs 2.87p/kWh and converts at 0.184 kgCO2e/kWh
  '5.1':    0.50,     # from carbonfootprint.com for 'Furniture'
  '5.2':    0.50,     # from carbonfootprint.com for 'Furniture'
  '5.3':    0.50,     # from carbonfootprint.com for 'Furniture'
  '5.4':    0.50,     # from carbonfootprint.com for 'Furniture'
  '5.5':    0.50,     # from carbonfootprint.com for 'Furniture'
  '5.6':    0.50,     # from carbonfootprint.com for 'Furniture'
  '6.1.1':  0.66,     # from carbonfootprint.com for 'Pharmaceuticals'
  '7.1':    0.78,     # from carbonfootprint.com for 'Motor vehicles (not including fuel costs)'
  '8.2':    0.39,     # from carbonfootprint.com for 'Television, radio and phone (equipment)'
  '8.3':    0.62,     # from carbonfootprint.com for 'Telephone, mobile/cell phone call costs'
  '9.1':    0.65,     # from carbonfootprint.com for 'Computers and IT equipment'
  '9.2':    0.29,     # from carbonfootprint.com for 'Recreational, cultural and sporting activities'
  '9.3':    0.29,     # from carbonfootprint.com for 'Recreational, cultural and sporting activities'
  '9.4':    0.29,     # from carbonfootprint.com for 'Recreational, cultural and sporting activities'
  '9.5':    0.66,     # from carbonfootprint.com for 'Paper based products (e.g. books, magazines, newspapers)'
  '9.6.1':  0.51,     # from carbonfootprint.com for 'Hotels, restaurants, and pubs etc.'
  '9.6.2':  2.0,      # FIX THIS - holidays abroad is 50% flights, 50% hotels
  '10.1':   0.25,     # from carbonfootprint.com for 'Education'
  '11.1':   0.51,     # from carbonfootprint.com for 'Hotels, restaurants, and pubs etc.'
  '12.4':   0.31,     # from carbonfootprint.com for 'Insurance'
  '14.6':   0,        # Assumed zero - Savings and investments
  '7.2.2':  2.31/1.30, # petrol 2.31 kg per litre (from https://people.exeter.ac.uk/TWDavies/energy_conversion/Calculation%20of%20CO2%20emissions%20from%20fuels.htm) and £1.30 per litre
  '13.4.2':  0 # Assumed zero - Cash gifts and donations
}

kgCO2epp['4.4.3'] = kgCO2epp['7.2.2'] # 'other fuels' as petrol
kgCO2epp['1.1.8'] = kgCO2epp['1.1.6'] # 'bacon/ham' - as per pork

# fill in all values
for leaf in leaves:
  if not leaf in kgCO2epp:
    parent = table[leaf].parent
    if parent in kgCO2epp:
      kgCO2epp[leaf] = kgCO2epp[parent]
    else:
      # print("using default for", leaf, table[leaf].name)
      kgCO2epp[leaf] = 0.5 # set default value

fREADME.write('''
We can now summarise all expenditure items with their CO2e impact and the new costs under different carbon tax rates.  To illustrate the impact a low price of £%d/tCO2e and a high price of £%d/tCO2e are used.
''' % (ctaxLo, ctaxHi))

fREADME.write('''
It is assumed that a carbon tax would be introduced gradually over a %d year timescale.  As such items that increase in cost less than %d percent (%0.2f percent per year) have been excluded for clarity.  The full table can be found in the appendix.
''' % (nyear, thresholdPC, (math.exp(math.log(1.0 + thresholdPC / 100) / nyear) - 1) * 100))

def writeItemTable(threshold):
  fREADME.write('''
| Item description | £  | kgCO2/£ | kgCO2 | £ (%%up) at £%d/t| £ (%%up) at £%d/t|
|:-----------------|---:|--------:|------:|-----------------:|-----------------:|
''' % (ctaxLo, ctaxHi))

  sumExpend = sumkgCO2e = 0.0
  kgCO2e = {}
  for leaf in leaves:
    kgCO2e[leaf] = kgCO2epp[leaf] * table[leaf].mean
    costLo = table[leaf].mean + kgCO2e[leaf] * ctaxLo / 1000
    pcUpLo = 100 * (costLo / table[leaf].mean - 1)
    costHi = table[leaf].mean + kgCO2e[leaf] * ctaxHi / 1000
    pcUpHi = 100 * (costHi / table[leaf].mean - 1)
    if(pcUpHi > threshold):
      fREADME.write('| %s %s | £%0.0f | %0.2f | %0.0f | £%0.0f (%d%%) | £%0.0f (%d%%) |\n' % (leaf, table[leaf].name, table[leaf].mean, kgCO2epp[leaf], kgCO2e[leaf], costLo, pcUpLo, costHi, pcUpHi)) 
    sumExpend += table[leaf].mean
    sumkgCO2e += kgCO2e[leaf]
  fREADME.write('| Household total | £%0.0f |  | %0.0f |\n\n' % (sumExpend, sumkgCO2e))

writeItemTable(thresholdPC)

fREADME.write('''
Note that no changes in manufacturing or consumption have been included in the table above.  This is a backstop calculation and at this stage we are just interested in the 'worse case' change.

### Carbon Footprint By Decile And Universal Income

The ONS data is segmented into income deciles so the carbon footprint can be calculated for each income segment under the two illustrative carbon tax rates.  The universal income is set so that there is no net effect to decile %d and so the net effect of tax and universal income can be calculated (this number is one of the parameters of the code - changing it and running again results in a different report). 
''' % (nEquality))

fREADME.write('''
| Decile | expenditure | tCO2e | ctax at £%d/t | ctax-UI at £%d/t | ctax at £%d/t | ctax-UI at £%d/t |
|:------:|--------------:|------:|--------------:|-----------------:|--------------:|-----------------:|
''' % (ctaxLo, ctaxLo, ctaxHi, ctaxHi))

def decileCO2e(index):
  kgCO2e = 0.0
  for leaf in leaves:
    kgCO2e += table[leaf].data[index] * kgCO2epp[leaf]
  return(kgCO2e / 1000)

uiLo = decileCO2e(nEquality - 1) * ctaxLo
uiHi = decileCO2e(nEquality - 1) * ctaxHi
lines = []
for index in range(0, ndec):
  tCO2e  = decileCO2e(index)
  expend = total[index]
  line   = (index + 1, expend, tCO2e, tCO2e * ctaxLo, tCO2e * ctaxLo - uiLo, tCO2e * ctaxHi, tCO2e * ctaxHi - uiHi)
  fREADME.write('| %d | £%0.0f | %0.1f | £%0.0f | £%0.0f | £%0.0f | £%0.0f |\n ' % line)
  lines.append(line)
mean = [np.mean([lines[j][i] for j in range(len(lines))]) for i in range(len(lines[0]))]
fREADME.write('| mean | £%0.0f | %0.1f | £%0.0f | £%0.0f | £%0.0f | £%0.0f |\n ' % tuple(mean[1:]))

fREADME.write('''

Looking at decile %d we see that the Universal Income is set to exactly match the carbon tax.  Deciles higher than this benefit financially, those lower fund decarbonisation.  The numbers in this table still don't reflect the change in expenditure due to price changes or any benefits of decarbonisation.''' % (nEquality))

fREADME.write('''

### Income Elasticity Of Demand

The [Income elasticity of demand](https://en.wikipedia.org/wiki/Income_elasticity_of_demand) measures the change in demand of an expenditure item with change in income.  Commonly the model assumes that the relative change in demand is proportional to the relative change in income, or equivalently that demand is an [exponential function](https://en.wikipedia.org/wiki/Exponential_function).  It is also possible to model demand as a [linear function](https://en.wikipedia.org/wiki/Linear_function) of income or as a [monomial](https://en.wikipedia.org/wiki/Monomial).

Elasticity has been estimated using all three functions. The appendix contains plots for all expenditure items and one is given below.   As can be seen there is no clear best fit, so for simplicity a linear relationship is used in the remainder of this work.

![7.2.2](7.2.2.png)

Note that whilst we regard income as the total of expenditure items, the income elasticity of demand model is not constrained so that the total change in demand equates to the change in income.  Thus, if we apply a change in income it predicts a change in expenditure for each item but the total of predicted item expenditures does not equal the total expenditure.  Other models could be developed but ethos of this work is to keep things as simple as possible so the process is iterated until the totals match.

Another major limitation of this model is that it does not consider cross correlations, that is that the change in demand of one item may affect another.  For example, when the carbon tax on natural gas makes electricity more economical for home heating it can be assumed that there will be a drastic reduction in gas usage and an equivalent increase in electricity usage.  More subtly, it also assumes that a household which has exactly the same increase in costs due to carbon tax as is matched with the universal income will not change any expenditures.  Whilst this may be true for many households, others may chose to spend on low carbon goods and so reduce carbon emissions.

### Change In Expenditure Under A Carbon Tax

It is now possible to calculate the expected change in demand for expenditure items and the CO2e for these items.  For every expenditure decile the carbon tax over all expenditure items is calculated.  If that matches the universal income then the books ballance and no further changes are necessary.  If there is a mismatch then the income elasticity of demand curves are used to adjust expenditure on each item until the carbon tax does match the universal income. 
''')

def expend2CO2e(expend):
  return np.dot(expend, [kgCO2epp[leaf] for leaf in leaves]) / 1000

# WARNING - really bad code - reads and overwrites global variables
def writeExpendChange(nEqual, nDump):

  fREADME.write('''

| Decile | prior expenditure | +ctax -UI at £%d/t | %%decrease in expenditure | prior tCO2e | post tCO2e | %%decrease in CO2e |
|:------:|------------:|-----------------:|--------------------------:|------------:|------------:|----:|
''' % (ctaxHi))

  lines = []
  uiTarget = decileCO2e(nEqual - 1) * ctaxHi
  for index in range(0, ndec):
    expend = [table[leaf].data[index] for leaf in leaves]
    initCO2e = expend2CO2e(expend)
    target = np.sum(expend) + uiTarget
    ctSum  = expend2CO2e(expend) * ctaxHi
    diff = np.sum(expend) + ctSum - target
    while abs(diff) > 0.01: # iterate until correct to the nearest penny

      # recompute expenditure to as to be closer to target
      expend = np.add(expend, [ - table[leaf].elasticity * diff for leaf in leaves ])

      # recompute the carbon tax at the current level of expenditure
      ctSum = expend2CO2e(expend) * ctaxHi

      diff = np.sum(expend) + ctSum - target

    quitCO2e = expend2CO2e(expend)
    line   = (index + 1, total[index], ctSum - uiTarget, 100 * (ctSum - uiTarget) / total[index], initCO2e, quitCO2e, 100 * (initCO2e - quitCO2e) / initCO2e)
    fREADME.write('| %d | £%0.0f | £%0.0f | %0.0f%% | %0.1f | %0.1f | %0.0f%% |\n' % line)
    lines.append(line)

    # if example decile then dump out
    if index == nDump - 1:
      eQuit = expend
      
  m = [np.mean([lines[j][i] for j in range(len(lines))]) for i in range(len(lines[0]))]
  # means of changes are the same as changes in means, so fix up
  m[3] = 100 * (m[1] - m[2]) / m[1]
  m[6] = 100 * (m[4] - m[5]) / m[4]
  fREADME.write('| mean | £%0.0f | £%0.0f | %0.0f%% | %0.1f | %0.1f | %0.0f%% |\n\n' % tuple(m[1:]))
  return m, list(eQuit)

mean, change = writeExpendChange(nEquality, nChange)
  
fREADME.write('''
Thus a carbon tax of £%d/tCO2e would be expected to raise £%0.0f p.a. per household and reduce average emissions from %0.1f tCO2e p.a. to %0.1f tCO2e p.a, a reduction of %0.0f%%.''' % (ctaxHi, mean[2], mean[4], mean[5], mean[6]))

fREADME.write('''  The change in expenditure is assumed to occur over %d years and so is %0.1f%% per year.  Note that this is the 'worse case' backstop, we still haven't factored in the decarbonisation of expenditure and so the changes would be significantly less than this.
''' % (nyear, (math.exp(math.log(1.0 + (mean[3] / 100)) / nyear) - 1.0) * 100))

fREADME.write('''

Note also that the percentage reduction in CO2e emitted is pretty much the same as the percentage decrease in household expenditure.   Households are expected to make larger reductions in high carbon items, but most expenditure has about the same amount of embedded carbon.  Thus the accuracy of the income elasticity of demand is not key to the operation of a carbon tax backstop, it merely provides the motivation to efficiently decarbonisation the production and supply of the consumed goods.

## Carbon Tax And Decarbonisation

So far we've assumed a high rate of carbon tax and seen that the worst case effect of the backstop is likely to be a small reduction in household spending every year and consequently a small reduction in CO2e per year - all of this done without significant decarbonisation.

There are many ways to decarbonise our economy.  Many items are reasonably achievable, wind is already the most economical way to generate electricity in the UK and solar worldwide.  The hardest areas to decarbonise are where the high energy density of fossil fuels can't easily be replaced, such as in aviation.  Thus the worse case is when we have to remove CO2e from the atmosphere, and this was used to set the carbon tax rate.

The cost of [Carbon Capture and Storage (CCS)](https://en.wikipedia.org/wiki/Carbon_capture_and_storage) is very hard to estimate.   The current marginal cost (e.g. from power plants or rewilding) is very low, but this does not scale to a Zero Carbon UK. [Bio-energy with carbon capture and storage](https://en.wikipedia.org/wiki/Bio-energy_with_carbon_capture_and_storage) and [direct air carbon capture and storage](https://en.wikipedia.org/wiki/Direct_air_capture) are both emerging technologies.  For example, figure 10.2 in [The Committee on Climate Change](https://www.theccc.org.uk) [Net Zero – Technical Report](https://www.theccc.org.uk/publication/net-zero-technical-report) has numbers around £200/tCO2e with great uncertainty.

This report calculated that a carbon tax rate of £%d/tCO2e would be expected to raise £%0.0f p.a. per household with average emissions of %0.1f tCO2e and thus support a removal rate of £%0.0f/tCO2e.  This is in line with worse case costs, so we can expect that decarbonisation would be achieved more effectively that this.''' % (ctaxHi, mean[2], mean[5], mean[2]/mean[5]))

fREADME.write('''

So what is the likely outcome of implementing a Carbon Tax Backstop?  It enables a trusted route to achieve carbon neutrality and so provides economic pressure to achieve this.  Industry would be able to plan to decarbonise and would see the economic benefit from doing so.  We have assumed worse case rates, so the real cost will be less than the numbers adopted in the backstop plan and decarbonisation will happen at considerably less cost than the worse case assumed.  Consequently the rates of revenue achieved would be considerably less than reported here.  Complete decarbonisation is not possible, but 90% should be, so the economic impact on household spending may only be 10-20% of that modeled here.   Thus the backstop achieves it's desired effect of decarbonisation without significant finanicial household burden.

## Conclusion              

Raising money through carbon tax/universal income to spend on sequestration is far from the best way to achieve carbon neutrality.  However, it does provide an effective economic incentive to implement better mechanisms and so serves it's purpose as a backstop to provide the certainty needed to prevent catastrophic climate breakdown.

---
---

## List of Appendices

''')

# read this file to find all appendix lines and list as anchor points
with open(sys.argv[0]) as fself:
  for line in fself: 
    m = re.match('## (Appendix.*) *$', line)
    if m :
      fREADME.write('[' + m.group(1) + '](#' + re.sub(':* +', '-', m.group(1).lower()) + ')  \n')
      
fREADME.write('''
## Appendix: Summary Of Assumptions And Limitations

The income elasticity of demand model is very basic, but there again the change in demand is not great for most expenditure items.  It would be an improvement to estimate the codependencies of expenditure items.  A basic model appears to be more than adequate, indeed assuming that all household expendure should carry the same rate of carbon tax would have been even more basic and would have resulted in the same conclusions.

We do not have CCS technology that can operate at scale.  Considerable capital expenditure will be required to develop this. However, this is at the far end of the backstop.  As the carbon tax will be phased in gradually over a number of years the initial low rate will discourage the emissions which are easy to eliminate and as the rate increases different techniques will come into play.   It is expected that CO2e emissions will be vastly reduced by the time this technology is needed.

This work does not consider how the carbon tax would be implemented not its effect on different sectors of the economy.  For discussion of this see [How to price carbon
to reach net-zero emissions in the UK](http://www.lse.ac.uk/GranthamInstitute/wp-content/uploads/2019/05/GRI_POLICY-REPORT_How-to-price-carbon-to-reach-net-zero-emissions-in-the-UK.pdf).

Some fossil fuels already have a significant carbon tax.  For example, petrol sold at £1.25/l includes £0.79 of VAT and duty.  At 2.31 kgCO2e/l the tax is already £340 per tCO2e.   A more indepth analysis would account for this.

## Appendix: Python Configuration

This report was generated from carbonTaxBackstop.py which can be found at [drtonyr.github.io/carbonTaxBackstop](https://drtonyr.github.io/carbonTaxBackstop).

There is a configuration section at the top of the code, the parameters used for this report were:
```
%s 
```
''' % (config))


fREADME.write('''
## Appendix: Total CO2e by item
''')

writeItemTable(0)

fREADME.write('''
## Appendix: Elasticity by item
''')

for leaf in leaves:
  fREADME.write('![' + leaf + '](' + leaf + '.png)\n')

fREADME.write('''
## Appendix: Maximum expenditure change

The maximum expenditure change occurs at the top decide.  A Carbon tax rate of £%0.0f/tCO2e is assumed.
''' % (ctaxHi))

fREADME.write('''
| Item description | kgCO2/£ | expenditure pre cTax/£ | expenditure post cTax/£ | % change |
|:-----------------|--------:|-----------------------:|------------------------:|---------:|
''')

for leaf, c in zip(leaves, change):
  init = table[leaf].data[nChange - 1]
  fREADME.write('| %s %s | %0.2f | %0.2f | %0.2f | %0.1f |\n' % (leaf, table[leaf].name, kgCO2epp[leaf], init, c, 100 * (c - init) / init))


fREADME.write('''

## Appendix: A Fiscally Neutral Carbon Tax and Household Income

It's interesting to consider the case where it's not felt necessary to fund decarbonisaton.  This would be fiscally neutral as the average household cost of the carbon tax matches the universal income.

''')

mean, _ = writeExpendChange(nEqualityZero, nChange)

fREADME.write('''
The main point to note is that there is no change in CO2e.  This is expected as the income elasticity of demand for expenditure item has been modelled independently and linearly.  The total expenditure remains the same so the increase in expenditure in lower deciles is balanced by the decrease in expenditure in upper deciles.

The fiscally neutral carbon tax provides part of the incentive to decarbonise but in a much weaker form.  The manufacturing and distribution of goods still has high incentive to decarbonise as companies and processes that don't will be replaced by more efficient companies and processes that do.  However, there is no incentive to 'go the last mile' and achieve carbon neutrality.
''')

fREADME.close()
