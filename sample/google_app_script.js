function invokeService(input) {
  
var row = input.length
var col = input[0].length
var input_data = JSON.stringify(input)
 var url ="http://104.155.149.60:8000/quote?data="+encodeURIComponent(input_data)
  var options = {
    "method" : "POST",
    "contentType" : "application/json",
  };
 var data = UrlFetchApp.fetch(url, options).getContentText()
 Logger.log(data)
 return data;
}


