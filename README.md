# iot-assignment

# Setup instructions

<ul>
  <li><a href="#1-run-directly-on-local-machine-">run directly on local machine 💻</a></li>
  <li><a href="#2-run-with-docker-">run with docker 🐳</a></li>
</ul>

## 1. Run Directly on Local Machine 💻

(recommend)

<ul>
    <li>Use Python version 3.9 up</li>
    <li>Use virtualenv</li>
</ul>

### backend

```
cd backend
```

```
pip install -r requirements.txt
```

```
py manage.py migrate
```

```
py manage.py runserver
```

```
http://localhost:8000
```

### frontend

```
cd frontend
```

```
npm install
```

```
npm run serve
```

```
http://localhost:8080
```

## 2. Run with Docker 🐳

```
docker-compose up -d
```

### backend

```
http://localhost:8000
```

### frontend

```
http://localhost:8080
```
