### 환경 구축 방법

1. git clone
```
https://github.com/Mactto/SqlAlchemy-join-example.git
```

2. create venv
```
create your virtual env for install librarys
```
  
3. install requirements
```
pip install -r requirements.txt
```

4. database url setting
```
cp .env.example .env

// and fill your database url
```

5. 

4. database initialize
```
// after create your database

alembic upgrade head
```

5. data initialize
```
python -m scripts.create_data
```

Setting is Complete
