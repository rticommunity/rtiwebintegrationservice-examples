## Running the Example

To run this example, execute _Web Integration Service_, _RTI Shapes Demo_, and
the Python client as follows.

### Running Web Integration Service
To run _Web Integration Service_, open a terminal and enter the following
command:

```
<NDDSHOME>/bin/rtiwebintegrationservice \
  -cfgFile /path/to/rtiwebintegrationservice-examples/examples/long_polling/long_polling.xml \
  -cfgName LongPolling \
  -enableKeepAlive yes
```

Where:

* The ``-cfgFile`` argument loads the appropriate configuration file
into _Web Integration Service_.
* The ``-cfgName`` argument specifies the configuration to be instantiated—in
this case ``LongPolling``—which starts
the ``LongPollingApplication``.
This application instantiates a _DomainParticipant_ with _DataReaders_ to read
to Square topics.
* The ``-enablekeepAlive`` argument configures the service to keep open the
underlying TCP connection between client and server between subsequent requests
and responses when possible.

### Running RTI Shapes Demo
Once you have started _Web Integration Service_, open _RTI Shapes
Demo_ and start publishing Squares of different colors on domain 0.

### Running Python Client Application
To read squares using Long Polling from your Python client application,
open another terminal and enter the following command:

```
python /path/to/rtiwebintegrationservice-examples/examples/long_polling/python/long_polling.py
```
