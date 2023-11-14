from suds.client import Client
import base64
user_login = 'v0rones88@yandex.ru'
user_pass = '123'

sample_encoded_login = user_login.encode("ascii") 
encoded_login = str(base64.b64encode(sample_encoded_login))[2: -1]

sample_encoded_pass = user_pass.encode("ascii") 
encoded_pass = str(base64.b64encode(sample_encoded_pass))[2: -1]


wsdl_url = 'https://services.allautoparts.ru/WEBService2/SearchService.svc/wsdl?wsdl'
service_url = 'https://services.allautoparts.ru/WEBService2/SearchService.svc'
wsdl_ip = 'https://services.allautoparts.ru/WEBService2/SupportService.svc/wsdl?wsdl'
service_ip = 'https://services.allautoparts.ru/WebService2/SupportService.svc'


client = Client(wsdl_url, location=service_url)
client_ip = Client(wsdl_ip, location=service_ip)

response = client.service.SearchOfferStep1(f'''<root> <SessionInfo ParentID="39118" UserLogin="{encoded_login}" UserPass="{encoded_pass}" /> <Search> <Key>SP-1004</Key> </Search> </root>''')
#response_ip = client_ip.service.GetRequestIP()


print(response)
