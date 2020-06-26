(function () {

    var signalObj = null;

    function startPlay() {
        if (signalObj)
            return;
 
        var hostname = location.hostname;
        var address = hostname + ':' + (location.port || (location.protocol === 'https:' ? 443 : 80)) + '/webrtc';
        var protocol = location.protocol === "https:" ? "wss:" : "ws:";
        var wsurl = protocol + '//' + address;

        var video1 = document.querySelector('#v1');
        var video2 = document.querySelector('#v2');

        signalObj = new signal(wsurl,
            function (stream) {
                console.log('got a stream!');
                document.querySelector('.oioi').style.display = 'none'
                document.querySelector('.vid').style.display = 'flex'
                video1.srcObject = stream;
                video1.play();
                video2.srcObject = stream;
                video2.play();
            },
            function (error) {
                alert(error);
                signalObj = null;
            },
            function () {
                console.log('websocket closed. bye bye!');
                video1.srcObject = null;
                video2.srcObject = null;
                signalObj = null;
            },
            function (message) {
                alert(message);
            }
        );
    }

    function stopPlay() {
        if (signalObj) {
            signalObj.hangup();
            signalObj = null;
        }
    }

    window.addEventListener('DOMContentLoaded', function () {

        var start = document.getElementById('start');
        if (start) {
            start.addEventListener('click', function (e) {
                startPlay();
            }, false);
        }
        else {
            // auto play if there is no stop button
            startPlay();
        }

        var stop = document.getElementById('stop');
        if (stop) {
            stop.addEventListener('click', function (e) {
                stopPlay();
            }, false);
        }

        // App will call viewPause/viewResume for view status change
        window.viewPause = stopPlay;
        window.viewResume = startPlay;
    });
})();
