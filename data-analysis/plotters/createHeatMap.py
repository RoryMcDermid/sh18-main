import matplotlib.pyplot as plt

def create_heatmap(dataset):
    plt.imshow(dataset, cmap='hot')
    plt.title('Heatmap of Transport Matrix')
    plt.xlabel('target indexes')
    plt.ylabel('source indexes')
    plt.show()