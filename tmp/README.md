# Introduction

1. The results reported below was being trained from the Google Researh's NMT model. ([google-research NMT](https://github.com/tensorflow/nmt))
2. If you want to reproduce the results, please follow
```wrap
- Import conda env: conda env create -f tmp/papagomt.yaml
- Run train script: python -m nmt.nmt --attention=scaled_luong --src=source --tgt=target --vocab_prefix=tmp/papago_data/vocab  --train_prefix=tmp/papago_data/train --dev_prefix=tmp/papago_data/test --test_prefix=tmp/papago_data/test --out_dir=tmp/papago_nmt_attention_model --num_train_steps=12000 --steps_per_stats=100 --num_layers=2 --num_units=128 --dropout=0.2 --metrics=bleu
```

# Description
1. your experiment design (including baselines and models and/or data exploration results)
2. evaluation metrics
3. experimental results.
### 1. experiment design
- basic seq2seq model with attention mechanism is adopted. I used scaled luong attention.
- data distribution is as follows. (vocab size of target language is much larger than source's one.)
<img src="https://user-images.githubusercontent.com/45305396/115143305-7212eb80-a081-11eb-9f7e-0862ce6a8401.png"  width="320" height="240"> <img src="https://user-images.githubusercontent.com/45305396/115143306-73441880-a081-11eb-960d-52491d6a8dff.png"  width="320" height="240"> \
<img src="https://user-images.githubusercontent.com/45305396/115143300-6fb09180-a081-11eb-857d-1211b079e8a1.png"  width="320" height="240"> <img src="https://user-images.githubusercontent.com/45305396/115143301-717a5500-a081-11eb-85a8-12b801b56287.png"  width="320" height="240">


### 2. evaluation metric
- BLUE, PPL

<img src="https://user-images.githubusercontent.com/45305396/115143832-860c1c80-a084-11eb-81be-1fe4e5c6e92a.PNG"  width="320" height="240"> <img src="https://user-images.githubusercontent.com/45305396/115143834-87d5e000-a084-11eb-9447-669c50223f64.PNG"  width="320" height="240"> <img src="https://user-images.githubusercontent.com/45305396/115143835-89070d00-a084-11eb-95e2-4a357e01585b.PNG"  width="320" height="240">


### 3. experimental results
- best performance of test set can be reproduced from `tmp/papago_nmt_attention_model/translate.ckpt-9000`

Metric | Score | 
--- | :---: | 
BLUE | 88.2 |
PPL  | 1.36  |



```wrap
# Best bleu, step 9000 lr 1 step-time 0.14s wps 26.58K ppl 1.02 gN 1.14 dev ppl 1.36, dev bleu 88.2, test ppl 1.36, test bleu 88.2, Sun Apr 18 18:17:13 2021
```
