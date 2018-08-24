function Get(yourUrl){
    var Httpreq = new XMLHttpRequest(); // a new request
    Httpreq.open("GET",yourUrl, false);
    Httpreq.send(null);
    //console.log(typeof(Httpreq.responseText));
    console.log(Httpreq.responseText);
    console.log((Httpreq.responseText).length);
  return (Httpreq.responseTex);
}
  var item = Get("https://www.poemist.com/api/v1/randompoems");
  document.getElementById("poem").innerHTML = item;
 // var  item = JSON.stringify(item);


// console.log("huuh" + item);

// document.getElementById("poem").innerHTML = item;
