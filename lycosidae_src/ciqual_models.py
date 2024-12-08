class payloadSearch:

    def __init__(self,searchValue) -> None:
        self.json = {
            "from": 0,
            "size": 10000,
            "query": {
                "bool": {
                "must": [
                    {
                    "multi_match": {
                        "query": searchValue,
                        "fields": [
                        "nomIndexFr^2",
                        "nomFr"
                        ]
                    }
                    }
                ],
                "should": [
                    {
                    "prefix": {
                        "nomSortFr": {
                        "value": searchValue,
                        "boost": 2
                        }
                    }
                    }
                ]
                }
            },
            "_source": {
                "excludes": [
                "compos",
                "groupeAfficheEng",
                "nomEng",
                "nomSortEng",
                "nomSortFr",
                "nomIndexFr",
                "nomIndexEng"
                ]
            }
        }

class payloadQuery:

    def __init__(self,queryString) -> None:
        self.json = {
            "from": 0,
            "size": 10000,
            "query": {
                "match_phrase": {
                "code": {
                    "query": queryString
                }
                }
            },
            "sort": "nomSortFr"
        }

def ciqualDico(val):
    dico = {
        # Energie : 2/2
        "Energie, Règlement UE N° 1169/2011 (kcal/100 g)" : "Energie.kcal",
        "Energie, Règlement UE N° 1169/2011 (kJ/100 g)"   : "Energie.kJ",
        # Nutriments : 5/5
        "Protéines, N x 6.25 (g/100 g)" : "Nutriments.Proteines",
        "Glucides (g/100 g)"            : "Nutriments.Glucides",
        "Eau (g/100 g)"                 : "Nutriments.Eau",
        "Fibres alimentaires (g/100 g)" : "Nutriments.Fibres",
        "Lipides (g/100 g)"             : "Nutriments.Lipides",
        # Glucides : 7/7
        "Fructose (g/100 g)"   : "Glucides.Fructose",
        "Galactose (g/100 g)"  : "Glucides.Galactose",
        "Glucose (g/100 g)"    : "Glucides.Glucose",
        "Lactose (g/100 g)"    : "Glucides.Lactose",
        "Maltose (g/100 g)"    : "Glucides.Maltose",
        "Saccharose (g/100 g)" : "Glucides.Saccharose",
        "Amidon (g/100 g)"     : "Glucides.Amidon",
        # Mineraux : 12/15
        "Sel chlorure de sodium (g/100 g)" : "Mineraux.Sel",
        "Sodium (mg/100 g)"                : "Mineraux.Sodium",
        "Magnésium (mg/100 g)"             : "Mineraux.Magnesium",
        "Phosphore (mg/100 g)"             : "Mineraux.Phosphore",
        "Potassium (mg/100 g)"             : "Mineraux.Potassium",
        "Calcium (mg/100 g)"               : "Mineraux.Calcium",
        "Manganèse (mg/100 g)"             : "Mineraux.Manganese",
        "Fer (mg/100 g)"                   : "Mineraux.Fer",
        "Cuivre (mg/100 g)"                : "Mineraux.Cuivre",
        "Zinc (mg/100 g)"                  : "Mineraux.Zinc",
        "Sélénium (µg/100 g)"              : "Mineraux.Selenium",
        "Iode (µg/100 g)"                  : "Mineraux.Iode",
        # Lipides : 11/16
        "Cholestérol (mg/100 g)"                                : "Lipides.Cholesterol",
        "AG 4:0, butyrique (g/100 g)"                           : "Lipides.AG satures courts.Butyrique",
        # "AG 6:0, caproïque (g/100 g)"                           : "Lipides.",
        # "AG 8:0, caprylique (g/100 g)"                          : "Lipides.",
        # "AG 10:0, caprique (g/100 g)"                           : "Lipides.",
        "AG 12:0, laurique (g/100 g)"                           : "Lipides.AG satures longs.Laurique",
        "AG 14:0, myristique (g/100 g)"                         : "Lipides.AG satures longs.Myristique",
        "AG 16:0, palmitique (g/100 g)"                         : "Lipides.AG satures longs.Palmitique",
        "AG 18:0, stéarique (g/100 g)"                          : "Lipides.AG satures longs.Stearique",
        "AG 18:1 9c (n-9), oléique (g/100 g)"                   : "Lipides.AG mono-insatures.Oleique",
        "AG 18:2 9c,12c (n-6), linoléique (g/100 g)"            : "Lipides.AG poly-insatures.Linoleique",
        "AG 18:3 c9,c12,c15 (n-3), alpha-linolénique (g/100 g)" : "Lipides.AG poly-insatures.Alpha-Linoleique",
        "AG 20:5 5c,8c,11c,14c,17c (n-3) EPA (g/100 g)"         : "Lipides.AG poly-insatures.EPA",
        "AG 22:6 4c,7c,10c,13c,16c,19c (n-3) DHA (g/100 g)"     : "Lipides.AG poly-insatures.DHA",
        # Vitamines : 14/15
        "Beta-Carotène (µg/100 g)"                      : "Vitamines.Beta-Carotene",
        "Vitamine A (µg/100 g)"                         : "Vitamines.A",
        "Vitamine B1 ou Thiamine (mg/100 g)"            : "Vitamines.B1",
        "Vitamine B2 ou Riboflavine (mg/100 g)"         : "Vitamines.B2",
        "Vitamine B3 ou PP ou Niacine (mg/100 g)"       : "Vitamines.B3",
        "Vitamine B5 ou Acide pantothénique (mg/100 g)" : "Vitamines.B5",
        "Vitamine B6 (mg/100 g)"                        : "Vitamines.B6",
        "Vitamine B7 (mg/100 g)"                        : "Vitamines.B7", # to be checked
        "Vitamine B9 ou Folates totaux (µg/100 g)"      : "Vitamines.B9",
        "Vitamine B12 (µg/100 g)"                       : "Vitamines.B12",
        "Vitamine C (mg/100 g)"                         : "Vitamines.C",
        "Vitamine D (µg/100 g)"                         : "Vitamines.D",
        "Vitamine E (mg/100 g)"                         : "Vitamines.E",
        "Vitamine K1 (µg/100 g)"                        : "Vitamines.K",
        # "Alcool (g/100 g)" : "",
        # "Rétinol (µg/100 g)" : "",
        # "Polyols totaux (g/100 g)" : "",
    }
    if val in dico.keys():
        return dico[val]
    else :
        return ""
    
## Generated list by ChatGPT 4o mini

fruits = [
    "Pomme", "Banane", "Orange", "Poire", "Fraise", "Cerise", "Kiwi", "Mango", "Melon", "Pastèque",
    "Peach", "Prune", "Raisin", "Abricot", "Ananas", "Pêche", "Cassis", "Framboise", "Myrtille", "Grenade",
    "Litchi", "Mandarine", "Clémentine", "Citron", "Citron vert", "Coing", "Rhubarbe", "Tamarillo", "Figue",
    "Pamplemousse", "Lime", "Pomélo", "Grenadille", "Jujube", "Baies de goji", "Myrte", "Durian", "Carambole",
    "Papaye", "Noix de coco", "Mamey", "Açaí", "Maracuja", "Fruits de la passion", "Pitaya", "Nectarine", 
    "Coco", "Fruit de la passion", "Sureau", "Goyave", "Limequat", "Mandarine verte", "Pistache", "Alpini",
    "Kaki", "Pawpaw", "Pomelo", "Quince", "Tangerine", "Mamey", "Salak", "Bergamot", "Jambolan", "Caryota",
    "Cherimoya", "Date", "Pruneau", "Dattier", "Myrtille", "Mulberry", "Gooseberry", "Lingonberry", "Starfruit",
    "Lingon", "Baies d'argousier", "Nashi", "Hibiscus", "Mulberry", "Pomelo rose", "Ambarella", "Baie d'açaï", 
    "Cajou", "Coconut water", "Feijoa", "Longan", "Salacca", "Pummelo", "Tamarind", "Goji", "Sweet lemon",
    "Lychee", "Mango", "Custard apple", "Fruits of the forest", "Indian fig", "White grape", "Sweet orange", 
    "Raspberry", "Pink grapefruit", "Raisin sec", "Lemonade", "Orange sanguine", "Apple", "Apple green", "Dragon fruit",
    "Cherries", "Fruits rouges", "Aronia", "Cranberry", "Clementine", "Cassis", "Boysenberry", "Persimmon", "Soursop"
]

legumes = [
    "Carotte", "Pomme de terre", "Tomate", "Courgette", "Poivron", "Aubergine", "Chou", "Chou-fleur", "Brocoli",
    "Épinard", "Laitue", "Romaine", "Chicorée", "Endive", "Cresson", "Oignon", "Ail", "Navet", "Radis", "Panais",
    "Poireau", "Fenouil", "Artichaut", "Asperge", "Haricot vert", "Petits pois", "Maïs", "Chou de Bruxelles", 
    "Céleri", "Céleri-rave", "Betterave", "Rutabaga", "Mâche", "Rochers de courge", "Topinambour", "Blette", 
    "Cresson de fontaine", "Coriandre", "Persil", "Basilic", "Romarin", "Thym", "Moutarde", "Taro", "Bambou", 
    "Courge", "Potiron", "Butternut", "Cucamelon", "Chou kale", "Chou chinois", "Mâche", "Gingembre", "Piment", 
    "Poivron doux", "Poivron rouge", "Poivron vert", "Piment d'Espelette", "Radis noir", "Radis rose", "Fève", 
    "Légumes racines", "Légumes de saison", "Violet artichaut", "Haricot beurre", "Tigernut", "Feuilles de moutarde", 
    "Cacahuète", "Bambou", "Salsifis", "Échalote", "Okra", "Ail des ours", "Câprons", "Gombos", "Racine de lotus", 
    "Courge spaghetti", "Chou vert", "Gingembre frais", "Fleur de courgette", "Brouet de céleri", "Menthe", "Marjolaine", 
    "Navet violet", "Pommes de terre nouvelles", "Potimarron", "Pois mange-tout", "Pomme de terre vitelotte", 
    "Kale", "Chou frisé", "Tomate cerise", "Légumes d'hiver", "Graines de courge", "Jalapenos", "Boursin", "Chou-rave",
    "Chou de Milan", "Céleri en branches", "Pois cassés", "Pois chiches", "Haricot tarbais", "Haricot coco", "Taro", 
    "Légumineuses", "Pois verts", "Patate douce", "Chou de Bruxelles rose", "Chou cabus", "Gombo", "Laitue frisée", 
    "Chou pointu", "Oignon nouveau", "Pomme de terre violette", "Fennel", "Pamplemousse rose", "Oignon doux", 
    "Ail noir", "Fleur de sel", "Mimolette", "Chou blanc", "Chou frisé noir", "Chou rouge", "Pommier de terre", 
    "Ginger root", "Cresson alénois", "Herbes de Provence", "Herbes fraîches", "Racine de gingembre", "Navet blanc", 
    "Chou vert frisé", "Tomate noire", "Piquillos", "Betterave jaune", "Pâtisson", "Taro blanc", "Poivron jaune", 
    "Légumes du jardin", "Chou chinois pékinois", "Chou marbré", "Hibiscus", "Chou brocoli", "Petits pois mange-tout", 
    "Aubergine longue", "Chou de Savoie", "Crosne", "Chou en tranches", "Patate douce violette", "Carotte jaune", 
    "Échalote rose", "Endive rouge", "Chou de Lombardie", "Mélange de légumes méditerranéens", "Poireau sauvage", 
    "Mélange de racines", "Cèleri branche", "Graines de chia", "Gombos africains", "Racine de céleri", "Pois d'angole"
]

viandes = [
    "Bœuf", "Porc", "Agneau", "Veau", "Mouton", "Chevreuil", "Sanglier", "Poulet", "Canard", "Dinde",
    "Oie", "Pigeon", "Caille", "Perdreau", "Lapin", "Bison", "Buffle", "Kangourou", "Crocodile", "Autruche",
    "Pélican", "Morse", "Phoque", "Cobaye", "Chèvre", "Alpaga", "Cheval", "Chameau", "Élan", "Biche",
    "Cerf", "Marmotte", "Lamproie", "Escargot", "Crabe", "Homard", "Crevette", "Huître", "Moules", "Coquilles Saint-Jacques",
    "Sardine", "Thon", "Morue", "Saumon", "Truite", "Anguille", "Calmar", "Pieuvre", "Anchois", "Turbot",
    "Saucisson", "Jambon", "Bacon", "Pâté", "Rillettes", "Chorizo", "Salami", "Boudin", "Saucisse", "Tartare",
    "Pastrami", "Prosciutto", "Mortadelle", "Capocollo", "Filet mignon", "Lièvre", "Poule faisane", "Bison", "Ragondin",
    "Ibis", "Tinamou", "Écureuil", "Ours", "Sanglier", "Faisan", "Pintade", "Caille", "Agneau de lait", "Cochon de lait",
    "Coq", "Canard colvert", "Dindon sauvage", "Perdrix", "Lièvre de garenne", "Biche de bois", "Grive", "Pigeon ramier",
    "Grive musicienne", "Oie sauvage", "Caille des blés", "Canard de barbarie", "Chèvre sauvage", "Veau de lait", "Sanglier sauvage",
    "Porc fermier", "Agneau du pré", "Poitrine de bœuf", "Ribs de porc", "Jarret de veau", "Côte de bœuf", "Entrecôte", "Bifteck",
    "Côtelette d'agneau", "Saucisse de Toulouse", "Pâté de campagne", "Saucisse de Morteau", "Merguez", "Boudin blanc", "Jambon de Bayonne",
    "Jambon cru", "Jambon cuit", "Bacon fumé", "Lardons", "Foie gras", "Langue de bœuf", "Ragoût de mouton", "Cervelle de veau",
    "Cervelle d'agneau", "Ragoût de sanglier", "Tartare de bœuf", "Tartare de saumon", "Steak de thon", "Côtelettes de porc", "Chili con carne",
    "Choucroute garnie", "Boeuf bourguignon", "Pot-au-feu", "Sauté de veau", "Blanquette de veau", "Côtes de porc grillées", "Canard aux cerises",
    "Moules marinières", "Escargots de Bourgogne", "Bœuf Stroganoff", "Côtelettes d'agneau au romarin", "Pâté en croûte", "Sole meunière",
    "Carpaccio", "Brochettes de poulet", "Côte de veau", "Tartare de porc", "Saucisse de porc", "Magret de canard", "Steak haché",
    "Tournedos", "Filet de porc", "Rôti de bœuf", "Rôti de porc", "Rôti de veau", "Rôti de lamb", "Ragoût de bœuf", "Paupiette de veau",
    "Saucisses de Toulouse", "Saucisses de Francfort", "Boudin noir", "Poitrine de porc", "Cuisses de grenouilles", "Pâté de foie",
    "Rillettes de canard", "Choucroute de poisson", "Tartare de veau", "Boeuf Wellington", "Quenelles de brochet", "Canard aux oranges",
    "Poisson d'eau douce", "Poisson du marché", "Pâté en croûte de gibier", "Porc au caramel", "Agneau au romarin", "Bœuf au poivre",
    "Magret de canard rôti", "Chapon", "Poularde", "Pâté de gibier", "Saucisse de veau", "Poulet rôti", "Veau aux morilles",
    "Côte de porc farcie", "Lapin à la moutarde", "Brochette de bœuf", "Saucisses de Strasbourg", "Saucisses de Montbéliard", "Lamb shank",
    "Ragout de lapin", "Boeuf en daube", "Cuisses de canard confites", "Côte de veau aux herbes", "Côte de porc grillée", "Foie de veau",
    "Jambon cru de Parme", "Lamb chops", "Pâté de lièvre", "Viande de cheval", "Mousseline de canard", "Côte de bœuf grillée",
    "Cotelette d'agneau grillée", "Poule au pot", "Côte de canard", "Filet de canard", "Canard au foie gras", "Côte de porc en sauce",
    "Steak de porc", "Filet mignon de bœuf", "Steak de kangourou", "Brochettes de porc", "Casserole de lapin", "Côtelette de veau",
    "Blanquette de bœuf", "Poule faisane aux morilles", "Magret de canard grillé", "Tournedos de bœuf", "Brochette de dinde",
    "Bœuf aux légumes", "Lapin aux pruneaux", "Pâté de canard", "Steak de veau", "Rôti de dinde", "Côte de bœuf de Salers"
]

huiles = [
    "Huile d'olive", "Huile de tournesol", "Huile de colza", "Huile de noix", "Huile de sésame", "Huile de lin",
    "Huile de coco", "Huile d'arachide", "Huile de pépins de raisin", "Huile de moutarde", "Huile de palme",
    "Huile d'avocat", "Huile de canola", "Huile de noisette", "Huile de soja", "Huile de chia", "Huile de ricin",
    "Huile de cameline", "Huile de jojoba", "Huile de bourrache", "Huile de nigelle", "Huile de tamanu", 
    "Huile d'amande douce", "Huile de chanvre", "Huile de carthame", "Huile de pépins de courge", "Huile de macadamia", 
    "Huile d'argan", "Huile de pépins de grenade", "Huile de moringa", "Huile d'olive vierge", "Huile de coco vierge", 
    "Huile d'olive extra vierge", "Huile d'argan biologique", "Huile essentielle de lavande", "Huile essentielle de menthe", 
    "Huile essentielle de rose", "Huile essentielle de tea tree", "Huile d'olive pure", "Huile d'olive bio", 
    "Huile de ricin pour cheveux", "Huile de pépins de raisin pour cuisson", "Huile de tournesol haute en oléique", 
    "Huile de noix de macadamia", "Huile de noix de coco vierge extra", "Huile de pépins de figue de barbarie",
    "Huile de pépins de framboise", "Huile de caméline bio", "Huile de sacha inchi", "Huile de safran", 
    "Huile de grenade", "Huile de marula", "Huile de baobab", "Huile de cacahuète", "Huile d'argan cosmétique", 
    "Huile de neem", "Huile d'olive au basilic", "Huile de truffe", "Huile de gingembre", "Huile de carotte", 
    "Huile d'avocat bio", "Huile de lin bio", "Huile de soja bio", "Huile de colza bio", "Huile d'amande douce bio",
    "Huile de romarin", "Huile d'olive infusée", "Huile d'olive aromatisée", "Huile d'olive pour cuisine méditerranéenne"
]

laitages = [
    "Lait", "Lait entier", "Lait demi-écrémé", "Lait écrémé", "Lait de vache", "Lait de chèvre", "Lait de brebis",
    "Lait d'amande", "Lait de soja", "Lait de riz", "Yaourt", "Yaourt nature", "Yaourt à la vanille", "Yaourt à la fraise",
    "Yaourt grec", "Yaourt au miel", "Yaourt aux fruits", "Fromage", "Fromage frais", "Fromage à pâte dure", 
    "Fromage à pâte molle", "Fromage bleu", "Roquefort", "Camembert", "Brie", "Chèvre frais", "Feta", "Comté", 
    "Emmental", "Gruyère", "Cantal", "Reblochon", "Saint-Nectaire", "Munster", "Boursin", "Chèvre sec", 
    "Parmesan", "Gorgonzola", "Cottage cheese", "Ricotta", "Mascarpone", "Quark", "Fromage blanc", "Crème", 
    "Crème fraîche", "Crème épaisse", "Crème légère", "Crème fouettée", "Beurre", "Beurre doux", "Beurre salé", 
    "Beurre clarifié", "Fromage râpé", "Fromage à pâte pressée", "Kéfir", "Lait ribot", "Lait concentré", 
    "Lait condensé sucré", "Lait en poudre", "Yaourt brassé", "Yaourt à boire", "Fromage de chèvre affiné", 
    "Fromage affiné", "Fromage de brebis", "Crème de lait", "Fromage blanc entier", "Lait d'avoine", "Lait de coco"
]

graisses = [
    "Beurre", "Beurre doux", "Beurre salé", "Beurre clarifié", "Margarine", "Saindoux", "Graisse de canard", 
    "Graisse de porc", "Lard", "Lardons", "Crème", "Crème fraîche", "Crème épaisse", "Crème légère", 
    "Crème fouettée", "Ghee", "Beurre de cacahuète", "Beurre d'amande", "Beurre de noisette", "Suet", 
    "Graines de chia", "Pistaches", "Amandes", "Noix de macadamia", "Noix de pécan", "Noix de cajou", 
    "Graines de tournesol", "Graines de courge", "Noix", "Tahin", "Beurre de karité", "Graisse d'oie"
]

noix = [
    "Amandes", "Noix", "Noix de cajou", "Noix de macadamia", "Noix de pécan", "Noix du Brésil", 
    "Noisettes", "Pistaches", "Cacahuètes", "Arachides", "Noix de pin", "Noix de coco", "Noix de Grenoble",
    "Graines de tournesol", "Graines de courge", "Châtaignes", "Pignons de pin", "Marrons", "Pistaches de Californie", 
    "Amandes de mer", "Fruits à coque", "Cacahuètes salées", "Amandes effilées", "Amandes entières", 
    "Noix de cajou grillées", "Noix de macadamia non salées", "Noix de pécan torréfiées"
]

boissons = [
    "Eau", "Eau plate", "Eau gazeuse", "Eau minérale", "Eau pétillante", "Soda", "Limonade", "Jus de fruit", 
    "Jus d'orange", "Jus de pomme", "Jus de raisin", "Jus de citron", "Jus de pamplemousse", "Thé", 
    "Thé vert", "Thé noir", "Thé blanc", "Infusion", "Café", "Café noir", "Café au lait", "Café glacé", 
    "Chocolat chaud", "Lait de soja", "Lait d'amande", "Lait de coco", "Lait d'avoine", "Boisson énergisante", 
    "Boisson gazeuse", "Eau de coco", "Bière", "Vin", "Vin rouge", "Vin blanc", "Vin rosé", "Champagne", 
    "Cidre", "Cocktail", "Rhum", "Vodka", "Tequila", "Whisky", "Liqueur", "Martini", "Cognac", "Gin", 
    "Mojito", "Margarita", "Piña Colada", "Baileys", "Alcool fort", "Alcool léger"
]

fruitsdemer = [
    "Poisson", "Saumon", "Truite", "Maquereau", "Thon", "Sardines", "Morue", "Colin", "Merlan", "Lieu", 
    "Flétan", "Sole", "Rascasse", "Perche", "Dorade", "Bar", "Anguille", "Haddock", "Crevettes", "Crevettes grises", 
    "Crevettes roses", "Homard", "Crabe", "Langouste", "Moules", "Huîtres", "Palourdes", "Coquilles Saint-Jacques", 
    "Calamars", "Seiches", "Encornets", "Poulpe", "Anchois", "Lotte", "Vivier", "Anguille de mer", "Raie", 
    "Aiglefin", "Nébulet", "Hareng", "Sole noire", "Moules de bouchot", "Caviar", "Oursins", "Pétoncles", 
    "Crapaudine", "Langoustines"
]

processed_food = [
    "Frites surgelées", "Pizza surgelée", "Lasagnes prêtes à cuire", "Soupes en conserve", "Plats cuisinés", 
    "Repas prêt-à-manger", "Noodles instantanés", "Riz précuit", "Pâtes prêtes à cuire", "Céréales du petit-déjeuner", 
    "Barres de chocolat", "Bonbons", "Biscuits", "Gâteaux industriels", "Chips", "Popcorn", "Cacahuètes salées", 
    "Charcuterie", "Jambon cuit", "Saucisson", "Saucisses", "Rillettes", "Pâté", "Fromage fondu", "Fromage râpé", 
    "Fromage à tartiner", "Ketchup", "Mayonnaise", "Sauces toutes prêtes", "Conserves de légumes", "Conserves de fruits", 
    "Jus de fruits concentré", "Compote de pommes", "Pâtisseries industrielles", "Crêpes prêtes", "Tartes prêtes à cuire", 
    "Pouding au chocolat", "Mousse au chocolat", "Yaourt sucré", "Crème dessert", "Glaces industrielles", 
    "Boissons sucrées", "Soda", "Eau aromatisée", "Boissons énergétiques", "Boissons lactées", "Boissons gazeuses", 
    "Café soluble", "Soupes déshydratées", "Céréales prêtes à l'emploi", "Repas congelés", "Ragoûts en boîte", 
    "Aliments en conserve", "Margarine", "Viande en conserve", "Pâtisseries surgelées", "Tacos préparés", "Repas rapide", 
    "Poisson pané", "Poulet pané", "Repas surgelés", "Gratin dauphinois surgelé", "Chili con carne prêt", "Poulet rôti prêt", 
    "Burgers surgelés", "Pain de mie", "Pain de campagne précuit", "Tartes aux fruits surgelées", "Riz sauté en boîte", 
    "Choucroute en conserve", "Boeuf haché surgelé", "Fricassée de volaille surgelée", "Bâtonnets de poisson", 
    "Raviolis en conserve", "Moussaka surgelée", "Aliments végétariens transformés", "Simili-carnés", "Cakes industriels", 
    "Crêpes à emporter", "Chocolat au lait industriel", "Pâtes à tartiner chocolatées", "Poudres pour boissons", 
    "Glaces à l'eau", "Bâtonnets glacés", "Popsicles", "Fruits au sirop", "Légumes à la sauce", "Tartinades", 
    "Plats en sauce préemballés", "Sushis industriels", "Viande séchée", "Steak haché surgelé", "Bouchées à la reine", 
    "Pâtés en croûte", "Clafoutis prêt à cuire", "Crèmes brûlées en pot", "Bouchées apéritives surgelées", 
    "Riz au lait en boîte", "Biscuit de Noël", "Mini-quiches", "Côtelettes d'agneau panées", "Macarons industriels", 
    "Crumble aux pommes prêt", "Tartelette au chocolat prête", "Cakes au yaourt", "Salades en sachet", "Purée en flocons", 
    "Sauces béchamel", "Tiramisu en pot", "Purée de pommes de terre en conserve", "Spaghetti sauce tomate", 
    "Légumes en conserve avec sauce", "Chili en conserve", "Tomates pelées en conserve", "Steak de soja", 
    "Burgers végétariens surgelés", "Pois cassés en conserve", "Viande en conserve à réchauffer", "Soupe en brique", 
    "Paëlla surgelée", "Pommes de terre dauphine surgelées", "Chocolat de cuisson", "Petits pois surgelés", 
    "Repas de fête surgelés", "Frikadelles en conserve", "Steaks végétariens", "Pâtes à pizza", "Pâtes prêtes à cuisiner", 
    "Haricots verts surgelés", "Fruits de mer en conserve", "Légumes mélangés surgelés", "Boeuf bourguignon prêt", 
    "Tartes salées congelées", "Couscous en conserve", "Boulettes de viande congelées", "Pâté de foie en conserve", 
    "Poêlée de légumes", "Légumes rôtis surgelés", "Frites fraîches surgelées", "Curry en conserve", "Soupe miso déshydratée", 
    "Burgers de légumes", "Gâteau au chocolat prêt", "Tartes aux légumes surgelées", "Fruits secs sucrés", "Bretzels", 
    "Soupes instantanées", "Compote industrielle", "Salades composées emballées", "Salades en boîte", "Légumes à la vapeur en conserve"
]
