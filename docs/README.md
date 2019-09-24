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

We can now summarise all expenditure items.  The ten highest values WILL BE highlighted.

| Item  | Description | cost(£) | Elast. | kgCO2/£ | kgCO2 | cost(%up) at £100/t | cost(%up) at £200/t | cost(%up) at £400/t |
| ----- | ----------- | -------:| ------:| -------:| -----:| -------------------:| -------------------:| -------------------:|
| 1.1.1 | Bread, rice and cereals | 283 | 0.72 | 204 | 0.35 | 304 (107) | 324 (114) | 365 (128) |
| 1.1.2 | Pasta products | 22 | 0.72 | 16 | 0.41 | 24 (107) | 26 (114) | 29 (128) |
| 1.1.3 | Buns, cakes, biscuits etc | 200 | 0.72 | 144 | 0.24 | 214 (107) | 228 (114) | 257 (128) |
| 1.1.4 | Pastry (savoury) | 48 | 0.72 | 34 | 0.50 | 51 (107) | 55 (114) | 62 (128) |
| 1.1.5 | Beef (fresh, chilled or frozen) | 103 | 1.80 | 185 | 0.68 | 121 (118) | 140 (136) | 177 (172) |
| 1.1.6 | Pork (fresh, chilled or frozen) | 32 | 1.14 | 36 | 0.52 | 35 (111) | 39 (122) | 46 (145) |
| 1.1.7 | Lamb (fresh, chilled or frozen) | 33 | 0.95 | 31 | 0.34 | 36 (109) | 39 (118) | 45 (137) |
| 1.1.8 | Poultry (fresh, chilled or frozen) | 121 | 1.14 | 138 | 0.59 | 135 (111) | 149 (122) | 176 (145) |
| 1.1.9 | Bacon and ham | 46 | 0.39 | 18 | 0.41 | 48 (103) | 49 (107) | 53 (115) |
| 1.1.10 | Other meat and meat preparations | 331 | 1.30 | 431 | 0.30 | 374 (113) | 417 (126) | 503 (152) |
| 1.1.11 | Fish and fish products | 151 | 0.72 | 109 | 0.60 | 162 (107) | 173 (114) | 195 (128) |
| 1.1.12 | Milk | 113 | 0.72 | 81 | 0.06 | 121 (107) | 129 (114) | 145 (128) |
| 1.1.13 | Cheese and curd | 103 | 0.72 | 75 | 0.60 | 111 (107) | 118 (114) | 133 (128) |
| 1.1.14 | Eggs | 37 | 0.72 | 27 | 0.39 | 40 (107) | 42 (114) | 48 (128) |
| 1.1.15 | Other milk products | 122 | 0.72 | 88 | 0.54 | 131 (107) | 140 (114) | 157 (128) |
| 1.1.16 | Butter | 25 | 0.72 | 18 | 0.36 | 27 (107) | 29 (114) | 32 (128) |
| 1.1.17 | Margarine, other vegetable fats and peanut butter | 31 | 0.72 | 22 | 0.30 | 33 (107) | 35 (114) | 40 (128) |
| 1.1.18 | Cooking oils and fats | 18 | 0.72 | 13 | 0.29 | 19 (107) | 20 (114) | 23 (128) |
| 1.1.19 | Fresh fruit | 207 | 0.72 | 149 | 0.63 | 222 (107) | 237 (114) | 267 (128) |
| 1.1.20 | Other fresh, chilled or frozen fruits | 24 | 0.72 | 18 | 0.53 | 26 (107) | 28 (114) | 31 (128) |
| 1.1.21 | Dried fruit and nuts | 44 | 0.72 | 31 | 0.76 | 47 (107) | 50 (114) | 56 (128) |
| 1.1.22 | Preserved fruit and fruit based products | 8 | 0.72 | 6 | 0.30 | 8 (107) | 9 (114) | 10 (128) |
| 1.1.23 | Fresh vegetables | 224 | 0.72 | 161 | 0.68 | 240 (107) | 256 (114) | 288 (128) |
| 1.1.24 | Dried vegetables | 4 | 0.72 | 3 | 0.51 | 4 (107) | 4 (114) | 5 (128) |
| 1.1.25 | Other preserved or processed vegetables | 87 | 0.72 | 63 | 0.76 | 93 (107) | 99 (114) | 112 (128) |
| 1.1.26 | Potatoes | 41 | 0.72 | 29 | 0.22 | 43 (107) | 46 (114) | 52 (128) |
| 1.1.27 | Other tubers and products of tuber vegetables | 85 | 0.72 | 61 | 0.05 | 91 (107) | 98 (114) | 110 (128) |
| 1.1.28 | Sugar and sugar products | 20 | 0.72 | 15 | 0.14 | 22 (107) | 23 (114) | 26 (128) |
| 1.1.29 | Jams, marmalades | 16 | 0.72 | 12 | 0.33 | 17 (107) | 18 (114) | 21 (128) |
| 1.1.30 | Chocolate | 110 | 0.72 | 79 | 0.40 | 118 (107) | 126 (114) | 141 (128) |
| 1.1.31 | Confectionery products | 41 | 0.72 | 29 | 0.16 | 43 (107) | 46 (114) | 52 (128) |
| 1.1.32 | Edible ices and ice cream | 34 | 0.72 | 25 | 0.19 | 37 (107) | 39 (114) | 44 (128) |
| 1.1.33 | Other food products | 135 | 0.72 | 97 | 0.58 | 144 (107) | 154 (114) | 173 (128) |
| 1.2.1 | Coffee | 49 | 0.50 | 24 | 0.47 | 51 (105) | 54 (110) | 59 (120) |
| 1.2.2 | Tea | 23 | 0.50 | 11 | 0.51 | 24 (104) | 25 (109) | 27 (120) |
| 1.2.3 | Cocoa and powdered chocolate | 5 | 0.50 | 3 | 0.00 | 5 (105) | 6 (110) | 6 (120) |
| 1.2.4 | Fruit and vegetable juices (inc. fruit squash) | 56 | 0.50 | 28 | 0.45 | 58 (105) | 61 (109) | 67 (120) |
| 1.2.5 | Mineral or spring waters | 21 | 0.50 | 10 | 0.36 | 22 (105) | 23 (110) | 25 (120) |
| 1.2.6 | Soft drinks (inc. fizzy and ready to drink fruit drinks) | 103 | 0.50 | 51 | 0.05 | 108 (105) | 113 (110) | 124 (120) |
| 2.1.1 | Spirits and liqueurs (brought home) | 102 | 0.50 | 51 | 0.64 | 107 (105) | 112 (110) | 122 (120) |
| 2.1.2 | Wines, fortified wines (brought home) | 235 | 0.15 | 35 | 1.41 | 238 (101) | 242 (102) | 249 (106) |
| 2.1.3 | Beer, lager, ciders and perry (brought home) | 113 | 0.50 | 57 | 0.64 | 119 (105) | 125 (110) | 136 (120) |
| 2.1.4 | Alcopops (brought home) | 3 | 0.50 | 1 | 0.00 | 3 (105) | 3 (110) | 3 (120) |
| 2.2.1 | Cigarettes | 137 | 0.50 | 69 | -0.33 | 144 (105) | 151 (110) | 165 (119) |
| 2.2.2 | Cigars, other tobacco products and narcotics | 59 | 0.50 | 29 | -0.95 | 62 (105) | 65 (110) | 71 (119) |
| 3.1.1 | Men's outer garments | 264 | 0.33 | 87 | 1.40 | 272 (103) | 281 (106) | 298 (113) |
| 3.1.2 | Men's under garments | 28 | 0.33 | 9 | 0.75 | 28 (103) | 29 (106) | 31 (113) |
| 3.1.3 | Women's outer garments | 438 | 0.33 | 145 | 1.10 | 453 (103) | 467 (106) | 496 (113) |
| 3.1.4 | Women's under garments | 64 | 0.33 | 21 | 0.65 | 67 (103) | 69 (106) | 73 (113) |
| 3.1.5 | Boys' outer garments (5-15) | 51 | 0.33 | 17 | 0.75 | 53 (103) | 55 (106) | 58 (113) |
| 3.1.6 | Girls' outer garments (5-15) | 51 | 0.33 | 17 | 0.54 | 53 (103) | 55 (106) | 58 (113) |
| 3.1.7 | Infants' outer garments (under 5) | 34 | 0.33 | 11 | 0.47 | 35 (103) | 37 (106) | 39 (113) |
| 3.1.8 | Children's under garments (under 16) | 21 | 0.33 | 7 | 0.22 | 22 (103) | 23 (106) | 24 (113) |
| 3.1.9 | Accessories | 40 | 0.33 | 13 | 1.04 | 41 (103) | 43 (106) | 45 (113) |
| 3.1.10 | Haberdashery and clothing hire | 15 | 0.33 | 5 | 0.84 | 16 (103) | 16 (106) | 17 (113) |
| 3.1.11 | Dry cleaners, laundry and dyeing | 9 | 0.33 | 3 | 1.83 | 9 (103) | 9 (106) | 10 (113) |
| 3.2 | Footwear | 248 | 0.33 | 82 | 0.64 | 256 (103) | 264 (106) | 280 (113) |
| 4.1.3 | Net rent | 1879 | 0.50 | 939 | 0.18 | 1973 (105) | 2067 (110) | 2255 (119) |
| 4.1.4 | Second dwelling rent | 3 | 0.50 | 1 | 0.00 | 3 (105) | 3 (110) | 3 (120) |
| 4.2 | Maintenance and repair of dwelling | 424 | 0.50 | 212 | 1.16 | 446 (105) | 467 (110) | 509 (119) |
| 4.3 | Water supply and miscellaneous services relating to the dwelling | 483 | 0.50 | 241 | 0.30 | 507 (105) | 531 (110) | 579 (119) |
| 4.4.1 | Electricity | 592 | 2.32 | 1372 | 0.14 | 729 (123) | 866 (146) | 1141 (192) |
| 4.4.2 | Gas | 512 | 6.41 | 3280 | 0.19 | 840 (164) | 1168 (228) | 1824 (356) |
| 4.4.3 | Other fuels | 69 | 0.50 | 35 | 0.75 | 73 (105) | 76 (110) | 83 (119) |
| 5.1.1 | Furniture and furnishings | 978 | 0.50 | 489 | 1.26 | 1026 (105) | 1075 (110) | 1173 (120) |
| 5.1.2 | Floor coverings | 197 | 0.50 | 98 | 1.08 | 206 (105) | 216 (110) | 236 (120) |
| 5.2 | Household textiles | 117 | 0.50 | 58 | 1.26 | 123 (105) | 129 (109) | 140 (120) |
| 5.3 | Household appliances | 226 | 0.50 | 113 | 1.28 | 237 (105) | 248 (110) | 271 (120) |
| 5.4 | Glassware, tableware and household utensils | 102 | 0.50 | 51 | 0.80 | 107 (105) | 112 (109) | 122 (120) |
| 5.5 | Tools and equipment for house and garden | 149 | 0.50 | 74 | 1.27 | 156 (105) | 164 (109) | 178 (120) |
| 5.6.1 | Cleaning materials | 123 | 0.50 | 61 | 0.43 | 129 (104) | 135 (109) | 147 (120) |
| 5.6.2 | Household goods and hardware | 87 | 0.50 | 44 | 0.51 | 92 (104) | 96 (110) | 105 (119) |
| 5.6.3 | Domestic services, carpet cleaning, hire/repair of furniture/furnishings | 138 | 0.50 | 69 | 1.60 | 145 (104) | 152 (110) | 165 (119) |
| 6.1.1 | Medicines, prescriptions, healthcare products etc | 109 | 0.66 | 72 | 0.74 | 116 (106) | 124 (113) | 138 (126) |
| 6.1.2 | Spectacles, lenses, accessories and repairs | 89 | 0.50 | 45 | 2.04 | 94 (105) | 98 (110) | 107 (120) |
| 6.2 | Hospital services | 159 | 0.50 | 79 | 1.81 | 167 (105) | 174 (109) | 190 (120) |
| 7.1.1 | Purchase of new cars and vans | 514 | 0.78 | 401 | 3.45 | 554 (107) | 594 (115) | 674 (131) |
| 7.1.2 | Purchase of second hand cars or vans | 888 | 0.78 | 693 | 1.34 | 957 (107) | 1027 (115) | 1165 (131) |
| 7.1.3 | Purchase of motorcycles and other vehicles | 32 | 0.78 | 25 | 1.76 | 34 (107) | 37 (115) | 42 (131) |
| 7.2.1 | Spares and accessories | 124 | 0.50 | 62 | 1.47 | 130 (105) | 137 (110) | 149 (120) |
| 7.2.2 | Petrol, diesel and other motor oils | 1103 | 1.78 | 1961 | 1.09 | 1300 (117) | 1496 (135) | 1888 (171) |
| 7.2.3 | Repairs and servicing | 339 | 0.50 | 169 | 1.23 | 355 (105) | 372 (110) | 406 (119) |
| 7.2.4 | Other motoring costs | 159 | 0.50 | 80 | 1.28 | 167 (104) | 175 (110) | 191 (119) |
| 7.3.1 | Rail and tube fares | 224 | 0.50 | 112 | 1.87 | 235 (105) | 246 (109) | 268 (120) |
| 7.3.2 | Bus and coach fares | 79 | 0.50 | 39 | -0.24 | 82 (105) | 86 (110) | 94 (120) |
| 7.3.3 | Combined fares | 32 | 0.50 | 16 | 3.23 | 34 (105) | 36 (110) | 39 (120) |
| 7.3.4 | Other travel and transport | 679 | 0.50 | 340 | 1.31 | 713 (105) | 747 (110) | 815 (119) |
| 8.1 | Postal services | 33 | 0.50 | 17 | 0.95 | 35 (105) | 37 (110) | 40 (120) |
| 8.2 | Telephone and telefax equipment | 59 | 0.50 | 29 | 1.35 | 62 (105) | 65 (110) | 71 (119) |
| 8.3 | Telephone and telefax services | 642 | 0.50 | 321 | 0.50 | 674 (105) | 706 (110) | 770 (120) |
| 8.4 | Internet subscription fees | 196 | 0.50 | 98 | 0.47 | 206 (104) | 216 (110) | 235 (120) |
| 9.1.1 | Audio equipment and accessories, CD players | 55 | 0.50 | 28 | 1.31 | 58 (105) | 61 (110) | 66 (120) |
| 9.1.2 | TV, video and computers | 182 | 0.50 | 91 | 1.22 | 191 (105) | 200 (110) | 218 (120) |
| 9.1.3 | Photographic, cine and optical equipment | 17 | 0.50 | 8 | 1.09 | 18 (104) | 19 (110) | 20 (119) |
| 9.2 | Other major durables for recreation and culture | 139 | 0.50 | 69 | 4.03 | 146 (105) | 152 (110) | 166 (120) |
| 9.3.1 | Games, toys and hobbies | 162 | 0.50 | 81 | 0.70 | 170 (105) | 178 (110) | 194 (119) |
| 9.3.2 | Computer software and games | 55 | 0.50 | 27 | 0.45 | 57 (105) | 60 (110) | 66 (120) |
| 9.3.3 | Equipment for sport, camping and open-air recreation | 53 | 0.50 | 26 | 1.34 | 55 (105) | 58 (110) | 63 (119) |
| 9.3.4 | Horticultural goods, garden equipment and plants | 134 | 0.50 | 67 | 1.03 | 140 (105) | 147 (110) | 160 (120) |
| 9.3.5 | Pets and pet food | 292 | 0.50 | 146 | 0.72 | 307 (105) | 321 (110) | 351 (120) |
| 9.4.1 | Sports admissions, subscriptions, leisure class fees and equipment hire | 341 | 0.29 | 99 | 1.56 | 350 (102) | 360 (105) | 380 (111) |
| 9.4.2 | Cinema, theatre and museums etc | 163 | 0.29 | 47 | 1.61 | 168 (102) | 173 (105) | 182 (111) |
| 9.4.3 | TV, video, satellite rental, cable subscriptions and TV licences | 367 | 0.29 | 106 | 0.60 | 377 (102) | 388 (105) | 409 (111) |
| 9.4.4 | Miscellaneous entertainments | 68 | 0.29 | 20 | 0.83 | 70 (102) | 72 (105) | 75 (111) |
| 9.4.5 | Development of film, deposit for film development, passport photos, holiday and school photos | 15 | 0.29 | 4 | 1.61 | 16 (102) | 16 (105) | 17 (111) |
| 9.4.6 | Gambling payments | 134 | 0.29 | 39 | 0.38 | 138 (102) | 142 (105) | 150 (111) |
| 9.5.1 | Books | 66 | 0.66 | 43 | 1.51 | 70 (106) | 74 (113) | 83 (126) |
| 9.5.2 | Diaries, address books, cards etc | 109 | 0.66 | 72 | 0.88 | 116 (106) | 123 (113) | 137 (126) |
| 9.5.3 | Newspapers | 68 | 0.66 | 45 | 0.49 | 73 (106) | 77 (113) | 86 (126) |
| 9.5.4 | Magazines and periodicals | 36 | 0.66 | 24 | 0.50 | 38 (106) | 41 (113) | 45 (126) |
| 9.6.1 | Package holidays - UK | 84 | 0.50 | 42 | 1.92 | 88 (104) | 92 (109) | 101 (120) |
| 9.6.2 | Package holidays - abroad | 1311 | 0.50 | 655 | 1.80 | 1376 (105) | 1442 (110) | 1573 (120) |
| 10.1 | Education fees | 393 | 0.25 | 98 | 4.30 | 403 (102) | 413 (105) | 432 (110) |
| 10.2 | Payments for school trips, other ad-hoc expenditure | 21 | 0.50 | 10 | 1.81 | 22 (105) | 23 (110) | 25 (120) |
| 11.1.1 | Restaurant and café meals | 967 | 0.51 | 493 | 1.28 | 1017 (105) | 1066 (110) | 1165 (120) |
| 11.1.2 | Alcoholic drinks (away from home) | 417 | 0.51 | 213 | 1.63 | 438 (105) | 460 (110) | 502 (120) |
| 11.1.3 | Take away meals eaten at home | 265 | 0.51 | 135 | 0.55 | 278 (105) | 292 (110) | 319 (120) |
| 11.1.4 | Other take-away and snack food | 266 | 0.51 | 136 | 0.95 | 280 (105) | 293 (110) | 321 (120) |
| 11.1.5 | Contract catering (food) and canteens | 103 | 0.51 | 53 | 1.12 | 108 (105) | 113 (110) | 124 (120) |
| 11.2.1 | Holiday in the UK | 311 | 0.50 | 155 | 1.72 | 327 (105) | 342 (110) | 373 (120) |
| 11.2.2 | Holiday abroad | 243 | 0.50 | 122 | 1.83 | 256 (105) | 268 (110) | 292 (120) |
| 11.2.3 | Room hire | 3 | 0.50 | 1 | 0.00 | 3 (105) | 3 (110) | 3 (120) |
| 12.1.1 | Hairdressing, beauty treatment | 199 | 0.50 | 100 | 1.39 | 209 (105) | 219 (110) | 239 (120) |
| 12.1.2 | Toilet paper | 43 | 0.50 | 22 | 0.23 | 45 (105) | 47 (110) | 52 (120) |
| 12.1.3 | Toiletries and soap | 128 | 0.50 | 64 | 0.55 | 135 (105) | 141 (110) | 154 (120) |
| 12.1.4 | Baby toiletries and accessories (disposable) | 40 | 0.50 | 20 | -0.08 | 41 (105) | 43 (110) | 47 (120) |
| 12.1.5 | Hair products, cosmetics and related electrical appliances | 239 | 0.50 | 120 | 1.01 | 251 (105) | 263 (110) | 287 (119) |
| 12.2 | Personal effects | 207 | 0.50 | 104 | 1.21 | 218 (104) | 228 (110) | 249 (120) |
| 12.3 | Social protection | 225 | 0.50 | 112 | 3.70 | 236 (105) | 247 (110) | 270 (119) |
| 12.4.1 | Household insurances - structural, contents and appliances | 237 | 0.31 | 73 | 0.90 | 244 (103) | 251 (106) | 266 (112) |
| 12.4.2 | Medical insurance premiums | 101 | 0.31 | 31 | 1.76 | 105 (103) | 108 (106) | 114 (112) |
| 12.4.3 | Vehicle insurance including boat insurance | 563 | 0.31 | 175 | 0.80 | 581 (103) | 598 (106) | 633 (112) |
| 12.4.4 | Non-package holiday, other travel insurance | 5 | 0.31 | 2 | 1.00 | 5 (103) | 5 (106) | 6 (112) |
| 12.5.1 | Moving house | 161 | 0.50 | 81 | 1.77 | 169 (105) | 177 (110) | 193 (120) |
| 12.5.2 | Bank, building society, post office, credit card charges | 28 | 0.50 | 14 | 1.23 | 29 (105) | 31 (110) | 34 (119) |
| 12.5.3 | Other services and professional fees | 74 | 0.50 | 37 | 1.51 | 78 (105) | 81 (110) | 89 (120) |
| 13.3 | Holiday spending | 643 | 0.50 | 321 | 1.93 | 675 (105) | 707 (110) | 771 (119) |
| 13.4.2 | Cash gifts and donations | 657 | 0.00 | 0 | 1.51 | 657 (100) | 657 (100) | 657 (100) |
| 14.6 | Savings and investments | 329 | 0.00 | 0 | 2.80 | 329 (100) | 329 (100) | 329 (100) |
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