const formatDropdownData: (systems: systemArray) => string[] = (
  systems: systemArray
) => {
  let result = systems.map((s) => s.SYSTEM_NAME);
  return result;
};

export default formatDropdownData;
