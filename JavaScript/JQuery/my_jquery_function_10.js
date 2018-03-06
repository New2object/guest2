/**
 * Created by Hasee on 2017/8/2.
 */
var jq=jQuery.noConflict();
jq(document).ready(function(){
   jq("button").click(function(){
      jq("p").text("jQuery 仍在运行！")
   });
});