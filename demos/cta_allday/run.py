from wtpy import WtEngine,EngineType

import sys
sys.path.append('../Strategies')
from DualThrust import StraDualThrust

class MyExecuter(BaseExtExecuter):
    def __init__(self, id: str, scale: float):
        super().__init__(id, scale)

    def init(self):
        print("inited")

    def set_position(self, stdCode: str, targetPos: float):
        print("position confirmed: %s -> %f " % (stdCode, targetPos))


if __name__ == "__main__":
    #创建一个运行环境，并加入策略
    env = WtEngine(EngineType.ET_CTA)
    env.init('./common/', "config.yaml", 
        contractfile="okex_tickers.json",
        sessionfile="btc_sessions.json",
        commfile=None,holidayfile=None,hotfile=None,secondfile=None)
    
    straInfo = StraDualThrust(name='pydt_okex', code="OKEX.BTC-USDT", barCnt=50, period="m1", days=30, k1=0.2, k2=0.2, isForStk=False)
    env.add_cta_strategy(straInfo)

    # 注册外部执行器
    myExecuter = MyExecuter('exec', 1)
    engine.add_exetended_executer(myExecuter)

    env.run()

    kw = input('press any key to exit\n')