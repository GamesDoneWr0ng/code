const progressBarEl = document.getElementById('progress-bar');

function updateProgressBar() {
    var percent = (window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100;
    var height = 48 / (48 + document.body.clientWidth) * 100
    
    //percent = Math.min(Math.max(percent, 0), 100); 

    if (percent <= height) {
        progressBarEl.style.height = percent/height * 48 + 'px';
        progressBarEl.style.width = '0%';
    } else {
        progressBarEl.style.height = '48px';
        progressBarEl.style.width = (percent-height) / document.body.clientWidth * (document.body.clientWidth + 24) + '%';
    }
}

window.onscroll = updateProgressBar;
updateProgressBar();