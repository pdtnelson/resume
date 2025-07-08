# Resume Application
A Vue 3 and FastAPI based application for hosting a resume and a personal blog. Allows for the user to create 
customized profiles and resumes for specific job opportunities. 

## Project Setup
### Frontend 
```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Type-Check, Compile and Minify for Production

```sh
npm run build
```

### Lint with [ESLint](https://eslint.org/)

```sh
npm run lint
```

## Backend
```sh
pip install -r requirements.txt
```

### Add required variables to .env
```
MONGO_CONN_STR=mongodb://user:pass@127.0.0.1:27017
MONGO_DATABASE=resume-db
JWT_SECRET=super_secret_secret
```

### Start the local database container
```sh
docker-compose up -d
```

### Run the backend via cli
```sh
fastapi dev main.py
```
