from torch.utils.data import DataLoader
def make_dataloader(dataset):
    return DataLoader(dataset = dataset, batch_size = 16, shuffle = True)