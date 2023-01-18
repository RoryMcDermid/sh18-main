const express = require("express");
const router = express.Router();

// import controllers
const {
  getAllSystems,
  getSystem,
  getAllSensorsInSystem,
  getDataFromSensors,
} = require("../controllers/systems");

router.get("/systems", getAllSystems);
router.get("/systems/:id", getSystem);
router.get("/systems/:systemid/sensors", getAllSensorsInSystem);
router.get("/systems/:systemid/sensors/:sensorids", getDataFromSensors);

module.exports = router;
