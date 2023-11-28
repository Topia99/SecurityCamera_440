# SecurityCamera_440


hunter@raspberrypi:~/Desktop/SecurityCamera_440/SecurityCamera $ python3 liveStream.py
 * Serving Flask app 'liveStream'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://10.66.45.179:8000
Press CTRL+C to quit
 * Restarting with stat
mmal: mmal_vc_port_enable: failed to enable port vc.null_sink:in:0(OPQV): ENOSPC
mmal: mmal_port_enable: failed to enable connected port (vc.null_sink:in:0(OPQV))0x18037e0 (ENOSPC)
mmal: mmal_connection_enable: output port couldn't be enabled
Traceback (most recent call last):
  File "/home/hunter/Desktop/SecurityCamera_440/SecurityCamera/liveStream.py", line 10, in <module>
    camera = picamera.PiCamera()
  File "/usr/lib/python3/dist-packages/picamera/camera.py", line 433, in __init__
    self._init_preview()
  File "/usr/lib/python3/dist-packages/picamera/camera.py", line 512, in _init_preview
    self._preview = PiNullSink(
  File "/usr/lib/python3/dist-packages/picamera/renderers.py", line 558, in __init__
    self.renderer.inputs[0].connect(source).enable()
  File "/usr/lib/python3/dist-packages/picamera/mmalobj.py", line 2210, in enable
    mmal_check(
  File "/usr/lib/python3/dist-packages/picamera/exc.py", line 184, in mmal_check
    raise PiCameraMMALError(status, prefix)
picamera.exc.PiCameraMMALError: Failed to enable connection: Out of resources
