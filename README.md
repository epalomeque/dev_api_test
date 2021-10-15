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
### Obtener resultados de la prueba "customer order status"
    GET /api/v1/customers
#### Request
    curl -i -H 'Accept: application/json' http://localhost:8000/api/v1/customers
#### Response
    HTTP/1.1 200 OK
    Date: Fri, 15 Oct 2021 11:36:16 GMT
    Server: WSGIServer/0.2 CPython/3.9.7
    Content-Type: application/json
    Vary: Accept, Cookie
    Allow: GET, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 191
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    
    [{"order_number":"ORD_1567","status":"PENDING"},{"order_number":"ORD_1234","status":"SHIPPED"},{"order_number":"ORD_9834","status":"SHIPPED"},{"order_number":"ORD_7654","status":"CANCELLED"}]


### Obtener resultados de la prueba "seasons problem"
    GET /api/v1/seasons
#### Request
    curl -i -H 'Accept: application/json' http://localhost:8000/api/v1/seasons
#### Response
    HTTP/1.1 200 OK
    Date: Fri, 15 Oct 2021 11:38:40 GMT
    Server: WSGIServer/0.2 CPython/3.9.7
    Content-Type: application/json
    Vary: Accept, Cookie
    Allow: GET, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 401
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    
    [{"ORD_ID":"113-8909896-6940269","SEASON":"Fall"},{"ORD_ID":"114-0291773-7262677","SEASON":"Winter"},{"ORD_ID":"114-0291773-7262697","SEASON":"Fall"},{"ORD_ID":"114-9900513-7761000","SEASON":"Fall"},{"ORD_ID":"112-5230502-8173028","SEASON":"Winter"},{"ORD_ID":"112-7714081-3300254","SEASON":"Spring"},{"ORD_ID":"114-5384551-1465853","SEASON":"Spring"},{"ORD_ID":"114-7232801-4607440","SEASON":"Fall"}]
    
### Obtener resultados de la prueba "detecting change"
    GET /api/v1/changes
#### Request
    curl -i -H 'Accept: application/json' http://localhost:8000/api/v1/changes
#### Response
    HTTP/1.1 200 OK
    Date: Fri, 15 Oct 2021 11:40:59 GMT
    Server: WSGIServer/0.2 CPython/3.9.7
    Content-Type: application/json
    Vary: Accept, Cookie
    Allow: GET, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 115
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    
    [{"dates":"01/02/20","was_rainy":true},{"dates":"01/06/20","was_rainy":true},{"dates":"01/08/20","was_rainy":true}]
    
## Modificar los datos de entrada de las pruebas
Cada módulo contiene en el archivo views.py una funcion llamada "gen_dataset" que es la encargada de generar 
el dataframe correspondiente para cada prueba,  
