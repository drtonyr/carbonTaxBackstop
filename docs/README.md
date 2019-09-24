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

| Item  | Description | cost(£) | Elast. | kgCO2/£ | kgCO2 | cost(%up) at £100/t | cost(%up) at £200/t | cost(%up) at £400/t |
| ----- | ----------- | -------:| ------:| -------:| -----:| -------------------:| -------------------:| -------------------:|
| 1.1.5 | Beef (fresh, chilled or frozen) | 103 | 1.80 | 185 | 0.68 | 121 (17) | 140 (36) | 177 (72) |
| 1.1.6 | Pork (fresh, chilled or frozen) | 32 | 1.14 | 36 | 0.52 | 35 (11) | 39 (22) | 46 (45) |
| 1.1.7 | Lamb (fresh, chilled or frozen) | 33 | 0.95 | 31 | 0.34 | 36 (9) | 39 (18) | 45 (37) |
| 1.1.8 | Poultry (fresh, chilled or frozen) | 121 | 1.14 | 138 | 0.59 | 135 (11) | 149 (22) | 176 (45) |
| 1.1.10 | Other meat and meat preparations | 331 | 1.30 | 431 | 0.30 | 374 (12) | 417 (26) | 503 (52) |
| 4.4.1 | Electricity | 592 | 2.32 | 1372 | 0.14 | 729 (23) | 866 (46) | 1141 (92) |
| 4.4.2 | Gas | 512 | 6.41 | 3280 | 0.19 | 840 (64) | 1168 (128) | 1824 (256) |
| 7.1.1 | Purchase of new cars and vans | 514 | 0.78 | 401 | 3.45 | 554 (7) | 594 (15) | 674 (31) |
| 7.1.2 | Purchase of second hand cars or vans | 888 | 0.78 | 693 | 1.34 | 957 (7) | 1027 (15) | 1165 (31) |
| 7.1.3 | Purchase of motorcycles and other vehicles | 32 | 0.78 | 25 | 1.76 | 34 (7) | 37 (15) | 42 (31) |
| 7.2.2 | Petrol, diesel and other motor oils | 1103 | 1.78 | 1961 | 1.09 | 1300 (17) | 1496 (35) | 1888 (71) |
## Appendix: Elasticity by item

![1.1.1](1.1.1.png
)![1.1.2](1.1.2.png
)![1.1.3](1.1.3.png
)![1.1.4](1.1.4.png
)![1.1.5](1.1.5.png
)![1.1.6](1.1.6.png
)![1.1.7](1.1.7.png
)![1.1.8](1.1.8.png
)![1.1.9](1.1.9.png
)![1.1.10](1.1.10.png
)![1.1.11](1.1.11.png
)![1.1.12](1.1.12.png
)![1.1.13](1.1.13.png
)![1.1.14](1.1.14.png
)![1.1.15](1.1.15.png
)![1.1.16](1.1.16.png
)![1.1.17](1.1.17.png
)![1.1.18](1.1.18.png
)![1.1.19](1.1.19.png
)![1.1.20](1.1.20.png
)![1.1.21](1.1.21.png
)![1.1.22](1.1.22.png
)![1.1.23](1.1.23.png
)![1.1.24](1.1.24.png
)![1.1.25](1.1.25.png
)![1.1.26](1.1.26.png
)![1.1.27](1.1.27.png
)![1.1.28](1.1.28.png
)![1.1.29](1.1.29.png
)![1.1.30](1.1.30.png
)![1.1.31](1.1.31.png
)![1.1.32](1.1.32.png
)![1.1.33](1.1.33.png
)![1.2.1](1.2.1.png
)![1.2.2](1.2.2.png
)![1.2.3](1.2.3.png
)![1.2.4](1.2.4.png
)![1.2.5](1.2.5.png
)![1.2.6](1.2.6.png
)![2.1.1](2.1.1.png
)![2.1.2](2.1.2.png
)![2.1.3](2.1.3.png
)![2.1.4](2.1.4.png
)![2.2.1](2.2.1.png
)![2.2.2](2.2.2.png
)![3.1.1](3.1.1.png
)![3.1.2](3.1.2.png
)![3.1.3](3.1.3.png
)![3.1.4](3.1.4.png
)![3.1.5](3.1.5.png
)![3.1.6](3.1.6.png
)![3.1.7](3.1.7.png
)![3.1.8](3.1.8.png
)![3.1.9](3.1.9.png
)![3.1.10](3.1.10.png
)![3.1.11](3.1.11.png
)![3.2](3.2.png
)![4.1.3](4.1.3.png
)![4.1.4](4.1.4.png
)![4.2](4.2.png
)![4.3](4.3.png
)![4.4.1](4.4.1.png
)![4.4.2](4.4.2.png
)![4.4.3](4.4.3.png
)![5.1.1](5.1.1.png
)![5.1.2](5.1.2.png
)![5.2](5.2.png
)![5.3](5.3.png
)![5.4](5.4.png
)![5.5](5.5.png
)![5.6.1](5.6.1.png
)![5.6.2](5.6.2.png
)![5.6.3](5.6.3.png
)![6.1.1](6.1.1.png
)![6.1.2](6.1.2.png
)![6.2](6.2.png
)![7.1.1](7.1.1.png
)![7.1.2](7.1.2.png
)![7.1.3](7.1.3.png
)![7.2.1](7.2.1.png
)![7.2.2](7.2.2.png
)![7.2.3](7.2.3.png
)![7.2.4](7.2.4.png
)![7.3.1](7.3.1.png
)![7.3.2](7.3.2.png
)![7.3.3](7.3.3.png
)![7.3.4](7.3.4.png
)![8.1](8.1.png
)![8.2](8.2.png
)![8.3](8.3.png
)![8.4](8.4.png
)![9.1.1](9.1.1.png
)![9.1.2](9.1.2.png
)![9.1.3](9.1.3.png
)![9.2](9.2.png
)![9.3.1](9.3.1.png
)![9.3.2](9.3.2.png
)![9.3.3](9.3.3.png
)![9.3.4](9.3.4.png
)![9.3.5](9.3.5.png
)![9.4.1](9.4.1.png
)![9.4.2](9.4.2.png
)![9.4.3](9.4.3.png
)![9.4.4](9.4.4.png
)![9.4.5](9.4.5.png
)![9.4.6](9.4.6.png
)![9.5.1](9.5.1.png
)![9.5.2](9.5.2.png
)![9.5.3](9.5.3.png
)![9.5.4](9.5.4.png
)![9.6.1](9.6.1.png
)![9.6.2](9.6.2.png
)![10.1](10.1.png
)![10.2](10.2.png
)![11.1.1](11.1.1.png
)![11.1.2](11.1.2.png
)![11.1.3](11.1.3.png
)![11.1.4](11.1.4.png
)![11.1.5](11.1.5.png
)![11.2.1](11.2.1.png
)![11.2.2](11.2.2.png
)![11.2.3](11.2.3.png
)![12.1.1](12.1.1.png
)![12.1.2](12.1.2.png
)![12.1.3](12.1.3.png
)![12.1.4](12.1.4.png
)![12.1.5](12.1.5.png
)![12.2](12.2.png
)![12.3](12.3.png
)![12.4.1](12.4.1.png
)![12.4.2](12.4.2.png
)![12.4.3](12.4.3.png
)![12.4.4](12.4.4.png
)![12.5.1](12.5.1.png
)![12.5.2](12.5.2.png
)![12.5.3](12.5.3.png
)![13.3](13.3.png
)![13.4.2](13.4.2.png
)![14.6](14.6.png
)