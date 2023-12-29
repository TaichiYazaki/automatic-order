# Automatic Order 構成方法
## seleniumのDockerコンテナ立ち上げ方法
mac m1を使っている場合は、通常の立ち上げとは異なる。
docker-compose.yamlのimageには、以下を記載する。

linux/mac m1用
```
seleniarm/standalone-chromium:latest
```
windows/その他
```
selenium/standalone-chrome:latest
```


[Docker images for Selenium, built for Debian ARM64, ARM/v7, and AMD64][seleniun for docker]





[seleniun for docker]: https://github.com/seleniumhq-community/docker-seleniarm