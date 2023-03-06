// set in localstorage
export const setLocalStorage = (key: string, value: Object) => {
    if (window !== undefined) {
      localStorage.setItem(key, JSON.stringify(value));
    }
  };
  // remove from localstorage
  export const removeLocalStorage = (key: string) => {
    if (window !== undefined) {
      localStorage.removeItem(key);
    }
  };