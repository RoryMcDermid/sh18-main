const Checkbox = ({ onChange }) => {
  return (
    <label
      htmlFor='default-toggle'
      className='inline-flex relative items-center cursor-pointer'
    >
      <input
        type='checkbox'
        id='default-toggle'
        className='sr-only peer'
        onChange={onChange}
      />
      <div
        className={`w-11 h-6 bg-gray-200 
          peer-focus:outline-none 
          rounded-full peer 
          peer-checked:after:translate-x-full
          peer-checked:after:border-white  
          after:absolute 
          after:top-[2px] 
          after:left-[2px] 
          after:bg-white
          after:border-gray-300 
          after:border 
          after:rounded-full
          after:h-5 
          after:w-5 
          after:transition-all
          peer-checked:bg-green-600`}
      />
    </label>
  );
};

export default Checkbox;
