### Run Project Services
**Flask Server**  
python -m hyperion_backend  
  
**Celery Worker**  
celery -A hyperion_backend.celery_worker.celery_app worker --loglevel=info -c 1 -P solo  

**Frontend (NodeJS)**  
npm run serve  

### Debug Project Services (Using PyCharm)  
**Flask server**  
Install the package hyperion_backend.  
Debug as module (check "backend.hyperion_backend" as module name).  

**Celery Worker**
Create a new debug profile of type shell.  
Set script path to "celery".  
Set the script options to "-A backend.hyperion_backend.celery_worker.celery_app worker --loglevel=info -c 1 -P solo"
Set the working directory to the main project directory ("hyperion").  