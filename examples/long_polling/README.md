# Long Polling
This example illustrates how to configure Web Integration Service and different
client applications to subscribe to Square topics using long polling.

Long polling emulates server push mechanism over regular HTTP using by
performing long-lasting HTTP requests until the server has a response
available instead of returning an empty response right away. In the context
of _Web Integration Service_, long polling enables client applications to
register on_data_available functions that get triggered when new data
becomes available in the _DataReader_ on which the ``read()`` or ``take()``
operation is being performed. To do so, _Web Integration Service_ clients
leverage a set of *WaitSets* that the server makes available to wait until
certain read conditions are met.


Instructions on how to run _Web Integration Service_ and the client applications
for each specific language are available under:

* [js/README.md](js/README.md)
* [python/README.md](python/README.md)
