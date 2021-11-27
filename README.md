# About

Hyperion is a SAAS app that enables to get super basic Open-source intelligence (OSINT) regard to specific domain name.   
That achieved buy  querying publicly available data sources such as whois, DNS data etc.

This project was not created with the purpose of being the next state-of-the-art OSINT system, that done only 
because I have needed a SAAS app with some logic, especially I/O operations. 
I have created this project for learning purposes with the fields of best practices while using some popular Python and
JavaScript frameworks:
  - Flask
  - Celery
  - VueJS

This project main focus is dealing with architectural and design aspects of a maintainable and efficient SAAS app using
the above frameworks. For example, some concepts being demonstrated here:
  - VueJS Components
  - Flask BluePrints 
       
### Run Project Services
**Flask Server**  
install hyperion_blueprints package
install hyperion_backend package  
python -m hyperion_backend  
  
**Celery Worker**  
install hyperion_backend package
install hyperion_worker package  
celery -A hyperion_worker.celery_worker.celery_app worker --loglevel=info -c 1 -P solo  

**Frontend (NodeJS)**  
npm install
npm run serve  

### Debug Project Services (Using PyCharm)  
**Flask server**  
Install the package.  
Debug as module (module name: hyperion_backend).  

**Celery Worker**  
Install the package.  
Debug as module
  - module name: celery.
  - parameters: -A hyperion_worker.celery_worker.celery_app worker --loglevel=info -c 1 -P solo
  - working directory: <YOUR-LOCAL-PATH-TO-PROJECT-DIRECTORY>\hyperion\backend\hyperion_worker   