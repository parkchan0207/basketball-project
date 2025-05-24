#!/usr/bin/env bash
set -e

# Python 버전 확인
python --version

# 기존 venv 제거 (있다면)
rm -rf venv

# 파이썬 가상환경 생성
python -m venv venv

# 가상환경 활성화
. venv/bin/activate

# pip 업그레이드
pip install --upgrade pip

# 의존성 설치
pip install -r requirements.txt

# 환경 변수 설정
export FLASK_APP=run.py
export FLASK_ENV=production

# 데이터베이스 디렉토리 확인
mkdir -p migrations

# 데이터베이스 초기화 및 마이그레이션
flask db init || true
flask db migrate
flask db upgrade 