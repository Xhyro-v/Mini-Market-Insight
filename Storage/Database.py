import json
import os

class Database:
    def __init__(self, filename):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        storage_dir = os.path.join(base_dir, "Storage")
        self.filepath = os.path.join(storage_dir, f"{filename}.json")

        if not os.path.exists(self.filepath):
            with open(self.filepath, "w") as f:
                json.dump({}, f)

        self.data = self._load()

    def _load(self):
        with open(self.filepath, "r") as f:
            return json.load(f)

    def _save(self):
        with open(self.filepath, "w") as f:
            json.dump(self.data, f, indent=4)

    def get(self, key):
        return self.data.get(key)

    def insert(self, key, value):
        self.data[key] = value
        self._save()