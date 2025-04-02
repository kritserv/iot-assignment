# iot-assignment

# Setup instructions

<ul>
  <li><a href="#1-run-directly-on-local-machine-">run directly on local machine 💻</a></li>
  <li><a href="#1-run-with-docker-">run with docker 🐳</li>
</ul>

## 1. Run Directly on Local Machine 💻

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

### backend

```
cd backend
```

```
docker build -t backend .
```

```
docker run -it -p 8000:8000 backend
```

```
http://localhost:8000
```

### frontend

```
cd frontend
```

```
docker build -t frontend .
```

```
docker run -it -p 8080:80 frontend
```

```
http://localhost:8080
```
