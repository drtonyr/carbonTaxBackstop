# Analysis of a Basic Carbon Tax for the UK
## WORK IN PROGRESS:  ETA EARLY OCTOBER 2019

## Abstract

This work investigates the inpact of a [Carbon Tax](https://en.wikipedia.org/wiki/Carbon_tax) on UK household spending.  It is widely accepted that we must achieve [carbon neutrality](https://en.wikipedia.org/wiki/Carbon_neutrality) as soon as is practical and a carbon tax is regarded as the main economic tool to achive this.

This work assumes that the UK can implement a carbon tax and that the revenues raised can be used to sequester carbon such that we achieve neurality.  Analysis of houshold spending gives a reasonable approximation of CO2e emissions by item expenditure.  Analysis of income elasticity by item gives an expectation of the change in spending at a given rate of carbon tax.  In order not to disavantage the lowest income households a universal household income is included so that there is no net change to the first decile.
Increasing the carbon tax thus both reduces expenditure on high carbon items and so reduces emissions and also raises revenues which can be spent on carbon capture and storage and so achieve net carbon zero.  Details of the expected changes are provided.

This analysis is intentionally basic so as to to form a complete isolated work.  The tax-and-sequester method is not proposed as the best route forward, it is proposed to provide one way forward to bound the changes needed to achieve carbon neutrality.  It is clearly better not to emit than to emit-tax-and-sequester but the taxation element will provide economic pressure to find better solutions. [Full source code](https://github.com/drtonyr/basicCarbonTaxUK) is [freely available](https://en.wikipedia.org/wiki/MIT_License).

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

We can now summarise all expenditure items with their CO2e impact and the new costs under different carbon tax rates.  To illustrate the impact a low price of £200/tCO2e and a high price of £800/tCO2e are used.

It is assumed that a carbon tax would be introduced gradually over a 10 year timescale.  As such items that increase in cost less than 60 percent (4.81 percent per year) have been excluded for clarity.  The full table can be found in the appendix.

| Item description | £  | kgCO2/£ | kgCO2 | £(%up) at £200/t| £(%up) at £800/t|
|:-----------------|---:|--------:|------:|----------------:|----------------:|
| 1.1.5 Beef (fresh, chilled or frozen) | 103 | 1.80 | 185 | 140 (36) | 251 (144) |
| 1.1.6 Pork (fresh, chilled or frozen) | 32 | 1.14 | 36 | 39 (22) | 61 (91) |
| 1.1.7 Lamb (fresh, chilled or frozen) | 33 | 0.95 | 31 | 39 (18) | 58 (75) |
| 1.1.8 Poultry (fresh, chilled or frozen) | 121 | 1.14 | 138 | 149 (22) | 232 (91) |
| 1.1.10 Other meat and meat preparations | 331 | 1.30 | 431 | 417 (26) | 676 (104) |
| 4.4.1 Electricity | 592 | 2.32 | 1372 | 866 (46) | 1689 (185) |
| 4.4.2 Gas | 512 | 6.41 | 3280 | 1168 (128) | 3136 (512) |
| 4.4.3 Other fuels | 69 | 1.78 | 123 | 94 (35) | 167 (142) |
| 7.1.1 Purchase of new cars and vans | 514 | 0.78 | 401 | 594 (15) | 834 (62) |
| 7.1.2 Purchase of second hand cars or vans | 888 | 0.78 | 693 | 1027 (15) | 1442 (62) |
| 7.1.3 Purchase of motorcycles and other vehicles | 32 | 0.78 | 25 | 37 (15) | 52 (62) |
| 7.2.2 Petrol, diesel and other motor oils | 1103 | 1.78 | 1961 | 1496 (35) | 2672 (142) |
| 9.6.2 Package holidays - abroad | 1311 | 2.00 | 2622 | 1835 (39) | 3408 (160) |
| Household total | 27319 |  | 21407 |


### Carbon footprint by decile and universal income

The ONS data is segmented into income deciles so the catbon footprint can be calculated for each income segment under the two illustrative catbon tax rates.  The universal income is set so that there is no net effect to decile 1 and so the net effect of tax and universal income can be calculated.

| Decile | expenditure | tCO2e | ctax at £200/t | ctax-UI at £200/t | ctax at £800/t | ctax-UI at £800/t |
|:------:|------------:|------:|--------------:|-----------------:|--------------:|-----------------:|
| 1 | 12449 | 11.3 | 2250 | 0 | 9000 | 0 |
 | 2 | 16219 | 13.9 | 2779 | 529 | 11116 | 2116 |
 | 3 | 18343 | 15.6 | 3119 | 869 | 12474 | 3474 |
 | 4 | 20842 | 17.0 | 3395 | 1145 | 13579 | 4579 |
 | 5 | 23455 | 18.8 | 3762 | 1512 | 15048 | 6048 |
 | 6 | 27734 | 21.5 | 4293 | 2043 | 17172 | 8172 |
 | 7 | 30103 | 23.7 | 4748 | 2498 | 18991 | 9991 |
 | 8 | 32965 | 25.2 | 5043 | 2793 | 20170 | 11170 |
 | 9 | 39465 | 30.5 | 6102 | 3852 | 24409 | 15409 |
 | 10 | 51615 | 36.6 | 7324 | 5074 | 29298 | 20298 |
 | mean | 27319 | 21.4 | 4281 | 2031 | 17126 | 8126 |
 

### Income elasticity of demand

The [Income elasticity of demand](https://en.wikipedia.org/wiki/Income_elasticity_of_demand) measures the change in demand of an expenditure item with change in income.  Commonly the model assumes that the relative change in depand is proportional to the relative change in income, or equivilently that demand is an [exponential function](https://en.wikipedia.org/wiki/Exponential_function).  It is also possible to model demand as a [linear function](https://en.wikipedia.org/wiki/Linear_function) of income or as a [monomial](https://en.wikipedia.org/wiki/Monomial).

Elasicity has been estimated using all three functions. The appendix contanis plots for all expenditure items and one is given below.   As can be seen there is no clear best funciton, so for simpliity a linear relationship is used in the remainder of this work.

![7.2.2](7.2.2.png)

Whilst we regard income as the total of expenditure items, the income elasticity of demand model is not constrained so that the total change in demand equates to the change in income.  Thus, if we apply a change in income it predicts a change in expenditure for each item but the total of predicted item expenditures does not equal the total expenditure.  Other models could be developed but ethos of this work is to keep things as basic as possible so the process is iterated until the totals match.

Another major limitation of this model is that it does not consider cross corelations, that is that the change in demand of one item may affect another.  For example, when the carbon tax on natural gas makes electicity more economical for home heating it can be assumed that there will be a drastic reduciton in gas usage and an equivelent increase in electicity usage.  More subtly, it also assumes that a household which has exactly the same increase in costs due to carbon tax as is matched with the universal income will not change any expenditures.  Whlist this may be true for some households, others may chose to spend on low carbon goods and so increase overall value and reduce carbon emissions.   Thus the model presented here can be considered an upper bound on what is needed, in practice we will ne able to get away with lower carbon tax rates.

### Change in expenditure under a carbon tax

It is now possible to calculate the expected change in demand for expenditure items and the CO2e for these items.  The biggest changes in behaviour occur at the highest income group, so that is used to illustrate the change.


| Decile | expenditure | ctax-UI at £800/t | %decrease in expenditure | prior tCO2e | post tCO2e  |
|:------:|------------:|-----------------:|--------------------------:|------------:|------------:|
| 1 | 12449 | 0 | 0 | 11.3 | 11.3 |
| 2 | 16219 | 1383 | 9 | 13.9 | 13.0 |
| 3 | 18343 | 2271 | 12 | 15.6 | 14.1 |
| 4 | 20842 | 2994 | 14 | 17.0 | 15.0 |
| 5 | 23455 | 3954 | 17 | 18.8 | 16.2 |
| 6 | 27734 | 5343 | 19 | 21.5 | 17.9 |
| 7 | 30103 | 6532 | 22 | 23.7 | 19.4 |
| 8 | 32965 | 7303 | 22 | 25.2 | 20.4 |
| 9 | 39465 | 10074 | 26 | 30.5 | 23.8 |
| 10 | 51615 | 13271 | 26 | 36.6 | 27.8 |
| mean | 27319 | 5312 | 17 | 21.4 | 17.9 |

Thus a carbon tax of 800 would be expected to raise £5312 p.a. per household with average emissions of 17.9 tCO2e and thus support a CCS rate of £297 /tCO2e.

### Carbon tax and Carbon Capture and Storage

The cost of [Carbon Capture and Storage (CCS)](https://en.wikipedia.org/wiki/Carbon_capture_and_storage) is very hard to estimate.   The current marginal cost (e.g. from power plants or rewilding) is very low, but this does not scale to a Zero Carbon UK. [Bio-energy with carbon capture and storage](https://en.wikipedia.org/wiki/Bio-energy_with_carbon_capture_and_storage) and [direct air carbon capture and storage](https://en.wikipedia.org/wiki/Direct_air_capture) are both emerging technologies.  For example, figure 10.2 in [The Committee on Climate Change](https://www.theccc.org.uk) [Net Zero – Technical Report](https://www.theccc.org.uk/publication/net-zero-technical-report) has numbers around £200/tCO2e with great uncertainty.

It is possible to sweep over at large range of tax rates and estimate the revenue generated and the correspondnig reduction in CO2e.  Dividing the expected CO2e by the reveue rasied gives a CSS rate which, if achieved, would result in carbon neutrality.


## Limitations              

## Conclusion              

A carbon tax with universal income is not an effective way to reduce emissions directly, indeed the universal income aspect ensures that lowest income households do not have to reduce emissions. However, it does provide a means to bound the changes needed to achieve carbon neutrality.

## Appendix: Full analysis by item


| Item description | £  | kgCO2/£ | kgCO2 | £(%up) at £200/t| £(%up) at £800/t|
|:-----------------|---:|--------:|------:|----------------:|----------------:|
| 1.1.1 Bread, rice and cereals | 283 | 0.72 | 204 | 324 (14) | 447 (57) |
| 1.1.2 Pasta products | 22 | 0.72 | 16 | 26 (14) | 35 (57) |
| 1.1.3 Buns, cakes, biscuits etc | 200 | 0.72 | 144 | 228 (14) | 315 (57) |
| 1.1.4 Pastry (savoury) | 48 | 0.72 | 34 | 55 (14) | 75 (57) |
| 1.1.5 Beef (fresh, chilled or frozen) | 103 | 1.80 | 185 | 140 (36) | 251 (144) |
| 1.1.6 Pork (fresh, chilled or frozen) | 32 | 1.14 | 36 | 39 (22) | 61 (91) |
| 1.1.7 Lamb (fresh, chilled or frozen) | 33 | 0.95 | 31 | 39 (18) | 58 (75) |
| 1.1.8 Poultry (fresh, chilled or frozen) | 121 | 1.14 | 138 | 149 (22) | 232 (91) |
| 1.1.9 Bacon and ham | 46 | 0.39 | 18 | 49 (7) | 60 (30) |
| 1.1.10 Other meat and meat preparations | 331 | 1.30 | 431 | 417 (26) | 676 (104) |
| 1.1.11 Fish and fish products | 151 | 0.72 | 109 | 173 (14) | 238 (57) |
| 1.1.12 Milk | 113 | 0.72 | 81 | 129 (14) | 178 (57) |
| 1.1.13 Cheese and curd | 103 | 0.72 | 75 | 118 (14) | 163 (57) |
| 1.1.14 Eggs | 37 | 0.72 | 27 | 42 (14) | 58 (57) |
| 1.1.15 Other milk products | 122 | 0.72 | 88 | 140 (14) | 193 (57) |
| 1.1.16 Butter | 25 | 0.72 | 18 | 29 (14) | 39 (57) |
| 1.1.17 Margarine, other vegetable fats and peanut butter | 31 | 0.72 | 22 | 35 (14) | 48 (57) |
| 1.1.18 Cooking oils and fats | 18 | 0.72 | 13 | 20 (14) | 28 (57) |
| 1.1.19 Fresh fruit | 207 | 0.72 | 149 | 237 (14) | 327 (57) |
| 1.1.20 Other fresh, chilled or frozen fruits | 24 | 0.72 | 18 | 28 (14) | 39 (57) |
| 1.1.21 Dried fruit and nuts | 44 | 0.72 | 31 | 50 (14) | 69 (57) |
| 1.1.22 Preserved fruit and fruit based products | 8 | 0.72 | 6 | 9 (14) | 12 (57) |
| 1.1.23 Fresh vegetables | 224 | 0.72 | 161 | 256 (14) | 352 (57) |
| 1.1.24 Dried vegetables | 4 | 0.72 | 3 | 4 (14) | 6 (57) |
| 1.1.25 Other preserved or processed vegetables | 87 | 0.72 | 63 | 99 (14) | 137 (57) |
| 1.1.26 Potatoes | 41 | 0.72 | 29 | 46 (14) | 64 (57) |
| 1.1.27 Other tubers and products of tuber vegetables | 85 | 0.72 | 61 | 98 (14) | 134 (57) |
| 1.1.28 Sugar and sugar products | 20 | 0.72 | 15 | 23 (14) | 32 (57) |
| 1.1.29 Jams, marmalades | 16 | 0.72 | 12 | 18 (14) | 25 (57) |
| 1.1.30 Chocolate | 110 | 0.72 | 79 | 126 (14) | 173 (57) |
| 1.1.31 Confectionery products | 41 | 0.72 | 29 | 46 (14) | 64 (57) |
| 1.1.32 Edible ices and ice cream | 34 | 0.72 | 25 | 39 (14) | 54 (57) |
| 1.1.33 Other food products | 135 | 0.72 | 97 | 154 (14) | 212 (57) |
| 1.2.1 Coffee | 49 | 0.72 | 35 | 56 (14) | 77 (57) |
| 1.2.2 Tea | 23 | 0.72 | 16 | 26 (14) | 36 (57) |
| 1.2.3 Cocoa and powdered chocolate | 5 | 0.72 | 4 | 6 (14) | 8 (57) |
| 1.2.4 Fruit and vegetable juices (inc. fruit squash) | 56 | 0.72 | 40 | 64 (14) | 88 (57) |
| 1.2.5 Mineral or spring waters | 21 | 0.72 | 15 | 24 (14) | 33 (57) |
| 1.2.6 Soft drinks (inc. fizzy and ready to drink fruit drinks) | 103 | 0.72 | 74 | 118 (14) | 162 (57) |
| 2.1.1 Spirits and liqueurs (brought home) | 102 | 0.50 | 51 | 112 (9) | 143 (40) |
| 2.1.2 Wines, fortified wines (brought home) | 235 | 0.15 | 35 | 242 (3) | 263 (12) |
| 2.1.3 Beer, lager, ciders and perry (brought home) | 113 | 0.50 | 57 | 125 (10) | 159 (39) |
| 2.1.4 Alcopops (brought home) | 3 | 0.50 | 1 | 3 (10) | 4 (39) |
| 2.2.1 Cigarettes | 137 | 0.50 | 69 | 151 (10) | 192 (40) |
| 2.2.2 Cigars, other tobacco products and narcotics | 59 | 0.50 | 29 | 65 (10) | 82 (40) |
| 3.1.1 Men's outer garments | 264 | 0.33 | 87 | 281 (6) | 333 (26) |
| 3.1.2 Men's under garments | 28 | 0.33 | 9 | 29 (6) | 35 (26) |
| 3.1.3 Women's outer garments | 438 | 0.33 | 145 | 467 (6) | 554 (26) |
| 3.1.4 Women's under garments | 64 | 0.33 | 21 | 69 (6) | 82 (26) |
| 3.1.5 Boys' outer garments (5-15) | 51 | 0.33 | 17 | 55 (6) | 65 (26) |
| 3.1.6 Girls' outer garments (5-15) | 51 | 0.33 | 17 | 55 (6) | 65 (26) |
| 3.1.7 Infants' outer garments (under 5) | 34 | 0.33 | 11 | 37 (6) | 43 (26) |
| 3.1.8 Children's under garments (under 16) | 21 | 0.33 | 7 | 23 (6) | 27 (26) |
| 3.1.9 Accessories | 40 | 0.33 | 13 | 43 (6) | 51 (26) |
| 3.1.10 Haberdashery and clothing hire | 15 | 0.33 | 5 | 16 (6) | 19 (26) |
| 3.1.11 Dry cleaners, laundry and dyeing | 9 | 0.33 | 3 | 9 (6) | 11 (26) |
| 3.2 Footwear | 248 | 0.33 | 82 | 264 (6) | 313 (26) |
| 4.1.3 Net rent | 1879 | 0.50 | 939 | 2067 (10) | 2630 (39) |
| 4.1.4 Second dwelling rent | 3 | 0.50 | 1 | 3 (10) | 4 (39) |
| 4.2 Maintenance and repair of dwelling | 424 | 0.50 | 212 | 467 (10) | 594 (40) |
| 4.3 Water supply and miscellaneous services relating to the dwelling | 483 | 0.50 | 241 | 531 (9) | 676 (40) |
| 4.4.1 Electricity | 592 | 2.32 | 1372 | 866 (46) | 1689 (185) |
| 4.4.2 Gas | 512 | 6.41 | 3280 | 1168 (128) | 3136 (512) |
| 4.4.3 Other fuels | 69 | 1.78 | 123 | 94 (35) | 167 (142) |
| 5.1.1 Furniture and furnishings | 978 | 0.50 | 489 | 1075 (10) | 1369 (40) |
| 5.1.2 Floor coverings | 197 | 0.50 | 98 | 216 (10) | 275 (39) |
| 5.2 Household textiles | 117 | 0.50 | 58 | 129 (9) | 164 (40) |
| 5.3 Household appliances | 226 | 0.50 | 113 | 248 (10) | 316 (39) |
| 5.4 Glassware, tableware and household utensils | 102 | 0.50 | 51 | 112 (9) | 143 (39) |
| 5.5 Tools and equipment for house and garden | 149 | 0.50 | 74 | 164 (9) | 208 (40) |
| 5.6.1 Cleaning materials | 123 | 0.50 | 61 | 135 (9) | 172 (39) |
| 5.6.2 Household goods and hardware | 87 | 0.50 | 44 | 96 (10) | 122 (40) |
| 5.6.3 Domestic services, carpet cleaning, hire/repair of furniture/furnishings | 138 | 0.50 | 69 | 152 (10) | 193 (39) |
| 6.1.1 Medicines, prescriptions, healthcare products etc | 109 | 0.66 | 72 | 124 (13) | 167 (52) |
| 6.1.2 Spectacles, lenses, accessories and repairs | 89 | 0.50 | 45 | 98 (10) | 125 (40) |
| 6.2 Hospital services | 159 | 0.50 | 79 | 174 (9) | 222 (39) |
| 7.1.1 Purchase of new cars and vans | 514 | 0.78 | 401 | 594 (15) | 834 (62) |
| 7.1.2 Purchase of second hand cars or vans | 888 | 0.78 | 693 | 1027 (15) | 1442 (62) |
| 7.1.3 Purchase of motorcycles and other vehicles | 32 | 0.78 | 25 | 37 (15) | 52 (62) |
| 7.2.1 Spares and accessories | 124 | 0.50 | 62 | 137 (9) | 174 (40) |
| 7.2.2 Petrol, diesel and other motor oils | 1103 | 1.78 | 1961 | 1496 (35) | 2672 (142) |
| 7.2.3 Repairs and servicing | 339 | 0.50 | 169 | 372 (10) | 474 (39) |
| 7.2.4 Other motoring costs | 159 | 0.50 | 80 | 175 (10) | 223 (40) |
| 7.3.1 Rail and tube fares | 224 | 0.50 | 112 | 246 (9) | 313 (39) |
| 7.3.2 Bus and coach fares | 79 | 0.50 | 39 | 86 (10) | 110 (40) |
| 7.3.3 Combined fares | 32 | 0.50 | 16 | 36 (10) | 46 (39) |
| 7.3.4 Other travel and transport | 679 | 0.50 | 340 | 747 (10) | 951 (40) |
| 8.1 Postal services | 33 | 0.50 | 17 | 37 (10) | 47 (39) |
| 8.2 Telephone and telefax equipment | 59 | 0.39 | 23 | 63 (7) | 77 (31) |
| 8.3 Telephone and telefax services | 642 | 0.62 | 398 | 721 (12) | 960 (49) |
| 8.4 Internet subscription fees | 196 | 0.50 | 98 | 216 (10) | 274 (40) |
| 9.1.1 Audio equipment and accessories, CD players | 55 | 0.65 | 36 | 62 (12) | 84 (52) |
| 9.1.2 TV, video and computers | 182 | 0.65 | 118 | 206 (12) | 277 (52) |
| 9.1.3 Photographic, cine and optical equipment | 17 | 0.65 | 11 | 19 (12) | 26 (52) |
| 9.2 Other major durables for recreation and culture | 139 | 0.29 | 40 | 147 (5) | 171 (23) |
| 9.3.1 Games, toys and hobbies | 162 | 0.29 | 47 | 171 (5) | 199 (23) |
| 9.3.2 Computer software and games | 55 | 0.29 | 16 | 58 (5) | 67 (23) |
| 9.3.3 Equipment for sport, camping and open-air recreation | 53 | 0.29 | 15 | 56 (5) | 65 (23) |
| 9.3.4 Horticultural goods, garden equipment and plants | 134 | 0.29 | 39 | 141 (5) | 165 (23) |
| 9.3.5 Pets and pet food | 292 | 0.29 | 85 | 309 (5) | 360 (23) |
| 9.4.1 Sports admissions, subscriptions, leisure class fees and equipment hire | 341 | 0.29 | 99 | 360 (5) | 420 (23) |
| 9.4.2 Cinema, theatre and museums etc | 163 | 0.29 | 47 | 173 (5) | 201 (23) |
| 9.4.3 TV, video, satellite rental, cable subscriptions and TV licences | 367 | 0.29 | 106 | 388 (5) | 452 (23) |
| 9.4.4 Miscellaneous entertainments | 68 | 0.29 | 20 | 72 (5) | 83 (23) |
| 9.4.5 Development of film, deposit for film development, passport photos, holiday and school photos | 15 | 0.29 | 4 | 16 (5) | 19 (23) |
| 9.4.6 Gambling payments | 134 | 0.29 | 39 | 142 (5) | 165 (23) |
| 9.5.1 Books | 66 | 0.66 | 43 | 74 (13) | 100 (52) |
| 9.5.2 Diaries, address books, cards etc | 109 | 0.66 | 72 | 123 (13) | 166 (52) |
| 9.5.3 Newspapers | 68 | 0.66 | 45 | 77 (13) | 104 (52) |
| 9.5.4 Magazines and periodicals | 36 | 0.66 | 24 | 41 (13) | 55 (52) |
| 9.6.1 Package holidays - UK | 84 | 0.51 | 43 | 93 (10) | 118 (40) |
| 9.6.2 Package holidays - abroad | 1311 | 2.00 | 2622 | 1835 (39) | 3408 (160) |
| 10.1 Education fees | 393 | 0.25 | 98 | 413 (5) | 472 (19) |
| 10.2 Payments for school trips, other ad-hoc expenditure | 21 | 0.50 | 10 | 23 (10) | 29 (39) |
| 11.1.1 Restaurant and café meals | 967 | 0.51 | 493 | 1066 (10) | 1362 (40) |
| 11.1.2 Alcoholic drinks (away from home) | 417 | 0.51 | 213 | 460 (10) | 587 (40) |
| 11.1.3 Take away meals eaten at home | 265 | 0.51 | 135 | 292 (10) | 373 (40) |
| 11.1.4 Other take-away and snack food | 266 | 0.51 | 136 | 293 (10) | 375 (40) |
| 11.1.5 Contract catering (food) and canteens | 103 | 0.51 | 53 | 113 (10) | 145 (40) |
| 11.2.1 Holiday in the UK | 311 | 0.50 | 155 | 342 (10) | 435 (39) |
| 11.2.2 Holiday abroad | 243 | 0.50 | 122 | 268 (9) | 341 (39) |
| 11.2.3 Room hire | 3 | 0.50 | 1 | 3 (10) | 4 (39) |
| 12.1.1 Hairdressing, beauty treatment | 199 | 0.50 | 100 | 219 (10) | 279 (40) |
| 12.1.2 Toilet paper | 43 | 0.50 | 22 | 47 (10) | 60 (39) |
| 12.1.3 Toiletries and soap | 128 | 0.50 | 64 | 141 (9) | 180 (40) |
| 12.1.4 Baby toiletries and accessories (disposable) | 40 | 0.50 | 20 | 43 (9) | 55 (40) |
| 12.1.5 Hair products, cosmetics and related electrical appliances | 239 | 0.50 | 120 | 263 (10) | 335 (40) |
| 12.2 Personal effects | 207 | 0.50 | 104 | 228 (9) | 290 (40) |
| 12.3 Social protection | 225 | 0.50 | 112 | 247 (10) | 314 (39) |
| 12.4.1 Household insurances - structural, contents and appliances | 237 | 0.31 | 73 | 251 (6) | 295 (24) |
| 12.4.2 Medical insurance premiums | 101 | 0.31 | 31 | 108 (6) | 127 (24) |
| 12.4.3 Vehicle insurance including boat insurance | 563 | 0.31 | 175 | 598 (6) | 703 (24) |
| 12.4.4 Non-package holiday, other travel insurance | 5 | 0.31 | 2 | 5 (6) | 6 (24) |
| 12.5.1 Moving house | 161 | 0.50 | 81 | 177 (10) | 226 (39) |
| 12.5.2 Bank, building society, post office, credit card charges | 28 | 0.50 | 14 | 31 (10) | 39 (39) |
| 12.5.3 Other services and professional fees | 74 | 0.50 | 37 | 81 (10) | 103 (39) |
| 13.3 Holiday spending | 643 | 0.50 | 321 | 707 (10) | 900 (39) |
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
