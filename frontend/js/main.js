const keyFrames = document.createElement('style')
keyFrames.ty = 'text/css';


const digits = document.getElementsByClassName("digit");

for (let i = 0; i < digits.length; i++) {
  digits[i].addEventListener("click", (e) => {
    for (let j = 1; j < 10; j++) {
      const subButton = document.createElement("div");
      subButton.classList.add("sub-button");
      subButton.classList.add( `sub-button${j}`);
      subButton.innerText = j.toString();
    //   subButton.style.top = `${j*5}px`
    //   subButton.style.left = `${j*5}px`
      e.target.appendChild(subButton);
    }
  });
}







