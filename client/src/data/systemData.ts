const allSystems = [
  {
    SYSTEM_ID: 1693,
    SYSTEM_NAME: "EP - Glasgow University ~ Gateways",
    SENSOR_COUNT: 0,
  },
  {
    SYSTEM_ID: 1752,
    SYSTEM_NAME: "EP - Glasgow University - Library",
    SENSOR_COUNT: 2,
  },
  {
    SYSTEM_ID: 1756,
    SYSTEM_NAME: "EP - Glasgow University - Fraser Building",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 1757,
    SYSTEM_NAME: "EP - Glasgow University - Main Building",
    SENSOR_COUNT: 4,
  },
  {
    SYSTEM_ID: 1758,
    SYSTEM_NAME: "EP - Glasgow University - QMU",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2388,
    SYSTEM_NAME: "EP - Glasgow University - Adam Smith Building",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2398,
    SYSTEM_NAME: "EP - Glasgow University - Anderson College",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2399,
    SYSTEM_NAME: "EP - Glasgow University - BHF and BRC Building",
    SENSOR_COUNT: 2,
  },
  {
    SYSTEM_ID: 2401,
    SYSTEM_NAME: "EP - Glasgow University - Bower Building ",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2403,
    SYSTEM_NAME: "EP - Glasgow University - Davidson Building",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2404,
    SYSTEM_NAME: "EP - Glasgow University - Estates Building",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2405,
    SYSTEM_NAME: "EP - Glasgow University - Florentine House",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2408,
    SYSTEM_NAME:
      "EP - Glasgow University - Garscube - Weiper Equine Centre- Needs Upgrade",
    SENSOR_COUNT: 0,
  },
  {
    SYSTEM_ID: 2410,
    SYSTEM_NAME: "EP - Glasgow University - Gilmorehill Halls",
    SENSOR_COUNT: 0,
  },
  {
    SYSTEM_ID: 2412,
    SYSTEM_NAME: "EP - Glasgow University - GUU",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2413,
    SYSTEM_NAME: "EP - Glasgow University - Graham Kerr Building",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2414,
    SYSTEM_NAME: "EP - Glasgow University - Gregory Building",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2417,
    SYSTEM_NAME: "EP - Glasgow University - Bute Gardens",
    SENSOR_COUNT: 4,
  },
  {
    SYSTEM_ID: 2418,
    SYSTEM_NAME: "EP - Glasgow University - Hillhead Street",
    SENSOR_COUNT: 7,
  },
  {
    SYSTEM_ID: 2419,
    SYSTEM_NAME: "EP - Glasgow University - Oakfield Avenue",
    SENSOR_COUNT: 16,
  },
  {
    SYSTEM_ID: 2420,
    SYSTEM_NAME: "EP - Glasgow University - Southpark Avenue",
    SENSOR_COUNT: 5,
  },
  {
    SYSTEM_ID: 2421,
    SYSTEM_NAME: "EP - Glasgow University - Hunterian Art Gallery",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2423,
    SYSTEM_NAME: "EP - Glasgow University - Ivy Lodge",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2425,
    SYSTEM_NAME: "EP - Glasgow University - John McIntyre Building",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2426,
    SYSTEM_NAME: "EP - Glasgow University - James Watt Nanofabrication",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2427,
    SYSTEM_NAME: "EP - Glasgow University - James Watt North",
    SENSOR_COUNT: 0,
  },
  {
    SYSTEM_ID: 2429,
    SYSTEM_NAME: "EP - Glasgow University - Garscube - Wolfson WOHL  ",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2431,
    SYSTEM_NAME: "EP - Glasgow University - Garscube - Botham",
    SENSOR_COUNT: 0,
  },
  {
    SYSTEM_ID: 2432,
    SYSTEM_NAME: "EP - Glasgow University - Garscube - Recreational Facility",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2433,
    SYSTEM_NAME: "EP - Glasgow University - Garscube - Henry Wellcome ",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2437,
    SYSTEM_NAME:
      "EP - Glasgow University - Garscube - Small Animal Hospital -Needs upgrade(10pulse input)",
    SENSOR_COUNT: 0,
  },
  {
    SYSTEM_ID: 2439,
    SYSTEM_NAME: "EP - Glasgow University - Garscube - Stoker",
    SENSOR_COUNT: 2,
  },
  {
    SYSTEM_ID: 2440,
    SYSTEM_NAME: "EP - Glasgow University - James Watt South",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2441,
    SYSTEM_NAME: "EP - Glasgow University - Joseph Black",
    SENSOR_COUNT: 9,
  },
  {
    SYSTEM_ID: 2442,
    SYSTEM_NAME: "EP - Glasgow University - Kelvin",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2443,
    SYSTEM_NAME: "EP - Glasgow University - Learning & Teaching",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2444,
    SYSTEM_NAME: "EP - Glasgow University - Lilybank House",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2446,
    SYSTEM_NAME: "EP - Glasgow University - Pearce Lodge",
    SENSOR_COUNT: 0,
  },
  {
    SYSTEM_ID: 2447,
    SYSTEM_NAME: "EP - Glasgow University - Professors Square ",
    SENSOR_COUNT: 2,
  },
  {
    SYSTEM_ID: 2448,
    SYSTEM_NAME: "EP - Glasgow University - Rankine",
    SENSOR_COUNT: 5,
  },
  {
    SYSTEM_ID: 2449,
    SYSTEM_NAME: "EP - Glasgow University - Reading Room ",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2450,
    SYSTEM_NAME: "EP - Glasgow University - Sir Alexander Stone",
    SENSOR_COUNT: 2,
  },
  {
    SYSTEM_ID: 2451,
    SYSTEM_NAME: "EP - Glasgow University - Sir Alwyn Williams",
    SENSOR_COUNT: 0,
  },
  {
    SYSTEM_ID: 2452,
    SYSTEM_NAME: "EP - Glasgow University - Sir Charles Wilson",
    SENSOR_COUNT: 2,
  },
  {
    SYSTEM_ID: 2453,
    SYSTEM_NAME: "EP - Glasgow University - St Andrews",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2454,
    SYSTEM_NAME: "EP - Glasgow University - Stevenson ",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2455,
    SYSTEM_NAME: "EP - Glasgow University - Thomson Building",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2456,
    SYSTEM_NAME: "EP - Glasgow University - University Gardens",
    SENSOR_COUNT: 2,
  },
  {
    SYSTEM_ID: 2457,
    SYSTEM_NAME: "EP - Glasgow University - West Medical Building",
    SENSOR_COUNT: 0,
  },
  {
    SYSTEM_ID: 2458,
    SYSTEM_NAME: "EP - Glasgow University - Western Infirmary Lecture Theatre",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2459,
    SYSTEM_NAME: "EP - Glasgow University - Wolfson Link",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2460,
    SYSTEM_NAME: "EP - Glasgow University - Wolfson Medical School",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2479,
    SYSTEM_NAME: "EP - Glasgow University 12 Input Logger",
    SENSOR_COUNT: 0,
  },
  {
    SYSTEM_ID: 2480,
    SYSTEM_NAME:
      "EP - Glasgow University - Garscube - Main Sub - 8MP-Needs Upgrade",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2527,
    SYSTEM_NAME: "EP - Glasgow University - 70 University Avenue",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2530,
    SYSTEM_NAME: "EP - Glasgow University - Plant Growth Room",
    SENSOR_COUNT: 2,
  },
  {
    SYSTEM_ID: 2540,
    SYSTEM_NAME: "EP - Glasgow University - Terraced Properties Master",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 2541,
    SYSTEM_NAME: "EP - Glasgow University - Garscube Master",
    SENSOR_COUNT: 4,
  },
  {
    SYSTEM_ID: 2542,
    SYSTEM_NAME: "EP - Glasgow University - Master",
    SENSOR_COUNT: 7,
  },
  {
    SYSTEM_ID: 2753,
    SYSTEM_NAME: "EP - Glasgow University - 17 Lilybank Gardens",
    SENSOR_COUNT: 0,
  },
  {
    SYSTEM_ID: 3046,
    SYSTEM_NAME: "EP - Glasgow University - Garscube - Alistair Currie",
    SENSOR_COUNT: 0,
  },
  {
    SYSTEM_ID: 3048,
    SYSTEM_NAME: "EP - Glasgow University - Garscube - Wind Tunnel",
    SENSOR_COUNT: 0,
  },
  {
    SYSTEM_ID: 3049,
    SYSTEM_NAME: "EP - Glasgow University - Garscube - Observatory",
    SENSOR_COUNT: 0,
  },
  {
    SYSTEM_ID: 3050,
    SYSTEM_NAME: "EP - Glasgow University - Garscube - BSU and Barrier Unit",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 3054,
    SYSTEM_NAME: "EP - Glasgow University - CCNI",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 3055,
    SYSTEM_NAME: "EP - Glasgow University - Robertson Building",
    SENSOR_COUNT: 0,
  },
  {
    SYSTEM_ID: 3056,
    SYSTEM_NAME: "EP - Glasgow University - JRF",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 3057,
    SYSTEM_NAME: "EP - Glasgow University - 13 Thurso Street",
    SENSOR_COUNT: 0,
  },
  {
    SYSTEM_ID: 3058,
    SYSTEM_NAME: "EP - Glasgow University - Central Research Facility",
    SENSOR_COUNT: 0,
  },
  {
    SYSTEM_ID: 3077,
    SYSTEM_NAME: "EP - Glasgow University - Garscube - Naval Architecture",
    SENSOR_COUNT: 0,
  },
  {
    SYSTEM_ID: 3082,
    SYSTEM_NAME: "EP - Glasgow University - Hetherington ",
    SENSOR_COUNT: 1,
  },
  {
    SYSTEM_ID: 3083,
    SYSTEM_NAME:
      "EP - Glasgow University - Garscube - Mary Stewart Building- needs upgrade",
    SENSOR_COUNT: 0,
  },
  {
    SYSTEM_ID: 3385,
    SYSTEM_NAME: "EP - Glasgow University - MPAN - 1800060477999 ",
    SENSOR_COUNT: 0,
  },
  {
    SYSTEM_ID: 3400,
    SYSTEM_NAME: "EP - Glasgow University - MPAN - 1800053988083",
    SENSOR_COUNT: 0,
  },
  {
    SYSTEM_ID: 3402,
    SYSTEM_NAME: "EP - Glasgow University - MPAN - 1800051757870",
    SENSOR_COUNT: 0,
  },
  {
    SYSTEM_ID: 3403,
    SYSTEM_NAME: "EP - Glasgow University - MPAN - 1800036597772",
    SENSOR_COUNT: 0,
  },
  {
    SYSTEM_ID: 3404,
    SYSTEM_NAME: "EP - Glasgow University - MPAN - 1800035342264",
    SENSOR_COUNT: 0,
  },
  {
    SYSTEM_ID: 3407,
    SYSTEM_NAME: "EP - Glasgow University - Weipers -MPAN - 1800035238261",
    SENSOR_COUNT: 0,
  },
  {
    SYSTEM_ID: 3430,
    SYSTEM_NAME: "EP - Glasgow University - MPAN - 1800060045547",
    SENSOR_COUNT: 0,
  },
  {
    SYSTEM_ID: 3431,
    SYSTEM_NAME: "EP - Glasgow University - Display Screen",
    SENSOR_COUNT: 0,
  },
];

const allSystemData: string[] = [];
allSystems.forEach((e) => {
  allSystemData.push(e.SYSTEM_NAME);
});

export default allSystemData;
