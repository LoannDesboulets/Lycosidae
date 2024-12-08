import numpy as np
DEFAULT_VAL = np.nan

class aliment:

    def __init__(self,name) -> None:

        self.name = name
        self.json = {
            "Qte"       : "100g", 
            "Energie" : {
                "kcal" : DEFAULT_VAL,
                "kJ"   : DEFAULT_VAL
            },
            "Nutriments" : {
                "Eau"       : DEFAULT_VAL,
                "Lipides"   : DEFAULT_VAL,
                "Glucides"  : DEFAULT_VAL,
                "Proteines" : DEFAULT_VAL,
                "Fibres"    : DEFAULT_VAL,
            },
            "Glucides" : {
                "Fructose"   : DEFAULT_VAL,
                "Glucose"    : DEFAULT_VAL,
                "Galactose"  : DEFAULT_VAL,
                "Lactose"    : DEFAULT_VAL,
                "Saccharose" : DEFAULT_VAL,
                "Maltose"    : DEFAULT_VAL,
                "Amidon"     : DEFAULT_VAL,
            },
            "Lipides" : {
                "AG satures longs" : {
                    "Laurique"    : DEFAULT_VAL,
                    "Myristique"  : DEFAULT_VAL,
                    "Palmitique"  : DEFAULT_VAL,
                    "Stearique"   : DEFAULT_VAL,
                    "Arachidique" : DEFAULT_VAL,
                },
                "AG satures courts" : {
                    "Acetique"    : DEFAULT_VAL,
                    "Propionique" : DEFAULT_VAL,
                    "Butyrique"   : DEFAULT_VAL,
                },
                "AG mono-insatures" : {
                    "Oleique" : DEFAULT_VAL,
                },
                "AG poly-insatures" : {
                    "Linoleique"        : DEFAULT_VAL,
                    "Alpha-Linoleique"  : DEFAULT_VAL,
                    "Linolenique"       : DEFAULT_VAL,
                    "Arachidonique"     : DEFAULT_VAL,
                    "EPA"               : DEFAULT_VAL,
                    "DHA"               : DEFAULT_VAL,
                },
                "Cholesterol" : DEFAULT_VAL,
            },
            "Vitamines"  : {
                "Beta-Carotene" : DEFAULT_VAL,
                "A"   : DEFAULT_VAL,
                "B1"  : DEFAULT_VAL,
                "B2"  : DEFAULT_VAL,
                "B3"  : DEFAULT_VAL,
                "B5"  : DEFAULT_VAL,
                "B6"  : DEFAULT_VAL,
                "B7"  : DEFAULT_VAL,
                "B9"  : DEFAULT_VAL,
                "B12" : DEFAULT_VAL,
                "C"   : DEFAULT_VAL,
                "D"   : DEFAULT_VAL,
                "E"   : DEFAULT_VAL,
                "K"   : DEFAULT_VAL,
                "Choline" : DEFAULT_VAL,
            },
            "Mineraux" : {
                "Sel"       : DEFAULT_VAL, # Sel = Sodium + Chlore
                "Sodium"    : DEFAULT_VAL,
                "Chlore"    : DEFAULT_VAL,
                "Calcium"   : DEFAULT_VAL,
                "Fer"       : DEFAULT_VAL,
                "Potassium" : DEFAULT_VAL,
                "Manganese" : DEFAULT_VAL,
                "Phosphore" : DEFAULT_VAL,
                "Magnesium" : DEFAULT_VAL,
                "Zinc"      : DEFAULT_VAL,
                "Selenium"  : DEFAULT_VAL,
                "Chrome"    : DEFAULT_VAL,
                "Cuivre"    : DEFAULT_VAL,
                "Fluor"     : DEFAULT_VAL,
                "Iode"      : DEFAULT_VAL,
            }
        }

    # To estimate how many values have been found
    def fillPercentage(self):
        self.missingPct = 0

    # Extract/Set deep nested value using chained key (by dots)
    def deep_get(self, key, default=None, raising=False):
        value = self.json
        try:
            for key in key.split('.'):
                if isinstance(value, dict):
                    value = value[key]
                    continue
                else:
                    if raising:
                        raise KeyError
                    return default
        except KeyError:
            if raising:
                raise
            return default
        else:
            return value
    def deep_set(self, key, value):
        d = self.json
        keys = key.split('.')
        latest = keys.pop()
        for k in keys:
            d = d.setdefault(k, {})
        d[latest] = value