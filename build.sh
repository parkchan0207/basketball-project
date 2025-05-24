#!/bin/bash
# 파이썬 가상환경 생성
python -m venv venv

# 가상환경 활성화
source venv/bin/activate

# 의존성 설치
pip install -r requirements.txt

# 데이터베이스 마이그레이션
flask db upgrade 