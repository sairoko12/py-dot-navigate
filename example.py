# -*- coding: utf-8 -*-


from dot_navigate import DotNavigate

# This data is dummy, not real values :)
complex_dictionary = {
    'planets': [
        {
            'earth': {
                'countries': {
                    'MX': {
                        'states': {
                            'cdmx': {
                                'total_population': 99999,
                                'coordinates': ['19.4978', '-99.1269', {
                                    'meta': False
                                }]
                            },
                            'toluca': {
                                'total_population': 38432,
                                'coordinates': ['12.123', '-99.123', {
                                    'meta': False
                                }]
                            },
                            'veracruz': {
                                'total_population': 343213,
                                'coordinates': ['12.123', '-99.123', {
                                    'meta': True
                                }]
                            }
                        }
                    },
                    'USA': {
                        'states': {
                            'texas': {
                                'total_population': 34323,
                                'coordinates': ['12.143', '-78.433', {
                                    'meta': False
                                }]
                            },
                            'california': {
                                'total_population': 342234,
                                'coordinates': ['43.9383', '-57.433', {
                                    'meta': True
                                }]
                            },
                            'arizona': {
                                'total_population': 23422,
                                'coordinates': ['93.123', '-57.29', {
                                    'meta': True
                                }]
                            }
                        }
                    }
                }
            }
        },
        {
            'mars': {
                'countries': "Not yet xD"
            }
        },
        {
            'saturn': {
                'countries': "Not yet xD"
            }
        }
    ],
    'constellations': {
        'andromeda': {
            'position': "missing data"
        },
        'aquarius': {
            'position': "missing data"
        }
    }
}

navigation = DotNavigate(complex_dictionary)
default_value = "Value not found :'("

california_total_popupalation = navigation.get('planets.0.earth.countries.USA.states.california.total_population', default_value)
print(california_total_popupalation)

toluca_meta = navigation.get('planets.0.earth.countries.MX.states.toluca.coordinates.2.meta', default_value)
print(toluca_meta)

arizona_latitude = navigation.get('planets.0.earth.countries.USA.states.arizona.coordinates.0', default_value)
print(arizona_latitude)

aquarius_info = navigation.get('constellations.aquarius', default_value)
print(aquarius_info)

saturn_countries = navigation.get('planets.2.saturn.countries', default_value)
print(saturn_countries)

value_not_found = navigation.get('missing.key', default_value)
print(value_not_found)
