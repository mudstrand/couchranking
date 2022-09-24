"# couchranking" 

from the couchraning/app directory run;

uvicorn main:app --host 0.0.0.0 --port 8000

use conda for the environment

installing modules
fastapi -> conda install -c conda-forge fastapi
uvicorn -> conda install -c conda-forge uvicorn
psycopg -> conda install psycopg2
pygresql -> conda install pygresql

mariadb -> from the conda env (couchranking) run -- pip install mariadb
psycopg-binary -> from the conda env (couchranking) run -- pip install psycopg2

Run omdb via curl
# search for one by title
curl -H "Content-Type: application/json"  http://www.omdbapi.com/\?t\=Breaking\&apikey\=<APIKEY> | jq
# search for many by title
curl -H "Content-Type: application/json"  http://www.omdbapi.com/\?s\=Breaking\&apikey\=<APIKEY>

Hitting couchranking with curl -> using jq to count the response
 curl -s http://192.168.50.4:8000/media/search/Breaking%20Bad | jq '.Search | length'