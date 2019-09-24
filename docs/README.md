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

| Item  | Description | Elastic. | Cost/£ | kgCO2/£ | kgCO2 | cost(%up) at £100/t | cost(%up) at £200/t | cost(%up) at £400/t |
| ----- | ----------- | --------:| ------:| -------:| -----:| -------------------:| -------------------:| -------------------:|
| 1.1.1 | Bread, rice and cereals | 283.40 | 0.72 | 204 | 0.35 | 20688.20(7199) | 41093.00(14399) | 81902.60(28799) |
| 1.1.2 | Pasta products | 22.36 | 0.72 | 16 | 0.41 | 1632.28(7200) | 3242.20(14400) | 6462.04(28800) |
| 1.1.3 | Buns, cakes, biscuits etc | 199.68 | 0.72 | 144 | 0.24 | 14576.64(7200) | 28953.60(14400) | 57707.52(28800) |
| 1.1.4 | Pastry (savoury) | 47.84 | 0.72 | 34 | 0.50 | 3492.32(7199) | 6936.80(14399) | 13825.76(28799) |
| 1.1.5 | Beef (fresh, chilled or frozen) | 102.96 | 1.80 | 185 | 0.68 | 18635.76(18000) | 37168.56(36000) | 74234.16(72000) |
| 1.1.6 | Pork (fresh, chilled or frozen) | 31.72 | 1.14 | 36 | 0.52 | 3647.80(11400) | 7263.88(22800) | 14496.04(45600) |
| 1.1.7 | Lamb (fresh, chilled or frozen) | 32.76 | 0.95 | 31 | 0.34 | 3131.68(9459) | 6230.60(18918) | 12428.44(37837) |
| 1.1.8 | Poultry (fresh, chilled or frozen) | 121.16 | 1.14 | 138 | 0.59 | 13933.40(11400) | 27745.64(22800) | 55370.12(45600) |
| 1.1.9 | Bacon and ham | 45.76 | 0.39 | 18 | 0.41 | 1810.79(3857) | 3575.82(7714) | 7105.87(15428) |
| 1.1.10 | Other meat and meat preparations | 331.24 | 1.30 | 431 | 0.30 | 43392.44(13000) | 86453.64(26000) | 172576.04(52000) |
| 1.1.11 | Fish and fish products | 151.32 | 0.72 | 109 | 0.60 | 11046.36(7200) | 21941.40(14400) | 43731.48(28800) |
| 1.1.12 | Milk | 112.84 | 0.72 | 81 | 0.06 | 8237.32(7200) | 16361.80(14400) | 32610.76(28800) |
| 1.1.13 | Cheese and curd | 103.48 | 0.72 | 75 | 0.60 | 7554.04(7200) | 15004.60(14400) | 29905.72(28800) |
| 1.1.14 | Eggs | 36.92 | 0.72 | 27 | 0.39 | 2695.16(7200) | 5353.40(14400) | 10669.88(28800) |
| 1.1.15 | Other milk products | 122.20 | 0.72 | 88 | 0.54 | 8920.60(7200) | 17719.00(14400) | 35315.80(28800) |
| 1.1.16 | Butter | 24.96 | 0.72 | 18 | 0.36 | 1822.08(7200) | 3619.20(14400) | 7213.44(28800) |
| 1.1.17 | Margarine, other vegetable fats and peanut butter | 30.68 | 0.72 | 22 | 0.30 | 2239.64(7200) | 4448.60(14400) | 8866.52(28800) |
| 1.1.18 | Cooking oils and fats | 17.68 | 0.72 | 13 | 0.29 | 1290.64(7200) | 2563.60(14400) | 5109.52(28800) |
| 1.1.19 | Fresh fruit | 207.48 | 0.72 | 149 | 0.63 | 15146.04(7199) | 30084.60(14399) | 59961.72(28799) |
| 1.1.20 | Other fresh, chilled or frozen fruits | 24.44 | 0.72 | 18 | 0.53 | 1784.12(7200) | 3543.80(14400) | 7063.16(28800) |
| 1.1.21 | Dried fruit and nuts | 43.68 | 0.72 | 31 | 0.76 | 3188.64(7200) | 6333.60(14400) | 12623.52(28800) |
| 1.1.22 | Preserved fruit and fruit based products | 7.80 | 0.72 | 6 | 0.30 | 569.40(7199) | 1131.00(14399) | 2254.20(28799) |
| 1.1.23 | Fresh vegetables | 223.60 | 0.72 | 161 | 0.68 | 16322.80(7200) | 32422.00(14400) | 64620.40(28800) |
| 1.1.24 | Dried vegetables | 3.90 | 0.72 | 3 | 0.51 | 284.70(7199) | 565.50(14399) | 1127.10(28799) |
| 1.1.25 | Other preserved or processed vegetables | 86.84 | 0.72 | 63 | 0.76 | 6339.32(7200) | 12591.80(14400) | 25096.76(28800) |
| 1.1.26 | Potatoes | 40.56 | 0.72 | 29 | 0.22 | 2960.88(7200) | 5881.20(14400) | 11721.84(28800) |
| 1.1.27 | Other tubers and products of tuber vegetables | 85.28 | 0.72 | 61 | 0.05 | 6225.44(7200) | 12365.60(14400) | 24645.92(28800) |
| 1.1.28 | Sugar and sugar products | 20.28 | 0.72 | 15 | 0.14 | 1480.44(7200) | 2940.60(14400) | 5860.92(28800) |
| 1.1.29 | Jams, marmalades | 16.12 | 0.72 | 12 | 0.33 | 1176.76(7200) | 2337.40(14400) | 4658.68(28800) |
| 1.1.30 | Chocolate | 109.72 | 0.72 | 79 | 0.40 | 8009.56(7199) | 15909.40(14399) | 31709.08(28799) |
| 1.1.31 | Confectionery products | 40.56 | 0.72 | 29 | 0.16 | 2960.88(7200) | 5881.20(14400) | 11721.84(28800) |
| 1.1.32 | Edible ices and ice cream | 34.32 | 0.72 | 25 | 0.19 | 2505.36(7200) | 4976.40(14400) | 9918.48(28800) |
| 1.1.33 | Other food products | 134.68 | 0.72 | 97 | 0.58 | 9831.64(7199) | 19528.60(14399) | 38922.52(28799) |
| 1.2.1 | Coffee | 48.88 | 0.50 | 24 | 0.47 | 2492.88(5000) | 4936.88(10000) | 9824.88(20000) |
| 1.2.2 | Tea | 22.88 | 0.50 | 11 | 0.51 | 1166.88(5000) | 2310.88(10000) | 4598.88(20000) |
| 1.2.3 | Cocoa and powdered chocolate | 5.20 | 0.50 | 3 | 0.00 | 265.20(5000) | 525.20(10000) | 1045.20(20000) |
| 1.2.4 | Fruit and vegetable juices (inc. fruit squash) | 55.64 | 0.50 | 28 | 0.45 | 2837.64(5000) | 5619.64(10000) | 11183.64(20000) |
| 1.2.5 | Mineral or spring waters | 20.80 | 0.50 | 10 | 0.36 | 1060.80(5000) | 2100.80(10000) | 4180.80(20000) |
| 1.2.6 | Soft drinks (inc. fizzy and ready to drink fruit drinks) | 102.96 | 0.50 | 51 | 0.05 | 5250.96(5000) | 10398.96(10000) | 20694.96(20000) |
| 2.1.1 | Spirits and liqueurs (brought home) | 101.92 | 0.50 | 51 | 0.64 | 5197.92(4999) | 10293.92(9999) | 20485.92(19999) |
| 2.1.2 | Wines, fortified wines (brought home) | 234.52 | 0.15 | 35 | 1.41 | 3752.32(1500) | 7270.12(3000) | 14305.72(6000) |
| 2.1.3 | Beer, lager, ciders and perry (brought home) | 113.36 | 0.50 | 57 | 0.64 | 5781.36(5000) | 11449.36(10000) | 22785.36(20000) |
| 2.1.4 | Alcopops (brought home) | 2.60 | 0.50 | 1 | 0.00 | 132.60(5000) | 262.60(10000) | 522.60(20000) |
| 2.2.1 | Cigarettes | 137.28 | 0.50 | 69 | -0.33 | 7001.28(5000) | 13865.28(10000) | 27593.28(20000) |
| 2.2.2 | Cigars, other tobacco products and narcotics | 58.76 | 0.50 | 29 | -0.95 | 2996.76(5000) | 5934.76(10000) | 11810.76(20000) |
| 3.1.1 | Men's outer garments | 263.64 | 0.33 | 87 | 1.40 | 8963.76(3299) | 17663.88(6599) | 35064.12(13199) |
| 3.1.2 | Men's under garments | 27.56 | 0.33 | 9 | 0.75 | 937.04(3300) | 1846.52(6600) | 3665.48(13200) |
| 3.1.3 | Women's outer garments | 438.36 | 0.33 | 145 | 1.10 | 14904.24(3300) | 29370.12(6600) | 58301.88(13200) |
| 3.1.4 | Women's under garments | 64.48 | 0.33 | 21 | 0.65 | 2192.32(3300) | 4320.16(6600) | 8575.84(13200) |
| 3.1.5 | Boys' outer garments (5-15) | 51.48 | 0.33 | 17 | 0.75 | 1750.32(3299) | 3449.16(6599) | 6846.84(13199) |
| 3.1.6 | Girls' outer garments (5-15) | 51.48 | 0.33 | 17 | 0.54 | 1750.32(3299) | 3449.16(6599) | 6846.84(13199) |
| 3.1.7 | Infants' outer garments (under 5) | 34.32 | 0.33 | 11 | 0.47 | 1166.88(3300) | 2299.44(6600) | 4564.56(13200) |
| 3.1.8 | Children's under garments (under 16) | 21.32 | 0.33 | 7 | 0.22 | 724.88(3300) | 1428.44(6600) | 2835.56(13200) |
| 3.1.9 | Accessories | 40.04 | 0.33 | 13 | 1.04 | 1361.36(3300) | 2682.68(6600) | 5325.32(13200) |
| 3.1.10 | Haberdashery and clothing hire | 15.08 | 0.33 | 5 | 0.84 | 512.72(3300) | 1010.36(6600) | 2005.64(13200) |
| 3.1.11 | Dry cleaners, laundry and dyeing | 8.58 | 0.33 | 3 | 1.83 | 291.72(3300) | 574.86(6600) | 1141.14(13200) |
| 3.2 | Footwear | 247.52 | 0.33 | 82 | 0.64 | 8415.68(3300) | 16583.84(6600) | 32920.16(13200) |
| 4.1.3 | Net rent | 1878.76 | 0.50 | 939 | 0.18 | 95816.76(5000) | 189754.76(10000) | 377630.76(20000) |
| 4.1.4 | Second dwelling rent | 2.60 | 0.50 | 1 | 0.00 | 132.60(5000) | 262.60(10000) | 522.60(20000) |
| 4.2 | Maintenance and repair of dwelling | 424.32 | 0.50 | 212 | 1.16 | 21640.32(5000) | 42856.32(10000) | 85288.32(20000) |
| 4.3 | Water supply and miscellaneous services relating to the dwelling | 482.56 | 0.50 | 241 | 0.30 | 24610.56(5000) | 48738.56(10000) | 96994.56(20000) |
| 4.4.1 | Electricity | 591.76 | 2.32 | 1372 | 0.14 | 137790.76(23184) | 274989.76(46369) | 549387.75(92739) |
| 4.4.2 | Gas | 511.68 | 6.41 | 3280 | 0.19 | 328557.39(64111) | 656603.11(128222) | 1312694.54(256445) |
| 4.4.3 | Other fuels | 69.16 | 0.50 | 35 | 0.75 | 3527.16(5000) | 6985.16(10000) | 13901.16(20000) |
| 5.1.1 | Furniture and furnishings | 977.60 | 0.50 | 489 | 1.26 | 49857.60(5000) | 98737.60(10000) | 196497.60(20000) |
| 5.1.2 | Floor coverings | 196.56 | 0.50 | 98 | 1.08 | 10024.56(5000) | 19852.56(10000) | 39508.56(20000) |
| 5.2 | Household textiles | 117.00 | 0.50 | 58 | 1.26 | 5967.00(5000) | 11817.00(10000) | 23517.00(20000) |
| 5.3 | Household appliances | 225.68 | 0.50 | 113 | 1.28 | 11509.68(5000) | 22793.68(10000) | 45361.68(20000) |
| 5.4 | Glassware, tableware and household utensils | 101.92 | 0.50 | 51 | 0.80 | 5197.92(5000) | 10293.92(10000) | 20485.92(20000) |
| 5.5 | Tools and equipment for house and garden | 148.72 | 0.50 | 74 | 1.27 | 7584.72(4999) | 15020.72(9999) | 29892.72(19999) |
| 5.6.1 | Cleaning materials | 122.72 | 0.50 | 61 | 0.43 | 6258.72(5000) | 12394.72(10000) | 24666.72(20000) |
| 5.6.2 | Household goods and hardware | 87.36 | 0.50 | 44 | 0.51 | 4455.36(5000) | 8823.36(10000) | 17559.36(20000) |
| 5.6.3 | Domestic services, carpet cleaning, hire/repair of furniture/furnishings | 137.80 | 0.50 | 69 | 1.60 | 7027.80(5000) | 13917.80(10000) | 27697.80(20000) |
| 6.1.1 | Medicines, prescriptions, healthcare products etc | 109.20 | 0.66 | 72 | 0.74 | 7316.40(6600) | 14523.60(13200) | 28938.00(26400) |
| 6.1.2 | Spectacles, lenses, accessories and repairs | 89.44 | 0.50 | 45 | 2.04 | 4561.44(5000) | 9033.44(10000) | 17977.44(20000) |
| 6.2 | Hospital services | 158.60 | 0.50 | 79 | 1.81 | 8088.60(5000) | 16018.60(10000) | 31878.60(20000) |
| 7.1.1 | Purchase of new cars and vans | 513.50 | 0.78 | 401 | 3.45 | 40566.50(7800) | 80619.50(15600) | 160725.50(31200) |
| 7.1.2 | Purchase of second hand cars or vans | 888.16 | 0.78 | 693 | 1.34 | 70164.64(7800) | 139441.12(15600) | 277994.08(31200) |
| 7.1.3 | Purchase of motorcycles and other vehicles | 31.98 | 0.78 | 25 | 1.76 | 2526.42(7800) | 5020.86(15600) | 10009.74(31200) |
| 7.2.1 | Spares and accessories | 124.28 | 0.50 | 62 | 1.47 | 6338.28(5000) | 12552.28(10000) | 24980.28(20000) |
| 7.2.2 | Petrol, diesel and other motor oils | 1103.44 | 1.78 | 1961 | 1.09 | 197176.24(17769) | 393249.04(35538) | 785394.64(71076) |
| 7.2.3 | Repairs and servicing | 338.52 | 0.50 | 169 | 1.23 | 17264.52(5000) | 34190.52(10000) | 68042.52(20000) |
| 7.2.4 | Other motoring costs | 159.12 | 0.50 | 80 | 1.28 | 8115.12(5000) | 16071.12(10000) | 31983.12(20000) |
| 7.3.1 | Rail and tube fares | 223.60 | 0.50 | 112 | 1.87 | 11403.60(5000) | 22583.60(10000) | 44943.60(20000) |
| 7.3.2 | Bus and coach fares | 78.52 | 0.50 | 39 | -0.24 | 4004.52(5000) | 7930.52(10000) | 15782.52(20000) |
| 7.3.3 | Combined fares | 32.50 | 0.50 | 16 | 3.23 | 1657.50(5000) | 3282.50(10000) | 6532.50(20000) |
| 7.3.4 | Other travel and transport | 679.12 | 0.50 | 340 | 1.31 | 34635.12(5000) | 68591.12(10000) | 136503.12(20000) |
| 8.1 | Postal services | 33.28 | 0.50 | 17 | 0.95 | 1697.28(5000) | 3361.28(10000) | 6689.28(20000) |
| 8.2 | Telephone and telefax equipment | 58.76 | 0.50 | 29 | 1.35 | 2996.76(5000) | 5934.76(10000) | 11810.76(20000) |
| 8.3 | Telephone and telefax services | 641.68 | 0.50 | 321 | 0.50 | 32725.68(5000) | 64809.68(10000) | 128977.68(20000) |
| 8.4 | Internet subscription fees | 196.04 | 0.50 | 98 | 0.47 | 9998.04(5000) | 19800.04(10000) | 39404.04(20000) |
| 9.1.1 | Audio equipment and accessories, CD players | 55.12 | 0.50 | 28 | 1.31 | 2811.12(5000) | 5567.12(10000) | 11079.12(20000) |
| 9.1.2 | TV, video and computers | 182.00 | 0.50 | 91 | 1.22 | 9282.00(5000) | 18382.00(10000) | 36582.00(20000) |
| 9.1.3 | Photographic, cine and optical equipment | 16.90 | 0.50 | 8 | 1.09 | 861.90(5000) | 1706.90(10000) | 3396.90(20000) |
| 9.2 | Other major durables for recreation and culture | 138.58 | 0.50 | 69 | 4.03 | 7067.58(5000) | 13996.58(10000) | 27854.58(20000) |
| 9.3.1 | Games, toys and hobbies | 161.72 | 0.50 | 81 | 0.70 | 8247.72(5000) | 16333.72(10000) | 32505.72(20000) |
| 9.3.2 | Computer software and games | 54.60 | 0.50 | 27 | 0.45 | 2784.60(5000) | 5514.60(10000) | 10974.60(20000) |
| 9.3.3 | Equipment for sport, camping and open-air recreation | 52.52 | 0.50 | 26 | 1.34 | 2678.52(5000) | 5304.52(10000) | 10556.52(20000) |
| 9.3.4 | Horticultural goods, garden equipment and plants | 133.64 | 0.50 | 67 | 1.03 | 6815.64(5000) | 13497.64(10000) | 26861.64(20000) |
| 9.3.5 | Pets and pet food | 292.24 | 0.50 | 146 | 0.72 | 14904.24(5000) | 29516.24(10000) | 58740.24(20000) |
| 9.4.1 | Sports admissions, subscriptions, leisure class fees and equipment hire | 340.60 | 0.29 | 99 | 1.56 | 10218.00(2900) | 20095.40(5800) | 39850.20(11600) |
| 9.4.2 | Cinema, theatre and museums etc | 163.28 | 0.29 | 47 | 1.61 | 4898.40(2900) | 9633.52(5800) | 19103.76(11600) |
| 9.4.3 | TV, video, satellite rental, cable subscriptions and TV licences | 366.60 | 0.29 | 106 | 0.60 | 10998.00(2900) | 21629.40(5800) | 42892.20(11600) |
| 9.4.4 | Miscellaneous entertainments | 67.60 | 0.29 | 20 | 0.83 | 2028.00(2900) | 3988.40(5800) | 7909.20(11600) |
| 9.4.5 | Development of film, deposit for film development, passport photos, holiday and school photos | 15.08 | 0.29 | 4 | 1.61 | 452.40(2900) | 889.72(5800) | 1764.36(11600) |
| 9.4.6 | Gambling payments | 134.16 | 0.29 | 39 | 0.38 | 4024.80(2900) | 7915.44(5800) | 15696.72(11600) |
| 9.5.1 | Books | 65.52 | 0.66 | 43 | 1.51 | 4389.84(6600) | 8714.16(13200) | 17362.80(26400) |
| 9.5.2 | Diaries, address books, cards etc | 108.68 | 0.66 | 72 | 0.88 | 7281.56(6599) | 14454.44(13199) | 28800.20(26399) |
| 9.5.3 | Newspapers | 68.12 | 0.66 | 45 | 0.49 | 4564.04(6600) | 9059.96(13200) | 18051.80(26400) |
| 9.5.4 | Magazines and periodicals | 35.88 | 0.66 | 24 | 0.50 | 2403.96(6600) | 4772.04(13200) | 9508.20(26400) |
| 9.6.1 | Package holidays - UK | 83.98 | 0.50 | 42 | 1.92 | 4282.98(5000) | 8481.98(10000) | 16879.98(20000) |
| 9.6.2 | Package holidays - abroad | 1310.92 | 0.50 | 655 | 1.80 | 66856.92(4999) | 132402.92(9999) | 263494.92(19999) |
| 10.1 | Education fees | 393.12 | 0.25 | 98 | 4.30 | 10221.12(2500) | 20049.12(5000) | 39705.12(10000) |
| 10.2 | Payments for school trips, other ad-hoc expenditure | 20.80 | 0.50 | 10 | 1.81 | 1060.80(5000) | 2100.80(10000) | 4180.80(20000) |
| 11.1.1 | Restaurant and café meals | 967.20 | 0.51 | 493 | 1.28 | 50294.40(5100) | 99621.60(10200) | 198276.00(20400) |
| 11.1.2 | Alcoholic drinks (away from home) | 417.04 | 0.51 | 213 | 1.63 | 21686.08(5099) | 42955.12(10199) | 85493.20(20399) |
| 11.1.3 | Take away meals eaten at home | 264.68 | 0.51 | 135 | 0.55 | 13763.36(5100) | 27262.04(10200) | 54259.40(20400) |
| 11.1.4 | Other take-away and snack food | 266.24 | 0.51 | 136 | 0.95 | 13844.48(5100) | 27422.72(10200) | 54579.20(20400) |
| 11.1.5 | Contract catering (food) and canteens | 102.96 | 0.51 | 53 | 1.12 | 5353.92(5100) | 10604.88(10200) | 21106.80(20400) |
| 11.2.1 | Holiday in the UK | 310.96 | 0.50 | 155 | 1.72 | 15858.96(5000) | 31406.96(10000) | 62502.96(20000) |
| 11.2.2 | Holiday abroad | 243.36 | 0.50 | 122 | 1.83 | 12411.36(5000) | 24579.36(10000) | 48915.36(20000) |
| 11.2.3 | Room hire | 2.60 | 0.50 | 1 | 0.00 | 132.60(5000) | 262.60(10000) | 522.60(20000) |
| 12.1.1 | Hairdressing, beauty treatment | 199.16 | 0.50 | 100 | 1.39 | 10157.16(5000) | 20115.16(10000) | 40031.16(20000) |
| 12.1.2 | Toilet paper | 43.16 | 0.50 | 22 | 0.23 | 2201.16(5000) | 4359.16(10000) | 8675.16(20000) |
| 12.1.3 | Toiletries and soap | 128.44 | 0.50 | 64 | 0.55 | 6550.44(5000) | 12972.44(10000) | 25816.44(20000) |
| 12.1.4 | Baby toiletries and accessories (disposable) | 39.52 | 0.50 | 20 | -0.08 | 2015.52(5000) | 3991.52(10000) | 7943.52(20000) |
| 12.1.5 | Hair products, cosmetics and related electrical appliances | 239.20 | 0.50 | 120 | 1.01 | 12199.20(5000) | 24159.20(10000) | 48079.20(20000) |
| 12.2 | Personal effects | 207.48 | 0.50 | 104 | 1.21 | 10581.48(5000) | 20955.48(10000) | 41703.48(20000) |
| 12.3 | Social protection | 224.64 | 0.50 | 112 | 3.70 | 11456.64(5000) | 22688.64(10000) | 45152.64(20000) |
| 12.4.1 | Household insurances - structural, contents and appliances | 236.60 | 0.31 | 73 | 0.90 | 7571.20(3100) | 14905.80(6200) | 29575.00(12400) |
| 12.4.2 | Medical insurance premiums | 101.40 | 0.31 | 31 | 1.76 | 3244.80(3100) | 6388.20(6200) | 12675.00(12400) |
| 12.4.3 | Vehicle insurance including boat insurance | 563.16 | 0.31 | 175 | 0.80 | 18021.12(3100) | 35479.08(6200) | 70395.00(12400) |
| 12.4.4 | Non-package holiday, other travel insurance | 4.94 | 0.31 | 2 | 1.00 | 158.08(3100) | 311.22(6200) | 617.50(12400) |
| 12.5.1 | Moving house | 161.20 | 0.50 | 81 | 1.77 | 8221.20(5000) | 16281.20(10000) | 32401.20(20000) |
| 12.5.2 | Bank, building society, post office, credit card charges | 28.08 | 0.50 | 14 | 1.23 | 1432.08(5000) | 2836.08(10000) | 5644.08(20000) |
| 12.5.3 | Other services and professional fees | 73.84 | 0.50 | 37 | 1.51 | 3765.84(5000) | 7457.84(10000) | 14841.84(20000) |
| 13.3 | Holiday spending | 642.72 | 0.50 | 321 | 1.93 | 32778.72(5000) | 64914.72(10000) | 129186.72(20000) |
| 13.4.2 | Cash gifts and donations | 656.76 | 0.00 | 0 | 1.51 | 656.76(0) | 656.76(0) | 656.76(0) |
| 14.6 | Savings and investments | 329.16 | 0.00 | 0 | 2.80 | 329.16(0) | 329.16(0) | 329.16(0) |
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