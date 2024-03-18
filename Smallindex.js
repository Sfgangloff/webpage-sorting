

//Part of script 
let playing = true;
function playPause() {
  if (playing) {
    const song = document.querySelector('#song'),
    thumbnail = document.querySelector('#thumbnail');
      thumbnail.src = "radio1.svg";
      button.play()
  setTimeout(function(){song.play();}, 500);  
    playing = false;
  } else {thumbnail.src = "radio.svg";
    button.play();
    song.pause();
    playing = true;
  }
}

//Part of script 

$(document).ready(function(){
  $("#buttonworkgroup").click(function(){
    $("#souspage").load("souspageworkgroup.txt");
  });
});


//Part of script 

$(document).ready(function(){
  $("#buttonresearch").click(function(){
    $("#souspage").load("souspageresearch.txt");
  });
});


//Part of script 

$(document).ready(function(){
  $("#buttonbibliography").click(function(){
    $("#souspage").load("souspagebibliography.txt");
  });
});


//Part of script 

$(document).ready(function(){
  $("#buttonhomepage").click(function(){
    $("#souspage").load("souspagehomepage.txt");
  });
});


//Part of script 

   
    function light() {
         const i=document.getElementById('counter').innerHTML; 
        
        if (i==="0") { var back = document.getElementById('background');
    back.style.filter="brightness(0.25)";
                      document.getElementById('counter').innerHTML=1;
		      document.getElementById('background').style.backgroundImage="url('images/sun1.jpg')";
                   }
        
        
        if (i==="1") { var back = document.getElementById('background');
    back.style.filter="brightness(0.50)";
                        document.getElementById('counter').innerHTML=2;
		        document.getElementById('background').style.backgroundImage="url('images/sun2.jpg')";
                   }
	    
	          if (i==="2") { var back = document.getElementById('background');
    back.style.filter="brightness(0.75)";
                        document.getElementById('counter').innerHTML=3;
				  document.getElementById('background').style.backgroundImage="url('images/sun3.jpg')";
                   }
    
        
          if (i==="3") { var back = document.getElementById('background');
    back.style.filter="brightness(1)";
                        document.getElementById('counter').innerHTML=0;
			  document.getElementById('background').style.backgroundImage="url('images/sun.jpg')";
                   }
        
       
        
    }
        
    