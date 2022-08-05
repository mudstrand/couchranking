"# couchranking" 

from the couchraning/app directory run;

uvicorn main:app --host 0.0.0.0 --port 8000

use conda for the environment

installing modules
fastapi -> conda install -c conda-forge fastapi
uvicorn -> conda install -c conda-forge uvicorn
mariadb -> from the conda env (couchranking) run -- pip instal mariadb