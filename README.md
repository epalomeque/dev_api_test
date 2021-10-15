# DEV_API_TEST

Prueba de desarrollo de software sobre python

## Requerimientos
    - Python 3.9
    - Probado unicamente en plataforma Linux

## Instalar 
    $ git clone https://github.com/epalomeque/dev_api_test.git
    $ cd dev_api_test 
    $ pip install -r requirements.txt
    $ python manage.py makemigrations
    $ python manage.py migrate

## Ejecutar
    $ python manage.py runserver 0.0.0.0:8000    

## Descripción de las APIS
    # Obtener resultados de la prueba "customer order status" 
    GET /api/v1/customers

    # Obtener resultados de la prueba "seasons problem"
    GET /api/v1/seasons
    
    # Obtener resultados de la prueba "detecting change"
    GET /api/v1/changes
    
## Modificar los datos de entrada de las pruebas
Cada módulo contiene en el archivo views.py una funcion llamada "gen_dataset" que es la encargada de generar 
el dataframe correspondiente para cada prueba,  
