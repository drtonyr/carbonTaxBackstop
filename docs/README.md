# Analysis of a Basic Carbon Tax for the UK
## Abstract

This work investigates the inpact of a [Carbon Tax](https://en.wikipedia.org/wiki/Carbon_tax) on UK household spending.  It is widely accepted that we must achieve [carbon neutrality](https://en.wikipedia.org/wiki/Carbon_neutrality) as soon as is practical and a carbon tax is regarded as the main economic tool to achive this.

This work assumes that the UK can implement a carbon tax and that the revenues raised can be used to sequester carbon such that we achieve neurality.  Analysis of houshold spending gives a reasonable approximation of CO2e emissions by item expenditure.  Analysis of income elasticity by item gives an expectation of the change in spending at a given rate of carbon tax.  In order not to disavantage the lowest income households a universal household income is included so that there is no net change to decile 2 (with lower deciles gaining and higher deciles contributing).  Increasing the carbon tax thus both reduces expenditure on high carbon items and so reduces emissions and also raises revenues which can be spent on carbon capture and storage and so achieve net carbon zero.  Details of the expected changes are provided.

This analysis is intentionally basic so as to to form a complete isolated project.  A discussion of the limitations is provided and it is concluded that the carvon tax rates calcuated here are an upper bound on what is necessary.  [Full source code](https://github.com/drtonyr/basicCarbonTaxUK) is [freely available](https://en.wikipedia.org/wiki/MIT_License).

## Methodolgy

The [Office for National Statistics (ONS)](https://www.ons.gov.uk/) collects and publishes a wide variety of data for the UK, specifically [Detailed household expenditure by equivalised disposable income decile group: Table 3.1E](https://www.ons.gov.uk/peoplepopulationandcommunity/personalandhouseholdfinances/expenditure/datasets/detailedhouseholdexpenditurebyequivaliseddisposableincomedecilegroupoecdmodifiedscaleuktable31e).

This work differs from the [COICOP](https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Classification_of_individual_consumption_by_purpose_(COICOP)) categories in the ONS table for a few items.  Some items have been excluded as they don't form part of the total calculation:

| Exclused item description |
|:-----------------|
| 4.1.1 Gross rent |
| 4.1.2 less housing benefit, rebates and allowances rec'd |


Some non-COICOP items were included as they consituted significant discressionay spending:

| Included item description |
|:-----------------|
| 13.3 Holiday spending |
| 13.4.2 Cash gifts and donations |
| 14.6 Savings and investments |


The weekly expenditures have been scaled to annual expenditures.  Throughout this work all values are per annum.

### Calculation of elasticity

### Calculation of carbon footprint

### Carbon Capture and Storage rates

The cost of [Carbon Capture and Storage (CCS)](https://en.wikipedia.org/wiki/Carbon_capture_and_storage) is very hard to estimate.   The current marginal cost (e.g. from power plamts or rewilding) is very low, but this does not scale to a Zero Carbon UK. [Bio-energy with carbon capture and storage](https://en.wikipedia.org/wiki/Bio-energy_with_carbon_capture_and_storage) and [direct air carbon capture and storage](https://en.wikipedia.org/wiki/Direct_air_capture) are both emerging technologies.  As such, it is beyond this work to give an accurate estimate of price.  Instead we use a low price of £100/tCO2e, a mid price of £200/tCO2e and a high price of £400/tCO2e to illustrate the range.


## Analysis by item

We can now summarise all expenditure items with their CO2e impact and the new costs under various CCS rates.

It is assumed that a carbon tax would be introduced gradually over a 10 year timescale.  As such items that increase in cost less than 30 percent (2.66 percent per year) have been excluded for clarity.  The full table can be found in the appendix.

| Item description | £  | kgCO2/£ | kgCO2 | £(%up) at £100/t| £(%up) at £200/t| £(%up) at £400/t|
|:-----------------|---:|--------:|------:|----------------:|----------------:|----------------:|
| 1.1.5 Beef (fresh, chilled or frozen) | 103 | 1.80 | 185 | 121 (17) | 140 (36) | 177 (72) |
| 1.1.6 Pork (fresh, chilled or frozen) | 32 | 1.14 | 36 | 35 (11) | 39 (22) | 46 (45) |
| 1.1.7 Lamb (fresh, chilled or frozen) | 33 | 0.95 | 31 | 36 (9) | 39 (18) | 45 (37) |
| 1.1.8 Poultry (fresh, chilled or frozen) | 121 | 1.14 | 138 | 135 (11) | 149 (22) | 176 (45) |
| 1.1.10 Other meat and meat preparations | 331 | 1.30 | 431 | 374 (12) | 417 (26) | 503 (52) |
| 4.4.1 Electricity | 592 | 2.32 | 1372 | 729 (23) | 866 (46) | 1141 (92) |
| 4.4.2 Gas | 512 | 6.41 | 3280 | 840 (64) | 1168 (128) | 1824 (256) |
| 4.4.3 Other fuels | 69 | 1.78 | 123 | 81 (17) | 94 (35) | 118 (71) |
| 7.1.1 Purchase of new cars and vans | 514 | 0.78 | 401 | 554 (7) | 594 (15) | 674 (31) |
| 7.1.2 Purchase of second hand cars or vans | 888 | 0.78 | 693 | 957 (7) | 1027 (15) | 1165 (31) |
| 7.1.3 Purchase of motorcycles and other vehicles | 32 | 0.78 | 25 | 34 (7) | 37 (15) | 42 (31) |
| 7.2.2 Petrol, diesel and other motor oils | 1103 | 1.78 | 1961 | 1300 (17) | 1496 (35) | 1888 (71) |
| 9.6.2 Package holidays - abroad | 1311 | 2.00 | 2622 | 1573 (19) | 1835 (39) | 2360 (80) |
| Household total | 27319 |  | 21407 |

## Appendix: Full analysis by item


| Item description | £  | kgCO2/£ | kgCO2 | £(%up) at £100/t| £(%up) at £200/t| £(%up) at £400/t|
|:-----------------|---:|--------:|------:|----------------:|----------------:|----------------:|
| 1.1.1 Bread, rice and cereals | 283 | 0.72 | 204 | 304 (7) | 324 (14) | 365 (28) |
| 1.1.2 Pasta products | 22 | 0.72 | 16 | 24 (7) | 26 (14) | 29 (28) |
| 1.1.3 Buns, cakes, biscuits etc | 200 | 0.72 | 144 | 214 (7) | 228 (14) | 257 (28) |
| 1.1.4 Pastry (savoury) | 48 | 0.72 | 34 | 51 (7) | 55 (14) | 62 (28) |
| 1.1.5 Beef (fresh, chilled or frozen) | 103 | 1.80 | 185 | 121 (17) | 140 (36) | 177 (72) |
| 1.1.6 Pork (fresh, chilled or frozen) | 32 | 1.14 | 36 | 35 (11) | 39 (22) | 46 (45) |
| 1.1.7 Lamb (fresh, chilled or frozen) | 33 | 0.95 | 31 | 36 (9) | 39 (18) | 45 (37) |
| 1.1.8 Poultry (fresh, chilled or frozen) | 121 | 1.14 | 138 | 135 (11) | 149 (22) | 176 (45) |
| 1.1.9 Bacon and ham | 46 | 0.39 | 18 | 48 (3) | 49 (7) | 53 (15) |
| 1.1.10 Other meat and meat preparations | 331 | 1.30 | 431 | 374 (12) | 417 (26) | 503 (52) |
| 1.1.11 Fish and fish products | 151 | 0.72 | 109 | 162 (7) | 173 (14) | 195 (28) |
| 1.1.12 Milk | 113 | 0.72 | 81 | 121 (7) | 129 (14) | 145 (28) |
| 1.1.13 Cheese and curd | 103 | 0.72 | 75 | 111 (7) | 118 (14) | 133 (28) |
| 1.1.14 Eggs | 37 | 0.72 | 27 | 40 (7) | 42 (14) | 48 (28) |
| 1.1.15 Other milk products | 122 | 0.72 | 88 | 131 (7) | 140 (14) | 157 (28) |
| 1.1.16 Butter | 25 | 0.72 | 18 | 27 (7) | 29 (14) | 32 (28) |
| 1.1.17 Margarine, other vegetable fats and peanut butter | 31 | 0.72 | 22 | 33 (7) | 35 (14) | 40 (28) |
| 1.1.18 Cooking oils and fats | 18 | 0.72 | 13 | 19 (7) | 20 (14) | 23 (28) |
| 1.1.19 Fresh fruit | 207 | 0.72 | 149 | 222 (7) | 237 (14) | 267 (28) |
| 1.1.20 Other fresh, chilled or frozen fruits | 24 | 0.72 | 18 | 26 (7) | 28 (14) | 31 (28) |
| 1.1.21 Dried fruit and nuts | 44 | 0.72 | 31 | 47 (7) | 50 (14) | 56 (28) |
| 1.1.22 Preserved fruit and fruit based products | 8 | 0.72 | 6 | 8 (7) | 9 (14) | 10 (28) |
| 1.1.23 Fresh vegetables | 224 | 0.72 | 161 | 240 (7) | 256 (14) | 288 (28) |
| 1.1.24 Dried vegetables | 4 | 0.72 | 3 | 4 (7) | 4 (14) | 5 (28) |
| 1.1.25 Other preserved or processed vegetables | 87 | 0.72 | 63 | 93 (7) | 99 (14) | 112 (28) |
| 1.1.26 Potatoes | 41 | 0.72 | 29 | 43 (7) | 46 (14) | 52 (28) |
| 1.1.27 Other tubers and products of tuber vegetables | 85 | 0.72 | 61 | 91 (7) | 98 (14) | 110 (28) |
| 1.1.28 Sugar and sugar products | 20 | 0.72 | 15 | 22 (7) | 23 (14) | 26 (28) |
| 1.1.29 Jams, marmalades | 16 | 0.72 | 12 | 17 (7) | 18 (14) | 21 (28) |
| 1.1.30 Chocolate | 110 | 0.72 | 79 | 118 (7) | 126 (14) | 141 (28) |
| 1.1.31 Confectionery products | 41 | 0.72 | 29 | 43 (7) | 46 (14) | 52 (28) |
| 1.1.32 Edible ices and ice cream | 34 | 0.72 | 25 | 37 (7) | 39 (14) | 44 (28) |
| 1.1.33 Other food products | 135 | 0.72 | 97 | 144 (7) | 154 (14) | 173 (28) |
| 1.2.1 Coffee | 49 | 0.72 | 35 | 52 (7) | 56 (14) | 63 (28) |
| 1.2.2 Tea | 23 | 0.72 | 16 | 25 (7) | 26 (14) | 29 (28) |
| 1.2.3 Cocoa and powdered chocolate | 5 | 0.72 | 4 | 6 (7) | 6 (14) | 7 (28) |
| 1.2.4 Fruit and vegetable juices (inc. fruit squash) | 56 | 0.72 | 40 | 60 (7) | 64 (14) | 72 (28) |
| 1.2.5 Mineral or spring waters | 21 | 0.72 | 15 | 22 (7) | 24 (14) | 27 (28) |
| 1.2.6 Soft drinks (inc. fizzy and ready to drink fruit drinks) | 103 | 0.72 | 74 | 110 (7) | 118 (14) | 133 (28) |
| 2.1.1 Spirits and liqueurs (brought home) | 102 | 0.50 | 51 | 107 (5) | 112 (9) | 122 (19) |
| 2.1.2 Wines, fortified wines (brought home) | 235 | 0.15 | 35 | 238 (1) | 242 (3) | 249 (6) |
| 2.1.3 Beer, lager, ciders and perry (brought home) | 113 | 0.50 | 57 | 119 (5) | 125 (10) | 136 (19) |
| 2.1.4 Alcopops (brought home) | 3 | 0.50 | 1 | 3 (5) | 3 (10) | 3 (19) |
| 2.2.1 Cigarettes | 137 | 0.50 | 69 | 144 (5) | 151 (10) | 165 (19) |
| 2.2.2 Cigars, other tobacco products and narcotics | 59 | 0.50 | 29 | 62 (5) | 65 (10) | 71 (19) |
| 3.1.1 Men's outer garments | 264 | 0.33 | 87 | 272 (3) | 281 (6) | 298 (13) |
| 3.1.2 Men's under garments | 28 | 0.33 | 9 | 28 (3) | 29 (6) | 31 (13) |
| 3.1.3 Women's outer garments | 438 | 0.33 | 145 | 453 (3) | 467 (6) | 496 (13) |
| 3.1.4 Women's under garments | 64 | 0.33 | 21 | 67 (3) | 69 (6) | 73 (13) |
| 3.1.5 Boys' outer garments (5-15) | 51 | 0.33 | 17 | 53 (3) | 55 (6) | 58 (13) |
| 3.1.6 Girls' outer garments (5-15) | 51 | 0.33 | 17 | 53 (3) | 55 (6) | 58 (13) |
| 3.1.7 Infants' outer garments (under 5) | 34 | 0.33 | 11 | 35 (3) | 37 (6) | 39 (13) |
| 3.1.8 Children's under garments (under 16) | 21 | 0.33 | 7 | 22 (3) | 23 (6) | 24 (13) |
| 3.1.9 Accessories | 40 | 0.33 | 13 | 41 (3) | 43 (6) | 45 (13) |
| 3.1.10 Haberdashery and clothing hire | 15 | 0.33 | 5 | 16 (3) | 16 (6) | 17 (13) |
| 3.1.11 Dry cleaners, laundry and dyeing | 9 | 0.33 | 3 | 9 (3) | 9 (6) | 10 (13) |
| 3.2 Footwear | 248 | 0.33 | 82 | 256 (3) | 264 (6) | 280 (13) |
| 4.1.3 Net rent | 1879 | 0.50 | 939 | 1973 (5) | 2067 (10) | 2255 (19) |
| 4.1.4 Second dwelling rent | 3 | 0.50 | 1 | 3 (5) | 3 (10) | 3 (19) |
| 4.2 Maintenance and repair of dwelling | 424 | 0.50 | 212 | 446 (5) | 467 (10) | 509 (19) |
| 4.3 Water supply and miscellaneous services relating to the dwelling | 483 | 0.50 | 241 | 507 (5) | 531 (9) | 579 (19) |
| 4.4.1 Electricity | 592 | 2.32 | 1372 | 729 (23) | 866 (46) | 1141 (92) |
| 4.4.2 Gas | 512 | 6.41 | 3280 | 840 (64) | 1168 (128) | 1824 (256) |
| 4.4.3 Other fuels | 69 | 1.78 | 123 | 81 (17) | 94 (35) | 118 (71) |
| 5.1.1 Furniture and furnishings | 978 | 0.50 | 489 | 1026 (5) | 1075 (10) | 1173 (20) |
| 5.1.2 Floor coverings | 197 | 0.50 | 98 | 206 (5) | 216 (10) | 236 (19) |
| 5.2 Household textiles | 117 | 0.50 | 58 | 123 (5) | 129 (9) | 140 (19) |
| 5.3 Household appliances | 226 | 0.50 | 113 | 237 (5) | 248 (10) | 271 (20) |
| 5.4 Glassware, tableware and household utensils | 102 | 0.50 | 51 | 107 (5) | 112 (9) | 122 (19) |
| 5.5 Tools and equipment for house and garden | 149 | 0.50 | 74 | 156 (5) | 164 (9) | 178 (19) |
| 5.6.1 Cleaning materials | 123 | 0.50 | 61 | 129 (5) | 135 (9) | 147 (20) |
| 5.6.2 Household goods and hardware | 87 | 0.50 | 44 | 92 (5) | 96 (10) | 105 (19) |
| 5.6.3 Domestic services, carpet cleaning, hire/repair of furniture/furnishings | 138 | 0.50 | 69 | 145 (4) | 152 (10) | 165 (19) |
| 6.1.1 Medicines, prescriptions, healthcare products etc | 109 | 0.66 | 72 | 116 (6) | 124 (13) | 138 (26) |
| 6.1.2 Spectacles, lenses, accessories and repairs | 89 | 0.50 | 45 | 94 (4) | 98 (10) | 107 (19) |
| 6.2 Hospital services | 159 | 0.50 | 79 | 167 (5) | 174 (9) | 190 (19) |
| 7.1.1 Purchase of new cars and vans | 514 | 0.78 | 401 | 554 (7) | 594 (15) | 674 (31) |
| 7.1.2 Purchase of second hand cars or vans | 888 | 0.78 | 693 | 957 (7) | 1027 (15) | 1165 (31) |
| 7.1.3 Purchase of motorcycles and other vehicles | 32 | 0.78 | 25 | 34 (7) | 37 (15) | 42 (31) |
| 7.2.1 Spares and accessories | 124 | 0.50 | 62 | 130 (5) | 137 (9) | 149 (19) |
| 7.2.2 Petrol, diesel and other motor oils | 1103 | 1.78 | 1961 | 1300 (17) | 1496 (35) | 1888 (71) |
| 7.2.3 Repairs and servicing | 339 | 0.50 | 169 | 355 (5) | 372 (10) | 406 (19) |
| 7.2.4 Other motoring costs | 159 | 0.50 | 80 | 167 (5) | 175 (10) | 191 (19) |
| 7.3.1 Rail and tube fares | 224 | 0.50 | 112 | 235 (5) | 246 (9) | 268 (19) |
| 7.3.2 Bus and coach fares | 79 | 0.50 | 39 | 82 (5) | 86 (10) | 94 (19) |
| 7.3.3 Combined fares | 32 | 0.50 | 16 | 34 (5) | 36 (10) | 39 (19) |
| 7.3.4 Other travel and transport | 679 | 0.50 | 340 | 713 (5) | 747 (10) | 815 (19) |
| 8.1 Postal services | 33 | 0.50 | 17 | 35 (5) | 37 (10) | 40 (19) |
| 8.2 Telephone and telefax equipment | 59 | 0.39 | 23 | 61 (3) | 63 (7) | 68 (15) |
| 8.3 Telephone and telefax services | 642 | 0.62 | 398 | 681 (6) | 721 (12) | 801 (24) |
| 8.4 Internet subscription fees | 196 | 0.50 | 98 | 206 (5) | 216 (10) | 235 (19) |
| 9.1.1 Audio equipment and accessories, CD players | 55 | 0.65 | 36 | 59 (6) | 62 (12) | 69 (25) |
| 9.1.2 TV, video and computers | 182 | 0.65 | 118 | 194 (6) | 206 (12) | 229 (26) |
| 9.1.3 Photographic, cine and optical equipment | 17 | 0.65 | 11 | 18 (6) | 19 (12) | 21 (26) |
| 9.2 Other major durables for recreation and culture | 139 | 0.29 | 40 | 143 (2) | 147 (5) | 155 (11) |
| 9.3.1 Games, toys and hobbies | 162 | 0.29 | 47 | 166 (2) | 171 (5) | 180 (11) |
| 9.3.2 Computer software and games | 55 | 0.29 | 16 | 56 (2) | 58 (5) | 61 (11) |
| 9.3.3 Equipment for sport, camping and open-air recreation | 53 | 0.29 | 15 | 54 (2) | 56 (5) | 59 (11) |
| 9.3.4 Horticultural goods, garden equipment and plants | 134 | 0.29 | 39 | 138 (2) | 141 (5) | 149 (11) |
| 9.3.5 Pets and pet food | 292 | 0.29 | 85 | 301 (2) | 309 (5) | 326 (11) |
| 9.4.1 Sports admissions, subscriptions, leisure class fees and equipment hire | 341 | 0.29 | 99 | 350 (2) | 360 (5) | 380 (11) |
| 9.4.2 Cinema, theatre and museums etc | 163 | 0.29 | 47 | 168 (2) | 173 (5) | 182 (11) |
| 9.4.3 TV, video, satellite rental, cable subscriptions and TV licences | 367 | 0.29 | 106 | 377 (2) | 388 (5) | 409 (11) |
| 9.4.4 Miscellaneous entertainments | 68 | 0.29 | 20 | 70 (2) | 72 (5) | 75 (11) |
| 9.4.5 Development of film, deposit for film development, passport photos, holiday and school photos | 15 | 0.29 | 4 | 16 (2) | 16 (5) | 17 (11) |
| 9.4.6 Gambling payments | 134 | 0.29 | 39 | 138 (2) | 142 (5) | 150 (11) |
| 9.5.1 Books | 66 | 0.66 | 43 | 70 (6) | 74 (13) | 83 (26) |
| 9.5.2 Diaries, address books, cards etc | 109 | 0.66 | 72 | 116 (6) | 123 (13) | 137 (26) |
| 9.5.3 Newspapers | 68 | 0.66 | 45 | 73 (6) | 77 (13) | 86 (26) |
| 9.5.4 Magazines and periodicals | 36 | 0.66 | 24 | 38 (6) | 41 (13) | 45 (26) |
| 9.6.1 Package holidays - UK | 84 | 0.51 | 43 | 88 (5) | 93 (10) | 101 (20) |
| 9.6.2 Package holidays - abroad | 1311 | 2.00 | 2622 | 1573 (19) | 1835 (39) | 2360 (80) |
| 10.1 Education fees | 393 | 0.25 | 98 | 403 (2) | 413 (5) | 432 (10) |
| 10.2 Payments for school trips, other ad-hoc expenditure | 21 | 0.50 | 10 | 22 (5) | 23 (10) | 25 (19) |
| 11.1.1 Restaurant and café meals | 967 | 0.51 | 493 | 1017 (5) | 1066 (10) | 1165 (20) |
| 11.1.2 Alcoholic drinks (away from home) | 417 | 0.51 | 213 | 438 (5) | 460 (10) | 502 (20) |
| 11.1.3 Take away meals eaten at home | 265 | 0.51 | 135 | 278 (5) | 292 (10) | 319 (20) |
| 11.1.4 Other take-away and snack food | 266 | 0.51 | 136 | 280 (5) | 293 (10) | 321 (20) |
| 11.1.5 Contract catering (food) and canteens | 103 | 0.51 | 53 | 108 (5) | 113 (10) | 124 (20) |
| 11.2.1 Holiday in the UK | 311 | 0.50 | 155 | 327 (5) | 342 (10) | 373 (19) |
| 11.2.2 Holiday abroad | 243 | 0.50 | 122 | 256 (5) | 268 (9) | 292 (19) |
| 11.2.3 Room hire | 3 | 0.50 | 1 | 3 (5) | 3 (10) | 3 (19) |
| 12.1.1 Hairdressing, beauty treatment | 199 | 0.50 | 100 | 209 (5) | 219 (10) | 239 (19) |
| 12.1.2 Toilet paper | 43 | 0.50 | 22 | 45 (5) | 47 (10) | 52 (19) |
| 12.1.3 Toiletries and soap | 128 | 0.50 | 64 | 135 (5) | 141 (9) | 154 (19) |
| 12.1.4 Baby toiletries and accessories (disposable) | 40 | 0.50 | 20 | 41 (5) | 43 (9) | 47 (19) |
| 12.1.5 Hair products, cosmetics and related electrical appliances | 239 | 0.50 | 120 | 251 (5) | 263 (10) | 287 (19) |
| 12.2 Personal effects | 207 | 0.50 | 104 | 218 (5) | 228 (9) | 249 (19) |
| 12.3 Social protection | 225 | 0.50 | 112 | 236 (5) | 247 (10) | 270 (19) |
| 12.4.1 Household insurances - structural, contents and appliances | 237 | 0.31 | 73 | 244 (3) | 251 (6) | 266 (12) |
| 12.4.2 Medical insurance premiums | 101 | 0.31 | 31 | 105 (3) | 108 (6) | 114 (12) |
| 12.4.3 Vehicle insurance including boat insurance | 563 | 0.31 | 175 | 581 (3) | 598 (6) | 633 (12) |
| 12.4.4 Non-package holiday, other travel insurance | 5 | 0.31 | 2 | 5 (3) | 5 (6) | 6 (12) |
| 12.5.1 Moving house | 161 | 0.50 | 81 | 169 (5) | 177 (10) | 193 (20) |
| 12.5.2 Bank, building society, post office, credit card charges | 28 | 0.50 | 14 | 29 (5) | 31 (10) | 34 (19) |
| 12.5.3 Other services and professional fees | 74 | 0.50 | 37 | 78 (5) | 81 (10) | 89 (19) |
| 13.3 Holiday spending | 643 | 0.50 | 321 | 675 (5) | 707 (10) | 771 (19) |
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
