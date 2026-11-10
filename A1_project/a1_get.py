import requests,sys
def get(url):
    try:
        r = requests.get(url,timeout = 5)
        # 1. 拿到响应后，立刻检查状态码
        assert r.status_code == 200, f"请求失败,HTTP{r.status_code}"
        # 2. 把 JSON 转成字典
        data = r.json()
        # 3. 提取 star 数并打印
        print(data["stargazers_count"])
    except requests.exceptions.RequestException as e:
        print(f"网络连接异常：{e}，请检查网络")
        sys.exit(1)
    except AssertionError as e:
        print(e)
        sys.exit(1)
if __name__ == '__main__':
    url = 'https://api.github.com/repos/psf/requests'
    # url = 'https://api.github.com/repos/psf/this_repo_does_not_exist'
    get(url)