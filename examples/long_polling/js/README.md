## Running the Example

### Running Web Integration Service
To run the example, open a terminal and enter the following command:

```
<NDDSHOME>/bin/rtiwebintegrationservice \
  -cfgFile /path/to/rtiwebintegrationservice-examples/examples/long_polling/long_polling.xml \
  -cfgName LongPolling \
  -documentRoot /path/to/rtiwebintegrationservice-examples \
  -enableKeepAlive yes
```

Where:

* The ```-cfgFile``` option adds loads the appropriate configuration file
into _Web Integration Service_.
* The ```-cfgName``` option specifies the configuration to be instantiated—in
this case ```LongPolling```—which starts
the ```LongPollingApplication```.
This application instantiates a _DomainParticipant_ with _DataReaders_ to read
to Square topics (i.e., Squares, Circles, and Triangles).
* The ```-documentRoot``` argument specifies the folder that _Web
Integration Services_ web server will provide when accessing the default URL.
That is ```http://<hostname>:8080```.
* The ```-enablekeepAlive``` option tries to maintain open the underlying TCP
connection between client and server between subsequent requests and responses.

### Running JavaScript Long Polling Example

Once you have started _Web Integration Service_, you can open _RTI Shapes
Demo_ and start publishing Squares on domain 0.

To read squares using long polling from your JavaScript client application,
open Open a browser and navigate to ```http://<hostname>:8080/examples/long_polling/js```.
You will the sequence of samples that are being read using long polling.
