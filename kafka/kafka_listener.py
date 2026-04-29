# -*- coding: utf-8 -*-
import sys
import time
import locale
import codecs
from kafka import KafkaConsumer
import json

# ====================== Configuration ======================
KAFKA_BOOTSTRAP = '192.168.1.93:9092'
KAFKA_USERNAME = 'admin'
KAFKA_PASSWORD = 'Ap2uH77YyYW5n8ddFHt7'

# Topic to listen to (change to your actual topic)
TOPIC_NAME = 'AIRCRAFT_STATE'
# ===========================================================

def _setup_console_encoding():
    # Fix Windows console encoding issues for Python 2.7 only
    if sys.version_info[0] >= 3:
        return
    try:
        console_enc = locale.getpreferredencoding()
        sys.stdout = codecs.getwriter(console_enc)(sys.stdout)
        sys.stderr = codecs.getwriter(console_enc)(sys.stderr)
    except Exception:
        pass

def _log(s):
    # Ensure text output in both Python 2.7 and 3.x
    try:
        if isinstance(s, bytes):
            s = s.decode("utf-8", "replace")
        elif sys.version_info[0] < 3 and isinstance(s, str):
            s = s.decode("utf-8", "replace")
    except Exception:
        pass
    print(s)

def main():
    _setup_console_encoding()
    _log("Python 2.7.18 Kafka listener starting...")
    _log("Bootstrap: " + KAFKA_BOOTSTRAP)
    _log("Topic: " + TOPIC_NAME)
    _log("========================================")

    try:
        consumer = KafkaConsumer(
            bootstrap_servers=[KAFKA_BOOTSTRAP],
            auto_offset_reset='latest',  # latest: newest messages; earliest: from beginning
            enable_auto_commit=True,
            group_id='python-listener-group',
            # SASL auth config
            security_protocol='SASL_PLAINTEXT',
            sasl_mechanism='PLAIN',
            sasl_plain_username=KAFKA_USERNAME,
            sasl_plain_password=KAFKA_PASSWORD,
            # For Python 2.7 compatibility
            api_version=(0, 10, 1)
        )

        # Pre-check Kafka connection before listening
        connect_timeout_sec = 10
        start_ts = time.time()
        connected = False
        while time.time() - start_ts < connect_timeout_sec:
            if consumer.bootstrap_connected():
                connected = True
                break
            try:
                # Force network connection attempt
                consumer.poll(timeout_ms=100)
            except Exception:
                pass
            time.sleep(0.2)

        if not connected:
            raise Exception("Kafka connection timeout: no connection in %ss" % connect_timeout_sec)

        _log("Kafka connection established, starting listener...")
        consumer.subscribe([TOPIC_NAME])

        # Listen for messages
        for msg in consumer:
            _log("\n===== Message Received =====")
            _log("Partition: %s" % msg.partition)
            _log("Offset: %s" % msg.offset)
            _log("Key: %s" % msg.key)
            _log("Value: %s" % msg.value)
            _log("===========================\n")

    except Exception as e:
        _log("Connection failed: %s" % str(e))
        sys.exit(1)

if __name__ == '__main__':
    main()
