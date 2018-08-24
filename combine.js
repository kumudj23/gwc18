var firstWord = prompt("What is the first word? ");
var firstLength = Number(prompt("What is the length you want to cut it at? "));
var secondWord = prompt("What is the second word? ");
var secondLength = Number(prompt("What is the length you want to cut it at? "));
var finalWord;

secondLength = secondWord.length - secondLength;
firstWord = firstWord.slice(0, firstLength);
secondWord = secondWord.slice(secondLength,);
finalWord = firstWord + secondWord;
document.getElementById("demo").innerHTML = finalWord;
