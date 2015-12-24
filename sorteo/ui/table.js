//    Demo json  loaded from dropbox 
//    Data = http://codepen.io/nakome/pen/DnEvr.js
//[   
//   {
//      "photo":"image url ",
//      "name":"Jhon",
//      "last":"Smith",
//      "email":"jhony@site.com",
//      "phone":"1-555-222-333",
//      "web":"http://jhonSmith.com"
//   },
//   { 
//      "photo":"image url",
//      "name":"Carla",
//      "last":"Doe",
//      "email":"carladoe@site.com",
//      "phone":"1-333-111-555",
//      "web":"http://carladoe.com"
//   }
// ]




(function(){
  
  'use-strict';
  
  var elem,
      // data-fn
      dataFn = $('[data-fn="contacts"]'),
      // data-url
      thisUrl = dataFn.data('url');
  
  
  if (typeof $.table_of_contacts == 'undefined')
    
    $.table_of_contacts = {};
  
  $.table_of_contacts.get = {
    
    init: function() {
      if(dataFn){
        this.getJson();
      }else{
        dataFn.html('No data found.');
      }
    },
    
    /* = Get data
    ------------------------*/
    execute: function(data){
      
      var self = this;
      
      // loading data before
      dataFn.html('<span class="loading_table">'+
                  'Loading Please Wait ....'+
                  '</span>');
      
      // No ajax cache
      $.ajaxSetup({ cache: false });
      
      // Get json


      var time_to_wait = 24500;


      for (var i = 0; i < data.length; i++){
        (function(i){
            setTimeout(function(){

              // load template
              var out_html = self.complete_line_and_template(data[i]); 


              out_html += self.complete_players_info(data[i].players);
              // close tag
              out_html += '</tbody>';
              // render templates
              dataFn.html(out_html);


            }, time_to_wait * i);
        }(i));
        

      } ;

    },
    

    // head table template
    complete_line_and_template: function(obj){
        
        
      var html_countundown =  '<meta charset="UTF-8">' + 
                              '<link href="http://fonts.googleapis.com/css?family=Bowlby+One+SC|Londrina+Outline" rel="stylesheet" type="text/css" />' +
                              '<link href="countdown.css" rel="stylesheet" type="text/css">' +
                              '<div class="cd-wrapper">' +
                              '<div class="cd-number-wrapper">' +
                              //'<img class="fg-wc-image" src="../images/fgolfwc"/>'+
                              '<span class="cd-number-twenty">20</span>' +
                              '<span class="cd-number-nineteen">19</span>' +
                              '<span class="cd-number-eighteen">18</span>' +
                              '<span class="cd-number-seventeen">17</span>' +
                              '<span class="cd-number-sixteen">16</span>' +
                              '<span class="cd-number-fifteen">15</span>' +
                              '<span class="cd-number-fourteen">14</span>' +
                              '<span class="cd-number-thirdteen">13</span>' +
                              '<span class="cd-number-twelve">12</span>' +
                              '<span class="cd-number-eleven">11</span>' +
                              '<span class="cd-number-ten">10</span>' +
                              '<span class="cd-number-nine">9</span>' +
                              '<span class="cd-number-eight">8</span>' +
                              '<span class="cd-number-seven">7</span>' +
                              '<span class="cd-number-six">6</span>' +
                              '<span class="cd-number-five">5</span>' +
                              '<span class="cd-number-four">4</span>' +
                              '<span class="cd-number-three">3</span>' +
                              '<span class="cd-number-two">2</span>' +
                              '<span class="cd-number-one">1</span>' +
                              '</div>' ;


      var html =  
        '<thead>'+
        '<tr>' +
        '<th> Line Number '+  obj.line_number +'</th>' +
        '<th> Date: ' + obj.line_info +'</th>'+
        '</tr>' +
        '<tr>'+
        '<th width="10%">Country</th>'+
        '<th>Player'+
        html_countundown +
        '</th>'+
        '</tr>'+
        '</thead>'+
        '<tbody >';
      return html;
    },
    // inner template
    complete_players_info: function(obj){
      
      var  html=
          //First player
          '<tr>'+
          '<td class="css3-notification-country-1st">'+
          '<img class="user-tumb" src="'+obj[0].country+'"/>'+
          '</td>'+
          '<td class="css3-notification-player-1st">'+obj[0].player+'</td>'+
          '</tr>'+

          //Second player
          '<tr>'+
          '<td class="css3-notification-country-2nd">'+
          '<img class="user-tumb" src="'+obj[1].country+'"/>'+
          '</td>'+
          '<td class="css3-notification-player-2nd">'+obj[1].player+'</td>'+
          '</tr>'+

          //Third player
          '<tr>'+
          '<td class="css3-notification-country-3rd">'+
          '<img class="user-tumb" src="'+obj[2].country+'"/>'+
          '</td>'+
          '<td class="css3-notification-player-3rd">'+obj[2].player+'</td>'+
          '</tr>'+

          //Fourth Player
          '<tr>'+
          '<td class="css3-notification-country-4th">'+
          '<img class="user-tumb" src="'+obj[3].country+'"/>'+
          '</td>'+
          '<td class="css3-notification-player-4th">'+obj[3].player+'</td>'+
          '</tr>';

      return html;
    }
    
  };
  
  $(document).ready(function() {
    $.ajax({
      type:"POST",
      url:"http://localhost:8000/execute",
    }).done(function(json_obj){
      console.log(json_obj);
      if(json_obj.Error){
        alert(json_obj.Error);
      }
      else{
        $.table_of_contacts.get.execute(json_obj);
      }
    });
  });

}).call(this)




