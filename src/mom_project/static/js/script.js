let current_slide = 0;
const slides = document.querySelectorAll('.slide');
const total_slides = slides.length;

function updateSlider() {
    const slider = document.getElementById('slider');
    slider.style.transform = `translateX(-${current_slide * 100}%`;
}

function next_slide() {
    current_slide = (current_slide + 1) % total_slides;
    updateSlider();
}

function prev_slide() {
    current_slide = (current_slide - 1 + total_slides) % total_slides;
    updateSlider();
}
