map2 = [{'label': 'Mojave Desert', 'lon':266, 'lat':636, 'popup':'Subtropical high-pressure zones in deserts limit the ability for cloud to release rain. Nearby mountain ranges also block moisture from reaching the Mojave Desert.'},
{'label': 'Sierra Nevada Mountains', 'lon':152, 'lat':828, 'popup':'Moist wind hits mountains and has to rise. At higher elevations, the air cools and condenses into snow and rain.'},
{'label': 'Southeast', 'lon':1260, 'lat':318, 'popup':'The Gulf of Mexico is a major source of moisture for this region. Moist air is often pulled inland, leading to large quantities of rain.'},
{'label': 'Washington', 'lon':179, 'lat':1179, 'popup':'Clockwise currents in the pacific ocean cause storms to be pushed inland, causing high amounts of rain. This doesn\'t happen to California because the currents run parallel to the coast.'},
{'label': 'San Joaquin Valley', 'lon':147, 'lat':661, 'popup':'As air goes over the Coast Range, it cools and loses moisture, so the air is dry when it lowers elevation to go into the San Joaquin Valley. This is known as the San Joaquin Valley being in a rain shadow.'},
{'label': 'Rocky Mountains', 'lon':538, 'lat':956, 'popup':'Moist wind hits the rocky mountains and has to rise. At higher elevations, the air cools and condenses into snow and rain.'},
{'label': 'Western USA', 'lon':481, 'lat':653, 'popup':'This is the rain shadow of the Rocky mountains, which causes this area to be very dry. A rain shadow occurs when winds go over a mountain range, causing the air to release its moisture and become dry. This air then goes over this area, causing there to be very little rain.'},
{'label': 'East Coast', 'lon':1691, 'lat':697, 'popup':'The Atlantic Ocean provides a continuous supply of humid air, leading to rain across the East Coast. Additionally, flat terrain on the East Coast allows moist air to travel far inland.'},
{'label': 'Great Basin', 'lon':881, 'lat':691, 'popup':'A change in elevation here causes the amount of rain to be significantly lower in the Great Basin.'}]




map1 = [
{'popup':'Austin and Houston are the biggest emission spots in Texas. Texas has the 2nd largest population and has a huge industrial district which contribute significantly to greenhouse gas emissions. Also, they lack interest in renewable energy, furthering this issue.', 'lon':1340,'lat': 632,'label':'622.4 MMT (1st)' },
{'popup':'LA and SF are the biggest emission spots in California. California is the most populated state and has a large transportation district which contributes significantly to the emissions. In recent years they have made strides to lower emissions which has made a large dent in emissions, but it still produces massive amounts of greenhouse gases.', 'lon':240, 'lat':1050,'label':'303.7 MMT (2nd)' },
{'popup':'Miami and Orlando are the biggest emission spots in Florida. Florida is one of the most populated states and has a large amount of emissions, mainly due to their plentiful power plants, transportation industry, and significant tourism. In recent years they have made strides to lower emissions, which has made a large dent in emissions, but it still produces massive amounts of greenhouse gases.', 'lon':2300,'lat': 400	, 'label':'207.3 MMT (3rd)' },
{'popup':'Philadelphia is the biggest emission location in Pennsylvania. Pennsylvania has a large amount of emissions, mainly due to their plentiful power plants, transportation industry, and significant tourism. In recent years, they have made strides to lower emissions, which has made a large dent in emissions, but it still produces massive amounts of greenhouse gases.','lon':2366,'lat': 1241	, 'label':'193.4 MMT (4th)' },
{'popup':'Columbus and Cleveland are the biggest emission locations in Ohio. Ohio has a large amount of emissions, mainly due to their emphasis on fracking and overall energy production. In recent years, they have made strides to lower emissions, which has made a large dent in emissions, but it still produces massive amounts of greenhouse gases.', 'lon':2114,'lat': 1179,'label':'185.8 MMT (5th)' },
{'popup':'New Orleans is the biggest emission location in Louisiana. Louisiana has a large amount of emissions, mainly due to their emphasis on fracking and overall energy production. In recent years, they have made strides to lower emissions, which has made a large dent in emissions, but it still produces massive amounts of greenhouse gases.', 'lon':1666,'lat': 635,'label':'183.6 MMT (6th)' },
{'popup':'Chicago is the biggest emission location in Illinois. Illinois has a large amount of emissions, mainly due to their large transportation and mining industries. In recent years, they have made strides to lower emissions, which has made a large dent in emissions, but it still produces massive amounts of greenhouse gases.', 'lon':1800,'lat': 1130,'label':'170.2 MMT (7th)' },
{'popup':'Indianapolis is the biggest emission location in Indiana. Indiana has a large amount of emissions, mainly due to lots of power plants and steelworking facilities. In recent years, they have made strides to lower emissions, which has made a dent in emissions, but it still produces massive amounts of greenhouse gases.', 'lon':1950,'lat': 1125,'label':'154.3 MMT (8th)' },
{'popup':'NYC is the biggest emission location in New York. New York has a large amount of emissions, mainly due to lots of energy production and transportation. In recent years, they have made strides to lower emissions, which has made a dent in emissions, but it still produces massive amounts of greenhouse gases.', 'lon':2450,'lat': 1400,'label':'143.7 MMT (9th)' },
{'popup':'Detroit is the biggest emission location in Michigan. Michigan has a large amount of emissions, mainly because they produce 20% of US cars. In recent years, they have made strides to lower emissions, which has made a dent in emissions, but it still produces massive amounts of greenhouse gases.', 'lon':2000,'lat': 1350,'label':'136.9 MMT (10th)' },
{'label':'The line here is caused by route 66, one of the longest highway in the US.','lon':1020,'lat':780},
{'label':'The line here is caused by route 20, the longest highway in the US.','lon':1333,'lat':1333},
]

map3 = [
{'popup':'This is the Sonoran desert, the hottest area of Arizona. It reached a maximum temperature of 112 degrees fahrenheit.','lon':255,'lat':300},
{'popup':'This cold area is the Rockies, a mountain range with an elevation of 14440 ft that spans nearly 3000 miles. As elevation rises, air molecules spread apart due to decreased atmospheric pressure, leading to a temperature decrease. When there are fewer molecules in a given space, the air is less capable of absorbing and retaining heat, resulting in cooler temperatures experienced at higher elevations.','lon':354,'lat':564},
{'popup':'The Mojave desert, better known as Death Valley, also resides mostly in California, resulting in extremely high temperatures. It once reached a temperature of 134 degrees fahrenheit, being the universally recognized hottest place on Earth.','lon':200,'lat':328},
{'popup':'This is the San Joaquin Valley, which has high temperatures due to its dry climate. This valley borders many mountains, resulting in a blockage of cold air and moisture, causing an even warmer area.','lon':106,'lat':452},
{'popup':'This is the Sierra Nevada mountain range that boasts an elevation of 14505 ft and is 400 miles long. Similar to the Rockies, it has extremely low temperatures due to its low air molecule density and inability to absorb as much heat as other areas.','lon':144,'lat':435},
{'popup':'This is the Cascade mountain range with an elevation of 14411 ft spanning 700 miles. Similar to other mountain ranges, the Cascade mountain range has very low temperatures due to its low air molecule density and inability to absorb as much heat as other areas.','lon':172,'lat':742},
{'popup':'Not only is this coast very close to the equator but it also borders the Gulf of Mexico. Bodies of water have 4 times the maximum heat capacity of land, hence the Gulf of Mexico is very hot, which has gusts blowing that further increase temperatures of land nearby. Thus, this coast is very hot as a result of these two factors.','lon':1007,'lat':135},
{'popup':'This area is closer to the equator than the very cold states, and further than very hot states, resulting in a middling temperature.','lon':778,'lat':421},
{'popup':'This region is very hot due to its dry and hot climate, which is basically a desert.','lon':580,'lat':107},
{'popup':'Due to Canada\'s extremely cold temperature, these states are also very cold. Furthermore, they\'re the furthest states away from the equator in the US.','lon':605,'lat':700},
]



for i in map1:
	i['lon'] /= 1000
	i['lat'] /= 1000

for i in map2:
	i['lon'] /= 1000
	i['lat'] /= 1000

for i in map3:
	i['lon'] /= 1000/2.2
	i['lat'] /= 1000/2.2