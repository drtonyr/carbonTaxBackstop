# Analysis of a basic carbon tax for the UK
## Abstract

This project investigates the inpact of a [Carbon Tax](https://en.wikipedia.org/wiki/Carbon_tax) on UK household spending.  It is widely accepted that we must achieve [carbon neutrality](https://en.wikipedia.org/wiki/Carbon_neutrality) as soon as is practical and a carbon tax is one of the major tools that are available to achive this.

This project takes an intentionally basic view of the problem.  It assumes that the UK can implement a carbon tax and that the revenues raised can be used to sequester carbon such that we achieve neurality.  In order not to disavantage the lowest income households a universal household income is included so that there is no net change to decile 2 (with lower deciles gaining and higher deciles contributing).  Constraining the problem allows for an analyis of the carbon tax.  All source code is available at [github.com/drtonyr/basicCarbonTaxUK](https://github.com/drtonyr/basicCarbonTaxUK) under [MIT licence](https://en.wikipedia.org/wiki/MIT_License) so that others may freely build on this work.

## Methodolgy

The [Office for National Statistics (ONS)](https://www.ons.gov.uk/) collects and publishes a wide variety of data for the UK, specifically [Detailed household expenditure by equivalised disposable income decile group: Table 3.1E](https://www.ons.gov.uk/peoplepopulationandcommunity/personalandhouseholdfinances/expenditure/datasets/detailedhouseholdexpenditurebyequivaliseddisposableincomedecilegroupoecdmodifiedscaleuktable31e).

This work differs from the ONS values in a couple of respects.  The [COICOP](https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Classification_of_individual_consumption_by_purpose_(COICOP)) categories have been expanded to include:  FINISH

The weekly expenditures have been scaled to annual expenditures.  Throughout this work all values are per annum.

### Calculation of elasticity

### Calculation of carbon footprint

### Carbon Capture and Storage rates

The cost of [Carbon Capture and Storage (CCS)](https://en.wikipedia.org/wiki/Carbon_capture_and_storage) is very hard to estimate.   The current marginal cost (e.g. from power plamts or rewilding) is very low, but this does not scale to a Zero Carbon UK. [Bio-energy with carbon capture and storage](https://en.wikipedia.org/wiki/Bio-energy_with_carbon_capture_and_storage) and [direct air carbon capture and storage](https://en.wikipedia.org/wiki/Direct_air_capture) are both emerging technologies.  As such, it is beyond this work to give an accurate estimate of price.  Instead we use a low price of £100/tCO2e, a mid price of £200/tCO2e and a high price of £400/tCO2e to illustrate the range.


## Analysis by item

We can now summarise all expenditure items with their CO2e impact and the new costs under various CCS rates.

It is assumed that a carbon tax would be introduced gradually over a 10 year timescale.  As such items that increase in cost less than 30 percent (2.66 percent per year) have been excluded for clarity.  The full table can be found in the appendix.

| Item description | £  | kgCO2/£ | kgCO2 | £(%up) at £100/t| £(%up) at £200/t| £(%up) at £400/t|
|------------------|---:|--------:|------:|----------------:|----------------:|----------------:|
