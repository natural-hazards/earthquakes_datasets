import pickle

if __name__ == '__main__':

    fn = 'data/okc/hh/hh_selected.pkl'

    with open(fn, 'rb') as file:
        ds = pickle.load(file)

        lst_waveforms = ds[0]
        np_labels = ds[1]

        print(f'#waveforms {len(lst_waveforms)}')
        print(f'#labels {len(np_labels)}')

