/*
 * (c) 2017 Copyright, Real-Time Innovations, Inc.  All rights reserved.
 * RTI grants Licensee a license to use, modify, compile, and create derivative
 * works of the Software.  Licensee has the right to distribute object form
 * only for use with RTI products.  The Software is provided "as is", with no
 * warranty of any type, including any warranty for fitness for any purpose.
 * RTI is under no obligation to maintain or support the Software.  RTI shall
 * not be liable for any incidental or consequential damages arising out of the
 * use or inability to use the software.
 */

function onDataAvailable(sampleSeq)
{
    var tableRows = '';

    sampleSeq.forEach(function(sample, i, samples) {
        var validData = sample.read_sample_info.valid_data;
        if (!validData) {
            return;
        }

        tableRows += "<tr><td>";
        tableRows += sample.data.color;
        tableRows += "</td><td>"
        tableRows += sample.data.x;
        tableRows += "</td><td>"
        tableRows += sample.data.y;
        tableRows += "</td><td>";
        tableRows += sample.data.shapesize;
        tableRows += "</td></tr>"
    });

    document.getElementById("samplesTable").innerHTML = tableRows;
}

function readOrTake(datareaderUrl, onDataAvailableFnc, take)
{
    // Timeout in seconds
    var maxWait = 30;
    // Do HTTP request, which calls read_or_take again upon completion
    $.ajax({
        url: datareaderUrl,
        success: function(data, textStatus, xhr) {
            if (xhr.status == 200 && data.length > 0) {
                // Call  onDataAvailableFnc only if data != []
                onDataAvailableFnc(data)
            }
        },
        error: function(xhr, textStatus, errorThrown) {
            console.log(errorThrown);
        },
        complete: function(xhr) {
            if (xhr.status == 200) {
                // Only call again if the request was OK
                readOrTake(datareaderUrl, onDataAvailableFnc)
            }
        },
        dataType: "json",
        data: {
            sampleFormat: "json",
            removeFromReaderCache: (take ? "true" : "false"),
            maxWait: maxWait,
            sampleStateMask: "NOT_READ"
        },
        timeout: (maxWait * 1000 * 2)})
}

function read(datareaderUrl, onDataAvailableFnc)
{
    readOrTake(datareaderUrl, onDataAvailableFnc, false)
}

function take(datareaderUrl, onDataAvailableFnc)
{
    readOrTake(datareaderUrl, onDataAvailableFnc, true)
}
