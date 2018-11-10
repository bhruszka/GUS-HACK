(function(d, s, id) {
  var js,
    fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s);
  js.id = id;
  js.src = "https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v3.0";
  fjs.parentNode.insertBefore(js, fjs);
  console.log("FACEBOOK");
})(document, "script", "facebook-jssdk");

(function(d, s, id) {
  var js,
    fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s);
  js.id = id;
  js.src =
    "https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v3.2&appId=1977034802365049&autoLogAppEvents=1";
  fjs.parentNode.insertBefore(js, fjs);
})(document, "script", "facebook-jssdk");