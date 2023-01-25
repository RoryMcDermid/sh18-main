const db = require("../database/databaseConfig");

exports.getAllSystems = (req, res) => {
  let sql = "SELECT * FROM systems";
  console.log(db);
  let query = db.query(sql, (error, results) => {
    if (error) throw error;
    res.send(results);
  });
};

exports.getSystem = (req, res) => {
  let sql = `SELECT * FROM systems WHERE SYSTEM_ID = ${req.params.id}`;
  let query = db.query(sql, (error, result) => {
    if (error) throw error;
    res.send(result);
  });
};

exports.getAllSensorsInSystem = (req, res) => {
  let sql = `SELECT * FROM sensors_for_${req.params.systemid}`;
  let query = db.query(sql, (error, result) => {
    if (error) throw error;
    res.send(result);
  });
};

exports.getDataFromSensors = async (req, res) => {
  let sql = "";
  if (req.params.sensorids.indexOf(",") > -1) {
    const queries = req.params.sensorids.split(",").map(async (sensorId) => {
      sql = `SELECT * FROM iter_${req.query.interval}_${sensorId} WHERE DATE_OF_RECORD>='${req.query.startDate}' AND DATE_OF_RECORD<'${req.query.endDate}'`;
      return new Promise((resolve, reject) => {
        db.query(sql, (error, result) => {
          if (error) reject(error);
          if (result) {
            resolve(result);
          }
        });
      });
    });
    const responses = await Promise.all(queries);
    res.send(responses);
  } else {
    sql = `SELECT * FROM iter_${req.query.interval}_${req.params.sensorids} WHERE DATE_OF_RECORD>='${req.query.startDate}' AND DATE_OF_RECORD<'${req.query.endDate}'`;
    let query = await new Promise((resolve, reject) => {
      db.query(sql, (error, result) => {
        if (error) reject(error);
        if (result) {
          resolve([result]);
        }
      });
    });
    res.send(query);
  }
};
