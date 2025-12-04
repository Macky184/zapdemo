# zapdemo - ZAPで「フォーム認証＋セッション管理」を実践するための最小Webアプリ

本リポジトリは、OWASP ZAPの認証・セッション管理の学習のためのWebアプリです。反射型クロスサイトスクリプティングとサーバサイドテンプレートインジェクション脆弱性を意図的に用意しています。

# 動作環境
- Docker (推奨：Docker Desktop)

Pythonやpipをインストール必要はありません。

# 起動方法
本リポジトリのフォルダへ移動します。
```
cd zapdemo
```
次に、Dockerイメージをビルドします。
```
docker build -t zapdemo .
```
終わったら、コンテナを起動してください。
```
docker run --name zapdemo-container -p 5000:5000 zapdemo
```
起動後、ブラウザで以下にアクセスできます。
http://localhost:5000/login
停止したい時は以下を行なってください。
```
docker stop zapdemo-container
```

# テストユーザー
一般ユーザー
ユーザー名：user
パスワード：userpass
管理者ユーザー
ユーザー名：admin
パスワード：adminpass