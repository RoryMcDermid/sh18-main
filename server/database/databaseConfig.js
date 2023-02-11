var mysql = require("mysql");
require("dotenv").config();

var db = mysql.createConnection(process.env.DATABASE_URL);
db.connect(function (err) {
  if (err) {
    console.log("error connecting:" + err.stack);
  }
  console.log("connected successfully to PlanetScale!");
});

module.exports = db;
