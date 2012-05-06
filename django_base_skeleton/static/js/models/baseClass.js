/**
 * author: Manpreet Singh Bhurji
 * Refer: https://developer.mozilla.org/en/Introduction_to_Object-Oriented_JavaScript
 *        http://phrogz.net/js/Classes/ExtendingJavaScriptObjectsAndClasses.html#prototype
 * Adding to BaseClass.prototype adds to all instances of BaseClass, so only add class fields to it.
 */

function BaseClass(id) {

  // if you want any property to appear in the JSON string when using JSON.stringify you need to add it to the object like - this.property
  this.id = null; // set default, if you don't do this JSON.stringify(new BaseClass()) == "{}"
  if (Utils_toType(id) === "number") {
    this.id = id; 
  }
}

(function() {
  // keep namespace clean
  function BaseClass_getById(id) {
    var copy = null;
    var id = parseInt(id, 10);
    if (id) {
      copy = this;
      console.log("Making ajax request...");
      /*
      copy.failed = true;
      copy.response = null;
      $.ajax({
        url: ""/ * add api url here * / + "/" + copy.getInfo()["type"] + "/?id=" + id,
        type: "GET",
        async: copy.async, // try adding this variable to the prototype
        dataType: 'json',
        success: function(response, textStatus, xmlHttpRequest) {
          copy.failed = false;
          copy.getResponse();
          switch(xmlHttpRequest.getResponseHeader("Content-Type").toLowerCase()){
            case "text/xml":
              copy.fromXML(response); // write function to build object from provided xml string
              break;
            case "application/json":
              copy.fromJSON(response); // write function to build object from provided json string
              break;
            default:
              copy.failed = true;
          }
        },
        error: function(xmlHttpRequest,textStatus,errorThrown) {
          copy.failed=(xmlHttpRequest.status ? xmlHttpRequest.status : true);
          copy.response = (xmlHttpRequest.status && errorThrown) ? errorThrown : "Server unresponsive";
        }
      });
      */
    }
  }
  
  function BaseClass_fromJSONObject(jsonObject) {
    var attr;
    for (attr in jsonObject) {
      this["set" + Utils_capitalize(attr)](jsonObject[attr]);
    }
    return this;
  }

  function BaseClass_toJSON() {
    return this;
  }
  
  BaseClass.prototype.getId = function() { return this.id; }
  BaseClass.prototype.setId = function(newId) { this.id = parseInt(newId, 10); }
  BaseClass.prototype.getById = BaseClass_getById;
  BaseClass.prototype.toJSON = BaseClass_toJSON;
  BaseClass.prototype.fromJSONObject = BaseClass_fromJSONObject;
  
})();

// inherit BaseClass
Poll.prototype = new BaseClass();
// correct the constructor pointer because it points to BaseClass
Poll.prototype.constructor = Poll;
function Poll(id, pubDate, question) {
  
  BaseClass.call(this, id);
  this.question = "";
  this.pubDate = null;
  this.pollingEnded = false;
  if (Utils_toType(id) === "number") {
    this.id = id;
  }
  if (Utils_toType(question) === "string") {
    this.question = question;
  }
  if (Utils_toType(pubDate) === "date") {
    this.pubDate = pubDate;
  }
  
  //it is better to add these to a prototype, if you intend to have many Poll objects  
  /*
  this.getQuestion = function() { return this.question; }
  this.setQuestion = function(newQuestion) { this.question = newQuestion; }
  this.getPubDate = function() { return this.pubDate; }
  this.setPubDate = function(newPubDate) { this.pubDate = new Date(newPubDate); }
  this.setPollingEnded = function(newPollingEnded) { this.pollingEnded = newPollingEnded; }
  this.getPollingEnded = function() { return this.pollingEnded; }
  */
}
(function() {
  
  Poll.prototype.getQuestion = function() { return this.question; };
  Poll.prototype.setQuestion = function(newQuestion) { this.question = newQuestion; };
  Poll.prototype.getPubDate = function() { return this.pubDate; };
  Poll.prototype.setPubDate = function(newPubDate) { this.pubDate = new Date(newPubDate); };
  Poll.prototype.setPollingEnded = function(newPollingEnded) { this.pollingEnded = newPollingEnded; };
  Poll.prototype.getPollingEnded = function() { return this.pollingEnded; };

})();

Choice.prototype = new BaseClass();
Choice.prototype.constructor = Choice;
function Choice(id, choice, votes, poll) {
  
  BaseClass.call(this, id);
  this.choice = "";
  this.votes = 0;
  this.pollId = null;
  if (Utils_toType(id) === "number") {
    this.id = id;
  }
  if (Utils_toType(votes) === "number") {
    this.votes = votes;
  }
  if (Utils_toType(choice) === "string") {
    this.choice = choice;
  }
  this.setPollId(poll);
}

(function() {

  function Choice_getPollId() {
    return this.pollId;
  }

  function Choice_setPollId(poll) {
    if (poll instanceof Poll) {
      this.pollId = parseInt(poll.getId(), 10);
    }else if (parseInt(poll, 10) && Utils_toType(parseInt(poll, 10)) === "number") {
      this.pollId = parseInt(poll, 10);
    }
  }
  
  Choice.prototype.getPollId = Choice_getPollId;
  Choice.prototype.setPollId = Choice_setPollId;
  Choice.prototype.getChoice = function() { return this.choice; };
  Choice.prototype.setChoice = function(newChoice) { this.choice = newChoice; };

})();