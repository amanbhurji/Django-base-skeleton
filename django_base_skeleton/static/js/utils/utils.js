/**
 * author: Manpreet Singh Bhurji
 * (c) 'toType' function by Angus Croll http://javascriptweblog.wordpress.com/
 */

Utils_toType = (function toType(global) {
  return function(obj) {
    if (obj === global) {
      return "global";
    }
    return ({}).toString.call(obj).match(/\s([a-z|A-Z]+)/)[1].toLowerCase();
  }
})(this);

// convert "this is a test" to "This Is A Test"
Utils_capitalize = function(str) {
  return str.replace( /(^|\s)([a-z])/g , function(m,a,b) { return a+b.toUpperCase(); } );
}
Utils_replaceUnderscoresWithSpaces = function(str) {
  return str.replace( /(_)/g, function(m,a) { return " "; } );
}
Utils_removeSpacesAndCaptalize = function(str) {
  return str.replace( /(^|\s+)([a-z])/g , function(m,a,b) { return b.toUpperCase(); } );  
}
Utils_removeUnderscoresAndSpacesAndCapitalize = function(str) {
  return Utils_removeSpacesAndCaptalize(Utils_replaceUnderscoresWithSpaces(str));
}