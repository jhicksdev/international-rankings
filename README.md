# International Rankings

_International Rankings_ is a JSON dataset containing records from various international rankings.

The dataset contains records from the following reports and indexes.

| Title                                                | Version | Source                                                                                                                                    |
| ---------------------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Corruption Perceptions Index                         | 2022    | [Transparency International](https://www.transparency.org/en/cpi/2022)                                                                    |
| Criminality Index                                    | 2021    | [Global Organized Crime Index](https://ocindex.net/)                                                                                      |
| Democracy Index                                      | 2022    | [Economist Intelligence Unit](https://www.eiu.com/n/campaigns/democracy-index-2022/)                                                      |
| Environmental Performance Index                      | 2022    | [Yale University](https://epi.yale.edu/)                                                                                                  |
| Fragile States Index                                 | 2022    | [Fragile States Index](https://fragilestatesindex.org/)                                                                                   |
| Gay Travel Index                                     | 2023    | [GayGuide UG](https://spartacus.gayguide.travel/blog/spartacus-gay-travel-index/)                                                         |
| Gender Inequality Index                              | 2021    | [United Nations Development Programme](https://hdr.undp.org/data-center/thematic-composite-indices/gender-inequality-index#/indicies/GII) |
| Global Acceptance Index                              | 2020    | [The Williams Institute](https://williamsinstitute.law.ucla.edu/projects/gai/)                                                            |
| Global Peace Index                                   | 2022    | [Vision of Humanity](https://www.visionofhumanity.org/maps/#/)                                                                            |
| Global Terrorism Index                               | 2021    | [Vision of Humanity](https://www.visionofhumanity.org/maps/global-terrorism-index/#/)                                                     |
| Good Country Index                                   | 1.5     | [The Good Country](https://index.goodcountry.org/)                                                                                        |
| Happy Planet Index                                   | 2019    | [Happy Planet Index](https://happyplanetindex.org/hpi/)                                                                                   |
| Human Development Index                              | 2021    | [United Nations Development Programme](https://hdr.undp.org/data-center/human-development-index#/indicies/HDI)                            |
| Inequality-adjusted Human Development Index          | 2021    | [United Nations Development Programme](https://hdr.undp.org/inequality-adjusted-human-development-index#/indicies/IHDI)                   |
| Legatum Prosperity Index                             | 2023    | [Prosperity](https://www.prosperity.com/)                                                                                                 |
| Planetary Pressures-adjusted Human Development Index | 2021    | [United Nations Development Programme](https://hdr.undp.org/planetary-pressures-adjusted-human-development-index#/indicies/PHDI)          |
| Positive Peace Index                                 | 2020    | [Vision of Humanity](https://www.visionofhumanity.org/maps/positive-peace-index/#/)                                                       |
| Resilience Index                                     | 2021    | [Global Organized Crime Index](https://ocindex.net/)                                                                                      |
| Social Progress Index                                | 2022    | [Social Progress Imperative](https://www.socialprogress.org/)                                                                             |
| World Happiness Report                               | 2023    | [World Happiness Report](https://worldhappiness.report/)                                                                                  |
| WorldRiskIndex                                       | 2022    | [WeltRisikoBericht](https://weltrisikobericht.de/weltrisikobericht-2022-e/)                                                               |

Fetch the dataset using the JavaScript Fetch API:

```javascript
const response = await fetch(
  "https://raw.githubusercontent.com/jhicksdev/international-rankings/main/rankings.min.json"
);
const rankings = await response.json();
console.log(rankings);
```

Example output:

```jsonc
{
  "version": "2023.5.3",
  "rankings": [
    {
      "title": "Human Development Index",
      "version": 2021,
      "records": [
        {
          "country": "Switzerland",
          "rank": 1,
          "score": 0.962
        }
      ]
    }
  ]
}

```
