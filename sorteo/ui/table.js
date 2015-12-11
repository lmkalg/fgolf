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
    getJson: function(url){
      
      var self = this;
      
      // loading data before
      dataFn.html('<span class="loading_table">'+
                  'Loading Please Wait ....'+
                  '</span>');
      
      // No ajax cache
      $.ajaxSetup({ cache: false });
      
      // Get json


      $.getJSON(thisUrl,function(data){
        var time_to_wait = 8000;
        for (var i = 0; i < data.length; i++){
          (function(i){
              setTimeout(function(){

                // load template
                var out_html = self.complete_line_and_template(data[i]); 
                $.each(data[i].players,function(i,obj){  
                  // load inner template
                  out_html += self.complete_players_info(obj);
                });  
                // close tag
                out_html += '</tbody>';
                // render templates
                dataFn.html(out_html);


              }, time_to_wait * i);
          }(i));
          

        }
        


         // error 
      }).error(function(j,t,e){ 
        // render error.
        dataFn.html('<span class="error_table">'+
                    'Error = '+e+
                    '</span>');
        
      });
    },
    

    // head table template
    complete_line_and_template: function(obj){
      var html = '<thead>'+
        '<tr>' +
        '<th> Line Number '+  obj.line_number +'</th>' +
        '<th> Date: ' + obj.line_info +'</th>'+
        '</tr>' +
        '<tr>'+
        '<th width="10%">Country</th>'+
        '<th>Player</th>'+
        '</tr>'+
        '</thead>'+
        '<tbody >';
      return html;
    },
    // inner template
    complete_players_info: function(obj){
      
      var  html= '<tr>'+
          '<td class="country-photo">'+
          '<img class="user-tumb" src="'+obj.country+'"/>'+
          '</td>'+
          '<td class="css3-notification">'+obj.player+'</td>'+
          '</tr>'; 
      return html;
    }
    
  };
  
  $(document).ready(function() {
    $.ajax({
      type:"POST",
      url:"http://localhost:8000/execute",
    }).done(function(trash){
      console.log(trash);
      console.log(1);
      $.table_of_contacts.get.init();
    });
  });

}).call(this)




