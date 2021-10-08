import requests

auth_token='c964678467cd53d0d79ca131f3463bba776d17d8'
hed = {'Authorization': 'token ' + auth_token}
data = {
            "nombre":"colmena_1",
            "local":"Wayllapampa",

            "t_int":17,
           
}

# data2 = {'id':"1", 
#             'Fecha':"Prueba4",
#             'Temperatura_Colmena_No_1':"3",
#             'Temperatura_Colmena_No_2':"3",
# }

urll = 'http://beeproject2021.pythonanywhere.com/add/data2/'
# url2 = 'http://beeproject2021.pythonanywhere.com/colmena2/'
# url3 = 'http://beeproject2021.pythonanywhere.com/colmena3/'
# urlno = 'http://beeproject2021.pythonanywhere.com/colmenaNo/'
response = requests.post(urll, json=data, headers=hed)
print(response)
print(response.json())
# response = requests.post(url2, json=data, headers=hed)
# print(response)
# print(response.json())
# response = requests.post(url3, json=data, headers=hed)
# print(response)
# print(response.json())
# response = requests.post(urlno, json=data2, headers=hed)
# print(response)
# print(response.json())