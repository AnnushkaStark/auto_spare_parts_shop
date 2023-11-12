from suds.client import Client
import base64
user_login = 'v0rones88@yandex.ru'
user_pass = '123'

sample_encoded_login = user_login.encode("ascii") 
encoded_login = base64.b64encode(sample_encoded_login)

sample_encoded_pass = user_pass.encode("ascii") 
encoded_pass = base64.b64encode(sample_encoded_pass)



wsdl_url = 'https://services.allautoparts.ru/WEBService2/SearchService.svc/wsdl?wsdl'
service_url = 'https://services.allautoparts.ru/WEBService2/SearchService.svc'

client = Client(wsdl_url, location=service_url)


response = client.service.SearchOfferStep1('SessionInfo ParentID="39118" UserLogin={encoded_login} UserPass={encoded_pass}')


print(response)