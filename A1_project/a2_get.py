import requests,sys
def get(url):
    try:
        r = requests.get(url,timeout=5)
        return r
    except requests.RequestException as e:  # 只捕网络层
        print(f"网络异常：{e}")
        sys.exit(1)

def check(resp,code):
    if resp.status_code != code:
       raise RuntimeError(f"状态码异常，期望:{code}，实际:{resp.status_code}")
    return resp
if __name__ == '__main__':
    url = 'https://api.github.com/repos/psf/requests'
    url_404 = 'https://api.github.com/repos/psf/this_repo_does_not_exist'
    try:
        r = get(url)
        data = check(r,200).json()
        print(data['stargazers_count'])
        r2 = get(url_404)
        data = check(r2, 404).json()
        print("预期的 404 校验成功，接口正常报错")
    except Exception as e:
        print(e)
        sys.exit(1)

