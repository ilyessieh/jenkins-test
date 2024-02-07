import os
import httpx

CAST_SERVICE_HOST_URL = 'http://localhost:8002/api/v1/casts/'
CAST_SERVICE_HOST_URL2 = 'http://cast_service:8000/api/v1/casts/'

def is_cast_present(cast_id: int):
    url = CAST_SERVICE_HOST_URL2 or CAST_SERVICE_HOST_URL
    r = httpx.get(f'{url}{cast_id}')
    return True if r.status_code == 200 else False