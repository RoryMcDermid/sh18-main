var mysql = require("mysql");

const config = {
  host: "localhost",
  user: "root",
  password: "password",
  database: "moxie_energy",
};
var db = mysql.createConnection(config);
db.connect(function (err) {
  if (err) {
    console.log("error connecting:" + err.stack);
  }
  console.log("connected successfully to DB.");
});

module.exports = db;
