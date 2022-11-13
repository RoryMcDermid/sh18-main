
var mysql = require('mysql');
const fs = require('fs');
var systems_data;


fs.readFile('../web-app/src/data/Systems/ListOfSystems.json', 'utf8', (err, jsonString) => {
  if (err) {
      console.log("File read failed:", err)
      return
  }
  systems_data = JSON.parse(jsonString); 
//  console.log("Json of data: ", systems_data);
})

console.log(systems_data);

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "password",
  database: "moxie_energy"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
    for (let system in systems_data) {
      // console.log(system);
      // console.log(systems_data[system]);

      var sql = "INSERT INTO systems (system_id) VALUES (" + system + ")";
      con.query(sql, function (err, result) {
        if (err) throw err;
          console.log("1 record inserted");
        });
    }
  
}) ; 