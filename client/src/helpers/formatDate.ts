const formatDate = (dateString: string) => {
  const dateParts = dateString.split(" ")[1].split("-");
  const timeParts = dateString.split(" ")[0].split(":");

  let tempDate = new Date(
    parseInt(dateParts[2]),
    parseInt(dateParts[1]) - 1,
    parseInt(dateParts[0]),
    parseInt(timeParts[0]),
    parseInt(timeParts[1])
  );

  return tempDate.toISOString();
};

export default formatDate;
