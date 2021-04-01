# Polyomino Solver
ポリオミノの箱詰めパズルを Fixstars Amplify で解くプログラム．

事前に Fixstars Amplify のアカウント登録とアクセストークンの取得が必要．

## Requirement

- Python 3.9

## 実行方法

1. アクセストークンを入力する
```sh
echo "TOKEN=access_token" > .env
```

2. パッケージをインストールする
```sh
pip install -r requirements.txt
```

3. プログラムを実行する
```
python -m psolver sample1.toml
```

## 実行結果

```
$ python -m psolver sample1.toml
┏━━━┳━━━┓
┃ ┏━┻━┓ ┃
┣━┛ ┏━┫ ┃
┃ ┏━┛ ┗━┫
┗━┻━━━━━┛
```

## 提出前チェック


- [x] README.mdの手順通りにして、プログラムが実行できる
- [x] 説明用スライドを用意した 
- [x] アクセストークンはリポジトリに含まれていない
- [x] MIT Licenseにした
