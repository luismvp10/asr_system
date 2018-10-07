
function getStateAgent(ip,id){

/*Si da 0 entonces esta activo el Agente*/
 $.ajax({
                    type: 'GET',
                    url: '/getStateAgent/'+ip,
                    success:  function(response){
                     console.log(response)
                     if(response==0)
                     $('#card'+id).css('background-color','#10b51da6');
                     else
                      $('#card'+id).css('background-color','#f13800b8');
                    },
                    error:function(){
                    alert('ERROR!');
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
console.log("Comunidad: "+comunidad)
console.log("IP: "+ ipString);
var ip= ipString.substring(1,lengString);
console.log(ip);
/*var a= '192.168.1.67';*/
/*Obtenemos el numero de Interfaces de Red con ayuda de la función en python*/
 $.ajax({
                    type: 'GET',
                    url: '/getInterfacesNet/'+comunidad+'/'+ip,
                    success:  function(response){
                     console.log(response)
                    },
                    error:function(){
                    alert('ERROR!');
                    },
                 });
}