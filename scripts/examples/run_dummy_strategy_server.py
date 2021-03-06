from gekkopy.serving import Strategy, StratServer
import numpy as np


class DummyStrategy(Strategy):
    """ Strategy that creates random advice, just to demo how to implement the
    interface. """

    def __init__(self):
        super().__init__()

    def window_size(self):
        return 5

    def advice(self, data):
        cond = np.ceil(np.sum(data)) % 3
        if cond == 1:
            return self.LONG
        elif cond == 2:
            return self.SHORT
        else:
            return self.HOLD


if __name__ == "__main__":
    dummy_strat = DummyStrategy()
    StratServer.register("dummy", dummy_strat)
    StratServer.start('localhost', port=2626, debug=True)
