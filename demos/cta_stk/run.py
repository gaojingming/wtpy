from wtpy import WtEngine,EngineType

import sys
sys.path.append('../Strategies')
from DualThrust import StraDualThrust

if __name__ == "__main__":
    #创建一个运行环境，并加入策略
    engine = WtEngine(EngineType.ET_CTA)
    engine.init('../common/', "config.yaml", commfile="stk_comms.json", contractfile="stocks.json")
    
    straInfo = StraDualThrust(name='pydt_SH600000', code="SSE.STK.600000", barCnt=50, period="d1", days=30, k1=0.1, k2=0.1, isForStk=True)
    engine.add_cta_strategy(straInfo)
    
    engine.run()

    kw = input('press any key to exit\n')