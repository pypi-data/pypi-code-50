YARRRML_MAPPING = '''mappings:
  awayTeam:
    predicateobjects:
      - [a, 'http://dbpedia.org/ontology/SportsTeam']
      - [a, 'http://dbpedia.org/ontology/Organisation']
      - [a, 'http://schema.org/SportsTeam']
      - ['http://www.w3.org/2000/01/rdf-schema#label', $(away_team)]
    source: dataset-source
    subject: https://data.opendatasoft.com/ld/resources/resultats-ligue-1@public/SoccerTeam/$(away_team)/
  homeTeam:
    predicateobjects:
      - [a, 'http://dbpedia.org/ontology/SportsTeam']
      - [a, 'http://dbpedia.org/ontology/Organisation']
      - [a, 'http://schema.org/SportsTeam']
      - ['http://www.w3.org/2000/01/rdf-schema#label', $(home_team)]
    source: dataset-source
    subject: https://data.opendatasoft.com/ld/resources/resultats-ligue-1@public/SoccerTeam/$(home_team)/
  match:
    predicateobjects:
      - [a, 'https://www.bbc.co.uk/ontologies/sport#terms_Match']
      - ['https://www.bbc.co.uk/ontologies/sport#terms_home_goal', $(home_goal), 'http://www.w3.org/2001/XMLSchema#integer']
      - ['https://www.bbc.co.uk/ontologies/sport#terms_away_goal', $(away_goal), 'http://www.w3.org/2001/XMLSchema#integer']
      - ['http://www.w3.org/2000/01/rdf-schema#label', $(home_team)-$(away_team)-$(start_date)-day$(name)]
      - ['https://www.bbc.co.uk/ontologies/sport#terms_awayCompetitor', awayTeam]
      - ['https://www.bbc.co.uk/ontologies/sport#terms_homeCopetitor', homeTeam]
      - ['https://www.bbc.co.uk/ontologies/sport#terms_isMatchOf', round]
    source: dataset-source
    subject: https://data.opendatasoft.com/ld/resources/resultats-ligue-1@public/SoccerMatch/$(home_team)-$(away_team)-$(start_date)/
  round:
    predicateobjects:
      - [a, 'https://www.bbc.co.uk/ontologies/sport#terms_Round']
      - ['http://www.w3.org/2000/01/rdf-schema#label', Ligue1 day $(name) $(start_date)-$(end_date)]
      - ['https://www.bbc.co.uk/ontologies/sport#terms_hasMatch', match]
      - ['http://dbpedia.org/ontology/startDate', $(start_date), 'http://www.w3.org/2001/XMLSchema#date']
      - ['http://dbpedia.org/ontology/endDate', $(end_date), 'http://www.w3.org/2001/XMLSchema#date']
    source: dataset-source
    subject: https://data.opendatasoft.com/ld/resources/resultats-ligue-1@public/LigueDay/$(name)-$(start_date)/
sources:
  dataset-source: [resultats-ligue-1@public.json~jsonpath, '$.records.[*].fields']'''
