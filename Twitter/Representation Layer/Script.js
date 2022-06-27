function myFunction() {
    const test = document.getElementById("search").value;
    
    return test;
  }
  
  function myOtherFunction() {
    const myDiv = document.getElementById("alpha");
    myDiv.innerText = myFunction();
  }