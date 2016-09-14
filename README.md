


#State REST API

This API provides basic infromation for all 50 United States in JSON format. Information includes State Capital, Population, Population Rank, Year State Joined the Union and State Nicknames.

Data source: Wikipedia, September 2016.

As for September 2016, this API is being hosted on [Heroko](https://stateapp.herokuapp.com)

#By State Name
**Description:** You can call with the full state name. Use '%20' for spaces. API will respond with relevant state information.
**Examples:**
http://baseURL.com/Washington
http://baseURL.com/North%20Carolina

#By State Abbreviation
**Description:** You can call using the State's abbreviation. API will respond with relevant state information.
**Examples:**
http://baseURL.com/ND
http://baseURL.com/PA

#Sample Response
```json
[ 
- {
state_name: "North Dakota",
state_abbrev: "ND",
capital: "Bismarck",
population: "756,927 (2015 est)",
population_rank: 47,
joined_union: "November 02, 1889",
nicknames: "Peace Garden State, Roughrider State, Flickertail State"
}
]
```
created by [neil-r.com](www.neil-r.com)