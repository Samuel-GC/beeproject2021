import requests

auth_token='bd24c48c4bf0ac3aab420d328d91f804b9e82a0b'
hed = {'Authorization': 'token ' + auth_token}
data = {'id':"1", 
            'Fecha':"Prueba4",
            'Clima':"Prueba4",
            'Temperatura_Ext':"3",
            'Temperatura':"3",
            'Humedad':"3" ,
            'Peso':"3",
            'Poblacion':"3",
            'Comida':"3",
            'Piquera':"Prueba3",
            'Reina':"Prueba3",
            'Revision':"Prueba3",
}

data2 = {'id':"1", 
            'Fecha':"Prueba4",
            'Temperatura_Colmena_No_1':"3",
            'Temperatura_Colmena_No_2':"3",
}

urll = 'http://beeproject2021.pythonanywhere.com/colmena1/'
url2 = 'http://beeproject2021.pythonanywhere.com/colmena2/'
url3 = 'http://beeproject2021.pythonanywhere.com/colmena3/'
urlno = 'http://beeproject2021.pythonanywhere.com/colmenaNo/'
response = requests.post(urll, json=data, headers=hed)
print(response)
print(response.json())
response = requests.post(url2, json=data, headers=hed)
print(response)
print(response.json())
response = requests.post(url3, json=data, headers=hed)
print(response)
print(response.json())
response = requests.post(urlno, json=data2, headers=hed)
print(response)
print(response.json())