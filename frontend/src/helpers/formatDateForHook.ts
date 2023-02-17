const formatDateForHook = (dateString: string) => {
  let tempDate = new Date(dateString);

  let dd = ("0" + tempDate.getDate()).slice(-2);
  let mm = ("0" + (tempDate.getMonth() + 1)).slice(-2);
  let yyyy = tempDate.getFullYear();

  return [dd, mm, yyyy].join("-");
};

export default formatDateForHook;
