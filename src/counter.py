class LineCounter:
    def __init__(self, line_y, class_map):
        self.line_y = line_y
        self.class_map = class_map
        self.counted_ids = set()
        self.counts = {name: 0 for name in class_map.values()}

    def update(self, tracks):
        for t in tracks:
            if len(t.history) < 2:
                continue

            prev_y = t.history[-2][1]
            curr_y = t.history[-1][1]

            if prev_y < self.line_y <= curr_y:
                if t.id not in self.counted_ids:
                    self.counts[t.cls] += 1
                    self.counted_ids.add(t.id)
