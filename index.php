
<!DOCTYPE html>
<html class="loading">
 <head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=0, minimal-ui">  
  <title>PUSY CHK</title>
  <link href="https://fonts.googleapis.com/css?family=Muli:300,300i,400,400i,600,600i,700,700i%7CComfortaa:300,400,700" rel="stylesheet">
  <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
  <link rel="stylesheet" type="text/css" href="theme-assets/css/vendors.css">
  <link rel="stylesheet" type="text/css" href="theme-assets/css/app-lite.css">
  <link rel="stylesheet" type="text/css" href="theme-assets/css/core/menu/menu-types/vertical-menu.css">
  <link rel="stylesheet" type="text/css" href="theme-assets/css/core/colors/palette-gradient.css">
  	 <script src="https://cdn.jsdelivr.net/npm/sweetalert2@9"></script>
  </head>

 
 <body class="vertical-layout" style="background-color:#112132;" data-color="bg-gradient-x-purple-blue">  
 <style>
		h5,h4{
			color:white; 
		}
		.text-center{
			background-color:#0e1d2c;
			border:1px solid #525252;
			border-radius:5px;
		}
		textarea{
			color:white;
			resize: none;
		}

		.text-center::placeholder{
			color:grey;
		}
		.text-center:focus{
			background-color:#0e1d2c;
		}

		textarea::-webkit-scrollbar {
 			width: 5px;
 			background-color: #112132; 
		}

		textarea::-webkit-scrollbar-thumb {
 			border-radius: 10px;
 			background-color: #2e4964; 
		}
		.lista_reprovadass{
			color:#747474;
		}
		.card-body{
			background-color: #1c3044; 
			border-radius:5px;
		}
		.text-center{
			border:none;
		}
		.badge-success,.btn-success{
			background-color: #ffe74c;
			color:black	;
			border:none;
		}
		.btn-success:hover{
			background-color: #c9b63c;
			border:none;
			color:black;
			shadow:hidden;
		}
		.aprovadas{
			background-color: #35a7ff;
			color:black	;
		}
		.badge-danger{
			background-color: #ff5964;
			color:white	;
		}
		.html body .content .content-wrapper{
			background-color:#112132;
		}

		.btn-bg-gradient {
 			background-image: linear-gradient(to right, #FF8008 0%, #FFC837 51%, #FF8008 100%);
  			 margin: 5px;
			 width:49%;
  		padding: 12px 40px;
  		text-align: center;
  		text-transform: uppercase;
  		transition: 0.5s;
  		background-size: 200% auto;
  		color: white;      
  		box-shadow: 0 0 20px #eee;
  		border-radius: 5px;
  		display: block;
			-webkit-box-shadow: 0 0 0 0 #514a9d;
 		}

 		.btn-bg-gradient:hover {
  			background-position: right center; /* change the direction of the change here */
  		color: #fff;
  		text-decoration: none;
 		}

		 .btn-bg-gradient-x {
			background-image: linear-gradient(to right, #ee0979 0%, #ff6a00 51%, #ee0979 100%);
      margin: 5px;
      padding: 12px 45px;
			
      text-align: center;
      text-transform: uppercase;
      transition: 0.5s;
      background-size: 200% auto;
      color: white;      
      box-shadow: 0 0 20px #eee;
      border-radius: 5px;
      display: block;
			-webkit-box-shadow: 0 0 0 0 #514a9d;
 		}

 		.btn-bg-gradient-x:hover {
			background-position: right center; /* change the direction of the change here */
      color: #fff;
      text-decoration: none;
 		}

		 .statusbar{
			height:320px;
			padding-top:50px;
		 }
		 .hr-statusbar{
			border:none;
			height:1px;
			background-color:#3c5c7c;
		 }
	</style>
  <div class="app-content content" style="display:block;">
   <div class="content-wrapper" style="background-color:#112132;">
       
 <div class="content-body" >
 	<div class="mt-2"></div>
	<div class="row" style="max-width: 700px; margin: auto;">  
		<div class="col-md-8">
			<div class="card" style="background-color:transparent;">
				<div class="card-body text-center" style="">
					<h4 class="mb-2"><strong>PUSSY CHECKER </strong></h4>
					<textarea rows="9.5" class="form-control text-center form-checker mb-2" placeholder="PUT YOUR CC HERE " style="color=white"></textarea>
				<select name="gate" id="gate" class="form-control" style="margin-bottom: 0px;">
					     

<option style="background:rgba(165, 154, 154, 0.281);color:rgb(255, 208, 0);color:white" value="api/api1.php">MEMBERSHIP API: 1</option>	       
<option style="background:rgba(165, 154, 154, 0.281);color:rgb(255, 208, 0);color:white" value="api/api2.php">MEMBERSHIP API: 2</option>	    
<option style="background:rgba(165, 154, 154, 0.281);color:rgb(255, 208, 0);color:white" value="api/api3.php">MEMBERSHIP API: 3</option>	    
<option style="background:rgba(165, 154, 154, 0.281);color:rgb(255, 208, 0);color:white" value="api/api4.php">MEMBERSHIP API: 4</option>	    
<option style="background:rgba(165, 154, 154, 0.281);color:rgb(255, 208, 0);color:white" value="api/api5.php">MEMBERSHIP API: 5</option>	   
<option style="background:rgba(165, 154, 154, 0.281);color:rgb(255, 208, 0);color:white" value="api/api6.php">MEMBERSHIP API: 6</option>	   
<option style="background:rgba(165, 154, 154, 0.281);color:rgb(255, 208, 0);color:white" value="api/api7.php">MEMBERSHIP API: 7</option>	 
<option style="background:rgba(165, 154, 154, 0.281);color:rgb(255, 208, 0);color:white" value="api/api9.php">BRAINTREE</option>
<option style="background:rgba(165, 154, 154, 0.281);color:rgb(255, 208, 0);color:white" value="api/shopify.php">shopify</option>
<option style="background:rgba(165, 154, 154, 0.281);color:rgb(255, 208, 0);color:white" value="api/shopify1.php">shopify</option>
<option style="background:rgba(165, 154, 154, 0.281);color:rgb(255, 208, 0);color:white" value="api/adyen.php">ADYEN</option>
</select>
</br>
<br>


		
		<button class="btn btn-success btn-play text-green" style="width: 45%; float: right; margin-top: 5px"><i class="fa fa-play"></i> START</button>
					<button class="btn btn-danger btn-stop text-black" style="width: 40%; float: left;margin-top: 5px" disabled><i class="fa fa-stop"></i> PAUSE</button>



				</div>
			</div>
		</div>
<div class="col-md-4">
 <div class="card mb-2">
 	<div class="card-body">

<h5>TOTAL <span class="badge badge-primary float-right carregadas">0</span></h5><hr>

<h5>CHARGED <span class="badge badge-success float-right charge">0</span></h5><hr>

<h5>CVV <span class="badge badge-success float-right cvvs">0</span></h5><hr>

<h5>CCN <span class="badge badge-success float-right aprovadas">0</span></h5><hr>

<h5>DECLINED <span class="badge badge-danger float-right reprovadas">0</span></h5>					

         </div> 
        </div>
       </div>
      		<div class="col-xl-12">
			<div class="card">
				<div class="card-body">
					<div class="float-right">
						<button type="show" class="btn btn-primary btn-sm show-charge"><i class="fa fa-eye-slash"></i></button>
					<button class="btn btn-success btn-sm btn-copy1"><i class="fa fa-copy"></i></button>					
					</div>
					<h4 class="card-title mb-1"><i class="fa fa-check-circle text-success"></i> CHARGED</h4>					
			<div id='lista_charge'></div>
				</div>				
			</div>
		</div>
		      		<div class="col-xl-12">
			<div class="card">
				<div class="card-body">
					<div class="float-right">
						<button type="show" class="btn btn-primary btn-sm show-live"><i class="fa fa-eye-slash"></i></button>
					<button class="btn btn-success btn-sm btn-copy2"><i class="fa fa-copy"></i></button>					
					</div>
					<h4 class="card-title mb-1"><i class="fa fa-check text-success"></i> CVV</h4>					
			<div id='lista_cvvs'></div>
				</div>				
			</div>
		</div>
		<div class="col-xl-12">
			<div class="card">
				<div class="card-body">
					<div class="float-right">
						<button type="show" class="btn btn-primary btn-sm show-lives"><i class="fa fa-eye-slash"></i></button>
					<button class="btn btn-success btn-sm btn-copy"><i class="fa fa-copy"></i></button>					
					</div>
					<h4 class="card-title mb-1"><i class="fa fa-times text-success"></i> CCN</h4>					
			<div id='lista_aprovadas'></div>
				</div>				
			</div>
		</div>
		<div class="col-xl-12">
			<div class="card">
				<div class="card-body">
					<div class="float-right">
						<button type='hidden' class="btn btn-primary btn-sm show-dies"><i class="fa fa-eye"></i></button>
					<button class="btn btn-danger btn-sm btn-trash"><i class="fa fa-trash"></i></button>					
					</div>
					<h4 class="card-title mb-1"><i class="fa fa-times text-danger"></i> DECLINED</h4>		
						<div style='display: none;' id='lista_reprovadas'></div>
				</div>				
			</div>
		</div>
		
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<style>

footer {text-align: middle;}
#copyright, ul {display: inline-block;}
ul {list-style: none; margin: 0; padding: 0;}
li {display: inline-block; padding-left: 6px; margin-left: 5px; border-left: 1px solid #000;}
li:first-child {border: none; padding-left: 0;}
a {text-transform: uppercase; color: #FD6258; text-decoration: none;}


</style>
</head>
<body>



</body>
</html>


</section>
    </div>
   </div>
  </div>
 
  <script src="theme-assets/js/core/libraries/jquery.min.js" type="text/javascript"></script>

<script>

$(document).ready(function(){



$('.show-charge').click(function(){
var type = $('.show-charge').attr('type');
$('#lista_charge').slideToggle();
if(type == 'show'){
$('.show-charge').html('<i class="fa fa-eye"></i>');
$('.show-charge').attr('type', 'hidden');
}else{
$('.show-charge').html('<i class="fa fa-eye-slash"></i>');
$('.show-charge').attr('type', 'show');
}});

$('.show-live').click(function(){
var type = $('.show-live').attr('type');
$('#lista_cvvs').slideToggle();
if(type == 'show'){
$('.show-live').html('<i class="fa fa-eye"></i>');
$('.show-live').attr('type', 'hidden');
}else{
$('.show-live').html('<i class="fa fa-eye-slash"></i>');
$('.show-live').attr('type', 'show');
}});

$('.show-lives').click(function(){
var type = $('.show-lives').attr('type');
$('#lista_aprovadas').slideToggle();
if(type == 'show'){
$('.show-lives').html('<i class="fa fa-eye"></i>');
$('.show-lives').attr('type', 'hidden');
}else{
$('.show-lives').html('<i class="fa fa-eye-slash"></i>');
$('.show-lives').attr('type', 'show');
}});

$('.show-dies').click(function(){
var type = $('.show-dies').attr('type');
$('#lista_reprovadas').slideToggle();
if(type == 'show'){
$('.show-dies').html('<i class="fa fa-eye"></i>');
$('.show-dies').attr('type', 'hidden');
}else{
$('.show-dies').html('<i class="fa fa-eye-slash"></i>');
$('.show-dies').attr('type', 'show');
}});

$('.btn-trash').click(function(){
	Swal.fire({title: 'REMOVED', icon: 'success', showConfirmButton: false, toast: true, position: 'top-end', timer: 3000});
$('#lista_reprovadas').text('');
});

$('.btn-copy1').click(function(){
	Swal.fire({title: 'COPIED', icon: 'success', showConfirmButton: false, toast: true, position: 'top-end', timer: 3000});
var lista_charge = document.getElementById('lista_charge').innerText;
var textarea = document.createElement("textarea");
textarea.value = lista_charge;
document.body.appendChild(textarea); 
textarea.select(); 
document.execCommand('copy');      document.body.removeChild(textarea); 
});

$('.btn-copy2').click(function(){
	Swal.fire({title: 'COPIED', icon: 'success', showConfirmButton: false, toast: true, position: 'top-end', timer: 3000});
var lista_live = document.getElementById('lista_cvvs').innerText;
var textarea = document.createElement("textarea");
textarea.value = lista_live;
document.body.appendChild(textarea); 
textarea.select(); 
document.execCommand('copy');      document.body.removeChild(textarea); 
});

$('.btn-copy').click(function(){
	Swal.fire({title: 'COPIED CCN', icon: 'success', showConfirmButton: false, toast: true, position: 'top-end', timer: 3000});
var lista_lives = document.getElementById('lista_aprovadas').innerText;
var textarea = document.createElement("textarea");
textarea.value = lista_lives;
document.body.appendChild(textarea); 
textarea.select(); 
document.execCommand('copy');      document.body.removeChild(textarea); 
});


$('.btn-play').click(function(){
var sec = $("#sec").val();
var e = document.getElementById("gate");
var gate = e.options[e.selectedIndex].value;
var lista = $('.form-checker').val().trim();
var array = lista.split('\n');
var charge = 0, live = 0, lives = 0, dies = 0, testadas = 0, txt = '';

if(!lista){
	Swal.fire({title: 'You did not provide a card :(', icon: 'error', showConfirmButton: false, toast: true, position: 'top-end', timer: 3000});
	return false;
}

Swal.fire({title: 'Checking...', icon: 'success', showConfirmButton: false, toast: true, position: 'top-end', timer: 3000});


var line = array.filter(function(value){
if(value.trim() !== ""){
	txt += value.trim() + '\n';
	return value.trim();
}
});

/*
var line = array.filter(function(value){
return(value.trim() !== "");
});
*/

var total = line.length;


/*
line.forEach(function(value){
txt += value + '\n';
});
*/
if(total >5000){
 Swal.fire({title: 'Hehehe im limited to only 5000 checks!!!', icon: 'warning', showConfirmButton: false, toast: true, position: 'top-end', timer: 3000});
 return false;
}

$('.carregadas').text(total);
$('.btn-play').attr('disabled', true);
$('.btn-stop').attr('disabled', false);

line.forEach(function(data){
var callBack = $.ajax({
	url: gate + '?lista=' + data,
	success: function(retorno){
		if(retorno.indexOf("CHARGED") >= 0){
			$('#lista_charge').append(retorno);
			removelinha();
			charge = charge +1;
			}
			else if(retorno.indexOf("CVV") >= 0){
			$('#lista_cvvs').append(retorno);
			removelinha();
			live = live +1;
		  }
			else if(retorno.indexOf("CCN") >= 0){
			$('#lista_aprovadas').append(retorno);
			removelinha();
			lives = lives +1;
		  }else{
			$('#lista_reprovadas').append(retorno);
			removelinha();
			dies = dies +1;
		}
		testadas = charge + live + lives + dies;
	  $('.charge').text(charge);
	  $('.cvvs').text(live);
		$('.aprovadas').text(lives);
		$('.reprovadas').text(dies);
		$('.testadas').text(testadas);
		
		if(testadas == total){
			Swal.fire({title: 'Completed!!!', icon: 'success', showConfirmButton: false, toast: true, position: 'top-end', timer: 3000});
			$('.btn-play').attr('disabled', false);
			$('.btn-stop').attr('disabled', true);
		}
    }
   });
   $('.btn-stop').click(function(){
   Swal.fire({title: 'PAUSED', icon: 'warning', showConfirmButton: false, toast: true, position: 'top-end', timer: 3000});
   $('.btn-play').attr('disabled', false);
   $('.btn-stop').attr('disabled', true);   
   	callBack.abort();
   	return false;
   });
  });
 });
});

function removelinha() {
var lines = $('.form-checker').val().split('\n');
lines.splice(0, 1);
$('.form-checker').val(lines.join("\n"));
}



	
</script>

 </body>
</html>