# Analysis of a Basic Carbon Tax for the UK
## Abstract

This work investigates the inpact of a [Carbon Tax](https://en.wikipedia.org/wiki/Carbon_tax) on UK household spending.  It is widely accepted that we must achieve [carbon neutrality](https://en.wikipedia.org/wiki/Carbon_neutrality) as soon as is practical and a carbon tax is regarded as the main economic tool to achive this.

This work assumes that the UK can implement a carbon tax and that the revenues raised can be used to sequester carbon such that we achieve neurality.  Analysis of houshold spending gives a reasonable approximation of CO2e emissions by item expenditure.  Analysis of income elasticity by item gives an expectation of the change in spending at a given rate of carbon tax.  In order not to disavantage the lowest income households a universal household income is included so that there is no net change to decile 2 (with lower deciles gaining and higher deciles contributing).  Increasing the carbon tax thus both reduces expenditure on high carbon items and so reduces emissions and also raises revenues which can be spent on carbon capture and storage and so achieve net carbon zero.  Details of the expected changes are provided.

This analysis is intentionally basic so as to to form a complete isolated project.  A discussion of the limitations is provided and it is concluded that the carvon tax rates calcuated here are an upper bound on what is necessary.  [Full source code](https://github.com/drtonyr/basicCarbonTaxUK) is [freely available](https://en.wikipedia.org/wiki/MIT_License).

## Methodolgy

The [Office for National Statistics (ONS)](https://www.ons.gov.uk/) collects and publishes a wide variety of data for the UK, specifically [Detailed household expenditure by equivalised disposable income decile group: Table 3.1E](https://www.ons.gov.uk/peoplepopulationandcommunity/personalandhouseholdfinances/expenditure/datasets/detailedhouseholdexpenditurebyequivaliseddisposableincomedecilegroupoecdmodifiedscaleuktable31e).

This work differs from the [COICOP](https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Classification_of_individual_consumption_by_purpose_(COICOP)) categories in the ONS table for a few items.  Some items have been excluded as they didn't form part of the total calculation:

| Item description |
|:-----------------|
