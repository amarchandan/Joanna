import requests

res = requests.get("https://rembelapi.omx.pw/api/api1.php?lista=4054285027493885|12|2023|938")
print(res.text)