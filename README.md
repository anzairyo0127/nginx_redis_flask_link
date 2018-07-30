# nginx_redis_flask_link
このリポジトリは、`DockerCompose`を使って、nginxとredisとflaskの３つのコンテナを作成することができます。

# クイックスタート
`docker-compose build`を行って、imageを作成してください。パソコンのスペックにもよりますが、ずいぶん時間がかかります。（主にアプリケーション用のコンテナに)
終わったら`docker-compose up`を行ってください。

`\flask_app\www\`がコンテナ内の`/var/www/`と共通しています。

`redis_test.py`は`redis_ctr`とつながり、`hoge`キーの`moge`バリューを作成します。

`page.py`は`uWSGI`にて、`nginx_ctr`とつながっています。

Docker-Toolboxでしたら`http://192.168.99.100`でブラウザにアクセスすれば、`Hello World!`と表示されるはずです。


## app_ctr
`app_ctr`は`python3.6.5`,`flask1.0.2`,`Python モジュールのuWSGI2.0.17`,`Pythonモジュールのredis2.10.6`
が入っているコンテナになります。
アプリケーション用のコンテナとして使ってください。
`\flask_app\www\`がコンテナ内の`/var/www/`と共有しております。
`redis_test.py`は`Pythonモジュールのredis`が入っております。
`page.py`は`uWSGI`にて、`nginx_ctr`とつながっています。

また、`\config\`もコンテナ内`/config/uwsgi/`と共有しています。

`uWSGI`の設定を変更したい場合は`\config\`の`uwsgi.ini`を変更してください。

## nginx_ctr
`nginx_ctr`は`nginx ver1.15`が入っています。
`port:80`で受け取ったパケットを`app_ctr`内の`uWSGI`のアプリケーションに渡しています。

`\nginx\publich\`は`/hostos/publich/`と共有しています。特に設定はしておりませんが、Logの出力などをホストOSにすることがあります。

`\nginx\config\nginx.conf`は`/etc/nginx/nginx.conf`と共通しており、`nginx`の大まかなコンフィグを設定できます。
今回は特に変更を加えておりません。

`\nginx\config\flask_app.conf`は`/etc/nginx/conf.d/flask_app.conf`と共通しており、カスタムコンフィグとなります。
基本、カスタムコンフィグの設定が優先されます。（記述部分は）
こちらにて、`開放するport番号`や`app_ctr`の`uWSGI`のリンクを記載しております。

## redis_ctr
`redis_ctr`は`redis ver4.0.10`が入っています。
`port:6379`にてDB処理を行います。
設定は`redis`のDockerHubのimageから何も変えておりません。