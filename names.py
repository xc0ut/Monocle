# -*- coding: utf-8 -*-
import config

EN_NAMES = {
    1: 'Bulbasaur', 2: 'Ivysaur', 3: 'Venusaur', 4: 'Charmander',
    5: 'Charmeleon', 6: 'Charizard', 7: 'Squirtle', 8: 'Wartortle',
    9: 'Blastoise', 10: 'Caterpie', 11: 'Metapod', 12: 'Butterfree',
    13: 'Weedle', 14: 'Kakuna', 15: 'Beedrill', 16: 'Pidgey',
    17: 'Pidgeotto', 18: 'Pidgeot', 19: 'Rattata', 20: 'Raticate',
    21: 'Spearow', 22: 'Fearow', 23: 'Ekans', 24: 'Arbok',
    25: 'Pikachu', 26: 'Raichu', 27: 'Sandshrew', 28: 'Sandslash',
    29: 'Nidoran♀', 30: 'Nidorina', 31: 'Nidoqueen', 32: 'Nidoran♂',
    33: 'Nidorino', 34: 'Nidoking', 35: 'Clefairy', 36: 'Clefable',
    37: 'Vulpix', 38: 'Ninetales', 39: 'Jigglypuff', 40: 'Wigglytuff',
    41: 'Zubat', 42: 'Golbat', 43: 'Oddish', 44: 'Gloom',
    45: 'Vileplume', 46: 'Paras', 47: 'Parasect', 48: 'Venonat',
    49: 'Venomoth', 50: 'Diglett', 51: 'Dugtrio', 52: 'Meowth',
    53: 'Persian', 54: 'Psyduck', 55: 'Golduck', 56: 'Mankey',
    57: 'Primeape', 58: 'Growlithe', 59: 'Arcanine', 60: 'Poliwag',
    61: 'Poliwhirl', 62: 'Poliwrath', 63: 'Abra', 64: 'Kadabra',
    65: 'Alakazam', 66: 'Machop', 67: 'Machoke', 68: 'Machamp',
    69: 'Bellsprout', 70: 'Weepinbell', 71: 'Victreebel', 72: 'Tentacool',
    73: 'Tentacruel', 74: 'Geodude', 75: 'Graveler', 76: 'Golem',
    77: 'Ponyta', 78: 'Rapidash', 79: 'Slowpoke', 80: 'Slowbro',
    81: 'Magnemite', 82: 'Magneton', 83: 'Farfetch\'d', 84: 'Doduo',
    85: 'Dodrio', 86: 'Seel', 87: 'Dewgong', 88: 'Grimer',
    89: 'Muk', 90: 'Shellder', 91: 'Cloyster', 92: 'Gastly',
    93: 'Haunter', 94: 'Gengar', 95: 'Onix', 96: 'Drowzee',
    97: 'Hypno', 98: 'Krabby', 99: 'Kingler', 100: 'Voltorb',
    101: 'Electrode', 102: 'Exeggcute', 103: 'Exeggutor', 104: 'Cubone',
    105: 'Marowak', 106: 'Hitmonlee', 107: 'Hitmonchan', 108: 'Lickitung',
    109: 'Koffing', 110: 'Weezing', 111: 'Rhyhorn', 112: 'Rhydon',
    113: 'Chansey', 114: 'Tangela', 115: 'Kangaskhan', 116: 'Horsea',
    117: 'Seadra', 118: 'Goldeen', 119: 'Seaking', 120: 'Staryu',
    121: 'Starmie', 122: 'Mr. Mime', 123: 'Scyther', 124: 'Jynx',
    125: 'Electabuzz', 126: 'Magmar', 127: 'Pinsir', 128: 'Tauros',
    129: 'Magikarp', 130: 'Gyarados', 131: 'Lapras', 132: 'Ditto',
    133: 'Eevee', 134: 'Vaporeon', 135: 'Jolteon', 136: 'Flareon',
    137: 'Porygon', 138: 'Omanyte', 139: 'Omastar', 140: 'Kabuto',
    141: 'Kabutops', 142: 'Aerodactyl', 143: 'Snorlax', 144: 'Articuno',
    145: 'Zapdos', 146: 'Moltres', 147: 'Dratini', 148: 'Dragonair',
    149: 'Dragonite', 150: 'Mewtwo', 151: 'Mew',
}

DE_NAMES = {
    1: 'Bisasam', 2: 'Bisaknosp', 3: 'Bisaflor', 4: 'Glumanda',
    5: 'Glutexo', 6: 'Glurak', 7: 'Schiggy', 8: 'Schillok',
    9: 'Turtok', 10: 'Raupy', 11: 'Safcon', 12: 'Smettbo',
    13: 'Hornliu', 14: 'Kokuna', 15: 'Bibor', 16: 'Taubsi',
    17: 'Tauboga', 18: 'Tauboss', 19: 'Rattfratz', 20: 'Rattikarl',
    21: 'Habitak', 22: 'Ibitak', 23: 'Rettan', 24: 'Arbok',
    25: 'Pikachu', 26: 'Raichu', 27: 'Sandan', 28: 'Sandamer',
    29: 'Nidoran♀', 30: 'Nidorina', 31: 'Nidoqueen', 32: 'Nidoran♂',
    33: 'Nidorino', 34: 'Nidoking', 35: 'Piepi', 36: 'Pixi',
    37: 'Vulpix', 38: 'Vulnona', 39: 'Pummeluff', 40: 'Knuddeluff',
    41: 'Zubat', 42: 'Golbat', 43: 'Myrapla', 44: 'Duflor',
    45: 'Giflor', 46: 'Paras', 47: 'Parasek', 48: 'Bluzuk',
    49: 'Omot', 50: 'Digda', 51: 'Digdri', 52: 'Mauzi',
    53: 'Snobilikat', 54: 'Enton', 55: 'Entoron', 56: 'Menki',
    57: 'Rasaff', 58: 'Fukano', 59: 'Arkani', 60: 'Quapsel',
    61: 'Quaputzi', 62: 'Quappo', 63: 'Abra', 64: 'Kadabra',
    65: 'Simsala', 66: 'Machollo', 67: 'Maschock', 68: 'Machomei',
    69: 'Knofensa', 70: 'Ultrigaria', 71: 'Sarzenia', 72: 'Tentacha',
    73: 'Tentoxa', 74: 'Kleinstein', 75: 'Georok', 76: 'Geowaz',
    77: 'Ponita', 78: 'Gallopa', 79: 'Flegmon', 80: 'Lahmus',
    81: 'Magnetilo', 82: 'Magneton', 83: 'Porenta', 84: 'Dodu',
    85: 'Dodri', 86: 'Jurob', 87: 'Jugong', 88: 'Sleima',
    89: 'Sleimok', 90: 'Muschas', 91: 'Austos', 92: 'Nebulak',
    93: 'Alpollo', 94: 'Gengar', 95: 'Onix', 96: 'Traumato',
    97: 'Hypno', 98: 'Krabby', 99: 'Kingler', 100: 'Voltobal',
    101: 'Lektrobal', 102: 'Owei', 103: 'Kokowei', 104: 'Tragosso',
    105: 'Knogga', 106: 'Kicklee', 107: 'Nockchan', 108: 'Schlurp',
    109: 'Smogon', 110: 'Smogmog', 111: 'Rihorn', 112: 'Rizeros',
    113: 'Chaneira', 114: 'Tangela', 115: 'Kangama', 116: 'Seeper',
    117: 'Seemon', 118: 'Goldini', 119: 'Golking', 120: 'Sterndu',
    121: 'Starmie', 122: 'Pantimos', 123: 'Sichlor', 124: 'Rossana',
    125: 'Elektek', 126: 'Magmar', 127: 'Pinsir', 128: 'Tauros',
    129: 'Karpador', 130: 'Garados', 131: 'Lapras', 132: 'Ditto',
    133: 'Evoli', 134: 'Aquana', 135: 'Blitza', 136: 'Flamara',
    137: 'Porygon', 138: 'Amonitas', 139: 'Amoroso', 140: 'Kabuto',
    141: 'Kabutops', 142: 'Aerodactyl', 143: 'Relaxo', 144: 'Arktos',
    145: 'Zapdos', 146: 'Lavados', 147: 'Dratini', 148: 'Dragonir',
    149: 'Dragoran', 150: 'Mewtu', 151: 'Mew',
}

FR_NAMES = {
    1: 'Bulbizarre', 2: 'Herbizarre', 3: 'Florizarre', 4: 'Salamèche',
    5: 'Reptincel', 6: 'Dracaufeu', 7: 'Carapuce', 8: 'Carabaffe',
    9: 'Tortank', 10: 'Chenipan', 11: 'Chrysacier', 12: 'Papilusion',
    13: 'Aspicot', 14: 'Coconfort', 15: 'Dardargnan', 16: 'Roucool',
    17: 'Roucoups', 18: 'Roucarnage', 19: 'Rattata', 20: 'Rattatac',
    21: 'Piafabec', 22: 'Rapasdepic', 23: 'Abo', 24: 'Arbok',
    25: 'Pikachu', 26: 'Raichu', 27: 'Sabelette', 28: 'Sablaireau',
    29: 'Nidoran♀', 30: 'Nidorina', 31: 'Nidoqueen', 32: 'Nidoran♂',
    33: 'Nidorino', 34: 'Nidoking', 35: 'Mélofée', 36: 'Mélodelfe',
    37: 'Goupix', 38: 'Feunard', 39: 'Rondoudou', 40: 'Grodoudou',
    41: 'Nosferapti', 42: 'Nosferalto', 43: 'Mystherbe', 44: 'Ortide',
    45: 'Rafflesia', 46: 'Paras', 47: 'Parasect', 48: 'Mimitoss',
    49: 'Aéromite', 50: 'Taupiqueur', 51: 'Triopikeur', 52: 'Miaouss',
    53: 'Persian', 54: 'Psykokwak', 55: 'Akwakwak', 56: 'Férosinge',
    57: 'Colossinge', 58: 'Caninos', 59: 'Arcanin', 60: 'Ptitard',
    61: 'Têtarte', 62: 'Tartard', 63: 'Abra', 64: 'Kadabra',
    65: 'Alakazam', 66: 'Machoc', 67: 'Machopeur', 68: 'Mackogneur',
    69: 'Chétiflor', 70: 'Boustiflor', 71: 'Empiflor', 72: 'Tentacool',
    73: 'Tentacruel', 74: 'Racaillou', 75: 'Gravalanch', 76: 'Grolem',
    77: 'Ponyta', 78: 'Galopa', 79: 'Ramoloss', 80: 'Flagadoss',
    81: 'Magnéti', 82: 'Magnéton', 83: 'Canarticho', 84: 'Doduo',
    85: 'Dodrio', 86: 'Otaria', 87: 'Lamantine', 88: 'Tadmorv',
    89: 'Grotadmorv', 90: 'Kokiyas', 91: 'Crustabri', 92: 'Fantominus',
    93: 'Spectrum', 94: 'Ectoplasma', 95: 'Onix', 96: 'Soporifik',
    97: 'Hypnomade', 98: 'Krabby', 99: 'Krabboss', 100: 'Voltorbe',
    101: 'Électrode', 102: 'Nœunœuf', 103: 'Noadkoko', 104: 'Osselait',
    105: 'Ossatueur', 106: 'Kicklee', 107: 'Tygnon', 108: 'Excelangue',
    109: 'Smogo', 110: 'Smogogo', 111: 'Rhinocorne', 112: 'Rhinoféros',
    113: 'Leveinard', 114: 'Saquedeneu', 115: 'Kangourex',
    116: 'Hypotrempe', 117: 'Hypocéan', 118: 'Poissirène',
    119: 'Poissoroy', 120: 'Stari', 121: 'Staross', 122: 'M. Mime',
    123: 'Insécateur', 124: 'Lippoutou', 125: 'Élektek', 126: 'Magmar',
    127: 'Scarabrute', 128: 'Tauros', 129: 'Magicarpe', 130: 'Léviator',
    131: 'Lokhlass', 132: 'Métamorph', 133: 'Évoli', 134: 'Aquali',
    135: 'Voltali', 136: 'Pyroli', 137: 'Porygon', 138: 'Amonita',
    139: 'Amonistar', 140: 'Kabuto', 141: 'Kabutops', 142: 'Ptéra',
    143: 'Ronflex', 144: 'Artikodin', 145: 'Électhor', 146: 'Sulfura',
    147: 'Minidraco', 148: 'Draco', 149: 'Dracolosse', 150: 'Mewtwo',
    151: 'Mew',
}

ZH_NAMES = {
    1: '妙蛙种子', 2: '妙蛙草', 3: '妙蛙花', 4: '小火龙', 5: '火恐龙',
    6: '喷火龙', 7: '杰尼龟', 8: '卡咪龟', 9: '水箭龟', 10: '绿毛虫',
    11: '铁甲蛹', 12: '巴大蝶', 13: '独角虫', 14: '铁壳蛹', 15: '大针蜂',
    16: '波波', 17: '比比鸟', 18: '大比鸟', 19: '小拉达', 20: '拉达',
    21: '烈雀', 22: '大嘴雀', 23: '阿柏蛇', 24: '阿柏怪', 25: '皮卡丘',
    26: '雷丘', 27: '穿山鼠', 28: '穿山王', 29: '尼多兰', 30: '尼多娜',
    31: '尼多后', 32: '尼多朗', 33: '尼多力诺', 34: '尼多王', 35: '皮皮',
    36: '皮可西', 37: '六尾', 38: '九尾', 39: '胖丁', 40: '胖可丁',
    41: '超音蝠', 42: '大嘴蝠', 43: '走路草', 44: '臭臭花', 45: '霸王花',
    46: '派拉斯', 47: '派拉斯特', 48: '毛球', 49: '摩鲁蛾', 50: '地鼠',
    51: '三地鼠', 52: '喵喵', 53: '猫老大', 54: '可达鸭', 55: '哥达鸭',
    56: '猴怪', 57: '火暴猴', 58: '卡蒂狗', 59: '风速狗', 60: '蚊香蝌蚪',
    61: '蚊香君', 62: '蚊香泳士', 63: '凯西', 64: '勇基拉', 65: '胡地',
    66: '腕力', 67: '豪力', 68: '怪力', 69: '喇叭芽', 70: '口呆花',
    71: '大食花', 72: '玛瑙水母', 73: '毒刺水母', 74: '小拳石', 75: '隆隆石',
    76: '隆隆岩', 77: '小火马', 78: '烈焰马', 79: '呆呆兽', 80: '呆壳兽',
    81: '小磁怪', 82: '三合一磁怪', 83: '大葱鸭', 84: '嘟嘟', 85: '嘟嘟利',
    86: '小海狮', 87: '白海狮', 88: '臭泥', 89: '臭臭泥', 90: '大舌贝',
    91: '刺甲贝', 92: '鬼斯', 93: '鬼斯通', 94: '耿鬼', 95: '大岩蛇',
    96: '催眠貘', 97: '引梦貘人', 98: '大钳蟹', 99: '巨钳蟹', 100: '霹雳电球',
    101: '顽皮雷弹', 102: '蛋蛋', 103: '椰蛋树', 104: '卡拉卡拉',
    105: '嘎啦嘎啦', 106: '飞腿郎', 107: '快拳郎', 108: '大舌头',
    109: '瓦斯弹', 110: '双弹瓦斯', 111: '独角犀牛', 112: '钻角犀兽',
    113: '吉利蛋', 114: '蔓藤怪', 115: '袋兽', 116: '墨海马', 117: '海刺龙',
    118: '角金鱼', 119: '金鱼王', 120: '海星星', 121: '宝石海星',
    122: '魔墙人偶', 123: '飞天螳螂', 124: '迷唇姐', 125: '电击兽',
    126: '鸭嘴火兽', 127: '凯罗斯', 128: '肯泰罗', 129: '鲤鱼王',
    130: '暴鲤龙', 131: '拉普拉斯', 132: '百变怪', 133: '伊布', 134: '水伊布',
    135: '雷伊布', 136: '火伊布', 137: '多边兽', 138: '菊石兽',
    139: '多刺菊石兽', 140: '化石盔', 141: '镰刀盔', 142: '化石翼龙',
    143: '卡比兽', 144: '急冻鸟', 145: '闪电鸟', 146: '火焰鸟', 147: '迷你龙',
    148: '哈克龙', 149: '快龙', 150: '超梦', 151: '梦幻'
}

MOVES = {
    1: {
        'name': 'Thunder Shock',
        'type': 'Electric'
    },
    2: {
        'name': 'Quick Attack',
        'type': 'Normal'
    },
    3: {
        'name': 'Scratch',
        'type': 'Normal'
    },
    4: {
        'name': 'Ember',
        'type': 'Fire'
    },
    5: {
        'name': 'Vine Whip',
        'type': 'Grass'
    },
    6: {
        'name': 'Tackle',
        'type': 'Normal'
    },
    7: {
        'name': 'Razor Leaf',
        'type': 'Grass'
    },
    8: {
        'name': 'Take Down',
    },
    9: {
        'name': 'Water Gun',
        'type': 'Water'
    },
    10: {
        'name': 'Bite',
        'type': 'Dark'
    },
    11: {
        'name': 'Double Slap'
    },
    12: {
        'name': 'Tackle',
        'type': 'Normal'
    },
    13: {
        'duration': 4000,
        'name': 'Wrap',
        'dps': 6.25,
        'energy': 20,
        'type': 'Normal',
        'damage': 25
    },
    14: {
        'duration': 5000,
        'name': 'Hyper Beam',
        'dps': 24.0,
        'energy': 100,
        'type': 'Normal',
        'damage': 120
    },
    15: {
        'name': 'Lick',
        'type': 'Ghost'
    },
    16: {
        'duration': 3500,
        'name': 'Dark Pulse',
        'dps': 12.85,
        'energy': 33,
        'type': 'Dark',
        'damage': 45
    },
    17: {
        'name': 'Smog',
    },
    18: {
        'duration': 2600,
        'name': 'Sludge',
        'dps': 11.53,
        'energy': 25,
        'type': 'Poison',
        'damage': 30
    },
    19: {
        'name': 'Metal Claw',
        'type': 'Steel'
    },
    20: {
        'duration': 2100,
        'name': 'Vice Grip',
        'dps': 11.9,
        'energy': 20,
        'type': 'Normal',
        'damage': 25
    },
    21: {
        'duration': 4600,
        'name': 'Flame Wheel',
        'dps': 8.69,
        'energy': 25,
        'type': 'Fire',
        'damage': 40
    },
    22: {
        'duration': 3200,
        'name': 'Megahorn',
        'dps': 25.0,
        'energy': 100,
        'type': 'Bug',
        'damage': 80
    },
    23: {
        'name': 'Wing Attack',
        'type': 'Flying'
    },
    24: {
        'duration': 2900,
        'name': 'Flamethrower',
        'dps': 18.96,
        'energy': 50,
        'type': 'Fire',
        'damage': 55
    },
    25: {
        'name': 'Sucker Punch',
        'type': 'Dark'
    },
    26: {
        'duration': 5800,
        'name': 'Dig',
        'dps': 12.06,
        'energy': 33,
        'type': 'Ground',
        'damage': 70
    },
    27: {
        'name': 'Low Kick',
        'type': 'Fighting'
    },
    28: {
        'duration': 2000,
        'name': 'Cross Chop',
        'dps': 30.0,
        'energy': 100,
        'type': 'Fighting',
        'damage': 60
    },
    29: {
        'name': 'Psycho Cut',
        'type': 'Psychic'
    },
    30: {
        'duration': 3800,
        'name': 'Psybeam',
        'dps': 10.52,
        'energy': 25,
        'type': 'Psychic',
        'damage': 40
    },
    31: {
        'duration': 4200,
        'name': 'Earthquake',
        'dps': 23.8,
        'energy': 100,
        'type': 'Ground',
        'damage': 100
    },
    32: {
        'duration': 3100,
        'name': 'Stone Edge',
        'dps': 25.8,
        'energy': 100,
        'type': 'Rock',
        'damage': 80
    },
    33: {
        'duration': 3500,
        'name': 'Ice Punch',
        'dps': 12.85,
        'energy': 33,
        'type': 'Ice',
        'damage': 45
    },
    34: {
        'duration': 2550,
        'name': 'Heart Stamp',
        'dps': 7.84,
        'energy': 25,
        'type': 'Psychic',
        'damage': 20
    },
    35: {
        'duration': 2500,
        'name': 'Discharge',
        'dps': 14.0,
        'energy': 33,
        'type': 'Electric',
        'damage': 35
    },
    36: {
        'duration': 3900,
        'name': 'Flash Cannon',
        'dps': 15.38,
        'energy': 33,
        'type': 'Steel',
        'damage': 60
    },
    37: {
        'name': 'Peck',
        'type': 'Flying'
    },
    38: {
        'duration': 2700,
        'name': 'Drill Peck',
        'dps': 14.81,
        'energy': 33,
        'type': 'Flying',
        'damage': 40
    },
    39: {
        'duration': 3650,
        'name': 'Ice Beam',
        'dps': 17.8,
        'energy': 50,
        'type': 'Ice',
        'damage': 65
    },
    40: {
        'duration': 3900,
        'name': 'Blizzard',
        'dps': 25.64,
        'energy': 100,
        'type': 'Ice',
        'damage': 100
    },
    41: {
        'name': 'Air Slash'
    },
    42: {
        'duration': 3800,
        'name': 'Heat Wave',
        'dps': 21.05,
        'energy': 100,
        'type': 'Fire',
        'damage': 80
    },
    43: {
        'name': 'Twineedle'
    },
    44: {
        'name': 'Poison Jab'
    },
    45: {
        'duration': 2900,
        'name': 'Aerial Ace',
        'dps': 10.34,
        'energy': 25,
        'type': 'Flying',
        'damage': 30
    },
    46: {
        'duration': 3400,
        'name': 'Drill Run',
        'dps': 14.7,
        'energy': 33,
        'type': 'Ground',
        'damage': 50
    },
    47: {
        'duration': 3200,
        'name': 'Petal Blizzard',
        'dps': 20.31,
        'energy': 50,
        'type': 'Grass',
        'damage': 65
    },
    48: {
        'duration': 3200,
        'name': 'Mega Drain',
        'dps': 4.68,
        'energy': 20,
        'type': 'Grass',
        'damage': 15
    },
    49: {
        'duration': 4250,
        'name': 'Bug Buzz',
        'dps': 17.64,
        'energy': 50,
        'type': 'Bug',
        'damage': 75
    },
    50: {
        'duration': 2400,
        'name': 'Poison Fang',
        'dps': 10.41,
        'energy': 20,
        'type': 'Poison',
        'damage': 25
    },
    51: {
        'duration': 2700,
        'name': 'Night Slash',
        'dps': 11.11,
        'energy': 25,
        'type': 'Dark',
        'damage': 30
    },
    52: {
        'name': 'Slash'
    },
    53: {
        'duration': 2900,
        'name': 'Bubble Beam',
        'dps': 10.34,
        'energy': 25,
        'type': 'Water',
        'damage': 30
    },
    54: {
        'duration': 2100,
        'name': 'Submission',
        'dps': 14.28,
        'energy': 33,
        'type': 'Fighting',
        'damage': 30
    },
    55: {
        'name': 'Karate Chop',
        'type': 'Fighting'
    },
    56: {
        'duration': 2250,
        'name': 'Low Sweep',
        'dps': 13.33,
        'energy': 25,
        'type': 'Fighting',
        'damage': 30
    },
    57: {
        'duration': 2350,
        'name': 'Aqua Jet',
        'dps': 10.63,
        'energy': 20,
        'type': 'Water',
        'damage': 25
    },
    58: {
        'duration': 2350,
        'name': 'Aqua Tail',
        'dps': 19.14,
        'energy': 50,
        'type': 'Water',
        'damage': 45
    },
    59: {
        'duration': 2400,
        'name': 'Seed Bomb',
        'dps': 16.66,
        'energy': 33,
        'type': 'Grass',
        'damage': 40
    },
    60: {
        'duration': 2700,
        'name': 'Psyshock',
        'dps': 14.81,
        'energy': 33,
        'type': 'Psychic',
        'damage': 40
    },
    62: {
        'duration': 3600,
        'name': 'Ancient Power',
        'dps': 9.72,
        'energy': 25,
        'type': 'Rock',
        'damage': 35
    },
    63: {
        'duration': 3400,
        'name': 'Rock Tomb',
        'dps': 8.82,
        'energy': 25,
        'type': 'Rock',
        'damage': 30
    },
    64: {
        'duration': 3200,
        'name': 'Rock Slide',
        'dps': 15.62,
        'energy': 33,
        'type': 'Rock',
        'damage': 50
    },
    65: {
        'duration': 2900,
        'name': 'Power Gem',
        'dps': 13.79,
        'energy': 33,
        'type': 'Rock',
        'damage': 40
    },
    66: {
        'duration': 3100,
        'name': 'Shadow Sneak',
        'dps': 4.83,
        'energy': 20,
        'type': 'Ghost',
        'damage': 15
    },
    67: {
        'duration': 2100,
        'name': 'Shadow Punch',
        'dps': 9.52,
        'energy': 25,
        'type': 'Ghost',
        'damage': 20
    },
    69: {
        'duration': 3100,
        'name': 'Ominous Wind',
        'dps': 9.67,
        'energy': 25,
        'type': 'Ghost',
        'damage': 30
    },
    70: {
        'duration': 3080,
        'name': 'Shadow Ball',
        'dps': 14.61,
        'energy': 33,
        'type': 'Ghost',
        'damage': 45
    },
    72: {
        'duration': 2800,
        'name': 'Magnet Bomb',
        'dps': 10.71,
        'energy': 25,
        'type': 'Steel',
        'damage': 30
    },
    74: {
        'duration': 2000,
        'name': 'Iron Head',
        'dps': 15.0,
        'energy': 33,
        'type': 'Steel',
        'damage': 30
    },
    75: {
        'duration': 2100,
        'name': 'Parabolic Charge',
        'dps': 7.14,
        'energy': 20,
        'type': 'Electric',
        'damage': 15
    },
    77: {
        'duration': 2400,
        'name': 'Thunder Punch',
        'dps': 16.66,
        'energy': 33,
        'type': 'Electric',
        'damage': 40
    },
    78: {
        'duration': 4300,
        'name': 'Thunder',
        'dps': 23.25,
        'energy': 100,
        'type': 'Electric',
        'damage': 100
    },
    79: {
        'duration': 2700,
        'name': 'Thunderbolt',
        'dps': 20.37,
        'energy': 50,
        'type': 'Electric',
        'damage': 55
    },
    80: {
        'duration': 2700,
        'name': 'Twister',
        'dps': 9.25,
        'energy': 20,
        'type': 'Dragon',
        'damage': 25
    },
    82: {
        'duration': 3600,
        'name': 'Dragon Pulse',
        'dps': 18.05,
        'energy': 50,
        'type': 'Dragon',
        'damage': 65
    },
    83: {
        'duration': 1500,
        'name': 'Dragon Claw',
        'dps': 23.33,
        'energy': 50,
        'type': 'Dragon',
        'damage': 35
    },
    84: {
        'duration': 3900,
        'name': 'Disarming Voice',
        'dps': 6.41,
        'energy': 20,
        'type': 'Fairy',
        'damage': 25
    },
    85: {
        'duration': 2800,
        'name': 'Draining Kiss',
        'dps': 8.92,
        'energy': 20,
        'type': 'Fairy',
        'damage': 25
    },
    86: {
        'duration': 4200,
        'name': 'Dazzling Gleam',
        'dps': 13.09,
        'energy': 33,
        'type': 'Fairy',
        'damage': 55
    },
    87: {
        'duration': 4100,
        'name': 'Moonblast',
        'dps': 20.73,
        'energy': 100,
        'type': 'Fairy',
        'damage': 85
    },
    88: {
        'duration': 2900,
        'name': 'Play Rough',
        'dps': 18.96,
        'energy': 50,
        'type': 'Fairy',
        'damage': 55
    },
    89: {
        'duration': 1500,
        'name': 'Cross Poison',
        'dps': 16.66,
        'energy': 25,
        'type': 'Poison',
        'damage': 25
    },
    90: {
        'duration': 2600,
        'name': 'Sludge Bomb',
        'dps': 21.15,
        'energy': 50,
        'type': 'Poison',
        'damage': 55
    },
    91: {
        'duration': 3400,
        'name': 'Sludge Wave',
        'dps': 20.58,
        'energy': 100,
        'type': 'Poison',
        'damage': 70
    },
    92: {
        'duration': 3000,
        'name': 'Gunk Shot',
        'dps': 21.66,
        'energy': 100,
        'type': 'Poison',
        'damage': 65
    },
    94: {
        'duration': 1600,
        'name': 'Bone Club',
        'dps': 15.62,
        'energy': 25,
        'type': 'Ground',
        'damage': 25
    },
    95: {
        'duration': 3400,
        'name': 'Bulldoze',
        'dps': 10.29,
        'energy': 25,
        'type': 'Ground',
        'damage': 35
    },
    96: {
        'duration': 2600,
        'name': 'Mud Bomb',
        'dps': 11.53,
        'energy': 25,
        'type': 'Ground',
        'damage': 30
    },
    99: {
        'duration': 3100,
        'name': 'Signal Beam',
        'dps': 14.51,
        'energy': 33,
        'type': 'Bug',
        'damage': 45
    },
    100: {
        'duration': 2100,
        'name': 'X Scissor',
        'dps': 16.66,
        'energy': 33,
        'type': 'Bug',
        'damage': 35
    },
    101: {
        'duration': 3100,
        'name': 'Flame Charge',
        'dps': 8.06,
        'energy': 20,
        'type': 'Fire',
        'damage': 25
    },
    102: {
        'duration': 2100,
        'name': 'Flame Burst',
        'dps': 14.28,
        'energy': 25,
        'type': 'Fire',
        'damage': 30
    },
    103: {
        'duration': 4100,
        'name': 'Fire Blast',
        'dps': 24.39,
        'energy': 100,
        'type': 'Fire',
        'damage': 100
    },
    104: {
        'duration': 2400,
        'name': 'Brine',
        'dps': 10.41,
        'energy': 25,
        'type': 'Water',
        'damage': 25
    },
    105: {
        'duration': 3300,
        'name': 'Water Pulse',
        'dps': 10.6,
        'energy': 25,
        'type': 'Water',
        'damage': 35
    },
    106: {
        'duration': 4000,
        'name': 'Scald',
        'dps': 13.75,
        'energy': 33,
        'type': 'Water',
        'damage': 55
    },
    107: {
        'duration': 3800,
        'name': 'Hydro Pump',
        'dps': 23.68,
        'energy': 100,
        'type': 'Water',
        'damage': 90
    },
    108: {
        'duration': 2800,
        'name': 'Psychic',
        'dps': 19.64,
        'energy': 50,
        'type': 'Psychic',
        'damage': 55
    },
    109: {
        'duration': 5100,
        'name': 'Psystrike',
        'dps': 13.72,
        'energy': 100,
        'type': 'Psychic',
        'damage': 70
    },
    111: {
        'duration': 3800,
        'name': 'Icy Wind',
        'dps': 6.57,
        'energy': 20,
        'type': 'Ice',
        'damage': 25
    },
    114: {
        'duration': 3600,
        'name': 'Giga Drain',
        'dps': 9.72,
        'energy': 33,
        'type': 'Grass',
        'damage': 35
    },
    115: {
        'duration': 2800,
        'name': 'Fire Punch',
        'dps': 14.28,
        'energy': 33,
        'type': 'Fire',
        'damage': 40
    },
    116: {
        'duration': 4900,
        'name': 'Solar Beam',
        'dps': 24.48,
        'energy': 100,
        'type': 'Grass',
        'damage': 120
    },
    117: {
        'duration': 2800,
        'name': 'Leaf Blade',
        'dps': 19.64,
        'energy': 50,
        'type': 'Grass',
        'damage': 55
    },
    118: {
        'duration': 2800,
        'name': 'Power Whip',
        'dps': 25.0,
        'energy': 100,
        'type': 'Grass',
        'damage': 70
    },
    121: {
        'duration': 3300,
        'name': 'Air Cutter',
        'dps': 9.09,
        'energy': 25,
        'type': 'Flying',
        'damage': 30
    },
    122: {
        'duration': 3200,
        'name': 'Hurricane',
        'dps': 25.0,
        'energy': 100,
        'type': 'Flying',
        'damage': 80
    },
    123: {
        'duration': 1600,
        'name': 'Brick Break',
        'dps': 18.75,
        'energy': 33,
        'type': 'Fighting',
        'damage': 30
    },
    125: {
        'duration': 3000,
        'name': 'Swift',
        'dps': 10.0,
        'energy': 25,
        'type': 'Normal',
        'damage': 30
    },
    126: {
        'duration': 2200,
        'name': 'Horn Attack',
        'dps': 11.36,
        'energy': 25,
        'type': 'Normal',
        'damage': 25
    },
    127: {
        'duration': 2100,
        'name': 'Stomp',
        'dps': 14.28,
        'energy': 25,
        'type': 'Normal',
        'damage': 30
    },
    129: {
        'duration': 2100,
        'name': 'Hyper Fang',
        'dps': 16.66,
        'energy': 33,
        'type': 'Normal',
        'damage': 35
    },
    131: {
        'duration': 1560,
        'name': 'Body Slam',
        'dps': 25.64,
        'energy': 50,
        'type': 'Normal',
        'damage': 40
    },
    132: {
        'duration': 3100,
        'name': 'Rest',
        'dps': 11.29,
        'energy': 33,
        'type': 'Normal',
        'damage': 35
    },
    133: {
        'duration': 1695,
        'name': 'Struggle',
        'dps': 8.84,
        'energy': 20,
        'type': 'Normal',
        'damage': 15
    },
    200: {
        'duration': 400,
        'name': 'Fury Cutter',
        'dps': 7.5,
        'energy': 12,
        'type': 'Bug',
        'damage': 3
    },
    201: {
        'duration': 450,
        'name': 'Bug Bite',
        'dps': 11.11,
        'energy': 7,
        'type': 'Bug',
        'damage': 5
    },
    202: {
        'duration': 500,
        'name': 'Bite',
        'dps': 12.0,
        'energy': 7,
        'type': 'Dark',
        'damage': 6
    },
    203: {
        'duration': 700,
        'name': 'Sucker Punch',
        'dps': 10.0,
        'energy': 4,
        'type': 'Dark',
        'damage': 7
    },
    204: {
        'duration': 500,
        'name': 'Dragon Breath',
        'dps': 12.0,
        'energy': 7,
        'type': 'Dragon',
        'damage': 6
    },
    205: {
        'duration': 600,
        'name': 'Thunder Shock',
        'dps': 8.33,
        'energy': 7,
        'type': 'Electric',
        'damage': 5
    },
    206: {
        'duration': 700,
        'name': 'Spark',
        'dps': 10.0,
        'energy': 4,
        'type': 'Electric',
        'damage': 7
    },
    207: {
        'duration': 600,
        'name': 'Low Kick',
        'dps': 8.33,
        'energy': 7,
        'type': 'Fighting',
        'damage': 5
    },
    208: {
        'duration': 800,
        'name': 'Karate Chop',
        'dps': 7.5,
        'energy': 7,
        'type': 'Fighting',
        'damage': 6
    },
    209: {
        'duration': 1050,
        'name': 'Ember',
        'dps': 9.52,
        'energy': 7,
        'type': 'Fire',
        'damage': 10
    },
    210: {
        'duration': 750,
        'name': 'Wing Attack',
        'dps': 12.0,
        'energy': 7,
        'type': 'Flying',
        'damage': 9
    },
    211: {
        'duration': 1150,
        'name': 'Peck',
        'dps': 8.69,
        'energy': 10,
        'type': 'Flying',
        'damage': 10
    },
    212: {
        'duration': 500,
        'name': 'Lick',
        'dps': 10.0,
        'energy': 7,
        'type': 'Ghost',
        'damage': 5
    },
    213: {
        'duration': 950,
        'name': 'Shadow Claw',
        'dps': 11.57,
        'energy': 7,
        'type': 'Ghost',
        'damage': 11
    },
    214: {
        'duration': 650,
        'name': 'Vine Whip',
        'dps': 10.76,
        'energy': 7,
        'type': 'Grass',
        'damage': 7
    },
    215: {
        'duration': 1450,
        'name': 'Razor Leaf',
        'dps': 10.34,
        'energy': 7,
        'type': 'Grass',
        'damage': 15
    },
    216: {
        'duration': 550,
        'name': 'Mud Shot',
        'dps': 10.9,
        'energy': 7,
        'type': 'Ground',
        'damage': 6
    },
    217: {
        'duration': 1400,
        'name': 'Ice Shard',
        'dps': 10.71,
        'energy': 7,
        'type': 'Ice',
        'damage': 15
    },
    218: {
        'duration': 810,
        'name': 'Frost Breath',
        'dps': 11.11,
        'energy': 7,
        'type': 'Ice',
        'damage': 9
    },
    219: {
        'duration': 1330,
        'name': 'Quick Attack',
        'dps': 7.51,
        'energy': 7,
        'type': 'Normal',
        'damage': 10
    },
    220: {
        'duration': 500,
        'name': 'Scratch',
        'dps': 12.0,
        'energy': 7,
        'type': 'Normal',
        'damage': 6
    },
    221: {
        'duration': 1100,
        'name': 'Tackle',
        'dps': 10.9,
        'energy': 7,
        'type': 'Normal',
        'damage': 12
    },
    222: {
        'duration': 540,
        'name': 'Pound',
        'dps': 12.96,
        'energy': 7,
        'type': 'Normal',
        'damage': 7
    },
    223: {
        'duration': 1130,
        'name': 'Cut',
        'dps': 10.61,
        'energy': 7,
        'type': 'Normal',
        'damage': 12
    },
    224: {
        'duration': 1050,
        'name': 'Poison Jab',
        'dps': 11.42,
        'energy': 7,
        'type': 'Poison',
        'damage': 12
    },
    225: {
        'duration': 1050,
        'name': 'Acid',
        'dps': 9.52,
        'energy': 7,
        'type': 'Poison',
        'damage': 10
    },
    226: {
        'duration': 570,
        'name': 'Psycho Cut',
        'dps': 12.28,
        'energy': 7,
        'type': 'Psychic',
        'damage': 7
    },
    227: {
        'duration': 1360,
        'name': 'Rock Throw',
        'dps': 8.82,
        'energy': 7,
        'type': 'Rock',
        'damage': 12
    },
    228: {
        'duration': 630,
        'name': 'Metal Claw',
        'dps': 12.69,
        'energy': 7,
        'type': 'Steel',
        'damage': 8
    },
    229: {
        'duration': 1200,
        'name': 'Bullet Punch',
        'dps': 8.33,
        'energy': 7,
        'type': 'Steel',
        'damage': 10
    },
    230: {
        'duration': 500,
        'name': 'Water Gun',
        'dps': 12.0,
        'energy': 7,
        'type': 'Water',
        'damage': 6
    },
    231: {
        'duration': 1230,
        'name': 'Splash',
        'dps': 0.0,
        'energy': 7,
        'type': 'Water',
        'damage': 0
    },
    233: {
        'duration': 1350,
        'name': 'Mud Slap',
        'dps': 11.11,
        'energy': 9,
        'type': 'Ground',
        'damage': 15
    },
    234: {
        'duration': 1050,
        'name': 'Zen Headbutt',
        'dps': 11.42,
        'energy': 4,
        'type': 'Psychic',
        'damage': 12
    },
    235: {
        'duration': 1510,
        'name': 'Confusion',
        'dps': 9.93,
        'energy': 7,
        'type': 'Psychic',
        'damage': 15
    },
    236: {
        'duration': 575,
        'name': 'Poison Sting',
        'dps': 10.43,
        'energy': 4,
        'type': 'Poison',
        'damage': 6
    },
    237: {
        'duration': 2300,
        'name': 'Bubble',
        'dps': 10.86,
        'energy': 15,
        'type': 'Water',
        'damage': 25
    },
    238: {
        'duration': 1040,
        'name': 'Feint Attack',
        'dps': 11.53,
        'energy': 7,
        'type': 'Dark',
        'damage': 12
    },
    239: {
        'duration': 1330,
        'name': 'Steel Wing',
        'dps': 11.27,
        'energy': 4,
        'type': 'Steel',
        'damage': 15
    },
    240: {
        'duration': 840,
        'name': 'Fire Fang',
        'dps': 11.9,
        'energy': 4,
        'type': 'Fire',
        'damage': 10
    },
    241: {
        'duration': 1410,
        'name': 'Rock Smash',
        'dps': 10.63,
        'energy': 7,
        'type': 'Fighting',
        'damage': 15
    }
}

POKEMON_NAMES = {
    'DE': DE_NAMES,
    'FR': FR_NAMES,
    'ZH': ZH_NAMES,
}.get(config.LANGUAGE.upper(), EN_NAMES)
