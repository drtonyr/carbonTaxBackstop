# Analysis of a Basic Carbon Tax for the UK
## WORK IN PROGRESS:  ETA EARLY OCTOBER 2019

## Abstract

This work investigates the inpact of a [Carbon Tax](https://en.wikipedia.org/wiki/Carbon_tax) on UK household spending.  It is widely accepted that we must achieve [carbon neutrality](https://en.wikipedia.org/wiki/Carbon_neutrality) as soon as is practical and a carbon tax is regarded as the main economic tool to achive this.

This work assumes that the UK can implement a carbon tax and that the revenues raised can be used to sequester carbon such that we achieve neurality.  Analysis of houshold spending gives a reasonable approximation of CO2e emissions by item expenditure.  Analysis of income elasticity by item gives an expectation of the change in spending at a given rate of carbon tax.  In order not to disavantage the lowest income households a universal household income is included so that there is no net change to decile 2 (with lower deciles gaining and higher deciles contributing).  Increasing the carbon tax thus both reduces expenditure on high carbon items and so reduces emissions and also raises revenues which can be spent on carbon capture and storage and so achieve net carbon zero.  Details of the expected changes are provided.

This analysis is intentionally basic so as to to form a complete isolated project.  A discussion of the limitations is provided and it is concluded that the carvon tax rates calcuated here are an upper bound on what is necessary.  [Full source code](https://github.com/drtonyr/basicCarbonTaxUK) is [freely available](https://en.wikipedia.org/wiki/MIT_License).

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

Various sources are used to estimate the mass of CO2e emitted per pound spent (kgC)e2/£).  In the case of fuel the emissions are known and current prices were used.  Other sources were researched and are documetned in the code.  A heiractical inheritence is used so that if a value was not found it inherits from the parent class.  As can be seen later, only a few items dominate the household CO2e emissions and so it is felt that the approximations used are appropriate.

We can now summarise all expenditure items with their CO2e impact and the new costs under different carbon tax rates.  To illustrate the impact a low price of £100/tCO2e and a high price of £400/tCO2e are used.

It is assumed that a carbon tax would be introduced gradually over a 10 year timescale.  As such items that increase in cost less than 30 percent (2.66 percent per year) have been excluded for clarity.  The full table can be found in the appendix.

| Item description | £  | kgCO2/£ | kgCO2 | £(%up) at £100/t| £(%up) at £400/t|
|:-----------------|---:|--------:|------:|----------------:|----------------:|
| 1.1.5 Beef (fresh, chilled or frozen) | 103 | 1.80 | 185 | 121 (17) | 177 (72) |
| 1.1.6 Pork (fresh, chilled or frozen) | 32 | 1.14 | 36 | 35 (11) | 46 (45) |
| 1.1.7 Lamb (fresh, chilled or frozen) | 33 | 0.95 | 31 | 36 (9) | 45 (37) |
| 1.1.8 Poultry (fresh, chilled or frozen) | 121 | 1.14 | 138 | 135 (11) | 176 (45) |
| 1.1.10 Other meat and meat preparations | 331 | 1.30 | 431 | 374 (12) | 503 (52) |
| 4.4.1 Electricity | 592 | 2.32 | 1372 | 729 (23) | 1141 (92) |
| 4.4.2 Gas | 512 | 6.41 | 3280 | 840 (64) | 1824 (256) |
| 4.4.3 Other fuels | 69 | 1.78 | 123 | 81 (17) | 118 (71) |
| 7.1.1 Purchase of new cars and vans | 514 | 0.78 | 401 | 554 (7) | 674 (31) |
| 7.1.2 Purchase of second hand cars or vans | 888 | 0.78 | 693 | 957 (7) | 1165 (31) |
| 7.1.3 Purchase of motorcycles and other vehicles | 32 | 0.78 | 25 | 34 (7) | 42 (31) |
| 7.2.2 Petrol, diesel and other motor oils | 1103 | 1.78 | 1961 | 1300 (17) | 1888 (71) |
| 9.6.2 Package holidays - abroad | 1311 | 2.00 | 2622 | 1573 (19) | 2360 (80) |
| Household total | 27319 |  | 21407 |


### Carbon footprint by decile and universal income

The ONS data is segmented into income deciles so the catbon footprint can be calculated for each income segment under the two illustrative catbon tax rates.  The universal income is set so that there is no net effect to decile 2 and so the net effect of tax and universal income can be calculated.
