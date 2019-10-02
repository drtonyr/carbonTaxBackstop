# Carbon Tax Backstop
## WORK IN PROGRESS:  ETA EARLY OCTOBER 2019

## Abstract

This work investigates the inpact of a [Carbon Tax](https://en.wikipedia.org/wiki/Carbon_tax) on UK household spending.  It is widely accepted that we must achieve [carbon neutrality](https://en.wikipedia.org/wiki/Carbon_neutrality) as soon as is practical and a carbon tax is regarded as the main economic tool to achive this.

This work assumes that a carbon tax can implement and that the revenues raised can be used to reduce and sequester CO2e emissions such that we achieve carbon neurality.  Analysis of houshold spending from the UK gives a reasonable approximation of CO2e emissions by item expenditure.  Analysis of income elasticity by item gives an expectation of the change in spending at a given rate of carbon tax.  In order not to disavantage the lowest income households a universal household income is included so that there is no net change to the first decile.
Increasing the carbon tax thus both reduces expenditure on high carbon items and so reduces emissions and also raises revenues which can be spent on carbon sequestration and so achieve net carbon zero.  Details of the expected changes are provided.

This analysis is intentionally limited so as to to form a complete isolated work.  The tax-and-sequester method is not proposed as the best route forward, it is proposed to provide one way forward to bound the changes needed to achieve carbon neutrality.  It is clearly better not to emit than to emit-tax-and-sequester and as such it provides a backstop and economic pressure to find better solutions. [Full source code](https://github.com/drtonyr/carbonTaxBackstop) is [freely available](https://en.wikipedia.org/wiki/MIT_License).

## Motivation

Broadly speaking, there are two styles of climate change policy:

* Aspirational:  These will have a clear target but are not backed up by a detailed implementation.  They carry an execution risk because they may not be practical and aspirations may change.
* Implementational:  These have a detailed implementation, typically involving many interdependent parts which sum to the desired target.  They carry an execution risk as inevitably some parts will work out and some won't - the Danish saying "Prediction is very difficult, especially about the future." is pertient as we are in danger of hitting a tipping point.

A backstop is valuable to all policies.  It provides a commitement now to the carbon neutrality goal and an insurance policy in case some aspects do not work out as expected.

## Methodolgy

### Household expenditure

The [Office for National Statistics (ONS)](https://www.ons.gov.uk/) collects and publishes a wide variety of data for the UK, specifically [Detailed household expenditure by equivalised disposable income decile group: Table 3.1E](https://www.ons.gov.uk/peoplepopulationandcommunity/personalandhouseholdfinances/expenditure/datasets/detailedhouseholdexpenditurebyequivaliseddisposableincomedecilegroupoecdmodifiedscaleuktable31e).

This work differs from the [COICOP](https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Classification_of_individual_consumption_by_purpose_(COICOP)) categories in the ONS table for a few items.  Some items have been excluded as they don't form part of the total calculation:

|    | Excluded item description |
|:---|:--------------------------|
| 4.1.1 | Gross rent |
| 4.1.2 | less housing benefit, rebates and allowances rec'd |


Some non-COICOP items were included as they consituted significant discretionary spending:

|    | Included item description |
|:---|:--------------------------|
| 13.3 | Holiday spending |
| 13.4.2 | Cash gifts and donations |
| 14.6 | Savings and investments |


The weekly expenditures have been scaled to annual expenditures.  Throughout this work all values are per annum.

### Calculation of carbon footprint

Various sources are used to estimate the mass of CO2e emitted per pound spent (kgCOe2/£).  In the case of fuel the emissions are known and current prices were used.  Other sources were researched and are documetned in the code.  A heiractical inheritence is used so that if a value was not found it inherits from the parent class.  As can be seen later, only a few items dominate the household CO2e emissions and so it is felt that the approximations used are appropriate.

We can now summarise all expenditure items with their CO2e impact and the new costs under different carbon tax rates.  To illustrate the impact a low price of £200/tCO2e and a high price of £500/tCO2e are used.

It is assumed that a carbon tax would be introduced gradually over a 10 year timescale.  As such items that increase in cost less than 50 percent (4.14 percent per year) have been excluded for clarity.  The full table can be found in the appendix.

| Item description | £  | kgCO2/£ | kgCO2 | £(%up) at £200/t| £(%up) at £500/t|
|:-----------------|---:|--------:|------:|----------------:|----------------:|
| 1.1.5 Beef (fresh, chilled or frozen) | 103 | 1.80 | 185 | 140 (36) | 196 (90) |
| 1.1.6 Pork (fresh, chilled or frozen) | 32 | 1.14 | 36 | 39 (22) | 50 (56) |
| 1.1.8 Poultry (fresh, chilled or frozen) | 121 | 1.14 | 138 | 149 (22) | 190 (56) |
| 1.1.10 Other meat and meat preparations | 331 | 1.30 | 431 | 417 (26) | 547 (65) |
| 4.4.1 Electricity | 592 | 2.32 | 1372 | 866 (46) | 1278 (115) |
| 4.4.2 Gas | 512 | 6.41 | 3280 | 1168 (128) | 2152 (320) |
| 4.4.3 Other fuels | 69 | 1.78 | 123 | 94 (35) | 131 (88) |
| 7.2.2 Petrol, diesel and other motor oils | 1103 | 1.78 | 1961 | 1496 (35) | 2084 (88) |
| 9.6.2 Package holidays - abroad | 1311 | 2.00 | 2622 | 1835 (39) | 2622 (100) |
| Household total | 27319 |  | 21407 |


### Carbon footprint by decile and universal income

The ONS data is segmented into income deciles so the catbon footprint can be calculated for each income segment under the two illustrative catbon tax rates.  The universal income is set so that there is no net effect to decile 1 and so the net effect of tax and universal income can be calculated.

| Decile | expenditure | tCO2e | ctax at £200/t | ctax-UI at £200/t | ctax at £500/t | ctax-UI at £500/t |
|:------:|------------:|------:|--------------:|-----------------:|--------------:|-----------------:|
| 1 | 12449 | 11.3 | 2250 | 0 | 5625 | 0 |
 | 2 | 16219 | 13.9 | 2779 | 529 | 6947 | 1322 |
 | 3 | 18343 | 15.6 | 3119 | 869 | 7796 | 2171 |
 | 4 | 20842 | 17.0 | 3395 | 1145 | 8487 | 2862 |
 | 5 | 23455 | 18.8 | 3762 | 1512 | 9405 | 3780 |
 | 6 | 27734 | 21.5 | 4293 | 2043 | 10732 | 5107 |
 | 7 | 30103 | 23.7 | 4748 | 2498 | 11869 | 6244 |
 | 8 | 32965 | 25.2 | 5043 | 2793 | 12606 | 6981 |
 | 9 | 39465 | 30.5 | 6102 | 3852 | 15256 | 9631 |
 | 10 | 51615 | 36.6 | 7324 | 5074 | 18311 | 12686 |
 | mean | 27319 | 21.4 | 4281 | 2031 | 10703 | 5078 |
 

### Income elasticity of demand

The [Income elasticity of demand](https://en.wikipedia.org/wiki/Income_elasticity_of_demand) measures the change in demand of an expenditure item with change in income.  Commonly the model assumes that the relative change in depand is proportional to the relative change in income, or equivilently that demand is an [exponential function](https://en.wikipedia.org/wiki/Exponential_function).  It is also possible to model demand as a [linear function](https://en.wikipedia.org/wiki/Linear_function) of income or as a [monomial](https://en.wikipedia.org/wiki/Monomial).

Elasicity has been estimated using all three functions. The appendix contanis plots for all expenditure items and one is given below.   As can be seen there is no clear best funciton, so for simpliity a linear relationship is used in the remainder of this work.

![7.2.2](7.2.2.png)

Whilst we regard income as the total of expenditure items, the income elasticity of demand model is not constrained so that the total change in demand equates to the change in income.  Thus, if we apply a change in income it predicts a change in expenditure for each item but the total of predicted item expenditures does not equal the total expenditure.  Other models could be developed but ethos of this work is to keep things as basic as possible so the process is iterated until the totals match.

Another major limitation of this model is that it does not consider cross corelations, that is that the change in demand of one item may affect another.  For example, when the carbon tax on natural gas makes electicity more economical for home heating it can be assumed that there will be a drastic reduciton in gas usage and an equivelent increase in electicity usage.  More subtly, it also assumes that a household which has exactly the same increase in costs due to carbon tax as is matched with the universal income will not change any expenditures.  Whlist this may be true for some households, others may chose to spend on low carbon goods and so increase overall value and reduce carbon emissions.   Thus the model presented here can be considered an upper bound on what is needed, in practice we will ne able to get away with lower carbon tax rates.

### Change in expenditure under a carbon tax

It is now possible to calculate the expected change in demand for expenditure items and the CO2e for these items.  The biggest changes in behaviour occur at the highest income group, so that is used to illustrate the change.


| Decile | expenditure | ctax-UI at £500/t | %decrease in expenditure | prior tCO2e | post tCO2e  |
|:------:|------------:|-----------------:|--------------------------:|------------:|------------:|
| 1 | 12449 | 0 | 0 | 11.3 | 11.3 |
| 2 | 16219 | 993 | 6 | 13.9 | 13.2 |
| 3 | 18343 | 1631 | 9 | 15.6 | 14.5 |
| 4 | 20842 | 2150 | 10 | 17.0 | 15.6 |
| 5 | 23455 | 2840 | 12 | 18.8 | 16.9 |
| 6 | 27734 | 3837 | 14 | 21.5 | 18.9 |
| 7 | 30103 | 4692 | 16 | 23.7 | 20.6 |
| 8 | 32965 | 5245 | 16 | 25.2 | 21.7 |
| 9 | 39465 | 7236 | 18 | 30.5 | 25.7 |
| 10 | 51615 | 9532 | 18 | 36.6 | 30.3 |
| mean | 27319 | 3816 | 12 | 21.4 | 18.9 |

Thus a carbon tax of £500/tCO2e would be expected to raise £3816 p.a. per household with average emissions of 18.9 tCO2e and thus support a removal rate of £202/tCO2e. The change in expenditure is assumed to occur over 10 years and so is 1.1% per year.


### Carbon tax and carbon sequestration

Talk about marginal costs here.

The cost of [Carbon Capture and Storage (CCS)](https://en.wikipedia.org/wiki/Carbon_capture_and_storage) is very hard to estimate.   The current marginal cost (e.g. from power plants or rewilding) is very low, but this does not scale to a Zero Carbon UK. [Bio-energy with carbon capture and storage](https://en.wikipedia.org/wiki/Bio-energy_with_carbon_capture_and_storage) and [direct air carbon capture and storage](https://en.wikipedia.org/wiki/Direct_air_capture) are both emerging technologies.  For example, figure 10.2 in [The Committee on Climate Change](https://www.theccc.org.uk) [Net Zero – Technical Report](https://www.theccc.org.uk/publication/net-zero-technical-report) has numbers around £200/tCO2e with great uncertainty.

It is possible to sweep over at large range of tax rates and estimate the revenue generated and the correspondnig reduction in CO2e.  Dividing the expected CO2e by the reveue rasied gives a CSS rate which, if achieved, would result in carbon neutrality.


## Limitations and Discussion              

As noted earlier, the income elasticity of demand model is bery basic.

Most importantly, we do not have CCS technology that can operate at scale.  Considerable capital expenditure will be required to develop this. However, this is at the far end of the backstop.  As the carbon tax will be phased in gradually over a number of years the initial low rate will discourage the emissions which are easy to eliminate and as the rate increases different techniques will come into play.   CCS is at the far end and thus it is expected that CO2e emmissions will be vastly reduced by the time this technoldy is needed.

This work does not consider how the carbon tax would be implemented not its effect on different sectors of the economy.  For discussion of this see [How to price carbon
to reach net-zero emissions in the UK](http://www.lse.ac.uk/GranthamInstitute/wp-content/uploads/2019/05/GRI_POLICY-REPORT_How-to-price-carbon-to-reach-net-zero-emissions-in-the-UK.pdf).

## Conclusion              

A carbon tax with universal income is not an effective way to reduce emissions directly. However, it does provide a means to bound the changes needed to achieve carbon neutrality.

## Appendix: Python configuration

This report was generated from catbonTaxBackstop.py which can be found at [drtonyr.github.io/carbonTaxBackstop](https://drtonyr.github.io/carbonTaxBackstop).

There is a configuration section at the top of the code, the pararmeters used for this report were:
```

## you might want to play with this block
exclItem = ['4.1.1', '4.1.2']          # excluded items
inclItem = ['13.3', '13.4.2', '14.6']  # included items
nyear = 10    # the number of years taken to get to Net Carbon Zero
nEquality = 1 #  decile with no net impact
ctaxLo = 200   # the low  illustrative Carbon Tax rate in £/tCO2e
ctaxHi = 500   # the high illustrative Carbon Tax rate in £/tCO2e
thresholdPC = 50 # the percentage increase over nyear considered small (30% works for £400/t, 40% at £500/t, 60% at £800/t)
cacheImg = True  # set to False to recalulate images even if already present

## you probably don't want to play with this block
path = r'docs/basicCarbonTaxUK.xls' # name of cached spreadsheet 
ndec = 10     # number of decile divisions
npoly = 1     # polynomial order
 
```
## Appendix: Full analysis by item


| Item description | £  | kgCO2/£ | kgCO2 | £(%up) at £200/t| £(%up) at £500/t|
|:-----------------|---:|--------:|------:|----------------:|----------------:|
| 1.1.1 Bread, rice and cereals | 283 | 0.72 | 204 | 324 (14) | 385 (36) |
| 1.1.2 Pasta products | 22 | 0.72 | 16 | 26 (14) | 30 (35) |
| 1.1.3 Buns, cakes, biscuits etc | 200 | 0.72 | 144 | 228 (14) | 272 (35) |
| 1.1.4 Pastry (savoury) | 48 | 0.72 | 34 | 55 (14) | 65 (35) |
| 1.1.5 Beef (fresh, chilled or frozen) | 103 | 1.80 | 185 | 140 (36) | 196 (90) |
| 1.1.6 Pork (fresh, chilled or frozen) | 32 | 1.14 | 36 | 39 (22) | 50 (56) |
| 1.1.7 Lamb (fresh, chilled or frozen) | 33 | 0.95 | 31 | 39 (18) | 48 (47) |
| 1.1.8 Poultry (fresh, chilled or frozen) | 121 | 1.14 | 138 | 149 (22) | 190 (56) |
| 1.1.9 Bacon and ham | 46 | 0.39 | 18 | 49 (7) | 55 (19) |
| 1.1.10 Other meat and meat preparations | 331 | 1.30 | 431 | 417 (26) | 547 (65) |
| 1.1.11 Fish and fish products | 151 | 0.72 | 109 | 173 (14) | 206 (36) |
| 1.1.12 Milk | 113 | 0.72 | 81 | 129 (14) | 153 (35) |
| 1.1.13 Cheese and curd | 103 | 0.72 | 75 | 118 (14) | 141 (36) |
| 1.1.14 Eggs | 37 | 0.72 | 27 | 42 (14) | 50 (36) |
| 1.1.15 Other milk products | 122 | 0.72 | 88 | 140 (14) | 166 (35) |
| 1.1.16 Butter | 25 | 0.72 | 18 | 29 (14) | 34 (36) |
| 1.1.17 Margarine, other vegetable fats and peanut butter | 31 | 0.72 | 22 | 35 (14) | 42 (36) |
| 1.1.18 Cooking oils and fats | 18 | 0.72 | 13 | 20 (14) | 24 (35) |
| 1.1.19 Fresh fruit | 207 | 0.72 | 149 | 237 (14) | 282 (35) |
| 1.1.20 Other fresh, chilled or frozen fruits | 24 | 0.72 | 18 | 28 (14) | 33 (35) |
| 1.1.21 Dried fruit and nuts | 44 | 0.72 | 31 | 50 (14) | 59 (36) |
| 1.1.22 Preserved fruit and fruit based products | 8 | 0.72 | 6 | 9 (14) | 11 (36) |
| 1.1.23 Fresh vegetables | 224 | 0.72 | 161 | 256 (14) | 304 (36) |
| 1.1.24 Dried vegetables | 4 | 0.72 | 3 | 4 (14) | 5 (36) |
| 1.1.25 Other preserved or processed vegetables | 87 | 0.72 | 63 | 99 (14) | 118 (35) |
| 1.1.26 Potatoes | 41 | 0.72 | 29 | 46 (14) | 55 (36) |
| 1.1.27 Other tubers and products of tuber vegetables | 85 | 0.72 | 61 | 98 (14) | 116 (36) |
| 1.1.28 Sugar and sugar products | 20 | 0.72 | 15 | 23 (14) | 28 (35) |
| 1.1.29 Jams, marmalades | 16 | 0.72 | 12 | 18 (14) | 22 (36) |
| 1.1.30 Chocolate | 110 | 0.72 | 79 | 126 (14) | 149 (36) |
| 1.1.31 Confectionery products | 41 | 0.72 | 29 | 46 (14) | 55 (36) |
| 1.1.32 Edible ices and ice cream | 34 | 0.72 | 25 | 39 (14) | 47 (36) |
| 1.1.33 Other food products | 135 | 0.72 | 97 | 154 (14) | 183 (36) |
| 1.2.1 Coffee | 49 | 0.72 | 35 | 56 (14) | 66 (35) |
| 1.2.2 Tea | 23 | 0.72 | 16 | 26 (14) | 31 (35) |
| 1.2.3 Cocoa and powdered chocolate | 5 | 0.72 | 4 | 6 (14) | 7 (35) |
| 1.2.4 Fruit and vegetable juices (inc. fruit squash) | 56 | 0.72 | 40 | 64 (14) | 76 (36) |
| 1.2.5 Mineral or spring waters | 21 | 0.72 | 15 | 24 (14) | 28 (35) |
| 1.2.6 Soft drinks (inc. fizzy and ready to drink fruit drinks) | 103 | 0.72 | 74 | 118 (14) | 140 (35) |
| 2.1.1 Spirits and liqueurs (brought home) | 102 | 0.50 | 51 | 112 (9) | 127 (25) |
| 2.1.2 Wines, fortified wines (brought home) | 235 | 0.15 | 35 | 242 (3) | 252 (7) |
| 2.1.3 Beer, lager, ciders and perry (brought home) | 113 | 0.50 | 57 | 125 (10) | 142 (25) |
| 2.1.4 Alcopops (brought home) | 3 | 0.50 | 1 | 3 (10) | 3 (25) |
| 2.2.1 Cigarettes | 137 | 0.50 | 69 | 151 (10) | 172 (25) |
| 2.2.2 Cigars, other tobacco products and narcotics | 59 | 0.50 | 29 | 65 (10) | 73 (25) |
| 3.1.1 Men's outer garments | 264 | 0.33 | 87 | 281 (6) | 307 (16) |
| 3.1.2 Men's under garments | 28 | 0.33 | 9 | 29 (6) | 32 (16) |
| 3.1.3 Women's outer garments | 438 | 0.33 | 145 | 467 (6) | 511 (16) |
| 3.1.4 Women's under garments | 64 | 0.33 | 21 | 69 (6) | 75 (16) |
| 3.1.5 Boys' outer garments (5-15) | 51 | 0.33 | 17 | 55 (6) | 60 (16) |
| 3.1.6 Girls' outer garments (5-15) | 51 | 0.33 | 17 | 55 (6) | 60 (16) |
| 3.1.7 Infants' outer garments (under 5) | 34 | 0.33 | 11 | 37 (6) | 40 (16) |
| 3.1.8 Children's under garments (under 16) | 21 | 0.33 | 7 | 23 (6) | 25 (16) |
| 3.1.9 Accessories | 40 | 0.33 | 13 | 43 (6) | 47 (16) |
| 3.1.10 Haberdashery and clothing hire | 15 | 0.33 | 5 | 16 (6) | 18 (16) |
| 3.1.11 Dry cleaners, laundry and dyeing | 9 | 0.33 | 3 | 9 (6) | 10 (16) |
| 3.2 Footwear | 248 | 0.33 | 82 | 264 (6) | 288 (16) |
| 4.1.3 Net rent | 1879 | 0.50 | 939 | 2067 (10) | 2348 (25) |
| 4.1.4 Second dwelling rent | 3 | 0.50 | 1 | 3 (10) | 3 (25) |
| 4.2 Maintenance and repair of dwelling | 424 | 0.50 | 212 | 467 (10) | 530 (25) |
| 4.3 Water supply and miscellaneous services relating to the dwelling | 483 | 0.50 | 241 | 531 (9) | 603 (25) |
| 4.4.1 Electricity | 592 | 2.32 | 1372 | 866 (46) | 1278 (115) |
| 4.4.2 Gas | 512 | 6.41 | 3280 | 1168 (128) | 2152 (320) |
| 4.4.3 Other fuels | 69 | 1.78 | 123 | 94 (35) | 131 (88) |
| 5.1.1 Furniture and furnishings | 978 | 0.50 | 489 | 1075 (10) | 1222 (25) |
| 5.1.2 Floor coverings | 197 | 0.50 | 98 | 216 (10) | 246 (25) |
| 5.2 Household textiles | 117 | 0.50 | 58 | 129 (9) | 146 (25) |
| 5.3 Household appliances | 226 | 0.50 | 113 | 248 (10) | 282 (25) |
| 5.4 Glassware, tableware and household utensils | 102 | 0.50 | 51 | 112 (9) | 127 (25) |
| 5.5 Tools and equipment for house and garden | 149 | 0.50 | 74 | 164 (9) | 186 (25) |
| 5.6.1 Cleaning materials | 123 | 0.50 | 61 | 135 (9) | 153 (25) |
| 5.6.2 Household goods and hardware | 87 | 0.50 | 44 | 96 (10) | 109 (25) |
| 5.6.3 Domestic services, carpet cleaning, hire/repair of furniture/furnishings | 138 | 0.50 | 69 | 152 (10) | 172 (25) |
| 6.1.1 Medicines, prescriptions, healthcare products etc | 109 | 0.66 | 72 | 124 (13) | 145 (32) |
| 6.1.2 Spectacles, lenses, accessories and repairs | 89 | 0.50 | 45 | 98 (10) | 112 (25) |
| 6.2 Hospital services | 159 | 0.50 | 79 | 174 (9) | 198 (25) |
| 7.1.1 Purchase of new cars and vans | 514 | 0.78 | 401 | 594 (15) | 714 (39) |
| 7.1.2 Purchase of second hand cars or vans | 888 | 0.78 | 693 | 1027 (15) | 1235 (38) |
| 7.1.3 Purchase of motorcycles and other vehicles | 32 | 0.78 | 25 | 37 (15) | 44 (39) |
| 7.2.1 Spares and accessories | 124 | 0.50 | 62 | 137 (9) | 155 (25) |
| 7.2.2 Petrol, diesel and other motor oils | 1103 | 1.78 | 1961 | 1496 (35) | 2084 (88) |
| 7.2.3 Repairs and servicing | 339 | 0.50 | 169 | 372 (10) | 423 (25) |
| 7.2.4 Other motoring costs | 159 | 0.50 | 80 | 175 (10) | 199 (25) |
| 7.3.1 Rail and tube fares | 224 | 0.50 | 112 | 246 (9) | 280 (25) |
| 7.3.2 Bus and coach fares | 79 | 0.50 | 39 | 86 (10) | 98 (25) |
| 7.3.3 Combined fares | 32 | 0.50 | 16 | 36 (10) | 41 (25) |
| 7.3.4 Other travel and transport | 679 | 0.50 | 340 | 747 (10) | 849 (25) |
| 8.1 Postal services | 33 | 0.50 | 17 | 37 (10) | 42 (25) |
| 8.2 Telephone and telefax equipment | 59 | 0.39 | 23 | 63 (7) | 70 (19) |
| 8.3 Telephone and telefax services | 642 | 0.62 | 398 | 721 (12) | 841 (31) |
| 8.4 Internet subscription fees | 196 | 0.50 | 98 | 216 (10) | 245 (25) |
| 9.1.1 Audio equipment and accessories, CD players | 55 | 0.65 | 36 | 62 (12) | 73 (32) |
| 9.1.2 TV, video and computers | 182 | 0.65 | 118 | 206 (12) | 241 (32) |
| 9.1.3 Photographic, cine and optical equipment | 17 | 0.65 | 11 | 19 (12) | 22 (32) |
| 9.2 Other major durables for recreation and culture | 139 | 0.29 | 40 | 147 (5) | 159 (14) |
| 9.3.1 Games, toys and hobbies | 162 | 0.29 | 47 | 171 (5) | 185 (14) |
| 9.3.2 Computer software and games | 55 | 0.29 | 16 | 58 (5) | 63 (14) |
| 9.3.3 Equipment for sport, camping and open-air recreation | 53 | 0.29 | 15 | 56 (5) | 60 (14) |
| 9.3.4 Horticultural goods, garden equipment and plants | 134 | 0.29 | 39 | 141 (5) | 153 (14) |
| 9.3.5 Pets and pet food | 292 | 0.29 | 85 | 309 (5) | 335 (14) |
| 9.4.1 Sports admissions, subscriptions, leisure class fees and equipment hire | 341 | 0.29 | 99 | 360 (5) | 390 (14) |
| 9.4.2 Cinema, theatre and museums etc | 163 | 0.29 | 47 | 173 (5) | 187 (14) |
| 9.4.3 TV, video, satellite rental, cable subscriptions and TV licences | 367 | 0.29 | 106 | 388 (5) | 420 (14) |
| 9.4.4 Miscellaneous entertainments | 68 | 0.29 | 20 | 72 (5) | 77 (14) |
| 9.4.5 Development of film, deposit for film development, passport photos, holiday and school photos | 15 | 0.29 | 4 | 16 (5) | 17 (14) |
| 9.4.6 Gambling payments | 134 | 0.29 | 39 | 142 (5) | 154 (14) |
| 9.5.1 Books | 66 | 0.66 | 43 | 74 (13) | 87 (33) |
| 9.5.2 Diaries, address books, cards etc | 109 | 0.66 | 72 | 123 (13) | 145 (33) |
| 9.5.3 Newspapers | 68 | 0.66 | 45 | 77 (13) | 91 (33) |
| 9.5.4 Magazines and periodicals | 36 | 0.66 | 24 | 41 (13) | 48 (33) |
| 9.6.1 Package holidays - UK | 84 | 0.51 | 43 | 93 (10) | 105 (25) |
| 9.6.2 Package holidays - abroad | 1311 | 2.00 | 2622 | 1835 (39) | 2622 (100) |
| 10.1 Education fees | 393 | 0.25 | 98 | 413 (5) | 442 (12) |
| 10.2 Payments for school trips, other ad-hoc expenditure | 21 | 0.50 | 10 | 23 (10) | 26 (25) |
| 11.1.1 Restaurant and café meals | 967 | 0.51 | 493 | 1066 (10) | 1214 (25) |
| 11.1.2 Alcoholic drinks (away from home) | 417 | 0.51 | 213 | 460 (10) | 523 (25) |
| 11.1.3 Take away meals eaten at home | 265 | 0.51 | 135 | 292 (10) | 332 (25) |
| 11.1.4 Other take-away and snack food | 266 | 0.51 | 136 | 293 (10) | 334 (25) |
| 11.1.5 Contract catering (food) and canteens | 103 | 0.51 | 53 | 113 (10) | 129 (25) |
| 11.2.1 Holiday in the UK | 311 | 0.50 | 155 | 342 (10) | 389 (25) |
| 11.2.2 Holiday abroad | 243 | 0.50 | 122 | 268 (9) | 304 (25) |
| 11.2.3 Room hire | 3 | 0.50 | 1 | 3 (10) | 3 (25) |
| 12.1.1 Hairdressing, beauty treatment | 199 | 0.50 | 100 | 219 (10) | 249 (25) |
| 12.1.2 Toilet paper | 43 | 0.50 | 22 | 47 (10) | 54 (25) |
| 12.1.3 Toiletries and soap | 128 | 0.50 | 64 | 141 (9) | 161 (25) |
| 12.1.4 Baby toiletries and accessories (disposable) | 40 | 0.50 | 20 | 43 (9) | 49 (25) |
| 12.1.5 Hair products, cosmetics and related electrical appliances | 239 | 0.50 | 120 | 263 (10) | 299 (25) |
| 12.2 Personal effects | 207 | 0.50 | 104 | 228 (9) | 259 (25) |
| 12.3 Social protection | 225 | 0.50 | 112 | 247 (10) | 281 (25) |
| 12.4.1 Household insurances - structural, contents and appliances | 237 | 0.31 | 73 | 251 (6) | 273 (15) |
| 12.4.2 Medical insurance premiums | 101 | 0.31 | 31 | 108 (6) | 117 (15) |
| 12.4.3 Vehicle insurance including boat insurance | 563 | 0.31 | 175 | 598 (6) | 650 (15) |
| 12.4.4 Non-package holiday, other travel insurance | 5 | 0.31 | 2 | 5 (6) | 6 (15) |
| 12.5.1 Moving house | 161 | 0.50 | 81 | 177 (10) | 202 (25) |
| 12.5.2 Bank, building society, post office, credit card charges | 28 | 0.50 | 14 | 31 (10) | 35 (25) |
| 12.5.3 Other services and professional fees | 74 | 0.50 | 37 | 81 (10) | 92 (25) |
| 13.3 Holiday spending | 643 | 0.50 | 321 | 707 (10) | 803 (25) |
| Household total | 27319 |  | 21407 |

## Appendix: Elasticity by item

![1.1.1](1.1.1.png)
![1.1.2](1.1.2.png)
![1.1.3](1.1.3.png)
![1.1.4](1.1.4.png)
![1.1.5](1.1.5.png)
![1.1.6](1.1.6.png)
![1.1.7](1.1.7.png)
![1.1.8](1.1.8.png)
![1.1.9](1.1.9.png)
![1.1.10](1.1.10.png)
![1.1.11](1.1.11.png)
![1.1.12](1.1.12.png)
![1.1.13](1.1.13.png)
![1.1.14](1.1.14.png)
![1.1.15](1.1.15.png)
![1.1.16](1.1.16.png)
![1.1.17](1.1.17.png)
![1.1.18](1.1.18.png)
![1.1.19](1.1.19.png)
![1.1.20](1.1.20.png)
![1.1.21](1.1.21.png)
![1.1.22](1.1.22.png)
![1.1.23](1.1.23.png)
![1.1.24](1.1.24.png)
![1.1.25](1.1.25.png)
![1.1.26](1.1.26.png)
![1.1.27](1.1.27.png)
![1.1.28](1.1.28.png)
![1.1.29](1.1.29.png)
![1.1.30](1.1.30.png)
![1.1.31](1.1.31.png)
![1.1.32](1.1.32.png)
![1.1.33](1.1.33.png)
![1.2.1](1.2.1.png)
![1.2.2](1.2.2.png)
![1.2.3](1.2.3.png)
![1.2.4](1.2.4.png)
![1.2.5](1.2.5.png)
![1.2.6](1.2.6.png)
![2.1.1](2.1.1.png)
![2.1.2](2.1.2.png)
![2.1.3](2.1.3.png)
![2.1.4](2.1.4.png)
![2.2.1](2.2.1.png)
![2.2.2](2.2.2.png)
![3.1.1](3.1.1.png)
![3.1.2](3.1.2.png)
![3.1.3](3.1.3.png)
![3.1.4](3.1.4.png)
![3.1.5](3.1.5.png)
![3.1.6](3.1.6.png)
![3.1.7](3.1.7.png)
![3.1.8](3.1.8.png)
![3.1.9](3.1.9.png)
![3.1.10](3.1.10.png)
![3.1.11](3.1.11.png)
![3.2](3.2.png)
![4.1.3](4.1.3.png)
![4.1.4](4.1.4.png)
![4.2](4.2.png)
![4.3](4.3.png)
![4.4.1](4.4.1.png)
![4.4.2](4.4.2.png)
![4.4.3](4.4.3.png)
![5.1.1](5.1.1.png)
![5.1.2](5.1.2.png)
![5.2](5.2.png)
![5.3](5.3.png)
![5.4](5.4.png)
![5.5](5.5.png)
![5.6.1](5.6.1.png)
![5.6.2](5.6.2.png)
![5.6.3](5.6.3.png)
![6.1.1](6.1.1.png)
![6.1.2](6.1.2.png)
![6.2](6.2.png)
![7.1.1](7.1.1.png)
![7.1.2](7.1.2.png)
![7.1.3](7.1.3.png)
![7.2.1](7.2.1.png)
![7.2.2](7.2.2.png)
![7.2.3](7.2.3.png)
![7.2.4](7.2.4.png)
![7.3.1](7.3.1.png)
![7.3.2](7.3.2.png)
![7.3.3](7.3.3.png)
![7.3.4](7.3.4.png)
![8.1](8.1.png)
![8.2](8.2.png)
![8.3](8.3.png)
![8.4](8.4.png)
![9.1.1](9.1.1.png)
![9.1.2](9.1.2.png)
![9.1.3](9.1.3.png)
![9.2](9.2.png)
![9.3.1](9.3.1.png)
![9.3.2](9.3.2.png)
![9.3.3](9.3.3.png)
![9.3.4](9.3.4.png)
![9.3.5](9.3.5.png)
![9.4.1](9.4.1.png)
![9.4.2](9.4.2.png)
![9.4.3](9.4.3.png)
![9.4.4](9.4.4.png)
![9.4.5](9.4.5.png)
![9.4.6](9.4.6.png)
![9.5.1](9.5.1.png)
![9.5.2](9.5.2.png)
![9.5.3](9.5.3.png)
![9.5.4](9.5.4.png)
![9.6.1](9.6.1.png)
![9.6.2](9.6.2.png)
![10.1](10.1.png)
![10.2](10.2.png)
![11.1.1](11.1.1.png)
![11.1.2](11.1.2.png)
![11.1.3](11.1.3.png)
![11.1.4](11.1.4.png)
![11.1.5](11.1.5.png)
![11.2.1](11.2.1.png)
![11.2.2](11.2.2.png)
![11.2.3](11.2.3.png)
![12.1.1](12.1.1.png)
![12.1.2](12.1.2.png)
![12.1.3](12.1.3.png)
![12.1.4](12.1.4.png)
![12.1.5](12.1.5.png)
![12.2](12.2.png)
![12.3](12.3.png)
![12.4.1](12.4.1.png)
![12.4.2](12.4.2.png)
![12.4.3](12.4.3.png)
![12.4.4](12.4.4.png)
![12.5.1](12.5.1.png)
![12.5.2](12.5.2.png)
![12.5.3](12.5.3.png)
![13.3](13.3.png)
![13.4.2](13.4.2.png)
![14.6](14.6.png)
