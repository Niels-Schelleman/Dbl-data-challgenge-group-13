class FrameConcat:

    def __init__(self, doubleframe):
        self.frames = doubleframe

    def concatinator(self):
        concatframes = []
        for i in range(2):
            Rep = self.frames[i]
            concatframes.append(pandas.concat(Rep, ignore_index=True))
        return concatframes
