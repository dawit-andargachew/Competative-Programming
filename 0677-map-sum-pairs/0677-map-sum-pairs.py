class MapSum:

    def __init__(self):
        self.words = {}
    
    def insert(self, key: str, val: int) -> None:
        self.words[key] = val
        
    def sum(self, prefix: str) -> int:
        total = 0

        for k,v in self.words.items():
            if k[:len(prefix)] == prefix:
                total += v
        return total