import json
import datetime as dt

# from backend.utils.get_features.generateMockData import get_date_boundaries
from generateMockData import generate_mock_data_naive, get_date_boundaries


def test():
    def load_data():
        with open("../get_test_data/eightMonthsData6313131.json", "r") as f:
            json_data = json.load(f)
        return json_data

    small_dataset = load_data()

    very_large_dataset = generate_mock_data_naive(small_dataset, num_of_years=10)

    assert len(very_large_dataset) / 96 == 3652

    start_date, end_date = get_date_boundaries(very_large_dataset)

    print(start_date)
    print(end_date)


if __name__ == "__main__":
    test()
