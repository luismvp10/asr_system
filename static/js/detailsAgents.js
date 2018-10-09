function getNoInterfaces(comunidad,ip){
/*Obtenemos el numero de Interfaces de Red con ayuda de la función en python*/
 $.ajax({
                    type: 'GET',
                    url: '/getInterfacesNet/'+comunidad+'/'+ip,
                    success:  function(response){
                     //console.log("N° de Interfaces: "+response);
                     $('#noInterfaces').text(""+response)
                    },
                    error:function(){
                   console.log('Se perdió la conexión! ');
                    },
                 });

}


function getAgentName(comunidad, ip){
 $.ajax({
                    type: 'GET',
                    url: '/getAgentName/'+comunidad+'/'+ip,
                    success:  function(response){
                     $('#username').text(""+response);
                    },
                    error:function(){
                   console.log('Se perdió la conexión! ');
                    },
                 });

}

function getOperativeSystem(comunidad, ip){
 $.ajax({
                    type: 'GET',
                    url: '/getOperativeSystem/'+comunidad+'/'+ip,
                    success:  function(response){
                     $('#so').text(""+response);
                    },
                    error:function(){
                   console.log('Se perdió la conexión! ');
                    },
                 });


}

function  getTimeActivity(comunidad, ip){
 $.ajax({
                    type: 'GET',
                    url: '/getTimeActivity/'+comunidad+'/'+ip,
                    success:  function(response){
                     $('#time').text(""+response);
                    },
                    error:function(){
                   console.log('Se perdió la conexión! ');
                    },
                 });
}


function getAgentLocation(comunidad, ip){

 $.ajax({
                    type: 'GET',
                    url: '/getAgentLocation/'+comunidad+'/'+ip,
                    success:  function(response){
                     $('#location').text(""+response);
                    },
                    error:function(){
                   console.log('Se perdió la conexión! ');
                    },
                 });

}

function getContact(comunidad, ip){

 $.ajax({
                    type: 'GET',
                    url: '/getContact/'+comunidad+'/'+ip,
                    success:  function(response){
                     $('#contact').text(""+response);
                    },
                    error:function(){
                   console.log('Se perdió la conexión! ');
                    },
                 });
}