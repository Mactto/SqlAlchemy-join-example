### Relate Post
[Python에서 N+1을 해결하는 방법](https://mactto.tistory.com/entry/Python%EC%97%90%EC%84%9C-N1%EC%9D%84-%ED%95%B4%EA%B2%B0%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95-SQLAlchemy)
  
  
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
