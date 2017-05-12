import requests
import time


def on_data_available(data):
    """ Handles data received by the read or take functions whenever data is
    available. In this case, the function prints out the data it receives,
    which is string represented in JSON format.
    """
    print(data)


def read_or_take(data_reader_url, on_data_available_fnc, take):
    """ Performs a read or take operation on a DDS DataReader using
    long-polling. If new data becomes available, the function automatically
    wakes up and calls a given on_data_available_fnc to handle those new
    samples.
    """
    # Timeout in Seconds
    max_wait = 30

    # Do HTTP request, which calls read_or_take again upon completion
    try:
        # We reuse the session to avoid closing the underlying TCP connection.
        # Remeber to execute Web Integration Service with
        # -enableKeepAlive yes and and a appropriate -keepAliveTimeout time.
        req_session = requests.Session()

        while True:
            # We call GET and use JSON format, take or read depending on the
            # take parameter, and a maxWait timeout of 30 seconds, which is the
            # time Web Integration Service's internal waitset will block until
            # there are samples with sampleStateMask = "NOT_READ."
            # Note that this configuration will work well for only one client
            # at a time, because as any other client calls read the sample
            # status will change. Therefore, with this configuration, different
            # clients need to use different DataReaders.
            response = req_session.get(
                data_reader_url,
                params={
                    "sampleFormat": "json",
                    "removeFromReaderCache": "true" if take else "false",
                    "maxWait": str(max_wait),
                    "sampleStateMask": "NOT_READ"
                },
                timeout=(max_wait * 2))
            if (response.status_code == 200) and (response.text != "[]"):
                # Only call on_data_available if the status code was 200, and
                # we did not get an empty sequence of samples.
                on_data_available(response.text)

    except Exception as e:
        print(e)
        pass


def read(data_reader_url, on_data_available_fnc):
    """Performns a read() operation on a DDS DataReader given its resource
    URL. The operation performs a long-polling operation that calls the
    given on_data_available_fnc whenever new samples become available.
    As opposed to the take() operation, the read() operation does not remove
    the samples it has read from the DataReaders cache.
    """
    read_or_take(data_reader_url, on_data_available_fnc, False)


def take(data_reader_url, on_data_available_fnc):
    """Performns a take() operation on a DDS DataReader given its resource
    URL. The operation performs a long-polling operation that calls the
    given on_data_available_fnc whenever new samples become available.
    After reading the available samples, the take() operation removes all data
    in the DataReaders cache.
    """
    read_or_take(data_reader_url, on_data_available_fnc, True)


def main():
    # Assume that we are running on localhost
    host = "localhost"
    port = 8080

    # Prepare request
    datareader_url = "http://" + host + ":" + str(port) \
        + "/dds/rest1" \
        + "/applications/LongPollingApplication" \
        + "/domain_participants/MyParticipant" \
        + "/subscribers/MySubscriber" \
        + "/data_readers/MySquareRdr"

    # The take function will block, if you want to continue your execution
    # then take and subsequent calls to on_data_available need to be run on
    # a separate thread.
    take(datareader_url, on_data_available)


if __name__ == "__main__":
    main()