**FastApi_Botiga**

Api rest amb fastapi de una botiga

# Pràctica: Fastapi
La pràctica consistia en dues parts:
        
        CRUD
        Carga massiva des d'un arxiu .csv

A la primera part s'havia de fer un conjunt de mètodes amb els seus 'Endpoints' i les seves rutes per poder provar el mètodes des del "Swagger" (també es pot fer des del propi navegador).

Només tenien crides als mètodes on és desenvolupava la lògica de la consulta i un 'return' amb format diccionari.

Dins la clase 'botifa_db' es feia tota la lògica, tipus de consultas i relacions entre mètodes de manera modular.

Cada mètode obre, actualitza (si és necessari) i tanca la connexió a la base de dades.

Aqui tenim un conjunt de consultes per comprobar el funcionament de la Api rest 'Fastapi'.