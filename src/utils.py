import yaml, time

def load_yaml(path):
    with open(path,"r") as f:
        return yaml.safe_load(f)

class FPS:
    def __init__(self):
        self.t0 = time.time()
        self.n = 0

    def update(self):
        self.n += 1
        if self.n % 30 == 0:
            fps = self.n / (time.time()-self.t0)
            print(f"FPS: {fps:.2f}")
