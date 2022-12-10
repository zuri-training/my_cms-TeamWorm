const inputs = document.querySelectorAll('input');

inputs.forEach(input => {
    input.oninput = ()=>{
        if (!input.validity.valid){
            input.style.outline = '1.5px solid red';
        } else{
            input.style.outline = '1.5px solid green';
        }
        if (input.value.length < 1){
            input.style.outline = '1.5px solid black';
        }
    }
})