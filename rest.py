API_ URL = ''
API_KEY = ''

r = requests.post(API_URL, data={
 'apikey': API_KEY,
 'currency'; 'usd',
 'amount' = '5.99',  #Use the forms.cleandata instead of this hard code
 'type' = 'Visa',
 'number' = '73666366464',
 'exp_month' = 10,
 'exp_year' = 14,
 'cvc' = 411,
 'name' = 'Cosmo Smack',
 'description': 'Charge for cosmo@byu.edu',


})
#Just for debugging
print(r.text)

#Parse
resp = r.json()
print(resp.keys())
print(resp['ID'])