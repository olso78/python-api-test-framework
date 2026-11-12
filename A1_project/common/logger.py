import logging

# 调用basicConfig
logging.basicConfig(
    level=logging.INFO,
    # 修正参数名和字符串
    format = '%(asctime)s - %(levelname)s - %(message)s',
    handlers = [
        logging.FileHandler('run.log',encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)