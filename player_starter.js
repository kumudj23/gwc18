// This code loads the IFrame Player API code asynchronously.
var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

// This function creates an <iframe> (and YouTube player) after the API code downloads.
var player;
function onYouTubeIframeAPIReady() {
  player = new YT.Player('player', {
    height: '390',
    width: '640',
    videoId: 'rqX8PFcOpxA',
    events: {
      'onReady': onPlayerReady,
      'onStateChange': onPlayerStateChange
    }
  });
}

// The API will call this function when the video player is ready.
function onPlayerReady(event) {
  //event.target.playVideo();
}

function play() {
  player.playVideo()
}

function pause() {
  player.pauseVideo()
}

function videoChangeOne() {
  player.loadVideoById({videoId:"rqX8PFcOpxA",
                        startSeconds:0,
                        suggestedQuality:"default"})
}

function videoChangeTwo() {
  player.loadVideoById({videoId:"O753uuutqH8",
                        startSeconds:0,
                        suggestedQuality:"default"})
}

function videoChangeThree() {
  player.loadVideoById({videoId:"9S_fnC5jPgw",
                        startSeconds:0,
                        suggestedQuality:"default"})
}

function onPlayerStateChange(event) {
  if(event.data == YT.PlayerState.ENDED) {
    player.destroy()
  }

}
