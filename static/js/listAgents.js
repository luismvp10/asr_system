
function getStateAgent(ip,id){
/*Si da 0 entonces esta activo el Agente*/
 $.ajax({
                    type: 'GET',
                    url: '/getStateAgent/'+ip,
                    success:  function(response){
                     console.log(response)
                     if(response==0){
                     $('#card'+id).css('background-color','#10b51da6');
                     $('#comunidadP'+id).css('margin-bottom','0%')
                     additonalInfo(id);
                     $('#gestionar'+id).show();
                     }
                     else{
                      $('#card'+id).css('background-color','#f13800b8');
                      $('#gestionar'+id).hide();
                      $('#comunidadP'+id).css('margin-bottom','32%')
                      $('#interfazP'+id).hide();
                      $('#interfaz'+id).hide();
                      }
                    },
                    error:function(){
                    console.log('Se perdió la conexión! ');
                    },
                 });
}
/*
function callbackFunc(response) {
    console.log(response);
}
*/

function additonalInfo(id) {
var ipString= $("#ip"+id).html();
var lengString= ipString.length;
var comunidad = $("#comunidad"+id).html();
//console.log("Comunidad: "+comunidad)
//console.log("IP: "+ ipString);
/*Se hace un substring para eliminar la basura que se le adjunta a la variable*/
var ip= ipString.substring(1,lengString);
///console.log(ip);
/*var a= '192.168.1.67';*/

/*Obtenemos el numero de Interfaces de Red con ayuda de la función en python*/
 $.ajax({
                    type: 'GET',
                    url: '/getInterfacesNet/'+comunidad+'/'+ip,
                    success:  function(response){
                     console.log("N° de Interfaces: "+response);
                     $('#interfazP'+id).show();
                     $('#interfaz'+id).text(""+response).show();

                    },
                    error:function(){
                   console.log('Se perdió la conexión! ');
                    },
                 });
}