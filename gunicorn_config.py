import multiprocessing
import os

# 워커 프로세스 수 설정
workers = multiprocessing.cpu_count() * 2 + 1

# 워커 클래스 설정
worker_class = 'sync'

# 타임아웃 설정
timeout = 120

# 바인딩할 주소와 포트
bind = f"0.0.0.0:{os.environ.get('PORT', '8080')}"

# 액세스 로그 설정
accesslog = '-'
errorlog = '-'

# 워커 타임아웃 설정
graceful_timeout = 120

# 최대 요청 수 설정
max_requests = 1000
max_requests_jitter = 50

# 프리로드 설정
preload_app = True 