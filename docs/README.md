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

### Carbon tax rates

It is anticipated that a carbon tax would be phased in over a number of years.  The final value will depend on many factors which are outside the scope of this work.  To illustrate the impact a low price of £100/tCO2e, a mid price of £200/tCO2e and a high price of £400/tCO2e are used.

We can now summarise all expenditure items with their CO2e impact and the new costs under various CCS rates.

It is assumed that a carbon tax would be introduced gradually over a 10 year timescale.  As such items that increase in cost less than 30 percent (2.66 percent per year) have been excluded for clarity.  The full table can be found in the appendix.

### Income elasticity of demand

The [Income elasticity of demand](https://en.wikipedia.org/wiki/Income_elasticity_of_demand) measures the change in demand of an expenditure item with change in income.  Commonly the model assumes that the relative change in depand is proportional to the relative change in income, or equivilently that demand is an [exponential function](https://en.wikipedia.org/wiki/Exponential_function).  It is also possible to model demand as a [linear function](https://en.wikipedia.org/wiki/Linear_function) of income or as a [monomial]https://en.wikipedia.org/wiki/Monomial).

The ONS data is segmented into income deciles, so elasicity can be estimated using all three functions. The appendix contanis plots for all expenditure items and one is given below.   As can be seen, there is no clear best funciton so for simpliity a linear relationship is used in the rest of this work.

![7.2.2](7.2.2.png)

Whilst we regard income as the total of expenditure items, the income elasticity of demand model is not constrained so that the total change in demand equates to the change in income.  Thus, if we apply a change in income it predicts a change in expenditure for each item but the total of predicted item expenditures does not equal the total expenditure.  Other models could be developed but ethos of this work is to keep things as basic as possible so the process is iterated until the totals match.

### Universal income

A 

### Final calculation of target CCS rates

Putting this all together, for any given rate of carbon tax we can calculate the expected change in demand for expenditure items and the CO2e for these items.  Dividing the amount of tax raised by the total CO2e consumed gives a target CSS rate.  A carbon tax that raised enough revune to match the cost of implementing CSS would be tax neural and carbon neurtal, achieving the goal.

