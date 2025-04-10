# Back Office Solution
```
- 간단한 업무 보조 및 보고서 제출 기능
- 업로드 이미지 및 자료는 수동 태그 기능을 통한 검색 기능
```

## Code Conventions
```
code 작성 시 에러를 줄이고 일관성 유지를 위해 업계 표준으로 적용.
```
* ## python
	```
	1. pip install black isort ruff mypy pre-commit
	2. vscode 사용 시 ruff, black formatter 설치
	3. 하단 json file 생성.
	```
	```
	{
		"python.formatting.provider": "black",
		"python.formatting.blackArgs": ["--line-length", "88"],
		"editor.formatOnSave": true,

		"python.linting.enabled": true,
		"python.linting.ruffEnabled": true,
		"python.linting.mypyEnabled": true,

		"python.analysis.typeCheckingMode": "strict",
		"editor.codeActionsOnSave": {
			"source.organizeImports": true
		}
	}
	```

## Backend
```
Django
Django Rest
```

## frontend
```
nextjs
typescript
```

## Ai engine
```
Fast-api
Clip-model
weaviate (Vector-DB)
```

## DB + No-sql DB
```
PostgresDB (subabase)
Redis
```