#!/bin/bash

# 환경 변수 설정
export FLASK_ENV=production
export FLASK_APP=run.py

# 데이터베이스 마이그레이션
flask db upgrade

# Gunicorn으로 서버 실행
gunicorn --config gunicorn_config.py run:app 