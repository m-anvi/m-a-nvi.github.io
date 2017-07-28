var wordsList = [];

function init() {
  // Load the words from the dictionary text file to wordsList
  var wordsFile = "https://raw.githubusercontent.com/GirlsFirst/SIP-2017/master/Unit2_Applications/dictionary-attack/dictionary.txt?token=ADcVhZjRMd86ZdhPE2jVvIaJdQdzLA6Yks5YvvVSwA%3D%3D";
  $.get(wordsFile, function(data) {
    document.getElementById("btnSubmit").disabled = true;
    wordsList = data.split('\n');
    document.getElementById("btnSubmit").disabled = false;
  });
}

window.onload = init;

/* ADD YOUR CODE BELOW */

function checkPassword() {
//  var strength = true;
  var pw=document.getElementById('pw');
//  for(var i=0; i<wordsList.length; i+=1) {
//you likely don't need a colon after conditionals
       if (pw.value==wordsList[0]) {
         window.alert("weak!")
//         strength = false;
       }
       else {
         window.alert("strong")
       }
//  }
//  if (strength = true): {
//     window.alert("strong")
//   }
}
