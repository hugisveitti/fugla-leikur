var bodyParser = require('body-parser');
var express = require('express');
var path = require('path');
var fs = require('fs');

var app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:true}));
app.use("/client", express.static(__dirname + "/client"));

var port = process.env.PORT || 3000;

var fs = require('fs');
var allirFuglar = JSON.parse(fs.readFileSync('data.json', 'UTF-8'));
var fjoldiFugla = 83;
console.log(allirFuglar)


app.listen(port, () => {
    console.log('listening on port ' + port);
});



app.get("/", (req, res) => {
    res.sendFile(__dirname + "/client/index.html");
});


app.get('/allirfuglar', (req, res) => {
    res.setHeader("Content-Type", "application/json; charset=utf-8");
    res.send(allirFuglar);
})

app.get('/randomfugl', (req, res) => {
    var birdsToSend = [];
    //svo ekki se sent sama fugl tvisvar
    var allBirdsRel = JSON.parse(JSON.stringify(allirFuglar));
    while(birdsToSend.length < 4){
        var rand = Math.floor((Math.random() * fjoldiFugla));
        console.log(rand)
        console.log(allirFuglar[rand]);
        birdsToSend.push(allBirdsRel[rand])
        allBirdsRel.splice(rand,1)
    }
    console.log(allirFuglar.length)
    res.setHeader("Content-Type", "application/json; charset=utf-8");

    res.redirect('/');
});

app.get('/highscores', (req, res) => {
    var allHighScores = JSON.parse(fs.readFileSync('highscore.json', 'UTF-8'));
    res.setHeader("Content-Type", "application/json; charset=utf-8");
    res.send(allHighScores);
})

app.post('/highscore', (req, res) => {
    console.log(req.body);

    fs.readFile('highscore.json', 'utf8', function readFileCallback(err, data){
    if (err){
        console.log(err);
    } else {
        console.log(data)
        obj = JSON.parse(data); //now it an object
        obj.push(req.body); //add some data
        json = JSON.stringify(obj); //convert it back to json
        fs.writeFile('highscore.json', json, 'utf8', callback); // write it back
    }});
    res.redirect('/');
    // res.redirect("/highscores")
});

function callback(){
    console.log('callback')
}
