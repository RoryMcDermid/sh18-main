const express = require("express");
const router = express.Router();

// import controllers
const {
  getAllSystems,
  getSystem,
  getAllSensorsInSystem,
  getFifteenMinDataFromSensors,
  getOneHourDataFromSensors,
  getFourHourDataFromSensors,
  getOneDayDataFromSensors,
} = require("../controllers/systems");

router.get("/systems", getAllSystems);
router.get("/systems/:id", getSystem);
router.get("/systems/:systemid/sensors", getAllSensorsInSystem);
router.get(
  "/systems/:systemid/sensors/:sensorid",
  getFifteenMinDataFromSensors
);
router.get(
  "/systems/:systemid/sensors/:sensorid/15min",
  getFifteenMinDataFromSensors
);
router.get(
  "/systems/:systemid/sensors/:sensorid/1hour",
  getOneHourDataFromSensors
);
router.get(
  "/systems/:systemid/sensors/:sensorid/4hour",
  getFourHourDataFromSensors
);
router.get(
  "/systems/:systemid/sensors/:sensorid/1day",
  getOneDayDataFromSensors
);

module.exports = router;
