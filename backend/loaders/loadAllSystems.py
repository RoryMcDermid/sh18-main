import json
from typing import List

def load_systems_from_file() -> List[int]:
    with open('data/all_systems.json', 'r') as f:
        all_systems = json.load(f)
    system_IDs = [int(system_id) for system_id in all_systems.keys()]
    return system_IDs

