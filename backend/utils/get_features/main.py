from generateMockData import generate_mock_data_naive


def test():
    def load_data():
        pass

    small_dataset = load_data()

    large_dataset = generate_mock_data_naive(small_dataset)


if __name__ == "__main__":
    test()
