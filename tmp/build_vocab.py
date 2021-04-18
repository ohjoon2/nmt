import os
import matplotlib.pyplot as plt


_ABS_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print('ABS_PATH: ', _ABS_PATH)
_X_DATA_PATH = _ABS_PATH + '/tmp/papago_data/{}.source'
_Y_DATA_PATH = _ABS_PATH + '/tmp/papago_data/{}.target'

_DEFAULT_TOKEN = ['<unk>', '<s>', '</s>']

splits = ['train', 'test']

def word_count(splits):
    x_data_distribution = {'train': {}, 'test': {}}
    y_data_distribution = {'train': {}, 'test': {}}
    for split in splits:
        x_data_path = _X_DATA_PATH.format(split)
        y_data_path = _Y_DATA_PATH.format(split)

        print('x_data_path: ', x_data_path)
        print('y_data_path: ', y_data_path)

        with open(x_data_path, 'r') as x_f:
            datas = x_f.readlines()
            for data in datas:
                sentence = data.split()
                for word in sentence:
                    if word not in x_data_distribution[split].keys():
                        x_data_distribution[split][word] = 1
                    else:
                        x_data_distribution[split][word] += 1

        with open(y_data_path, 'r') as y_f:
            datas = y_f.readlines()
            for data in datas:
                sentence = data.split()
                for word in sentence:
                    if word not in y_data_distribution[split].keys():
                        y_data_distribution[split][word] = 1
                    else:
                        y_data_distribution[split][word] += 1

    return x_data_distribution, y_data_distribution


def draw_word_distribution(**kwargs):
    for split in splits:
        bars = []
        x_data = kwargs['input_data'][split]
        y_data = kwargs['label_data'][split]

        print(f'{split} input data words: ', len(x_data))
        print(f'{split} label data words: ', len(y_data))

        x_keys = x_data.keys()
        x_values = x_data.values()

        y_keys = y_data.keys()
        y_values = y_data.values()

        bars.append([x_keys, x_values, 'train', len(x_keys)])
        bars.append([y_keys, y_values, 'test', len(y_keys)])

        for bar in bars:
            plt.bar(bar[0], bar[1])
            plt.title(f'{split}-{bar[2]} word frequency (#words: {bar[3]})')
            plt.show()


x_data, y_data = word_count(splits=splits)  # x_data: {'train': {1:153, 2:243, id: frequency}, 'test': {...}}

with open(_ABS_PATH + '/tmp/papago_data/vocab.source', 'w') as f_source:
    x = x_data['train']
    y = y_data['train']
    words = list(set(list(x.keys()) + list(y.keys())))
    words = _DEFAULT_TOKEN + words
    for w in list(words):
        f_source.write(w + '\n')

with open(_ABS_PATH + '/tmp/papago_data/vocab.target', 'w') as f_target:
    x = x_data['test']
    y = y_data['test']
    words = list(set(list(x.keys()) + list(y.keys())))
    words = _DEFAULT_TOKEN + words
    for w in list(words):
        f_target.write(w + '\n')






# draw_word_distribution(input_data=x_data, label_data=y_data)  # for 'train/test' data analysis
