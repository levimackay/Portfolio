let selectElem = document.querySelector('select');

let logo = document.querySelector('img');

function changeTheme(){
    let current = selectElem.value;
    if (current == 'dark') {
        //give body the dark class
        document.body.classList.add('dark');
        //change the image to the dark one
        logo.setAttribute('src', '../mission/images/byui-logo_white.png');
    } else if (current == 'light') {
        //take off the dark class 
        document.body.classList.remove('dark');
        //change the image back to the original
        logo.setAttribute('src', '../mission/images/byui-logo_blue.webp');
       
    }
}

selectElem.addEventListener('change', changeTheme);