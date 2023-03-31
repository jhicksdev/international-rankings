# International Rankings DB

_International Rankings DB_ is an SQLite database containing values from various international rankings.

The database contains values from the following reports and indexes.

| Title                                                | Version | Source                                                                                                                                    |
| ---------------------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Corruption Perceptions Index                         | 2022    | [Transparency International](https://www.transparency.org/en/cpi/2022)                                                                    |
| Democracy Index                                      | 2022    | [Economist Intelligence Unit](https://www.eiu.com/n/campaigns/democracy-index-2022/)                                                      |
| Environmental Performance Index                      | 2022    | [Yale University](https://epi.yale.edu/)                                                                                                  |
| Fragile States Index                                 | 2022    | [Fragile States Index](https://fragilestatesindex.org/)                                                                                   |
| Gay Travel Index                                     | 2023    | [GayGuide UG](https://spartacus.gayguide.travel/blog/spartacus-gay-travel-index/)                                                         |
| Gender Inequality Index                              | 2021    | [United Nations Development Programme](https://hdr.undp.org/data-center/thematic-composite-indices/gender-inequality-index#/indicies/GII) |
| Global Acceptance Index                              | 2020    | [The Williams Institute](https://williamsinstitute.law.ucla.edu/projects/gai/)                                                            |
| Global Organized Crime Index                         | 2021    | [The Organized Crime Index](https://ocindex.net/)                                                                                         |
| Global Peace Index                                   | 2022    | [Vision of Humanity](https://www.visionofhumanity.org/maps/#/)                                                                            |
| Global Terrorism Index                               | 2021    | [Vision of Humanity](https://www.visionofhumanity.org/maps/global-terrorism-index/#/)                                                     |
| Good Country Index                                   | 1.5     | [The Good Country](https://index.goodcountry.org/)                                                                                        |
| Happy Planet Index                                   | 2019    | [Happy Planet Index](https://happyplanetindex.org/hpi/)                                                                                   |
| Human Development Index                              | 2021    | [United Nations Development Programme](https://hdr.undp.org/data-center/human-development-index#/indicies/HDI)                            |
| Inequality-adjusted Human Development Index          | 2021    | [United Nations Development Programme](https://hdr.undp.org/inequality-adjusted-human-development-index#/indicies/IHDI)                   |
| Legatum Prosperity Index                             | 2023    | [Prosperity](https://www.prosperity.com/)                                                                                                 |
| Planetary Pressures-adjusted Human Development Index | 2021    | [United Nations Development Programme](https://hdr.undp.org/planetary-pressures-adjusted-human-development-index#/indicies/PHDI)          |
| Positive Peace Index                                 | 2020    | [Vision of Humanity](https://www.visionofhumanity.org/maps/positive-peace-index/#/)                                                       |
| Social Progress Index                                | 2022    | [Social Progress Imperative](https://www.socialprogress.org/)                                                                             |
| World Happiness Report                               | 2023    | [World Happiness Report](https://worldhappiness.report/)                                                                                  |
| WorldRiskIndex                                       | 2022    | [WeltRisikoBericht](https://weltrisikobericht.de/weltrisikobericht-2022-e/)                                                               |

Select the _INTERNATIONAL_RANKINGS_ table using the `sqlite3` command:

```bash
sqlite3 ./main.db 'SELECT * FROM INTERNATIONAL_RANKINGS'
```

Generate a JSON file containing the table records using this command:

```bash
python3 ./to_json.py
```

Fetch the JSON data using the JavaScript Fetch API:

```javascript
fetch("./records.json")
  .then((response) => response.json())
  .then((records) => console.log(records));
```

Example output:

```jsonc
[
  // ...,
  {
    "title": "Human Development Index",
    "version": "2021",
    "country_name": "Switzerland",
    "rank": 1,
    "score": 0.962
  }
  // ...
]
```
