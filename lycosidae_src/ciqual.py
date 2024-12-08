# Web scraping
from requests import post
# Custom data models
from ciqual_models    import payloadSearch, payloadQuery, ciqualDico
from nutrition_models import aliment
# Database manager
from minio   import Minio
from urllib3 import PoolManager
import pickle, io
# Load environment variables from the .env file
from dotenv import load_dotenv
import os
load_dotenv()

## Connect to database
## -------------------
httpClient = PoolManager(
                cert_reqs = 'CERT_REQUIRED',
                ca_certs  = os.getenv("CA_CERTS_PATH")
)
client = Minio(
	endpoint    = os.getenv("MINIO_URL"),
    access_key  = os.getenv("ACCESS_KEY"),   
    secret_key  = os.getenv("SECRET_KEY"),
	secure      = True,
	http_client = httpClient
)

client.list_buckets()
bucket_name = "ciqual"

## NOT RUN
## Iterate over each object and remove it
# objects = client.list_objects(bucket_name, recursive=True) # List objects in the bucket (using recursive to get all objects)
# for obj in objects:
# 	client.remove_object(bucket_name, obj.object_name)
# 	print(f"Object {obj.object_name} deleted successfully.")
# client.remove_bucket(bucket_name)

## Rebuild the bucket if necessary
found = client.bucket_exists(bucket_name)
if not found:
	client.make_bucket(bucket_name)

## Loop over a list of search terms
## --------------------------------
from ciqual_models import fruits, legumes, viandes, huiles, laitages, graisses, noix, fruitsdemer, boissons, processed_food
keywordList = fruits + legumes + viandes + huiles +laitages + graisses + noix + fruitsdemer + boissons + processed_food
for keyword in keywordList :

	# Loop over all aliments linked to the keyword 
	searchResponse = post('https://ciqual.anses.fr/esearch/aliments/_search', json=payloadSearch(keyword).json, timeout=500)
	results = searchResponse.json()["hits"]["hits"]
	for i in range(len(results)):

		alimentCode = results[i]["_source"]["code"]
		queryResponse = post('https://ciqual.anses.fr/esearch/aliments/_search', json=payloadQuery(alimentCode).json)
		food = aliment(results[i]["_source"]["nomFr"])

		# Check if that food already exists, add it otherwise
		objects = client.list_objects(bucket_name, prefix=food.name, recursive=True)
		print(food.name)
		if not any(obj.object_name == food.name for obj in objects): #food.name is not part of ciqual objects
			

			# Loop over fields in returned response
			n = len(queryResponse.json()["hits"]["hits"][0]["_source"]["compos"]) # 0 because there should always be only one "hits" since I used the aliment code
			for j in range(n):
				name  = queryResponse.json()["hits"]["hits"][0]["_source"]["compos"][j]["constNomFr"]
				value = queryResponse.json()["hits"]["hits"][0]["_source"]["compos"][j]["compoTeneur"]
				# Turn value into float (text, french formatted numbers into strings, etc...)
				value = float(value.replace(",",".").replace("<","").replace("traces","0"))
				# Map the found field with the custom data model  
				key = ciqualDico(name)
				if key != "":
					food.deep_set(key,value)

			# Save the object (as pickle) to Minio bucket
			bytes_file = pickle.dumps(food)
			client.put_object(
				bucket_name = bucket_name,
				object_name = food.name,
				data        = io.BytesIO(bytes_file),
				length      = len(bytes_file)
			)

## NOT RUN
# Example to read one object		
# food = pickle.loads(client.get_object(bucket_name=bucket_name,object_name="Avocat, pulpe, cru").read())
# food.json