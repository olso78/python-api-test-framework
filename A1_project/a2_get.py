import requests,sys
from api.client import get
from common.assert_util import check

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
    except RuntimeError as e:
        print(f"校验失败: {e}")
        sys.exit(1)

