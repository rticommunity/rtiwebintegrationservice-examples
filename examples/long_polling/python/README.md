## Running the Example

### Running Web Integration Service
To run the example, open a terminal and enter the following command:

```
<NDDSHOME>/bin/rtiwebintegrationservice \
  -cfgFile /path/to/rtiwebintegrationservice-examples/long_polling/long_polling.xml \
  -cfgName LongPolling \
  -enableKeepAlive yes
```

Where:

* The ```-cfgFile``` option adds loads the appropriate configuration file
into _Web Integration Service_.
* The ```-cfgName``` option specifies the configuration to be instantiated—in
this case ```LongPolling```—which starts the ```LongPollingApplication```.
This application instantiates a _DomainParticipant_ with _DataReaders_ to read
to Square topics (i.e., Squares, Circles, and Triangles).
* The ```-enablekeepAlive``` option tries to maintain open the underlying TCP
connection between client and server between subsequent requests and responses.

### Running Python Long Polling Example

Once you have started _Web Integration Service_, you can open _RTI Shapes
Demo_ and start publishing Squares on domain 0.

To read squares using long polling from your Python application, open another
terminal and enter the following command:

```
python /path/to/rtiwebintegrationservice-examples/long_polling/python/long_polling.py
```
