const slidervalue = document.querySelector('sapn');
const inputslider = document.querySelector('input');
inputslider.oninput = (()+> {
        let value = inputslider.value
        slidervalue.textContent = value ;
});
