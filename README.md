## Django Coding Challenge - Ip Rest Api

## Setup environment -

#### Clone or Download the repository
```bash
git clone https://github.com/shravanskp/ip_rest_api_test.git
cd ip_rest_api_test
```

#### Create virtual environment and activate
```bash
python -m venv env

source env/bin/activate 
```

#### Install Dependencies

```bash
pip install -r requirements.txt
```

#### Database Migrations

```bash
python manage.py makemigraations

python manage.py migrate
```

#### Now launch the server
```bash
python manage.py runserver
```

#### To run tests
```bash
python manage.py test
```


### Available Routes - 
| Ent-Point  | Method  |
|---|---|
| http://localhost:8000/api/ips/  | POST |
| http://localhost:8000/api/ips/  | GET  |
| http://localhost:8000/api/ips/{id}/  | GET  |
| http://localhost:8000/api/ips/{id}/acquire/  | PUT  |
| http://localhost:8000/api/ips/{id}/release/  | PUT  |
