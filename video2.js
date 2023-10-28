window.document.onkeydown = function(e) {
    if (!e) {
      e = event;
    }
    if (e.keyCode == 27) {
      lightbox_close2();
    }
  }
  
  function lightbox_open2() {
    var lightBoxVideo = document.getElementById("VisaChipCardVideo2");
    window.scrollTo(0, 0);
    document.getElementById('light2').style.display = 'block';
    document.getElementById('fade2').style.display = 'block';
    lightBoxVideo.play();
  }
  
  function lightbox_close2() {
    var lightBoxVideo = document.getElementById("VisaChipCardVideo2");
    document.getElementById('light2').style.display = 'none';
    document.getElementById('fade2').style.display = 'none';
    lightBoxVideo.pause();
  }