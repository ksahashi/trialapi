# ECRにpush

## リポジトリ作成

マネコンもしくはCLIで作って確認

## プッシュコマンド実行

マネコンで ECR のリポジトリ名リンクからイメージに入って [プッシュコマンドを表示] すると以下のようにしないさいと表示される

> 次の手順を使用して、リポジトリに対してイメージを認証し、プッシュします。Amazon ECR 認証情報ヘルパーなどの追加のレジストリ認証方法については、レジストリの認証 を参照してください。
> 認証トークンを取得し、レジストリに対して Docker クライアントを認証します。AWS CLI を使用してください:

`aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 045224308799.dkr.ecr.us-east-1.amazonaws.com`

> 注意: AWS CLI の使用中にエラーが発生した場合は、最新バージョンの AWS CLI と Docker がインストールされていることを確認してください。
> 以下のコマンドを使用して、Docker イメージを構築します。一から Docker ファイルを構築する方法については、「こちらをクリック 」の手順を参照してください。既にイメージが構築されている場合は、このステップをスキップします。

`docker build -t traialapi-repo .`

> 構築が完了したら、このリポジトリにイメージをプッシュできるように、イメージにタグを付けます。

`docker tag traialapi-repo:latest 045224308799.dkr.ecr.us-east-1.amazonaws.com/traialapi-repo:latest`

> A以下のコマンドを実行して、新しく作成した AWS リポジトリにこのイメージをプッシュします:

`docker push 045224308799.dkr.ecr.us-east-1.amazonaws.com/traialapi-repo:latest`

マネコンで見ると何かのイメージがプッシュされた

## ローカルのdocker image削除

docker rmi で削除

## ECRにプッシュしたイメージをpull

`docker pull 045224308799.dkr.ecr.us-east-1.amazonaws.com/traialapi-repo:latest`

docker imagesで見るとpulされてる

# ECS(Fargate)構築

こっちはメチャ大変…
[参考](https://qiita.com/tatsuya11bbs/items/3466dd0c6b84731fe62e#1-vpc作成)

## VPC作成

- 名前: fargate-trialapi
- IPv4 CIDR: 10.0.0.0/16
  他はデフォルト

## サブネット作成

- VPC ID: vpc-0b0b1baf7b6eb7375
  以下4つ作る
- fargate-traialapi-public-subnet01 us-east-1a 10.0.0.0/16 10.0.0.0/24
- fargate-traialapi-public-subnet02 us-east-1c 10.0.0.0/16 10.0.1.0/24
- fargate-traialapi-private-subnet01 us-east-1a 10.0.0.0/16 10.0.2.0/24
- fargate-traialapi-private-subnet02 us-east-1c 10.0.0.0/16 10.0.3.0/24

## インターネットゲートウェイ作成

- 名前: fargate-trialapi-igw
- 作ったインターネットゲートウェイをVPCにアタッチ

## NATゲートウェイ作成

### ひとつめ

- 名前: fargate-trialapi-netgw01
- サブネット: fargate-traialapi-public-subnet01
- [Elastic IPを割り当て]クリック

### ふたつめ

- 名前: fargate-trialapi-netgw02
- サブネット: fargate-traialapi-public-subnet02
- [Elastic IPを割り当て]クリック

## ルートテーブル作成

### デフォルトルートテーブル作成

- 名前: fargate-trialapi-default-rt という名前でこのVPCのデフォルトルートテーブルを作成(?)
- ルートを編集: 0.0.0.0/0 インターネットゲートウェイ igw-xxx(fargate-trialapi-igwを選択)
- このルートテーブルを [サブネットとの関連付けを編集] でパブリックサブネットを紐づける

### プライベートテーブル作成1

- 名前: fargate-trialapi-private-rt01
- VPC: このVPC
- ルートを編集: 0.0.0.0/0 NATゲートウェイ nat-xxx(fargate-trialapi-netgw01)

### プライベートテーブル作成2

- 名前: fargate-trialapi-private-rt02
- VPC: このVPC
- ルートを編集: 0.0.0.0/0 NATゲートウェイ nat-xxx(fargate-trialapi-netgw02)

## ALB作成

### セキュリティグループ作成

- グループ名: fargate-trialapi-sg-for-alb
- 説明: fargate-trialapi-sg-for-alb
- VPC: このVPC
- インバウンドルール
  - HTTP Anywhere-IPv4

### ターゲットグループ作成

- ターゲットタイプの選択: IPアドレス
- グループ名: fargate-trialapi-tg
- プロトコル: HTTP ポート: 8000
- VPC: このVPC
- IPアドレス
  - ネットワーク: fargate-trialapi-vpc

### EC2 > ロードバランサー作成

- ロードバランサータイプ: Application Load Balancer
- 名前: fargate-trialapi-alb
- VPC: このVPC
  - us-east-1a: fargate-traialapi-public-subnet01
  - us-east-1c: fargate-traialapi-public-subnet02
- セキュリティグループ: fargate-trialapi-sg-for-alb
- リスナーとルーティングのデフォルトアクションで fargate-trialapi-tg が選べない?(VPCのほうでターゲットグループ作ったから?) ので EC2のほうのターゲットグループから fargate-trialapi-ec2-tg を作った

## ECS作成

### タスク定義作成

- タスク定義ファミリー: fargate-trialapi-task-definition
- タスクロール: なし
- タスク実行ロール: 本当は何設定したほうが良いらしいが選べないので、とりあえず「新しいロール作成」にしたら勝手に作られた
- コンテナ-1
  - 名前: fargate-trialapi-container
  - イメージURI: 045224308799.dkr.ecr.us-east-1.amazonaws.com/traialapi-repo:latest
  - ポートマッピング: 8000 TCP 8000 HTTP

### クラスター作成

- 名前: fargate-trialapi-cluster
- モニタリング - オプション: Container Insights

#### クラスター > サービス作成

- コンピューティングオプション: 起動タイプ
- ファミリー: fargate-trialapi-task-definition
- サービス名: fargate-trialapi-service
- 必要なタスク数: 2
- ネットワーキング
  - VPC: このVPC
  - サブネット: public-subnet01, public-subnet02 の2つ
  - セキュリティグループ: 新しいセキュリティグループの作成
  - インバウンドルール
    - HTTP ソースグループ sg-xxx(fargate-trialapi-sg-for-alb)
    - カスタムTCP 8000 ソースグループ sg-xxx(fargate-trialapi-sg-for-alb)
  - パブリックIP: OFF
- ロードバランシング
  - Applicatin Load Balancer: 既存のロードバランサーを使用
  - ロードバランサー: fargate-trialapi-alb
  - リスナー: 既存のリスナーを使用 80:HTTP
  - ターゲットグループ: 既存のターゲットグループを使用

ずっとサービスのデプロイ進行中で終わったと思ったら、デプロイ失敗…
何時間もやってやっぱり上手く行かねぇ… AWS気が狂ってる!
やめよう…
