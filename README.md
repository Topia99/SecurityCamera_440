hunter@raspberrypi:~/Desktop/SecurityCamera_440/SecurityCamera $ python app.py
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8000
 * Running on http://10.66.45.179:8000
Press CTRL+C to quit
Exception in thread Thread-1:
Traceback (most recent call last):
  File "/usr/lib/python3.9/threading.py", line 954, in _bootstrap_inner
    self.run()
  File "/usr/lib/python3.9/threading.py", line 892, in run
    self._target(*self._args, **self._kwargs)
  File "/home/hunter/Desktop/SecurityCamera_440/SecurityCamera/app.py", line 34, in run_server
    app.run(host='0.0.0.0', port=8000, debug=True)
  File "/home/hunter/.local/lib/python3.9/site-packages/flask/app.py", line 612, in run
    run_simple(t.cast(str, host), port, self, **options)
  File "/home/hunter/.local/lib/python3.9/site-packages/werkzeug/serving.py", line 1099, in run_simple
    run_with_reloader(
  File "/home/hunter/.local/lib/python3.9/site-packages/werkzeug/_reloader.py", line 439, in run_with_reloader
    signal.signal(signal.SIGTERM, lambda *args: sys.exit(0))
  File "/usr/lib/python3.9/signal.py", line 47, in signal
    handler = _signal.signal(_enum_to_int(signalnum), _enum_to_int(handler))
ValueError: signal only works in main thread of the main interpreter

