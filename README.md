# chocolate-puzzle-solver
[明治ミルクチョコレートパズル](https://www.hanayamatoys.co.jp/product/category/puzzle/meiji/meiji-milk.html)及びポリオミノの箱詰めパズルを Fixstars Amplify で解くプログラム．

事前に Fixstars Amplify のアカウント登録とアクセストークンの取得が必要．

## Requirement
- Python 3.9

## Usage
```sh
echo "TOKEN=access_token" > .env
pip install -r requirements.txt
python -m cpsolver sample.toml
```

