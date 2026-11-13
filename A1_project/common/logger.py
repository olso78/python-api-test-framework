import logging
from pathlib import Path
# 定位到 A1_project/reports/run.log
LOG = Path(__file__).parent.parent / "reports" / "run.log"
# 如果 reports 文件夹不存在，自动创建（parents=True 可连建多级，exist_ok=True 防报错）
LOG.parent.mkdir(parents=True,exist_ok=True)
# 调用basicConfig
logging.basicConfig(
    level=logging.INFO,
    # 修正参数名和字符串
    format = '%(asctime)s - %(levelname)s - %(message)s',
    handlers = [
        logging.FileHandler(LOG,encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)