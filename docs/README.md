# A Carbon Tax Backstop to guarantee Carbon Neutrality
<p align="center">
Tony Robinson<br>02 November 2019
</p>
## Abstract

This work models the impact of a [Carbon Tax](https://en.wikipedia.org/wiki/Carbon_tax) on UK household spending and tax raised.  It is widely accepted that we must achieve [carbon neutrality](https://en.wikipedia.org/wiki/Carbon_neutrality) as soon as is practical and a carbon tax is regarded as the main economic tool to achieve this.

This work assumes that a carbon tax will be implemented and that the revenues raised can be used to reduce [CO2e](https://en.wikipedia.org/wiki/Carbon_dioxide_equivalent) emissions such that we achieve carbon neutrality.  Analysis of household spending from the UK gives a reasonable approximation of CO2e emissions by item expenditure.  Analysis of income elasticity by item gives an expectation of the change in spending at a given rate of carbon tax.  In order not to disadvantage the lowest income households a universal household income is included so that there is no net change to the first decile.
Increasing the carbon tax thus both reduces expenditure on high carbon items (reducing emissions) and also raises revenues which can be spent on decarbonifying our economy so achieve net carbon zero.  Details of the expected changes are provided.

This analysis is modelled as a backstop, that is a mechanism to guarantee that the desired outcome will be achieved whilst leaving open better means of achieving the outcome.  All major political parties will be committing to carbon neutrality for the UK between 2030 and 2050.   This work allows them to guarantee that their target will be hit whilst not having to specify every detail.  The report expcts carbon neutrality to be achievable with only modest changes in household expenditure.

This report is generated from python source code which is [freely available](https://github.com/drtonyr/carbonTaxBackstop).

## Motivation

A [Carbon Tax](https://en.wikipedia.org/wiki/Carbon_tax) offers a means to rectify that fossil fuel costs do not account for cleaning up the resulting emissions.  This is unsustainable and necessitates change before much more damnage is done.

Broadly speaking, the spectrum of climate change policy ranges between:

* Aspirational:  These polices will have a clear target but are not backed up by a detailed implementation.  They carry an execution risk because they may not be practical and aspirations may change.
* Implementational:  These have a detailed implementation, typically involving many interdependent parts which sum to the desired target.  They carry an execution risk as inevitably some parts will work out and some won't - the Danish saying "Prediction is very difficult, especially about the future." is pertinent as there are many things we can't model exactly.

A backstop is means of guaranteeing the desired outcome, if better means are found then it need not be used.

A carbon tax backstop is valuable to all policies and all political parties.  It provides the ability to commit to carbon neutrality which is now of key importance to the UK electorate ([Climate crisis affects how majority will vote in UK election](https://www.theguardian.com/environment/2019/oct/30/climate-crisis-affects-how-majority-will-vote-in-uk-election-poll)).

## Methodology

This report considers the effect of a carbon tax on household consumption, both directly in terms of the amount consumed of various categories and indirectly in terms of the embedded carbon in the consumed goods and services.

Production of goods and services is highly driven by economic considerations, efficiency is well defined, a company or process that isn't as efficient as competitors will have to adapt or cease.  It is therefore expected that a carbon tax will be highly productive in driving rapid change.

Household spending is only weakly driven by economics, there is no clear definition of efficiency or what is to be optimised and behaviours change slowly.  Nevertheless, it is total household spending that drives the economy and households that vote for parliament that implement climate change policies.

This report looks a the effect of carbon tax on household spending.  It is not assumed that households will make complex economic decisions, it is assumed that the companies and processes that supply households will adapt to economic circumstances.

### Household Expenditure

The [Office for National Statistics (ONS)](https://www.ons.gov.uk/) collects and publishes a wide variety of data for the UK, specifically [Detailed household expenditure by equivalised disposable income decile group: Table 3.1E](https://www.ons.gov.uk/peoplepopulationandcommunity/personalandhouseholdfinances/expenditure/datasets/detailedhouseholdexpenditurebyequivaliseddisposableincomedecilegroupoecdmodifiedscaleuktable31e).   This breaks household expenditure down into about 140 [COICOP](https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Classification_of_individual_consumption_by_purpose_(COICOP)) categories, and further breaks down all categories into deciles of total household spending.

This work adjusts COICOP categories for a few items.  Some items have been excluded as they don't form part of the total calculation:

|    | Excluded item description |
|:---|:--------------------------|
| 4.1.1 | Gross rent |
| 4.1.2 | less housing benefit, rebates and allowances rec'd |


Some non-COICOP items in the ONS data were included as they constituted significant discretionary spending:

|    | Included item description |
|:---|:--------------------------|
| 13.3 | Holiday spending |
| 13.4.2 | Cash gifts and donations |
| 14.6 | Savings and investments |


The weekly expenditures provided have been scaled to annual expenditures.  Throughout this work all values are per annum.

### Calculation Of Carbon Footprint

Various sources are used to estimate the mass of CO2e emitted per pound spent (kgCOe2/£).  In the case of fuel the emissions are known and current household prices were used.  Other sources were researched and are documented in the code.  Hierarchical inheritance is used so that if a value is not know it is assumed to be the same as it's parent.  As can be seen later, only a few items dominate the household CO2e emissions and so it is felt that the approximations used are appropriate.

We can now summarise all expenditure items with their CO2e impact and the new costs under different carbon tax rates.  To illustrate the impact a low price of £200/tCO2e and a high price of £500/tCO2e are used.

It is assumed that a carbon tax would be introduced gradually over a 10 year timescale.  As such items that increase in cost less than 50 percent (4.14 percent per year) have been excluded for clarity.  The full table can be found in the appendix.

| Item description | £  | kgCO2/£ | kgCO2 | £(%up) at £200/t| £(%up) at £500/t|
|:-----------------|---:|--------:|------:|----------------:|----------------:|
| 1.1.5 Beef (fresh, chilled or frozen) | 103 | 1.80 | 186 | 141 (36) | 196 (89) |
| 1.1.6 Pork (fresh, chilled or frozen) | 32 | 1.14 | 36 | 39 (22) | 50 (57) |
| 1.1.8 Poultry (fresh, chilled or frozen) | 122 | 1.14 | 139 | 149 (22) | 191 (57) |
| 1.1.10 Other meat and meat preparations | 332 | 1.30 | 432 | 419 (26) | 548 (65) |
| 4.4.1 Electricity | 594 | 2.32 | 1377 | 869 (46) | 1282 (115) |
| 4.4.2 Gas | 513 | 6.41 | 3292 | 1172 (128) | 2159 (320) |
| 4.4.3 Other fuels | 69 | 1.78 | 123 | 94 (35) | 131 (88) |
| 7.2.2 Petrol, diesel and other motor oils | 1107 | 1.78 | 1967 | 1501 (35) | 2091 (88) |
| 9.6.2 Package holidays - abroad | 1315 | 2.00 | 2631 | 1842 (39) | 2631 (100) |
| Household total | 27412 |  | 21480 |


Note that no changes in manufacturing or consumption have been included in the table above.  This is a backstop calculation and at this stage we are just interested in the worse case change.

### Carbon Footprint By Decile And Universal Income

The ONS data is segmented into income deciles so the carbon footprint can be calculated for each income segment under the two illustrative carbon tax rates.  The universal income is set so that there is no net effect to decile 1 and so the net effect of tax and universal income can be calculated (this number is one of the parameters of the code - changing it and running again results in a different report). 

| Decile | expenditure/£ | tCO2e | ctax at £200/t | ctax-UI at £200/t | ctax at £500/t | ctax-UI at £500/t |
|:------:|--------------:|------:|--------------:|-----------------:|--------------:|-----------------:|
| 1 | 12491 | 11.3 | 2258 | 0 | 5644 | 0 |
 | 2 | 16274 | 13.9 | 2788 | 531 | 6971 | 1327 |
 | 3 | 18405 | 15.6 | 3129 | 871 | 7823 | 2179 |
 | 4 | 20913 | 17.0 | 3406 | 1149 | 8516 | 2872 |
 | 5 | 23535 | 18.9 | 3775 | 1517 | 9437 | 3793 |
 | 6 | 27829 | 21.5 | 4308 | 2050 | 10769 | 5125 |
 | 7 | 30205 | 23.8 | 4764 | 2506 | 11910 | 6265 |
 | 8 | 33078 | 25.3 | 5060 | 2802 | 12649 | 7005 |
 | 9 | 39600 | 30.6 | 6123 | 3865 | 15308 | 9663 |
 | 10 | 51791 | 36.7 | 7349 | 5092 | 18373 | 12729 |
 | mean | 27412 | 21.5 | 4296 | 2038 | 10740 | 5096 |
 

Looking at decile 1 we see that the Universal Income is set to exactly match the carbon tax.  Deciles higher than this benefit financially, those lower fund decarbonisation.  The numbers in this table still don't reflect the change in expenditure due to price changes or any benefits of decarbonisation.

### Income Elasticity Of Demand

The [Income elasticity of demand](https://en.wikipedia.org/wiki/Income_elasticity_of_demand) measures the change in demand of an expenditure item with change in income.  Commonly the model assumes that the relative change in demand is proportional to the relative change in income, or equivalently that demand is an [exponential function](https://en.wikipedia.org/wiki/Exponential_function).  It is also possible to model demand as a [linear function](https://en.wikipedia.org/wiki/Linear_function) of income or as a [monomial](https://en.wikipedia.org/wiki/Monomial).

Elasticity has been estimated using all three functions. The appendix contains plots for all expenditure items and one is given below.   As can be seen there is no clear best fit, so for simplicity a linear relationship is used in the remainder of this work.

![7.2.2](7.2.2.png)

Note that whilst we regard income as the total of expenditure items, the income elasticity of demand model is not constrained so that the total change in demand equates to the change in income.  Thus, if we apply a change in income it predicts a change in expenditure for each item but the total of predicted item expenditures does not equal the total expenditure.  Other models could be developed but ethos of this work is to keep things as simple as possible so the process is iterated until the totals match.

Another major limitation of this model is that it does not consider cross correlations, that is that the change in demand of one item may affect another.  For example, when the carbon tax on natural gas makes electricity more economical for home heating it can be assumed that there will be a drastic reduction in gas usage and an equivalent increase in electricity usage.  More subtly, it also assumes that a household which has exactly the same increase in costs due to carbon tax as is matched with the universal income will not change any expenditures.  Whilst this may be true for some households, others may chose to spend on low carbon goods and so increase overall value and reduce carbon emissions.   Thus the model presented here can be considered an upper bound on what is needed, in practice we will be able to get away with lower carbon tax rates - this being perfectly acceptable behaviour for a backstop.

### Change In Expenditure Under A Carbon Tax

It is now possible to calculate the expected change in demand for expenditure items and the CO2e for these items.  For every expenditure decile the carbon tax over all expenditure items is calculated.  If that matches the universal income then the books ballance and no further changes are necessary.  If there is a mismatch then the income elasticity of demand curves are used to adjust expenditure on each item until the carbon tax does match the universal income. 


| Decile | expenditure/£ | ctax-UI at £500/t | %decrease in expenditure | prior tCO2e | post tCO2e  |
|:------:|--------------:|-----------------:|--------------------------:|------------:|------------:|
| 1 | 12491 | 0 | 0 | 11.3 | 11.3 |
| 2 | 16274 | 997 | 6 | 13.9 | 13.3 |
| 3 | 18405 | 1637 | 9 | 15.6 | 14.6 |
| 4 | 20913 | 2158 | 10 | 17.0 | 15.6 |
| 5 | 23535 | 2850 | 12 | 18.9 | 17.0 |
| 6 | 27829 | 3850 | 14 | 21.5 | 19.0 |
| 7 | 30205 | 4708 | 16 | 23.8 | 20.7 |
| 8 | 33078 | 5263 | 16 | 25.3 | 21.8 |
| 9 | 39600 | 7261 | 18 | 30.6 | 25.8 |
| 10 | 51791 | 9564 | 18 | 36.7 | 30.4 |
