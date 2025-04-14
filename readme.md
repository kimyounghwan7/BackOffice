# Back Office Solution

```
- 간단한 업무 보조 및 보고서 제출 기능
- 업로드 이미지 및 자료는 수동 태그 기능을 통한 검색 기능
```

## Code Conventions

```
code 작성 시 에러를 줄이고 일관성 유지를 위해 업계 표준으로 적용.
vscode를 통해서 협업하는 것을 기준으로 세팅.
vscode가 아니라 다른 idle에 경우 .vscode 디렉토리를 전부 지우고 세팅.
```

- ## python
  ```
  작업 환경에 설치.
  docker를 통해 container 내부에서 작업 시 container 내부에 세팅.
  Host pc에서 작업 시 Local에 세팅.
  1. pip install black isort ruff mypy
  2. vscode 사용 시 ruff, black formatter 설치
  3. 하단 json file 생성.
  ```
- ## Typescript
  ```
  1. npm install
  2. 작동으로 적용됨.
  ```

## Backend

- ## Django, Django Rest

  ```
  1.backend web project init
  docker-compose -f .\docker-compose-dev.yml run bo_backend django-admin startproject config .

  2.django build
  docker-compose -f .\docker-compose-dev.yml run bo_backend python manage.py collectstatic --noinput

  3.배포시 command 변경
  gunicorn config.asgi:application --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

  4.apps에 app 추가시 backend/apps/{app_name} 디렉토리 생성 후 아래 명령어 실행.
  docker-compose -f .\docker-compose-dev.yml run bo_backend python manage.py startapp {app_name} apps/{app_name}
  ```

- ## App List
  ```
  core
  users
  report
  announcement
  archive
  ```

## Frontend

- ## Nextjs + Typescript

  ```
  1. node_module install
  docker-compose -f .\docker-compose-dev.yml run bo_frontend npm install --force --legacy-peer-deps

  2. shadcn components init & add
  docker-compose -f .\docker-compose-dev.yml run bo_frontend npx shadcn@latest init
  docker-compose -f .\docker-compose-dev.yml run bo_frontend npx shadcn@latest add {componentName}
  componentNames: button, form, card
  ```

## Ai engine

- ## Fast-api + M-Clip-model + weaviate (Vector-DB)

  ```

  ```

## DB + No-sql DB

- ## PostgresDB (subabase), Redis

  ```

  ```
