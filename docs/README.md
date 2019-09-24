# Analysis of a basic carbon tax for the UK

## Abstract

This project investigates the inpact of a [Carbon Tax](https://en.wikipedia.org/wiki/Carbon_tax) on UK household spending.  It is widely accepted that we must achieve [carbon neutrality](https://en.wikipedia.org/wiki/Carbon_neutrality) as soon as is practical and a carbon tax is one of the major tools that are available to achive this.

This project takes an intentionally basic view of the problem.  It assumes that the UK can implement a carbon tax and that the revenues raised can be used to sequester carbon such that we achieve neurality.  In order not to disavantage the lowest income households a universal household income is included so that there is no net change to decile 2 (with lower deciles gaining and higher deciles contributing).  Constraining the problem allows for an analyis of the carbon tax.  All source code is available at [https://github.com/drtonyr/basicCarbonTaxUK] under MIT licence so that others may freely build on this work.

## Methodolgy

The [Office for National Statistics](https://www.ons.gov.uk/) collects and publishes a wide variety of data for the UK, specifically [https://www.ons.gov.uk/peoplepopulationandcommunity/personalandhouseholdfinances/expenditure/datasets/detailedhouseholdexpenditurebyequivaliseddisposableincomedecilegroupoecdmodifiedscaleuktable31e](Detailed household expenditure by equivalised disposable income decile group: Table 3.1E).

### Calculation of elasticity

### Calculation of carbon footprint

## Analysis by item

We can now summarise all expenditure items.  The ten highest values WILL BE highlighted.

| Item  | Description | Soend/£ | kgCO2/£ | kgCO2 | elasticity |
| ----- | ----------- | -------:| -------:| -----:| ----------:|
| 1.1.1 | Bread, rice and cereals | 283.40 | 0.72 | 0.20 | 0.35 |
| 1.1.2 | Pasta products | 22.36 | 0.72 | 0.02 | 0.41 |
| 1.1.3 | Buns, cakes, biscuits etc | 199.68 | 0.72 | 0.14 | 0.24 |
| 1.1.4 | Pastry (savoury) | 47.84 | 0.72 | 0.03 | 0.50 |
| 1.1.5 | Beef (fresh, chilled or frozen) | 102.96 | 1.80 | 0.19 | 0.68 |
| 1.1.6 | Pork (fresh, chilled or frozen) | 31.72 | 1.14 | 0.04 | 0.52 |
| 1.1.7 | Lamb (fresh, chilled or frozen) | 32.76 | 0.95 | 0.03 | 0.34 |
| 1.1.8 | Poultry (fresh, chilled or frozen) | 121.16 | 1.14 | 0.14 | 0.59 |
| 1.1.9 | Bacon and ham | 45.76 | 0.39 | 0.02 | 0.41 |
| 1.1.10 | Other meat and meat preparations | 331.24 | 1.30 | 0.43 | 0.30 |
| 1.1.11 | Fish and fish products | 151.32 | 0.72 | 0.11 | 0.60 |
| 1.1.12 | Milk | 112.84 | 0.72 | 0.08 | 0.06 |
| 1.1.13 | Cheese and curd | 103.48 | 0.72 | 0.07 | 0.60 |
| 1.1.14 | Eggs | 36.92 | 0.72 | 0.03 | 0.39 |
| 1.1.15 | Other milk products | 122.20 | 0.72 | 0.09 | 0.54 |
| 1.1.16 | Butter | 24.96 | 0.72 | 0.02 | 0.36 |
| 1.1.17 | Margarine, other vegetable fats and peanut butter | 30.68 | 0.72 | 0.02 | 0.30 |
| 1.1.18 | Cooking oils and fats | 17.68 | 0.72 | 0.01 | 0.29 |
| 1.1.19 | Fresh fruit | 207.48 | 0.72 | 0.15 | 0.63 |
| 1.1.20 | Other fresh, chilled or frozen fruits | 24.44 | 0.72 | 0.02 | 0.53 |
| 1.1.21 | Dried fruit and nuts | 43.68 | 0.72 | 0.03 | 0.76 |
| 1.1.22 | Preserved fruit and fruit based products | 7.80 | 0.72 | 0.01 | 0.30 |
| 1.1.23 | Fresh vegetables | 223.60 | 0.72 | 0.16 | 0.68 |
| 1.1.24 | Dried vegetables | 3.90 | 0.72 | 0.00 | 0.51 |
| 1.1.25 | Other preserved or processed vegetables | 86.84 | 0.72 | 0.06 | 0.76 |
| 1.1.26 | Potatoes | 40.56 | 0.72 | 0.03 | 0.22 |
| 1.1.27 | Other tubers and products of tuber vegetables | 85.28 | 0.72 | 0.06 | 0.05 |
| 1.1.28 | Sugar and sugar products | 20.28 | 0.72 | 0.01 | 0.14 |
| 1.1.29 | Jams, marmalades | 16.12 | 0.72 | 0.01 | 0.33 |
| 1.1.30 | Chocolate | 109.72 | 0.72 | 0.08 | 0.40 |
| 1.1.31 | Confectionery products | 40.56 | 0.72 | 0.03 | 0.16 |
| 1.1.32 | Edible ices and ice cream | 34.32 | 0.72 | 0.02 | 0.19 |
| 1.1.33 | Other food products | 134.68 | 0.72 | 0.10 | 0.58 |
| 1.2.1 | Coffee | 48.88 | 0.50 | 0.02 | 0.47 |
| 1.2.2 | Tea | 22.88 | 0.50 | 0.01 | 0.51 |
| 1.2.3 | Cocoa and powdered chocolate | 5.20 | 0.50 | 0.00 | 0.00 |
| 1.2.4 | Fruit and vegetable juices (inc. fruit squash) | 55.64 | 0.50 | 0.03 | 0.45 |
| 1.2.5 | Mineral or spring waters | 20.80 | 0.50 | 0.01 | 0.36 |
| 1.2.6 | Soft drinks (inc. fizzy and ready to drink fruit drinks) | 102.96 | 0.50 | 0.05 | 0.05 |
| 2.1.1 | Spirits and liqueurs (brought home) | 101.92 | 0.50 | 0.05 | 0.64 |
| 2.1.2 | Wines, fortified wines (brought home) | 234.52 | 0.15 | 0.04 | 1.41 |
| 2.1.3 | Beer, lager, ciders and perry (brought home) | 113.36 | 0.50 | 0.06 | 0.64 |
| 2.1.4 | Alcopops (brought home) | 2.60 | 0.50 | 0.00 | 0.00 |
| 2.2.1 | Cigarettes | 137.28 | 0.50 | 0.07 | -0.33 |
| 2.2.2 | Cigars, other tobacco products and narcotics | 58.76 | 0.50 | 0.03 | -0.95 |
| 3.1.1 | Men's outer garments | 263.64 | 0.33 | 0.09 | 1.40 |
| 3.1.2 | Men's under garments | 27.56 | 0.33 | 0.01 | 0.75 |
| 3.1.3 | Women's outer garments | 438.36 | 0.33 | 0.14 | 1.10 |
| 3.1.4 | Women's under garments | 64.48 | 0.33 | 0.02 | 0.65 |
| 3.1.5 | Boys' outer garments (5-15) | 51.48 | 0.33 | 0.02 | 0.75 |
| 3.1.6 | Girls' outer garments (5-15) | 51.48 | 0.33 | 0.02 | 0.54 |
| 3.1.7 | Infants' outer garments (under 5) | 34.32 | 0.33 | 0.01 | 0.47 |
| 3.1.8 | Children's under garments (under 16) | 21.32 | 0.33 | 0.01 | 0.22 |
| 3.1.9 | Accessories | 40.04 | 0.33 | 0.01 | 1.04 |
| 3.1.10 | Haberdashery and clothing hire | 15.08 | 0.33 | 0.00 | 0.84 |
| 3.1.11 | Dry cleaners, laundry and dyeing | 8.58 | 0.33 | 0.00 | 1.83 |
| 3.2 | Footwear | 247.52 | 0.33 | 0.08 | 0.64 |
| 4.1.3 | Net rent | 1878.76 | 0.50 | 0.94 | 0.18 |
| 4.1.4 | Second dwelling rent | 2.60 | 0.50 | 0.00 | 0.00 |
| 4.2 | Maintenance and repair of dwelling | 424.32 | 0.50 | 0.21 | 1.16 |
| 4.3 | Water supply and miscellaneous services relating to the dwelling | 482.56 | 0.50 | 0.24 | 0.30 |
| 4.4.1 | Electricity | 591.76 | 2.32 | 1.37 | 0.14 |
| 4.4.2 | Gas | 511.68 | 6.41 | 3.28 | 0.19 |
| 4.4.3 | Other fuels | 69.16 | 0.50 | 0.03 | 0.75 |
| 5.1.1 | Furniture and furnishings | 977.60 | 0.50 | 0.49 | 1.26 |
| 5.1.2 | Floor coverings | 196.56 | 0.50 | 0.10 | 1.08 |
| 5.2 | Household textiles | 117.00 | 0.50 | 0.06 | 1.26 |
| 5.3 | Household appliances | 225.68 | 0.50 | 0.11 | 1.28 |
| 5.4 | Glassware, tableware and household utensils | 101.92 | 0.50 | 0.05 | 0.80 |
| 5.5 | Tools and equipment for house and garden | 148.72 | 0.50 | 0.07 | 1.27 |
| 5.6.1 | Cleaning materials | 122.72 | 0.50 | 0.06 | 0.43 |
| 5.6.2 | Household goods and hardware | 87.36 | 0.50 | 0.04 | 0.51 |
| 5.6.3 | Domestic services, carpet cleaning, hire/repair of furniture/furnishings | 137.80 | 0.50 | 0.07 | 1.60 |
| 6.1.1 | Medicines, prescriptions, healthcare products etc | 109.20 | 0.66 | 0.07 | 0.74 |
| 6.1.2 | Spectacles, lenses, accessories and repairs | 89.44 | 0.50 | 0.04 | 2.04 |
| 6.2 | Hospital services | 158.60 | 0.50 | 0.08 | 1.81 |
| 7.1.1 | Purchase of new cars and vans | 513.50 | 0.78 | 0.40 | 3.45 |
| 7.1.2 | Purchase of second hand cars or vans | 888.16 | 0.78 | 0.69 | 1.34 |
| 7.1.3 | Purchase of motorcycles and other vehicles | 31.98 | 0.78 | 0.02 | 1.76 |
| 7.2.1 | Spares and accessories | 124.28 | 0.50 | 0.06 | 1.47 |
| 7.2.2 | Petrol, diesel and other motor oils | 1103.44 | 1.78 | 1.96 | 1.09 |
| 7.2.3 | Repairs and servicing | 338.52 | 0.50 | 0.17 | 1.23 |
| 7.2.4 | Other motoring costs | 159.12 | 0.50 | 0.08 | 1.28 |
| 7.3.1 | Rail and tube fares | 223.60 | 0.50 | 0.11 | 1.87 |
| 7.3.2 | Bus and coach fares | 78.52 | 0.50 | 0.04 | -0.24 |
| 7.3.3 | Combined fares | 32.50 | 0.50 | 0.02 | 3.23 |
| 7.3.4 | Other travel and transport | 679.12 | 0.50 | 0.34 | 1.31 |
| 8.1 | Postal services | 33.28 | 0.50 | 0.02 | 0.95 |
| 8.2 | Telephone and telefax equipment | 58.76 | 0.50 | 0.03 | 1.35 |
| 8.3 | Telephone and telefax services | 641.68 | 0.50 | 0.32 | 0.50 |
| 8.4 | Internet subscription fees | 196.04 | 0.50 | 0.10 | 0.47 |
| 9.1.1 | Audio equipment and accessories, CD players | 55.12 | 0.50 | 0.03 | 1.31 |
| 9.1.2 | TV, video and computers | 182.00 | 0.50 | 0.09 | 1.22 |
| 9.1.3 | Photographic, cine and optical equipment | 16.90 | 0.50 | 0.01 | 1.09 |
| 9.2 | Other major durables for recreation and culture | 138.58 | 0.50 | 0.07 | 4.03 |
| 9.3.1 | Games, toys and hobbies | 161.72 | 0.50 | 0.08 | 0.70 |
| 9.3.2 | Computer software and games | 54.60 | 0.50 | 0.03 | 0.45 |
| 9.3.3 | Equipment for sport, camping and open-air recreation | 52.52 | 0.50 | 0.03 | 1.34 |
| 9.3.4 | Horticultural goods, garden equipment and plants | 133.64 | 0.50 | 0.07 | 1.03 |
| 9.3.5 | Pets and pet food | 292.24 | 0.50 | 0.15 | 0.72 |
| 9.4.1 | Sports admissions, subscriptions, leisure class fees and equipment hire | 340.60 | 0.29 | 0.10 | 1.56 |
| 9.4.2 | Cinema, theatre and museums etc | 163.28 | 0.29 | 0.05 | 1.61 |
| 9.4.3 | TV, video, satellite rental, cable subscriptions and TV licences | 366.60 | 0.29 | 0.11 | 0.60 |
| 9.4.4 | Miscellaneous entertainments | 67.60 | 0.29 | 0.02 | 0.83 |
| 9.4.5 | Development of film, deposit for film development, passport photos, holiday and school photos | 15.08 | 0.29 | 0.00 | 1.61 |
| 9.4.6 | Gambling payments | 134.16 | 0.29 | 0.04 | 0.38 |
| 9.5.1 | Books | 65.52 | 0.66 | 0.04 | 1.51 |
| 9.5.2 | Diaries, address books, cards etc | 108.68 | 0.66 | 0.07 | 0.88 |
| 9.5.3 | Newspapers | 68.12 | 0.66 | 0.04 | 0.49 |
| 9.5.4 | Magazines and periodicals | 35.88 | 0.66 | 0.02 | 0.50 |
| 9.6.1 | Package holidays - UK | 83.98 | 0.50 | 0.04 | 1.92 |
| 9.6.2 | Package holidays - abroad | 1310.92 | 0.50 | 0.66 | 1.80 |
| 10.1 | Education fees | 393.12 | 0.25 | 0.10 | 4.30 |
| 10.2 | Payments for school trips, other ad-hoc expenditure | 20.80 | 0.50 | 0.01 | 1.81 |
| 11.1.1 | Restaurant and café meals | 967.20 | 0.51 | 0.49 | 1.28 |
| 11.1.2 | Alcoholic drinks (away from home) | 417.04 | 0.51 | 0.21 | 1.63 |
| 11.1.3 | Take away meals eaten at home | 264.68 | 0.51 | 0.13 | 0.55 |
| 11.1.4 | Other take-away and snack food | 266.24 | 0.51 | 0.14 | 0.95 |
| 11.1.5 | Contract catering (food) and canteens | 102.96 | 0.51 | 0.05 | 1.12 |
| 11.2.1 | Holiday in the UK | 310.96 | 0.50 | 0.16 | 1.72 |
| 11.2.2 | Holiday abroad | 243.36 | 0.50 | 0.12 | 1.83 |
| 11.2.3 | Room hire | 2.60 | 0.50 | 0.00 | 0.00 |
| 12.1.1 | Hairdressing, beauty treatment | 199.16 | 0.50 | 0.10 | 1.39 |
| 12.1.2 | Toilet paper | 43.16 | 0.50 | 0.02 | 0.23 |
| 12.1.3 | Toiletries and soap | 128.44 | 0.50 | 0.06 | 0.55 |
| 12.1.4 | Baby toiletries and accessories (disposable) | 39.52 | 0.50 | 0.02 | -0.08 |
| 12.1.5 | Hair products, cosmetics and related electrical appliances | 239.20 | 0.50 | 0.12 | 1.01 |
| 12.2 | Personal effects | 207.48 | 0.50 | 0.10 | 1.21 |
| 12.3 | Social protection | 224.64 | 0.50 | 0.11 | 3.70 |
| 12.4.1 | Household insurances - structural, contents and appliances | 236.60 | 0.31 | 0.07 | 0.90 |
| 12.4.2 | Medical insurance premiums | 101.40 | 0.31 | 0.03 | 1.76 |
| 12.4.3 | Vehicle insurance including boat insurance | 563.16 | 0.31 | 0.17 | 0.80 |
| 12.4.4 | Non-package holiday, other travel insurance | 4.94 | 0.31 | 0.00 | 1.00 |
| 12.5.1 | Moving house | 161.20 | 0.50 | 0.08 | 1.77 |
| 12.5.2 | Bank, building society, post office, credit card charges | 28.08 | 0.50 | 0.01 | 1.23 |
| 12.5.3 | Other services and professional fees | 73.84 | 0.50 | 0.04 | 1.51 |
| 13.3 | Holiday spending | 642.72 | 0.50 | 0.32 | 1.93 |
| 13.4.2 | Cash gifts and donations | 656.76 | 0.00 | 0.00 | 1.51 |
| 14.6 | Savings and investments | 329.16 | 0.00 | 0.00 | 2.80 |
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