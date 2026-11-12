import requests

def check(resp,code):
    if resp.status_code != code:
       raise RuntimeError(f"状态码异常，期望:{code}，实际:{resp.status_code}")
    return resp