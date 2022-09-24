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