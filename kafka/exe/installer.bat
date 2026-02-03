@echo off
echo 正在打包Kafka生产者为Windows 7可执行文件...

pyinstaller --onefile ^
            --console ^
            --name kafka_producer_win7 ^
            --add-data ".;." ^
            --hidden-import kafka.producer.kafka ^
            --hidden-import kafka.client_async ^
            --hidden-import kafka.protocol ^
            --hidden-import kafka.serializer ^
            kafka_producer_win7.py

echo 打包完成! 可执行文件位于 dist 文件夹中
pause