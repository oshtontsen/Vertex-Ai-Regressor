from utils.train import train
from utils.preprocess import preprocess
from utils.save import save_model


def main():
    # Test csv
    data_path = 'data/melb_data.csv'
    df = preprocess(data_path)
    # TODO: Test json
    # data_path = 'data/sample_input.json'
    df = preprocess(data_path, 'json')
    model = train(df)
    save_model(model)


if __name__ == "__main__":
    main()