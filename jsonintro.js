// This code loads the IFrame Player API code asynchronously.
var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

/*
 * Parameters:
 * object_id: represents the player object (to be returned)
 *    div_id: a string representing the id of the div to replace
 *         h: an int representing the height of the player
 *         w: an int representing the width of the player
 *  video_id: a string representing the video id to be loaded in the player
 *
 * Returns:
 *   the player object
 */
function makePlayerObject(object_id, div_id, h, w, video_id){
  /* How can we modify this code block to generalize making an object? */
  object_id = new YT.Player(div_id, {
          height: h,
          width: w,
          videoId: video_id
  });
  return object_id;
}

function change(player){
  player.setSize(540, 250);
}

function reset(player){
  player.setSize(640, 350)

}

var player1;
var player2;

function onYouTubeIframeAPIReady() {
  /* Write code to make 2 players */
  player1 = makePlayerObject(player1, "player1", 350, 640, "rqX8PFcOpxA")
  player2 = makePlayerObject(player2, "player2", 350, 640, "O753uuutqH8")
}
