import random

def get_questions():
    questions = [
        {
            'question': 'Pirmą kartą Lietuva paminėta 1009 m. Šv.Brunono misijos aprašyme. Kokia buvo jo misija?',
            'choices': ['Skleisti krikščionybę', 'Plėtoti mokslą ', 'Skleisti Islamą'],
            'answer': 'Skleisti krikščionybę'
        },
        {
            'question': '1253 m. liepos 6 d. karūnuotas valdovas Mindaugas. Kokiai valstybei jis vadovavo?',
            'choices': ['Varšuvos kunigaikštystei', 'Prūsijai', 'Lietuvos Didžiajai Kunigaikštystei'],
            'answer': 'Lietuvos Didžiajai Kunigaikštystei'
        },
        {
            'question': 'Kokį priešą Lietuva nugalėjo Žalgirio mūšyje 1410 m. liepos 15 d.?',
            'choices': ['Kryžiuočius', 'Kazokus', 'Krikščionių Ordiną'],
            'answer': 'Krikščionių Ordiną'
        },
        {
            'question': 'Seniausias universitetas rytų Europoje buvo įkurtas 1579 m. Kuriame mieste?',
            'choices': ['Berlyne', 'Vilniuje', 'Maskvoje'],
            'answer': 'Vilniuje'
        },
        {
            'question': 'Pirmasis atkurtosios Lietuvos aukščiausiasis vadovas ',
            'choices': [' Vytautas Landsbergis', 'Antanas Smetona', 'Jonas Basanavičius'],
            'answer': ' Vytautas Landsbergis'
        },
    
         {
            'question': 'Kas pirmoji pripažino atkurtą Lietuvos nepriklausomybę? ',
            'choices': ['Islandija', 'Vokietija', 'Didžioji Britanija'],
            'answer': 'Islandija'
        },
        {
            'question': ' Kas 2017 m. rado Vasario 16-osios Lietuvos Nepriklausomybės Akto originalą?',
            'choices': ['Lukas Urbietis', 'Liudas Mažylis', 'Edvardas Mikuckis'],
            'answer': 'Liudas Mažylis'
        },
        {
            'question': ' Kokiai kalbų šeimai priklauso lietuvių kalba?',
            'choices': ['Altajaus', 'Uralo', 'Indoeuropiečių'],
            'answer': 'Indoeuropiečių'
        },
        {
            'question': ' Lietuvių kalba panaši į...',
            'choices': ['sanskritą, lotynų kalbą', 'Anglų kalbą', 'Rusų kalbą'],
            'answer': 'sanskritą, lotynų kalbą'
        },
        {
            'question': ' Kuriame amžiuje buvo parengtas Lietuvos Pirmasis Statutas, pirmoji spausdinta lietuviška knyga, pastatomi Valdovų rūmai, įkurtas VU',
            'choices': ['XV a.', 'XVI a.', 'XVII a.'],
            'answer': 'XVI a.'
        },
        {
            'question': '  Kelintais metais Lietuva tapo Europos Sajungos valstybę? Kelintais metais Lietuva tapo Europos Sajungos valstybę?',
            'choices': ['2004m.', '2002m.', '2000m.'],
            'answer': '2004m.'
        },
        {
            'question': 'Kada įvyko Lietuvos-Lenkijos antrasis padalijimas?  2.kiek metų Lietuvos vardo nebuvo žemėlapyje? ',
            'choices': ['1792m.', '1796 m.', '1793m.'],
            'answer': '1793m.'
        },
        {
            'question': ' Kiek metų Lietuvos vardo nebuvo žemėlapyje?',
            'choices': ['121m.', '123m', '118m.'],
            'answer': '123m'
        },
        {
            'question': 'Kokiai valstybei Lietuva priklausė nuo 1795 m.? ',
            'choices': ['Prūsijai', 'Varšuvos kunigaikštystei', 'Rusijos imperijai'],
            'answer': 'Rusijos imperijai'
        },
        {
            'question': 'Kokiai valstybei nuo 1795 m. Priklausė Mažoji Lietuva? ',
            'choices': ['Prūsijai', 'Rusijos imperijai', 'Varšuvos kunigaikštystei'],
            'answer': 'Prūsijai'
        },
        {
            'question': ' Kuriai iš šių valstybių 1812 m. trumpam priklausė Lietuva?',
            'choices': ['Vokietijai', 'Prancūzijai', 'Italijai'],
            'answer': 'Prancūzijai'
        },
        {
            'question': ' Kaip vadinosi pirmoji Lietuvos istorija?',
            'choices': ['Priešistorinė Lietuva', 'Lietuvių tautos atgimimo istorija', 'Darbai senųjų Lietuvių ir Žemaičių'],
            'answer': 'Darbai senųjų Lietuvių ir Žemaičių'
        },
        {
            'question': ' Pirmasis sukilimas prieš Rusijos imperiją?',
            'choices': ['1830-1831 m', '1820-1821m.', '1864m.'],
            'answer': '1830-1831 m'
        },
        {
            'question': 'Kaip vadinosi slaptųjų  mokyklų mokytojas? ',
            'choices': ['Redaktorius', ' Daraktorius', 'Direktorius'],
            'answer': ' Daraktorius'
        },
        {
            'question': ' Kada leistas laikraštis „Aušra“?',
            'choices': ['1891-1894 m', '1982-1985 m', '1883-1886 m'],
            'answer': '1883-1886 m'
        },
        {
            'question': ' Kas yra REDAKTORIUS?',
            'choices': ['amatininkas, sėkmingai baigęs profesinį amatininko mokymą', 'žmogus, valdantis darbinį ar kovos dramblį', 'Laikraščio vadovas'],
            'answer': 'Laikraščio vadovas'
        },
        {
            'question': 'Kada panaikintas Lietuviškos spaudos draudimas? ',
            'choices': ['1906m.', '1912m.', '1904 m'],
            'answer': '1904 m'
        },
        {
            'question': 'Garsus Lietuvių kompozitorius ir dailininkas: ',
            'choices': ['Rokas Šliūpas', 'M. K. Čiurlionis', 'Almantas Grikevičius'],
            'answer': 'M. K. Čiurlionis'
        },
       {
            'question': 'Kas įkūrė pirmąjį muziejų Lietuvoje- Baublį?',
            'choices': ['Ugnė karvelis', 'Juozas Aputis', 'Julius Janonis'],
            'answer': 'Julius Janonis'
        },
        {
            'question': 'Kuriame iš šių miestų spaudos draudimo metu nebuvo spausdinamos slaptos lietuviškos knygos?',
            'choices': ['Suvalkai', 'Tilžė', 'Ragainė'],
            'answer': 'Suvalkai'
        },
       

        
    ]
    random.shuffle(questions)
    return questions[:25]
