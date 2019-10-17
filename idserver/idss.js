var express = require('express');
var async = require('async');  
var bodyParser = require('body-parser')


var sqlite3 = require('sqlite3').verbose();
var db = new sqlite3.Database('../db.sqlite3');


var skey = 'Dd2uyQ3fYbRKG9PK';

skey = undefined;


var app = express();


app.use( bodyParser.json() );       // to support JSON-encoded bodies
app.use(bodyParser.urlencoded({     // to support URL-encoded bodies
  extended: true
})); 

app.get('/users/', function(req, res, next) {
var rkey = req.params.key;	
if (skey != rkey)
{
 res.status(403).send('Wrong key');
}
else
{

db.all("SELECT id,username,first_name,last_name,email from auth_user",function(err1,users){
  	
    for (var i=0; i<users.length; i++) 
   {
     users[i].infodent = "";
   }

   db.all("SELECT user_id, infodent from home_customer",function(err2,infod){
   
   for (var i=0; i<users.length; i++) {
     for (var j=0; j<infod.length; j++) {
     	if (infod[j].user_id == users[i].id)
     	{
     		users[i].infodent = infod[j].infodent;  
     	}


     }
   }

   var st = "";
   for (var i=0; i<users.length; i++) {
   	st += users[i].id;
   	st += "\\";
   	st += users[i].username;
   	st += "\\";
   	st += users[i].first_name;
   	st += "\\";
   	st += users[i].last_name;
   	st += "\\";
   	st += users[i].email;
   	st += "\\";
   	st += users[i].infodent;
   	if (i != users.length-1) st += "|";


   }
   console.log('GET /users/');
   res.status(200).send(st);


   });

  });
 }

});

app.post('/users/:id', function(req, res) {
  console.log('POST /users/');
    /*console.log('ID = ' + req.params.id);
    console.log('INFODENT = ' + req.body.infodent);
    console.log('LAST_NAME = ' + req.body.last_name);
    console.log('FIRST_NAME = ' + req.body.first_name);*/
  var rkey = req.params.key;  
  if (skey != rkey)
  {
   res.status(403).send('Wrong key');
  }
  else
  {

    if (req.body.infodent != undefined)
    {
    
    //"UPDATE home_customer SET infodent="+req.body.infodent+" WHERE user_id="+req.params.id+";"

    var sql = 'INSERT OR IGNORE INTO home_customer (user_id,infodent,account)\nVALUES ('+req.params.id+','+req.body.infodent+',"");';
    sql += "UPDATE home_customer SET infodent = "+req.body.infodent+" WHERE user_id = "+req.params.id+";";

     console.log(sql);
    db.exec(sql ,function(err){
       if (err==null) {res.status(200).send("Ok");} 
       else {res.status(500).send(err);} 
       
    })
    }
     else
    {
      res.status(200).send("No changes");
    }
  }

});

app.get('/deluser/:id', function(req, res, next) {
  console.log('GET /deluser/');
  var rkey = req.params.key;  
  if (skey != rkey)
  {
   res.status(403).send('Wrong key');
  }
  else
  {
    var sql = 'DELETE FROM home_customer WHERE user_id = '+req.params.id+';';
    db.all(sql,function(err){
    if (err==null) {res.status(200).send("Ok");} 
      else {res.status(500).send(err);
     console.log(err); } 

    });
  }

});

app.post('/account/:id', function(req, res) {
  console.log('POST /account/');
  var rkey = req.params.key;  
  if (skey != rkey)
  {
   res.status(403).send('Wrong key');
  }
  else
  {
     console.log(req.body.html);
    if (req.body.html != undefined)
    {
    
    //"UPDATE home_customer SET infodent="+req.body.infodent+" WHERE user_id="+req.params.id+";"

    var sql = 'UPDATE home_customer SET account="'+req.body.html+'" WHERE user_id='+req.params.id+';';

     console.log(sql);
       db.exec(sql ,function(err){
		  
		   
       if (err==null) {res.status(200).send("Ok");} 
       else {res.status(500).send(err);} 
       
    })
    }
     else
    {
      res.status(200).send("No changes");
    }
  }

});


app.on('close', function () {
  console.log("Closed");
  db.close();
});

var server = app.listen(3050, function () {

  var host = server.address().address;
  var port = server.address().port;

  console.log('Example app listening at http://%s:%s', host, port);

});



