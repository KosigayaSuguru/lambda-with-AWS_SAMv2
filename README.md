# lambda template with AWS SAM

## アプリケーションの配置について

### 機能別のコード

コントローラの位置づけに当たる層を、トップ(lambda_functions)/Function名（function1）/相対import対策(fn)/app.pyとする。  
app.py内で機能ごとに任意の関数を生成し、template.yaml内でハンドラとして指定する。  
機能ごとの固有のコード（再利用を意識しなくて良いコード）がある場合、この中に作成する。  

app.py内で相対importを使用できるようにするため、fnディレクトリを挟む。  

template.yamlのCodeUriに指定するのはこの階層にする。  
そのため、この階層にrequirements.txtを配置する必要があるが、中身は空にすること。  
ライブラリが必要となる場合、プロジェクトルートのrequirements.txtに記載する。  
※詳細は "共通ライブラリ" 参照

### ビジネスロジック、共通コード

ビジネスロジックは layer/python 以下に追加し、ビジネスロジック用のレイヤーとしてアップロードする。  
※なるべく再利用されることを考慮する。  
※サンプルでいうと、layer/python/service/hoge_service.py  

### 共通ライブラリ

`pip install` 対象である共通ライブラリは、venv内のライブラリ部分をライブラリ用のレイヤーとしてアップロードする。  

※手順
* Function毎のrequirement.txtに記載するのではなく、プロジェクトルートのrequirement.txtに記載し、`pip install -r requirement.txt` する。  
* インストールされたvenv内のsite-packages配下をレイヤーとしてアップロードする。  
* ハンドラとして呼び出されるpythonファイル（app.py）の先頭で、 `sys.path.append('/opt')` することで、アップロードしたライブラリ用レイヤーに対してパスを通す。

あまり綺麗なやり方ではないが、ライブラリ部分をレイヤーとして共通化することが可能になる。  
※Function毎のrequirement.txtに記載してアップロードすると下記が問題になる。  
* 同じライブラリを複数機能で使用する場合、それぞれでFunction毎にrequirement.txtのインストールをしていると時間がかかる。
* アップロードされるpythonのzipが巨大になるため、lambdaのコンソールから直接編集できなくなる。  

## 注意

CI/CDする場合、CI/CD用のビルドを行う環境で、 ↓を行うこと。
* venvの作成
* `pip install -r requirements.txt`

## 動作確認用コンテナ

```
cd docker
docker-compose up
docker-compose rm -fs
```

### MySQL

* ポート`33306`で待ち受け（一応、`docker-compose.yaml`内を参照）。
* `docker\mysql-init`内にDB初期化用のSQLを配置してある。
* 一回`docker-compose up`後、`mysql-local-data`内にMySQLのデータが保持される。

とりあえず中身が見たい時、↓でコンテナに入って、
```
docker exec -it docker_mysql_1 bash
```
コンテナ内で
```
mysql -u root -ppassword
```

## VSCode+Remote-SSHの設定方法

wiki 参照

## トラブルシューティング

### Linux上でMySQLアクセス時にエラーが出る場合

とりあえず↓を実行する。  
https://qiita.com/k_hoso/items/578503e10b2bbbcc9c1c

### Lambda上で動作させるためには

↓参照。  
https://qiita.com/k_hoso/items/6bab9eb288cba01cdb18

